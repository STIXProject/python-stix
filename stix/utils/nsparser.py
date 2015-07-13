# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import collections
import itertools
import warnings

from mixbox import idgen
from mixbox.entities import Entity
from mixbox.exceptions import ignored
from mixbox.namespaces import Namespace, NamespaceSet, register_namespace
from mixbox.namespaces import (get_full_ns_map, get_full_prefix_map,
                               get_full_schemaloc_map)

import cybox.utils.nsparser

try:
    import maec.utils.nsparser
except ImportError:
    pass

from .walk import iterwalk


class DuplicatePrefixError(Exception):
    def __init__(self, message, prefix, namespaces):
        super(DuplicatePrefixError, self).__init__(message)
        self.prefix = prefix
        self.namespaces = namespaces


class NamespaceInfo(object):
    # These appear in every exported document

    _BASELINE_NAMESPACES = {
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'stix': 'http://stix.mitre.org/stix-1',
        'stixCommon': 'http://stix.mitre.org/common-1',
        'stixVocabs': 'http://stix.mitre.org/default_vocabularies-1',
        'cybox': 'http://cybox.mitre.org/cybox-2',
        'cyboxCommon': 'http://cybox.mitre.org/common-2',
        'cyboxVocabs': 'http://cybox.mitre.org/default_vocabularies-2'
    }

    def __init__(self):
        # Namespaces that are "collected" from the Python objects during
        # serialization. Key is the namespace alias/prefix. Value is the
        # namespace. There are many classes without a defined prefix, so
        # the ``None`` prefix is predefined as a ``set()``.
        self._collected_namespaces = {None: set()}

        # Namespaces and schemalocations that are attached to STIX/CybOX
        # entities when parsed from an external source.
        self._input_namespaces = {}
        self._input_schemalocs = {}

        # A list of classes that have been visited/seen during the namespace
        # collection process. This speeds up the collect() method.
        self._collected_classes = set()

        # Namespaces and schemalocations that will appear in the output
        # XML document.
        self.finalized_namespaces = None
        self.finalized_schemalocs = None

        # Namespace dictionary that gets passed to the bindings.
        self.binding_namespaces = None

    def update(self, ns_info):
        self._collected_namespaces.update(ns_info._collected_namespaces)  # noqa
        self._input_namespaces.update(ns_info._input_namespaces)  # noqa
        self._input_schemalocs.update(ns_info._input_schemalocs)  # noqa

    def _parse_collected_classes(self):
        collected = self._collected_classes

        # Generator which yields all Entity subclasses
        # that were collected.
        entity_subclasses = (
            klass for klass in collected if issubclass(klass, Entity)
        )

        # Local function for adding namespaces that have no defined prefix
        # mapping at the class-level. These will be resolved in the
        # self._finalize_namespaces() function.
        no_alias = self._collected_namespaces[None].add

        for klass in entity_subclasses:
            # Prevents exception being raised if/when
            # collections.MutableSequence or another base class appears in the
            # MRO.
            ns = getattr(klass, "_namespace", None)
            if not ns:
                continue

            # cybox.objects.* ObjectProperties derivations have an _XSI_NS
            # class-level attribute which holds the namespace alias to be
            # used for its namespace.
            alias = getattr(klass, "_XSI_NS", None)
            if alias:
                self._collected_namespaces[alias] = ns
                continue

            # Many Entity classes have an _XSI_TYPE attribute that
            # contains a `prefix:namespace` formatted QNAME for the
            # associated xsi:type.
            xsi_type = getattr(klass, "_XSI_TYPE", None)
            if not xsi_type:
                no_alias(ns)
                continue

            # Attempt to split the xsi:type attribute value into the ns alias
            # and the typename.
            typeinfo = xsi_type.split(":")
            if len(typeinfo) == 2:
                self._collected_namespaces[typeinfo[0]] = ns
            else:
                no_alias(ns)

    def _fix_example_namespace(self):
        """Attempts to resolve issues where our samples use
        'http://example.com/' for our example namespace but python-stix uses
        'http://example.com' by removing the former.

        """
        example_prefix = 'example'  # Example ns prefix
        idgen_prefix = idgen.get_id_namespace_prefix()

        # If the ID namespace alias doesn't match the example alias, return.
        if idgen_prefix != example_prefix:
            return

        # If the example namespace prefix isn't in the parsed namespace
        # prefixes, return.
        if example_prefix not in self._input_namespaces:
            return

        self._input_namespaces[example_prefix] = idgen.EXAMPLE_NAMESPACE.name

    def _check_namespaces(self, ns_dict):
        """Check that all the prefixes in `ns_dict` are mapped to only
        one namespace.

        Args:
            ns_dict: A ``prefix: [namespaces]`` dictionary.

        Raises:
        `   .DuplicatePrefixError: If a prefix is mapped to more than one
                namespace.

        """
        for prefix, namespaces in ns_dict.iteritems():
            if len(namespaces) == 1:
                continue

            error = "Namespace prefix '{0}' mapped to multiple namespaces: {1}"
            error = error.format(prefix, namespaces)

            raise DuplicatePrefixError(
                message=error,
                prefix=prefix,
                namespaces=tuple(namespaces)
            )

    def _resolve_unprefixed(self, no_prefix):
        """Resolve namespace aliases for the unprefixed namespaces found on
        collected python-stix objects.

        Args:
            A collection of namespaces that were not mapped to a namespace
            prefix by a python Object.

        """
        collected_unprefixed = {}

        for ns in no_prefix:
            alias = DEFAULT_STIX_NAMESPACES[ns]
            collected_unprefixed[alias] = ns

        return collected_unprefixed

    def _finalize_namespaces(self, ns_dict=None):
        """Returns a dictionary of namespaces to be exported with an XML
        document.

        This loops over all the namespaces that were discovered and built
        during the execution of ``collect()`` and
        ``_parse_collected_classes()`` and attempts to merge them all.

        Returns:
            An ``alias: namespace`` dictionary containing all namespaces
            required to be present on an exported document.

        Raises:
            .DuplicatePrefixError: If namespace prefix was mapped to more than
                one namespace.

        """
        if not ns_dict:
            ns_dict = {}

        # Copy and flip the input dictionary from ns=>alias to alias=>ns
        user_namespaces = {}
        for ns, alias in ns_dict.iteritems():
            user_namespaces[alias] = ns

        # Our return value
        ns_dict = collections.defaultdict(set)

        # Add the ID namespaces
        id_alias = idgen.get_id_namespace_alias()
        id_ns = idgen.get_id_namespace()
        ns_dict[id_alias].add(id_ns)

        # Build namespace dictionaries from the collected Entity objects.
        collected_prefixed = dict(self._collected_namespaces.iteritems())

        # Pop the unprefixed entries.
        no_prefix = collected_prefixed.pop(None, set())

        # Resolve namespace aliases for the unprefixed namespaces.
        collected_unprefixed = self._resolve_unprefixed(no_prefix)

        # Remap the example namespace to the one expected by the APIs if the
        # sample example namespace is found.
        self._fix_example_namespace()

        # All the namespaces dictionaries we need to merge and export.
        namespace_dicts = itertools.chain(
            self._BASELINE_NAMESPACES.iteritems(),
            self._input_namespaces.iteritems(),
            collected_prefixed.iteritems(),
            collected_unprefixed.iteritems(),
            user_namespaces.iteritems()
        )

        # Build our merged namespace dictionary. It will be inspected for
        # duplicate ns prefix mappings.
        for alias, ns in namespace_dicts:
            ns_dict[alias].add(ns)

        # Check that all the prefixes are mapped to only one namespace
        self._check_namespaces(ns_dict)

        # Flatten the dictionary by popping the namespace from the namespace
        # set values in ns_dict.
        flattened = {}
        for alias, ns_set in ns_dict.iteritems():
            flattened[alias] = ns_set.pop()

        # Return the flattened dictionary
        return flattened

    def _finalize_schemalocs(self, schemaloc_dict=None):
        # If schemaloc_dict was passed in, make a copy so we don't mistakenly
        # modify the original.
        if schemaloc_dict:
            schemaloc_dict = dict(schemaloc_dict.iteritems())
        else:
            schemaloc_dict = {}

        # Get our id namespace
        id_ns = idgen.get_id_namespace()

        # Build our schemalocation dictionary!
        #
        # Initialize it from values found in the parsed, input schemalocations
        # (if there are any) and the schemaloc_dict parameter values (if there
        # are any).
        #
        # If there is a schemalocation found in both the parsed schemalocs and
        # the schema_loc dict, use the schemaloc_dict value.
        for ns, loc in self._input_schemalocs.iteritems():
            if ns in schemaloc_dict:
                continue
            schemaloc_dict[ns] = loc

        # Iterate over the finalized namespaces for a document and attempt
        # to map them to schemalocations. Warn if the namespace should have a
        # schemalocation and we can't find it anywhere.
        nsset = set(self.finalized_namespaces.itervalues())
        for ns in nsset:
            if ns in DEFAULT_STIX_SCHEMALOCATIONS:
                schemaloc_dict[ns] = DEFAULT_STIX_SCHEMALOCATIONS[ns]
            elif ns in schemaloc_dict:
                continue
            elif (ns == id_ns) or (ns in NO_SCHEMALOC_NEEDED):
                continue
            else:
                error = "Unable to map namespace '{0}' to schemaLocation"
                warnings.warn(error.format(ns))

        return schemaloc_dict

    def _finalize_binding_namespaces(self):
        """Returns a namespace-to-prefix dictionary view of the
        finalized_namespaces (which are mapped prefix-to-namespace).

        The bindings expect an NS-to-prefix mapping, while our ns processing
        code builds dictionaries that map prefix-to-Namespace(s). Because of
        this, we need to flip our dictionaries before handing them off to the
        bindings for serialization.

        """
        if not self.finalized_namespaces:
            return {}  # TODO: Should this return the DEFAULT_STIX_NAMESPACES?

        binding_namespaces = {}
        for alias, ns in self.finalized_namespaces.iteritems():
            binding_namespaces[ns] = alias

        # Always use the default STIX prefixes for STIX namespaces.
        # This is because of xsi:type prefixes used by the STIX/CybOX user-level
        # API classes.
        binding_namespaces.update(DEFAULT_STIX_NAMESPACES)

        return binding_namespaces

    def finalize(self, ns_dict=None, schemaloc_dict=None):
        self._parse_collected_classes()
        self.finalized_namespaces = self._finalize_namespaces(ns_dict)
        self.finalized_schemalocs = self._finalize_schemalocs(schemaloc_dict)
        self.binding_namespaces = self._finalize_binding_namespaces()

    def collect(self, entity):
        # Collect all the classes we need to inspect for namespace information
        self._collected_classes.update(entity.__class__.__mro__)

        # Collect the input namespaces if this entity came from some external
        # source.
        if hasattr(entity, "__input_namespaces__"):
            self._input_namespaces.update(entity.__input_namespaces__)

        # Collect the input schemalocation information if this entity came
        # from some external source.
        if hasattr(entity, "__input_schemalocations__"):
            self._input_schemalocs.update(entity.__input_schemalocations__)


