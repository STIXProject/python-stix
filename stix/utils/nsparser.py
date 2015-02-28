# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import warnings
import itertools

from cybox import Entity as CyboxEntity
from cybox.common import ObjectProperties, BaseProperty
from cybox.common import VocabString as CyboxVocabString
import cybox.utils.nsparser as cybox_nsparser

from stix import Entity as StixEntity
from stix.utils import (ignored, get_id_namespace, get_id_namespace_alias)

class NamespaceInfo(object):
    def __init__(self):
        self.namespaces = {}
        self.input_namespaces = {}
        self.input_schemalocs = {}

    def update(self, ns_info):
        self.namespaces.update(ns_info.namespaces)
        self.input_namespaces.update(ns_info.input_namespaces)
        self.input_schemalocs.update(ns_info.input_schemalocs)

    def finalize(self, ns_dict=None, schemaloc_dict=None):
        if not ns_dict:
            ns_dict = {}

        if not schemaloc_dict:
            schemaloc_dict = {}

        id_ns = get_id_namespace()
        id_ns_alias = get_id_namespace_alias()

        d_ns = {
            'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
            'http://stix.mitre.org/stix-1': 'stix',
            'http://stix.mitre.org/common-1': 'stixCommon',
            'http://stix.mitre.org/default_vocabularies-1': 'stixVocabs',
            'http://cybox.mitre.org/cybox-2': 'cybox',
            'http://cybox.mitre.org/common-2': 'cyboxCommon',
            'http://cybox.mitre.org/default_vocabularies-2': 'cyboxVocabs',
            id_ns: id_ns_alias
        }

        for ns, alias in self.input_namespaces.iteritems():
            if ns not in DEFAULT_STIX_NAMESPACES:
                d_ns[ns] = alias

        for ns, alias in self.namespaces.iteritems():
            if alias:
                d_ns[ns] = alias
            else:
                default_alias = DEFAULT_STIX_NAMESPACES[ns]
                d_ns[ns] = default_alias

        d_ns.update(ns_dict)

        # Attempts to resolve issues where our samples use
        # 'http://example.com/' for our example namespace but python-stix uses
        # 'http://example.com' by removing the former.
        examples = (
            ('http://example.com/' in d_ns),
            ('http://example.com' in d_ns)
        )

        if all(examples):
            del d_ns['http://example.com/']

        aliases = {}
        for ns, alias in d_ns.iteritems():
            if alias not in aliases:
                aliases[alias] = ns
            else:
                # TODO: Should we just throw an exception here?
                # The XML will be invalid if there is a duplicate ns alias
                message = "namespace alias '{0}' mapped to '{1}' and '{2}'"
                message = message.format(alias, ns, aliases[alias])
                warnings.warn(message)

        d_sl = dict(self.input_schemalocs.items())

        # Iterate over input/discovered namespaces for document and attempt
        # to map them to schemalocations. Warn if unable to map ns to schemaloc.
        for ns, _ in d_ns.iteritems():
            if ns in DEFAULT_STIX_SCHEMALOCATIONS:
                schemalocation = DEFAULT_STIX_SCHEMALOCATIONS[ns]
                d_sl[ns] = schemalocation
            else:
                unmappable = (
                    (ns == id_ns),
                    (ns in schemaloc_dict),
                    (ns in self.input_schemalocs),
                    (ns in XML_NAMESPACES)
                )

                if any(unmappable):
                    continue

                warnings.warn(
                    "Unable to map namespace '%s' to schemaLocation" % ns
                )

        d_sl.update(schemaloc_dict)
        self.finalized_schemalocs = d_sl
        self.finalized_namespaces = d_ns

    def collect(self, entity):
        # Traverse the MRO so we can collect _namespace attributes on Entity
        # derivations (e.g., WinFile extends File).
        for klass in entity.__class__.__mro__:
            if klass in (StixEntity, CyboxEntity, CyboxVocabString):
                break

            # Prevents exception being raised if/when
            # collections.MutableSequence or another base class appears in the
            # MRO.
            ns = getattr(klass, "_namespace", None)
            if not ns:
                continue

            # cybox.objects.* ObjectPropreties derivations have an _XSI_NS
            # class-level attribute which holds the namespace alias to be
            # used for its namespace.
            alias = getattr(klass, "_XSI_NS", None)
            if alias:
                self.namespaces[ns] = alias
                continue

            xsi_type = getattr(klass, "_XSI_TYPE", None)
            if not xsi_type:
                self.namespaces[ns] = None
                continue

            try:
                alias, type_ = xsi_type.split(":")
            except:
                self.namespaces[ns] = None
            else:
                self.namespaces[ns] = alias

        input_ns = getattr(entity, "__input_namespaces__", None)
        if input_ns is not None:
            self.input_namespaces.update(input_ns)

        input_locs = getattr(entity, "__input_schemalocations__", None)
        if input_locs is not None:
            self.input_schemalocs.update(input_locs)


    def __setitem__(self, key, value):
        self.namespaces[key] = value


