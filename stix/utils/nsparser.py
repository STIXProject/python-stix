# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import collections
import warnings
import itertools

# external
import cybox
import cybox.core
import cybox.common
import cybox.utils

# internal
import stix

# relative
from . import ignored, idgen
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
        entity_klasses = (stix.Entity, cybox.Entity)

        # Generator which yields all stix.Entity and cybox.Entity subclasses
        # that were collected.
        entity_subclasses = (
            klass for klass in collected if issubclass(klass, entity_klasses)
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

            # Many stix/cybox entity classes have an _XSI_TYPE attribute that
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
        ex_api_ns = idgen.EXAMPLE_NAMESPACE.keys()[0]
        ex_prefix = 'example'  # Example ns prefix
        id_alias = idgen.get_id_namespace_alias()

        # If the ID namespace alias doesn't match the example alias, return.
        if id_alias != ex_prefix:
            return

        # If the example namespace prefix isn't in the parsed namespace
        # prefixes, return.
        if ex_prefix not in self._input_namespaces:
            return

        self._input_namespaces[ex_prefix] = ex_api_ns

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
        no_prefix = collected_prefixed.pop(None, ())

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
            elif (ns == id_ns) or (ns in XML_NAMESPACES):
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


class NamespaceParser(object):
    def __init__(self):
        pass

    def get_namespaces(self, entity, ns_dict=None):
        ns_info = NamespaceInfo()

        for node in iterwalk(entity):
            ns_info.collect(node)

        ns_info.finalize(ns_dict=ns_dict)
        return ns_info.finalized_namespaces

    def get_namespace_schemalocation_dict(self, entity, ns_dict=None, schemaloc_dict=None):
        ns_info = NamespaceInfo()

        for node in iterwalk(entity):
            ns_info.collect(node)

        ns_info.finalize(ns_dict=ns_dict, schemaloc_dict=schemaloc_dict)
        return ns_info.finalized_schemalocs

    def get_xmlns_str(self, ns_dict):
        pairs = sorted(ns_dict.iteritems())
        return "\n\t".join(
            'xmlns:%s="%s"' % (alias, ns) for alias, ns in pairs
        )

    def get_schemaloc_str(self, schemaloc_dict):
        if not schemaloc_dict:
            return ""

        schemaloc_str_start = 'xsi:schemaLocation="\n\t'
        schemaloc_str_end = '"'

        pairs = sorted(schemaloc_dict.iteritems())
        schemaloc_str_content = "\n\t".join(
            "%s %s" % (ns, loc) for ns, loc in pairs
        )

        return schemaloc_str_start + schemaloc_str_content + schemaloc_str_end

    def get_namespace_def_str(self, namespaces, schemaloc_dict):
        if not any((namespaces, schemaloc_dict)):
            return ""

        parts = (
            self.get_xmlns_str(namespaces),
            self.get_schemaloc_str(schemaloc_dict)
        )

        return "\n\t".join(parts)


#: Schema locations for standard XML namespaces
XML_NAMESPACES = {
    'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
    'http://www.w3.org/2001/XMLSchema': 'xs',
    'http://www.w3.org/1999/xlink': 'xlink',
    'http://www.w3.org/2000/09/xmldsig#': 'ds'
}

#: Schema locations for namespaces defined by the STIX language
STIX_NS_TO_SCHEMALOCATION = {
    'http://data-marking.mitre.org/Marking-1': 'http://stix.mitre.org/XMLSchema/data_marking/1.1.1/data_marking.xsd',
    'http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1': 'http://stix.mitre.org/XMLSchema/extensions/marking/simple/1.1.1/simple_marking.xsd',
    'http://data-marking.mitre.org/extensions/MarkingStructure#TLP-1': 'http://stix.mitre.org/XMLSchema/extensions/marking/tlp/1.1.1/tlp_marking.xsd',
    'http://data-marking.mitre.org/extensions/MarkingStructure#Terms_Of_Use-1': 'http://stix.mitre.org/XMLSchema/extensions/marking/terms_of_use/1.0.1/terms_of_use_marking.xsd',
    'http://stix.mitre.org/Campaign-1': 'http://stix.mitre.org/XMLSchema/campaign/1.1.1/campaign.xsd',
    'http://stix.mitre.org/CourseOfAction-1': 'http://stix.mitre.org/XMLSchema/course_of_action/1.1.1/course_of_action.xsd',
    'http://stix.mitre.org/ExploitTarget-1': 'http://stix.mitre.org/XMLSchema/exploit_target/1.1.1/exploit_target.xsd',
    'http://stix.mitre.org/Incident-1': 'http://stix.mitre.org/XMLSchema/incident/1.1.1/incident.xsd',
    'http://stix.mitre.org/Indicator-2': 'http://stix.mitre.org/XMLSchema/indicator/2.1.1/indicator.xsd',
    'http://stix.mitre.org/TTP-1': 'http://stix.mitre.org/XMLSchema/ttp/1.1.1/ttp.xsd',
    'http://stix.mitre.org/ThreatActor-1': 'http://stix.mitre.org/XMLSchema/threat_actor/1.1.1/threat_actor.xsd',
    'http://stix.mitre.org/common-1': 'http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd',
    'http://stix.mitre.org/default_vocabularies-1': 'http://stix.mitre.org/XMLSchema/default_vocabularies/1.1.1/stix_default_vocabularies.xsd',
    'http://stix.mitre.org/extensions/AP#CAPEC2.7-1': 'http://stix.mitre.org/XMLSchema/extensions/attack_pattern/capec_2.7/1.0.1/capec_2.7_attack_pattern.xsd',
    'http://stix.mitre.org/extensions/Address#CIQAddress3.0-1': 'http://stix.mitre.org/XMLSchema/extensions/address/ciq_3.0/1.1.1/ciq_3.0_address.xsd',
    'http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1': 'http://stix.mitre.org/XMLSchema/extensions/identity/ciq_3.0/1.1.1/ciq_3.0_identity.xsd',
    'http://stix.mitre.org/extensions/Malware#MAEC4.1-1': 'http://stix.mitre.org/XMLSchema/extensions/malware/maec_4.1/1.0.1/maec_4.1_malware.xsd',
    'http://stix.mitre.org/extensions/StructuredCOA#Generic-1': 'http://stix.mitre.org/XMLSchema/extensions/structured_coa/generic/1.1.1/generic_structured_coa.xsd',
    'http://stix.mitre.org/extensions/TestMechanism#Generic-1': 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/generic/1.1.1/generic_test_mechanism.xsd',
    'http://stix.mitre.org/extensions/TestMechanism#OVAL5.10-1': 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/oval_5.10/1.1.1/oval_5.10_test_mechanism.xsd',
    'http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1': 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/open_ioc_2010/1.1.1/open_ioc_2010_test_mechanism.xsd',
    'http://stix.mitre.org/extensions/TestMechanism#Snort-1': 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/snort/1.1.1/snort_test_mechanism.xsd',
    'http://stix.mitre.org/extensions/TestMechanism#YARA-1': 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/yara/1.1.1/yara_test_mechanism.xsd',
    'http://stix.mitre.org/extensions/Vulnerability#CVRF-1': 'http://stix.mitre.org/XMLSchema/extensions/vulnerability/cvrf_1.1/1.1.1/cvrf_1.1_vulnerability.xsd',
    'http://stix.mitre.org/stix-1': 'http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd'
}

#: Schema locations for namespaces defined by the CybOX language
CYBOX_NS_TO_SCHEMALOCATION = dict(
    (ns, loc) for ns, _, loc in cybox.utils.nsparser.NS_LIST if loc
)

#: Schema locations for namespaces not defined by STIX, but hosted on the STIX website
EXT_NS_TO_SCHEMALOCATION = {
    'urn:oasis:names:tc:ciq:xal:3': 'http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xAL.xsd',
    'urn:oasis:names:tc:ciq:xpil:3': 'http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xPIL.xsd',
    'urn:oasis:names:tc:ciq:xnl:3': 'http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xNL.xsd'
}

#: Default namespace->alias mappings. These can be overriden by user-provided dictionaries on export.
DEFAULT_STIX_NS_TO_PREFIX = {
    'http://cybox.mitre.org/common-2': 'cyboxCommon',
    'http://cybox.mitre.org/cybox-2': 'cybox',
    'http://data-marking.mitre.org/Marking-1': 'marking',
    'http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1': 'simpleMarking',
    'http://data-marking.mitre.org/extensions/MarkingStructure#TLP-1': 'tlpMarking',
    'http://data-marking.mitre.org/extensions/MarkingStructure#Terms_Of_Use-1': 'TOUMarking',
    'http://stix.mitre.org/Campaign-1': 'campaign',
    'http://stix.mitre.org/CourseOfAction-1': 'coa',
    'http://stix.mitre.org/ExploitTarget-1': 'et',
    'http://stix.mitre.org/Incident-1': 'incident',
    'http://stix.mitre.org/Indicator-2': 'indicator',
    'http://stix.mitre.org/TTP-1': 'ttp',
    'http://stix.mitre.org/ThreatActor-1': 'ta',
    'http://stix.mitre.org/stix-1': 'stix',
    'http://stix.mitre.org/common-1': 'stixCommon',
    'http://stix.mitre.org/default_vocabularies-1': 'stixVocabs',
    'http://stix.mitre.org/extensions/AP#CAPEC2.7-1': 'stix-capec',
    'http://stix.mitre.org/extensions/Address#CIQAddress3.0-1': 'stix-ciqaddress',
    'http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1': 'stix-ciqidentity',
    'http://stix.mitre.org/extensions/Malware#MAEC4.1-1': 'stix-maec',
    'http://stix.mitre.org/extensions/StructuredCOA#Generic-1': 'genericStructuredCOA',
    'http://stix.mitre.org/extensions/TestMechanism#Generic-1': 'genericTM',
    'http://stix.mitre.org/extensions/TestMechanism#OVAL5.10-1': 'stix-oval',
    'http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1': 'stix-openioc',
    'http://stix.mitre.org/extensions/TestMechanism#Snort-1': 'snortTM',
    'http://stix.mitre.org/extensions/TestMechanism#YARA-1': 'yaraTM',
    'http://stix.mitre.org/extensions/Vulnerability#CVRF-1': 'stix-cvrf'
}

#: Mapping of extension namespaces to their (typical) prefixes.
DEFAULT_EXT_TO_PREFIX = {
    'http://capec.mitre.org/capec-2': 'capec',
    'http://maec.mitre.org/XMLSchema/maec-package-2': 'maecPackage',
    'http://oval.mitre.org/XMLSchema/oval-definitions-5': 'oval-def',
    'http://oval.mitre.org/XMLSchema/oval-variables-5': 'oval-var',
    'http://schemas.mandiant.com/2010/ioc': 'ioc',
    'http://schemas.mandiant.com/2010/ioc/TR/': 'ioc-tr',
    'http://www.icasi.org/CVRF/schema/cvrf/1.1': 'cvrf',
    'urn:oasis:names:tc:ciq:xal:3': 'xal',
    'urn:oasis:names:tc:ciq:xpil:3': 'xpil',
    'urn:oasis:names:tc:ciq:xnl:3': 'xnl'
}

#: Mapping of CybOX namespaces to default aliases
DEFAULT_CYBOX_NAMESPACES = dict(
    (ns, alias) for (ns, alias, _) in cybox.utils.nsparser.NS_LIST
)


#: Mapping of all STIX/STIX Extension/CybOX/XML namespaces
DEFAULT_STIX_NAMESPACES  = dict(
    itertools.chain(
        DEFAULT_CYBOX_NAMESPACES.iteritems(),
        XML_NAMESPACES.iteritems(),
        DEFAULT_STIX_NS_TO_PREFIX.iteritems(),
        DEFAULT_EXT_TO_PREFIX.iteritems()
    )
)

#: Prefix-to-namespace mapping of the `DEFAULT_STIX_NAMESPACES` mapping
DEFAULT_STIX_PREFIX_TO_NAMESPACE = dict(
    (alias, ns) for ns, alias in DEFAULT_STIX_NAMESPACES.iteritems()
)

#: Tuple of all keys found in `DEFAULT_STIX_NAMESPACES` mapping.
DEFAULT_STIX_NAMESPACES_TUPLE = tuple(DEFAULT_STIX_NAMESPACES.keys())

#: Mapping of STIX/CybOX/STIX Extension namespaces to canonical schema locations
DEFAULT_STIX_SCHEMALOCATIONS = dict(
    itertools.chain(
        STIX_NS_TO_SCHEMALOCATION.iteritems(),
        EXT_NS_TO_SCHEMALOCATION.iteritems(),
        CYBOX_NS_TO_SCHEMALOCATION.iteritems(),
    )
)

# python-maec support code
with ignored(ImportError):
    from maec.utils.nsparser import NS_LIST

    ns_to_prefix = dict(
        (ns, prefix) for (ns, prefix, _) in NS_LIST
    )

    del ns_to_prefix['http://maec.mitre.org/default_vocabularies-1']

    prefix_to_ns = dict(
        (prefix, ns) for (ns, prefix) in ns_to_prefix.iteritems()
    )

    ns_to_schemalocation = dict(
        (ns, schemaloc) for ns, _, schemaloc in NS_LIST if schemaloc
    )

    DEFAULT_STIX_NAMESPACES.update(ns_to_prefix)
    DEFAULT_STIX_PREFIX_TO_NAMESPACE.update(prefix_to_ns)
    DEFAULT_STIX_NAMESPACES_TUPLE = tuple(DEFAULT_STIX_NAMESPACES.iterkeys())
    DEFAULT_STIX_SCHEMALOCATIONS.update(ns_to_schemalocation)