def get_namespaces(entity, ns_dict=None):
    ns_info = NamespaceInfo()

    for node in iterwalk(entity):
        ns_info.collect(node)

    ns_info.finalize(ns_dict=ns_dict)
    return ns_info.finalized_namespaces


def get_namespace_schemalocation_dict(entity, ns_dict=None, schemaloc_dict=None):
    ns_info = NamespaceInfo()

    for node in iterwalk(entity):
        ns_info.collect(node)

    ns_info.finalize(ns_dict=ns_dict, schemaloc_dict=schemaloc_dict)
    return ns_info.finalized_schemalocs


def get_xmlns_str(ns_dict):
    pairs = sorted(ns_dict.iteritems())
    return "\n\t".join(
        'xmlns:%s="%s"' % (alias, ns) for alias, ns in pairs
    )


def get_schemaloc_str(schemaloc_dict):
    if not schemaloc_dict:
        return ""

    schemaloc_str_start = 'xsi:schemaLocation="\n\t'
    schemaloc_str_end = '"'

    pairs = sorted(schemaloc_dict.iteritems())
    schemaloc_str_content = "\n\t".join(
        "%s %s" % (ns, loc) for ns, loc in pairs
    )

    return schemaloc_str_start + schemaloc_str_content + schemaloc_str_end