class NamespaceParser(object):
    def __init__(self):
        pass

    def _walkns(self, entity):
        # Skip some python-cybox classes and properties
        skip = {ObjectProperties : ('_parent'),
                BaseProperty: None}

        def can_skip(obj, field):
            for klass, props in skip.iteritems():
                if isinstance(obj, klass):
                    return (props is None) or (field in props)
            return False

        def get_members(obj):
            for k, v in obj.__dict__.iteritems():
                if v and not can_skip(obj, k):
                    yield v
            try:
                for field in obj._fields.itervalues():
                    yield field
            except AttributeError:
                # no _fields or itervalues()
                pass

        visited = []
        def descend(obj):
            for member in get_members(obj):
                if '_namespace' in member.__class__.__dict__:
                    yield member
                    for i in descend(member):
                        yield i

                if hasattr(member, "__getitem__"):
                    for i in member:
                        if '_namespace' in i.__class__.__dict__:
                            yield i
                            for d in descend(i):
                                yield d
        # end descend()

        if '_namespace' in entity.__class__.__dict__:
            yield entity
            for node in descend(entity):
                yield node


    def get_namespaces(self, entity, ns_dict=None):
        ns_info = NamespaceInfo()

        for node in self._walkns(entity):
            ns_info.collect(node)

        ns_info.finalize(ns_dict=ns_dict)
        return ns_info.finalized_namespaces


    def get_namespace_schemalocation_dict(self, entity, ns_dict=None, schemaloc_dict=None):
        ns_info = NamespaceInfo()

        for node in self._walkns(entity):
            ns_info.collect(node)

        ns_info.finalize(ns_dict=ns_dict, schemaloc_dict=schemaloc_dict)
        return ns_info.finalized_schemalocs


    def get_xmlns_str(self, ns_dict):
        pairs = sorted(ns_dict.iteritems())
        return "\n\t".join(
            'xmlns:%s="%s"' % (alias, ns) for ns, alias in pairs
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
CYBOX_NS_TO_SCHEMALOCATION = dict((ns, schemaloc) for ns, _, schemaloc in cybox_nsparser.NS_LIST if schemaloc)

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

DEFAULT_CYBOX_NAMESPACES = dict(
    (ns, alias) for (ns, alias, _) in cybox_nsparser.NS_LIST
)

DEFAULT_STIX_NAMESPACES  = dict(
    itertools.chain(
        DEFAULT_CYBOX_NAMESPACES.iteritems(),
        XML_NAMESPACES.iteritems(),
        DEFAULT_STIX_NS_TO_PREFIX.iteritems(),
        DEFAULT_EXT_TO_PREFIX.iteritems()
    )
)

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

    DEFAULT_MAEC_NAMESPACES = dict((ns, alias) for (ns, alias, _) in NS_LIST)
    del DEFAULT_MAEC_NAMESPACES['http://maec.mitre.org/default_vocabularies-1']
    MAEC_NS_TO_SCHEMALOCATION = dict(
        (ns, schemaloc) for ns, _, schemaloc in NS_LIST if schemaloc
    )

    DEFAULT_STIX_NAMESPACES.update(DEFAULT_MAEC_NAMESPACES)
    DEFAULT_STIX_SCHEMALOCATIONS.update(MAEC_NS_TO_SCHEMALOCATION)
