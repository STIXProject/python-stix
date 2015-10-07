# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import itertools
import warnings

from mixbox import idgen
from mixbox.entities import Entity
import mixbox.namespaces

# internal
import stix


class NamespaceInfo(object):

    def __init__(self):
        # Namespaces that are "collected" from the Python objects during
        # serialization.  This will be a (mixbox) NamespaceSet.
        self._collected_namespaces = None

        # Namespaces and schemalocations that are attached to STIX/CybOX
        # entities when parsed from an external source.
        self._input_namespaces = {}
        self._input_schemalocs = {}

        # A list of classes that have been visited/seen during the namespace
        # collection process. This speeds up the collect() method.
        self._collected_classes = set()

        # Namespaces and schemalocations that will appear in the output
        # XML document.
        self.finalized_schemalocs = None

        # Namespace dictionary that gets passed to the bindings.
        self.binding_namespaces = None

    def update(self, ns_info):
        self._collected_namespaces.update(ns_info._collected_namespaces)  # noqa
        self._input_namespaces.update(ns_info._input_namespaces)  # noqa
        self._input_schemalocs.update(ns_info._input_schemalocs)  # noqa

    def _parse_collected_classes(self):
        collected = self._collected_classes
        entity_klasses = (stix.Entity, Entity)

        # Generator which yields all stix.Entity and mixbox.Entity subclasses
        # that were collected.
        entity_subclasses = (
            klass for klass in collected if issubclass(klass, entity_klasses)
        )

        alias_to_ns_uri = {}
        no_alias_ns_uris = []
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
                alias_to_ns_uri[alias] = ns
                continue

            # Many stix/cybox entity classes have an _XSI_TYPE attribute that
            # contains a `prefix:namespace` formatted QNAME for the
            # associated xsi:type.
            xsi_type = getattr(klass, "_XSI_TYPE", None)
            if not xsi_type:
                no_alias_ns_uris.append(ns)
                continue

            # Attempt to split the xsi:type attribute value into the ns alias
            # and the typename.
            typeinfo = xsi_type.split(":")
            if len(typeinfo) == 2:
                alias_to_ns_uri[typeinfo[0]] = ns
            else:
                no_alias_ns_uris.append(ns)

        # Unrecognized namespace URIs will cause an error at this stage.
        self._collected_namespaces = mixbox.namespaces.make_namespace_subset_from_uris(
            itertools.chain(alias_to_ns_uri.itervalues(), no_alias_ns_uris)
        )

        # For some reason, prefixes are specified in API class vars and also in
        # our big namespace tables.  From python-cybox issue #274 [1], I
        # conclude that the tables may take priority here.  And those are
        # already going to be preferred at this point.  So the only thing I can
        # think to do with class var values is fill in any missing prefixes
        # we may have (but I doubt there will be any).
        #
        # 1. https://github.com/CybOXProject/python-cybox/issues/274
        for prefix, ns_uri in alias_to_ns_uri.iteritems():
            if self._collected_namespaces.preferred_prefix_for_namespace(ns_uri) is None:
                self._collected_namespaces.set_preferred_prefix_for_namespace(
                    ns_uri, prefix, True)

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

    def _finalize_namespaces(self, ns_dict=None):
        """Returns a dictionary of namespaces to be exported with an XML
        document.

        This loops over all the namespaces that were discovered and built
        during the execution of ``collect()`` and
        ``_parse_collected_classes()`` and attempts to merge them all.

        Raises:
            mixbox.namespaces.DuplicatePrefixError: If namespace prefix was
                mapped to more than one namespace.

        """

        if ns_dict:
            # Add the user's entries to our set
            for ns, alias in ns_dict.iteritems():
                self._collected_namespaces.add_namespace_uri(ns, alias)

        # Add the ID namespaces
        self._collected_namespaces.add_namespace_uri(
            idgen.get_id_namespace(),
            idgen.get_id_namespace_alias()
        )

        # Remap the example namespace to the one expected by the APIs if the
        # sample example namespace is found.
        self._fix_example_namespace()

        # Add _input_namespaces
        for prefix, uri in self._input_namespaces.iteritems():
            self._collected_namespaces.add_namespace_uri(uri, prefix)

        # Add some default XML namespaces to make sure they're there.
        self._collected_namespaces.import_from(mixbox.namespaces.XML_NAMESPACES)

        # python-stix's generateDS-generated binding classes can't handle
        # default namespaces.  So make sure there are no preferred defaults in
        # the set.  Get prefixes from the global namespace set if we have to.
        for ns_uri in self._collected_namespaces.namespace_uris:
            if self._collected_namespaces.preferred_prefix_for_namespace(ns_uri) is None:
                prefixes = self._collected_namespaces.get_prefixes(ns_uri)
                if len(prefixes) > 0:
                    prefix = next(iter(prefixes))
                else:
                    prefix = mixbox.namespaces.lookup_name(ns_uri)

                if prefix is None:
                    raise mixbox.namespaces.NoPrefixesError(ns_uri)

                self._collected_namespaces.set_preferred_prefix_for_namespace(
                    ns_uri, prefix, True)

    def _finalize_schemalocs(self, schemaloc_dict=None):
        # If schemaloc_dict was passed in, make a copy so we don't mistakenly
        # modify the original.
        if schemaloc_dict:
            schemaloc_dict = dict(schemaloc_dict.iteritems())
        else:
            schemaloc_dict = {}

        # Build our schemalocation dictionary!
        #
        # Initialize it from values found in the parsed, input schemalocations
        # (if there are any) and the schemaloc_dict parameter values (if there
        # are any).
        #
        # If there is a schemalocation found in both the parsed schemalocs and
        # the schema_loc dict, use the schemaloc_dict value.
        for ns, loc in self._input_schemalocs.iteritems():
            if ns not in schemaloc_dict:
                schemaloc_dict[ns] = loc

        # Now use the merged dict to update any schema locations we don't
        # already have.
        for ns, loc in schemaloc_dict.iteritems():
            if self._collected_namespaces.contains_namespace(ns) and \
                self._collected_namespaces.get_schema_location(ns) is None:
                self._collected_namespaces.set_schema_location(ns, loc)

        # Warn if we are missing any schemalocations
        id_ns = idgen.get_id_namespace()
        for ns in self._collected_namespaces.namespace_uris:
            if self._collected_namespaces.get_schema_location(ns) is None:
                if ns == id_ns or \
                        mixbox.namespaces.XML_NAMESPACES.contains_namespace(ns) or \
                        ns in schemaloc_dict:
                    continue

                error = "Unable to map namespace '{0}' to schemaLocation"
                warnings.warn(error.format(ns))

    def finalize(self, ns_dict=None, schemaloc_dict=None):
        self._parse_collected_classes()
        self._finalize_namespaces(ns_dict)
        self._finalize_schemalocs(schemaloc_dict)

        self.finalized_schemalocs = \
            self._collected_namespaces.get_uri_schemaloc_map()
        self.binding_namespaces = \
            self._collected_namespaces.get_uri_prefix_map()

    def get_xmlns_string(self, delim):
        if self._collected_namespaces is None:
            return ""
        return self._collected_namespaces.get_xmlns_string(
            preferred_prefixes_only=False, delim=delim
        )

    def get_schema_location_string(self, delim):
        if self._collected_namespaces is None:
            return ""
        return self._collected_namespaces.get_schemaloc_string(delim=delim)

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