# These namespaces don't need to have a schemalocation included during export.
NO_SCHEMALOC_NEEDED = [
    'http://www.w3.org/2001/XMLSchema-instance',
    'http://www.w3.org/2001/XMLSchema',
    'http://www.w3.org/1999/xlink',
    'http://www.w3.org/2000/09/xmldsig#',
]

#: Data Marking Namespaces
NS_MARKING = Namespace('http://data-marking.mitre.org/Marking-1', 'marking', 'http://stix.mitre.org/XMLSchema/data_marking/1.2/data_marking.xsd')
NS_MARKING_SIMPLE = Namespace('http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1', 'simpleMarking', 'http://stix.mitre.org/XMLSchema/extensions/marking/simple/1.2/simple_marking.xsd')
NS_MARKING_TLP = Namespace('http://data-marking.mitre.org/extensions/MarkingStructure#TLP-1', 'tlpMarking', 'http://stix.mitre.org/XMLSchema/extensions/marking/tlp/1.2/tlp_marking.xsd')
NS_MARKING_TERMSOFUSE = Namespace('http://data-marking.mitre.org/extensions/MarkingStructure#Terms_Of_Use-1', 'TOUMarking', 'http://stix.mitre.org/XMLSchema/extensions/marking/terms_of_use/1.1/terms_of_use_marking.xsd')

#: STIX Namespaces
NS_STIX_CORE = Namespace('http://stix.mitre.org/stix-1', 'stix', 'http://stix.mitre.org/XMLSchema/core/1.2/stix_core.xsd')
NS_STIX_COMMON = Namespace('http://stix.mitre.org/common-1', 'stixCommon', 'http://stix.mitre.org/XMLSchema/common/1.2/stix_common.xsd')
NS_STIX_VOCABS = Namespace('http://stix.mitre.org/default_vocabularies-1', 'stixVocabs', 'http://stix.mitre.org/XMLSchema/default_vocabularies/1.2.0/stix_default_vocabularies.xsd')
NS_STIX_CAMPAIGN = Namespace('http://stix.mitre.org/Campaign-1', 'campaign', 'http://stix.mitre.org/XMLSchema/campaign/1.2/campaign.xsd')
NS_STIX_COURSE_OF_ACTION = Namespace('http://stix.mitre.org/CourseOfAction-1', 'coa', 'http://stix.mitre.org/XMLSchema/course_of_action/1.2/course_of_action.xsd')
NS_STIX_EXPLOIT_TARGET = Namespace('http://stix.mitre.org/ExploitTarget-1', 'et', 'http://stix.mitre.org/XMLSchema/exploit_target/1.2/exploit_target.xsd')
NS_STIX_INCIDENT = Namespace('http://stix.mitre.org/Incident-1', 'incident', 'http://stix.mitre.org/XMLSchema/incident/1.2/incident.xsd')
NS_STIX_INDICATOR = Namespace('http://stix.mitre.org/Indicator-2', 'indicator', 'http://stix.mitre.org/XMLSchema/indicator/2.2/indicator.xsd')
NS_STIX_REPORT = Namespace('http://stix.mitre.org/Report-1', 'report', 'http://stix.mitre.org/XMLSchema/report/1.0/report.xsd')
NS_STIX_TTP = Namespace('http://stix.mitre.org/TTP-1', 'ttp', 'http://stix.mitre.org/XMLSchema/ttp/1.2/ttp.xsd')
NS_STIX_THREAT_ACTOR = Namespace('http://stix.mitre.org/ThreatActor-1', 'ta', 'http://stix.mitre.org/XMLSchema/threat_actor/1.2/threat_actor.xsd')
NS_STIX_EXT_AP_CAPEC = Namespace('http://stix.mitre.org/extensions/AP#CAPEC2.7-1', 'stix-capec', 'http://stix.mitre.org/XMLSchema/extensions/attack_pattern/capec_2.7/1.1/capec_2.7_attack_pattern.xsd')
NS_STIX_EXT_ADDRESS_CIQ= Namespace('http://stix.mitre.org/extensions/Address#CIQAddress3.0-1', 'stix-ciqaddress', 'http://stix.mitre.org/XMLSchema/extensions/address/ciq_3.0/1.2/ciq_3.0_address.xsd')
NS_STIX_EXT_IDENTITY_CIQ= Namespace('http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1', 'ciqIdentity', 'http://stix.mitre.org/XMLSchema/extensions/identity/ciq_3.0/1.2/ciq_3.0_identity.xsd')
NS_STIX_EXT_MALWARE_MAEC = Namespace('http://stix.mitre.org/extensions/Malware#MAEC4.1-1', 'stix-maec', 'http://stix.mitre.org/XMLSchema/extensions/malware/maec_4.1/1.1/maec_4.1_malware.xsd')
NS_STIX_EXT_COA_GENERIC = Namespace('http://stix.mitre.org/extensions/StructuredCOA#Generic-1', 'genericStructuredCOA', 'http://stix.mitre.org/XMLSchema/extensions/structured_coa/generic/1.2/generic_structured_coa.xsd')
NS_STIX_EXT_TEST_GENERIC = Namespace('http://stix.mitre.org/extensions/TestMechanism#Generic-1', 'genericTM', 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/generic/1.2/generic_test_mechanism.xsd')
NS_STIX_EXT_TEST_OVAL = Namespace('http://stix.mitre.org/extensions/TestMechanism#OVAL5.10-1', 'stix-oval', 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/oval_5.10/1.2/oval_5.10_test_mechanism.xsd')
NS_STIX_EXT_TEST_OPENIOC = Namespace('http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1', 'stix-openioc', 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/open_ioc_2010/1.2/open_ioc_2010_test_mechanism.xsd')
NS_STIX_EXT_TEST_SNORT = Namespace('http://stix.mitre.org/extensions/TestMechanism#Snort-1', 'snortTM', 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/snort/1.2/snort_test_mechanism.xsd')
NS_STIX_EXT_TEST_YARA = Namespace('http://stix.mitre.org/extensions/TestMechanism#YARA-1', 'yaraTM', 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/yara/1.2/yara_test_mechanism.xsd')
NS_STIX_EXT_VULN_CVRF = Namespace('http://stix.mitre.org/extensions/Vulnerability#CVRF-1', 'stix-cvrf', 'http://stix.mitre.org/XMLSchema/extensions/vulnerability/cvrf_1.1/1.2/cvrf_1.1_vulnerability.xsd')

#: Namespaces used by external schemas that are incorporated in STIX.
NS_CAPEC = Namespace('http://capec.mitre.org/capec-2', 'capec', '')
NS_MAEC_PACKAGE = Namespace('http://maec.mitre.org/XMLSchema/maec-package-2', 'maecPackage', '')
NS_OVAL_DEF = Namespace('http://oval.mitre.org/XMLSchema/oval-definitions-5', 'oval-def', '')
NS_OVAL_VAR = Namespace('http://oval.mitre.org/XMLSchema/oval-variables-5', 'oval-var', '')
NS_OPENIOC = Namespace('http://schemas.mandiant.com/2010/ioc', 'ioc', '')
NS_OPENIOC_TR = Namespace('http://schemas.mandiant.com/2010/ioc/TR/', 'ioc-tr', '')
NS_CVRF = Namespace('http://www.icasi.org/CVRF/schema/cvrf/1.1', 'cvrf', '')
# NOTE: These three schemas are hosted on the STIX site despite them being
# defined outside of STIX
NS_OASIS_CIQ_XAL = Namespace('urn:oasis:names:tc:ciq:xal:3', 'xal', 'http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xAL.xsd')
NS_OASIS_CIQ_XPIL = Namespace('urn:oasis:names:tc:ciq:xpil:3', 'xpil', 'http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xPIL.xsd')
NS_OASIS_CIQ_XNL = Namespace('urn:oasis:names:tc:ciq:xnl:3', 'xnl', 'http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xNL.xsd')


STIX_NAMESPACES = NamespaceSet()
EXTENSION_NAMESPACES = NamespaceSet()

# Magic to automatically register all Namespaces defined in this module.
for k, v in dict(globals()).items():
    if k.startswith('NS_'):
        register_namespace(v)
        if k.startswith('NS_MARKING_') or k.startswith('NS_STIX_'):
            STIX_NAMESPACES.add(v)
        else:
            EXTENSION_NAMESPACES.add(v)


#: Default namespace->alias mappings. These can be overriden by user-provided dictionaries on export.
DEFAULT_STIX_NS_TO_PREFIX = {x.name: x.prefix for x in STIX_NAMESPACES}
# NOTE: CybOX Core and Common are no longer in this mapping. Is this OK?
# 'http://cybox.mitre.org/common-2': 'cyboxCommon',
# 'http://cybox.mitre.org/cybox-2': 'cybox',

DEFAULT_STIX_NAMESPACES = get_full_ns_map()
DEFAULT_STIX_PREFIX_TO_NAMESPACE = get_full_prefix_map()
DEFAULT_STIX_SCHEMALOCATIONS = get_full_schemaloc_map()