Namespace = mixbox.namespaces.Namespace

NS_CAMPAIGN_OBJECT = Namespace("http://stix.mitre.org/Campaign-1", "campaign", "http://stix.mitre.org/XMLSchema/campaign/1.2/campaign.xsd")
NS_CAPEC_OBJECT = Namespace("http://capec.mitre.org/capec-2", "capec", "")
NS_CIQIDENTITY_OBJECT = Namespace("http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1", "ciqIdentity", "http://stix.mitre.org/XMLSchema/extensions/identity/ciq_3.0/1.2/ciq_3.0_identity.xsd")
NS_COA_OBJECT = Namespace("http://stix.mitre.org/CourseOfAction-1", "coa", "http://stix.mitre.org/XMLSchema/course_of_action/1.2/course_of_action.xsd")
NS_CVRF_OBJECT = Namespace("http://www.icasi.org/CVRF/schema/cvrf/1.1", "cvrf", "")
NS_ET_OBJECT = Namespace("http://stix.mitre.org/ExploitTarget-1", "et", "http://stix.mitre.org/XMLSchema/exploit_target/1.2/exploit_target.xsd")
NS_GENERICSTRUCTUREDCOA_OBJECT = Namespace("http://stix.mitre.org/extensions/StructuredCOA#Generic-1", "genericStructuredCOA", "http://stix.mitre.org/XMLSchema/extensions/structured_coa/generic/1.2/generic_structured_coa.xsd")
NS_GENERICTM_OBJECT = Namespace("http://stix.mitre.org/extensions/TestMechanism#Generic-1", "genericTM", "http://stix.mitre.org/XMLSchema/extensions/test_mechanism/generic/1.2/generic_test_mechanism.xsd")
NS_INCIDENT_OBJECT = Namespace("http://stix.mitre.org/Incident-1", "incident", "http://stix.mitre.org/XMLSchema/incident/1.2/incident.xsd")
NS_INDICATOR_OBJECT = Namespace("http://stix.mitre.org/Indicator-2", "indicator", "http://stix.mitre.org/XMLSchema/indicator/2.2/indicator.xsd")
NS_IOC_OBJECT = Namespace("http://schemas.mandiant.com/2010/ioc", "ioc", "")
NS_IOCTR_OBJECT = Namespace("http://schemas.mandiant.com/2010/ioc/TR/", "ioc-tr", "")
NS_MARKING_OBJECT = Namespace("http://data-marking.mitre.org/Marking-1", "marking", "http://stix.mitre.org/XMLSchema/data_marking/1.2/data_marking.xsd")
NS_OVALDEF_OBJECT = Namespace("http://oval.mitre.org/XMLSchema/oval-definitions-5", "oval-def", "")
NS_OVALVAR_OBJECT = Namespace("http://oval.mitre.org/XMLSchema/oval-variables-5", "oval-var", "")
NS_REPORT_OBJECT = Namespace("http://stix.mitre.org/Report-1", "report", "http://stix.mitre.org/XMLSchema/report/1.0/report.xsd")
NS_SIMPLEMARKING_OBJECT = Namespace("http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1", "simpleMarking", "http://stix.mitre.org/XMLSchema/extensions/marking/simple/1.2/simple_marking.xsd")
NS_SNORTTM_OBJECT = Namespace("http://stix.mitre.org/extensions/TestMechanism#Snort-1", "snortTM", "http://stix.mitre.org/XMLSchema/extensions/test_mechanism/snort/1.2/snort_test_mechanism.xsd")
NS_STIX_OBJECT = Namespace("http://stix.mitre.org/stix-1", "stix", "http://stix.mitre.org/XMLSchema/core/1.2/stix_core.xsd")
NS_STIXCAPEC_OBJECT = Namespace("http://stix.mitre.org/extensions/AP#CAPEC2.7-1", "stix-capec", "http://stix.mitre.org/XMLSchema/extensions/attack_pattern/capec_2.7/1.1/capec_2.7_attack_pattern.xsd")
NS_STIXCIQADDRESS_OBJECT = Namespace("http://stix.mitre.org/extensions/Address#CIQAddress3.0-1", "stix-ciqaddress", "http://stix.mitre.org/XMLSchema/extensions/address/ciq_3.0/1.2/ciq_3.0_address.xsd")
NS_STIXCVRF_OBJECT = Namespace("http://stix.mitre.org/extensions/Vulnerability#CVRF-1", "stix-cvrf", "http://stix.mitre.org/XMLSchema/extensions/vulnerability/cvrf_1.1/1.2/cvrf_1.1_vulnerability.xsd")
NS_STIXMAEC_OBJECT = Namespace("http://stix.mitre.org/extensions/Malware#MAEC4.1-1", "stix-maec", "http://stix.mitre.org/XMLSchema/extensions/malware/maec_4.1/1.1/maec_4.1_malware.xsd")
NS_STIXOPENIOC_OBJECT = Namespace("http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1", "stix-openioc", "http://stix.mitre.org/XMLSchema/extensions/test_mechanism/open_ioc_2010/1.2/open_ioc_2010_test_mechanism.xsd")
NS_STIXOVAL_OBJECT = Namespace("http://stix.mitre.org/extensions/TestMechanism#OVAL5.10-1", "stix-oval", "http://stix.mitre.org/XMLSchema/extensions/test_mechanism/oval_5.10/1.2/oval_5.10_test_mechanism.xsd")
NS_STIXCOMMON_OBJECT = Namespace("http://stix.mitre.org/common-1", "stixCommon", "http://stix.mitre.org/XMLSchema/common/1.2/stix_common.xsd")
NS_STIXVOCABS_OBJECT = Namespace("http://stix.mitre.org/default_vocabularies-1", "stixVocabs", "http://stix.mitre.org/XMLSchema/default_vocabularies/1.2.0/stix_default_vocabularies.xsd")
NS_TA_OBJECT = Namespace("http://stix.mitre.org/ThreatActor-1", "ta", "http://stix.mitre.org/XMLSchema/threat_actor/1.2/threat_actor.xsd")
NS_TLPMARKING_OBJECT = Namespace("http://data-marking.mitre.org/extensions/MarkingStructure#TLP-1", "tlpMarking", "http://stix.mitre.org/XMLSchema/extensions/marking/tlp/1.2/tlp_marking.xsd")
NS_TOUMARKING_OBJECT = Namespace("http://data-marking.mitre.org/extensions/MarkingStructure#Terms_Of_Use-1", "TOUMarking", "http://stix.mitre.org/XMLSchema/extensions/marking/terms_of_use/1.1/terms_of_use_marking.xsd")
NS_TTP_OBJECT = Namespace("http://stix.mitre.org/TTP-1", "ttp", "http://stix.mitre.org/XMLSchema/ttp/1.2/ttp.xsd")
NS_XAL_OBJECT = Namespace("urn:oasis:names:tc:ciq:xal:3", "xal", "http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xAL.xsd")
NS_XNL_OBJECT = Namespace("urn:oasis:names:tc:ciq:xnl:3", "xnl", "http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xNL.xsd")
NS_XPIL_OBJECT = Namespace("urn:oasis:names:tc:ciq:xpil:3", "xpil", "http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xPIL.xsd")
NS_YARATM_OBJECT = Namespace("http://stix.mitre.org/extensions/TestMechanism#YARA-1", "yaraTM", "http://stix.mitre.org/XMLSchema/extensions/test_mechanism/yara/1.2/yara_test_mechanism.xsd")

STIX_NAMESPACES = mixbox.namespaces.NamespaceSet()

# Magic to automatically register all Namespaces defined in this module.
for k, v in globals().items():
    if k.startswith('NS_'):
        mixbox.namespaces.register_namespace(v)
        STIX_NAMESPACES.add_namespace(v)

