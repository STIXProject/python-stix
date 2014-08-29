# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import collections
import warnings
import stix
from stix.utils import get_id_namespace
import cybox
from cybox.core import Observables, Observable
from cybox.common import ObjectProperties
import cybox.utils.nsparser as cybox_nsparser

def walkns(entity):
    yieldable = (stix.Entity, cybox.Entity)
    skip = {ObjectProperties : '_parent'}

    def can_skip(obj, field):
        for klass, prop in skip.iteritems():
            if prop == field and isinstance(obj, klass):
                return True
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
        if id(obj) in visited:
            return
        visited.append(id(obj))

        for member in get_members(obj):
            if isinstance(member, yieldable):
                yield member
                for i in descend(member):
                    yield i

            if hasattr(member, "__getitem__"):
                for i in member:
                    if isinstance(i, yieldable):
                        yield i
                        for d in descend(i):
                            yield d

        visited.remove(id(obj))
    # end descend()


    for node in descend(entity):
        yield node
# end walkns()


class NamespaceParser(object):
    def __init__(self):
        pass

    def _get_observable_namespace_dict(self, obs):
        '''Returns a dict of namespaces used within a CybOX Observable'''
        namespaces = {'http://cybox.mitre.org/default_vocabularies-2': 'cyboxVocabs'}
        
        obs_namespaces = obs._get_namespaces()
        for namespace in obs_namespaces:
            namespaces[namespace.name] = namespace.prefix
            
        return namespaces

    def _get_namespace_dict(self, entity):
        all_namespaces = {}

        if not isinstance(entity, (stix.Entity, cybox.Entity)):
            raise ValueError("Must provide an instance of stix.Entity or cybox.core.Observable")

        entity.nsparser_touched = True
        if isinstance(entity, Observable):
            all_namespaces.update(self._get_observable_namespace_dict(entity))
        elif isinstance(entity, Observables):
            for child in entity._get_children():
                all_namespaces.update(self._get_namespace_dict(child))
        elif hasattr(entity, "_namespace"):
            if hasattr(entity, "_XSI_TYPE") and entity._XSI_TYPE:
                ns_alias = entity._XSI_TYPE.split(":")[0]
                all_namespaces[entity._namespace] = ns_alias
            else:
                all_namespaces[entity._namespace] = None

            for child in entity._get_children():
                if not hasattr(child, "nsparser_touched"):
                    if hasattr(child, "_namespace") or isinstance(child, Observable):
                        all_namespaces.update(self._get_namespace_dict(child))

        del entity.nsparser_touched
        return all_namespaces


    def get_namespaces(self, entity, ns_dict=None):
        import stix.utils.idgen as idgen

        if not ns_dict:
            ns_dict = {}

        entity_namespaces = \
            {'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
             'http://stix.mitre.org/stix-1': 'stix',
             'http://stix.mitre.org/common-1': 'stixCommon',
             'http://stix.mitre.org/default_vocabularies-1': 'stixVocabs',
             'http://cybox.mitre.org/cybox-2': 'cybox',
             'http://cybox.mitre.org/common-2': 'cyboxCommon',
             'http://cybox.mitre.org/default_vocabularies-2': 'cyboxVocabs',
             idgen.get_id_namespace(): idgen.get_id_namespace_alias()}

        try:
            for ns, alias in entity.__input_namespaces__.iteritems():
                if ns not in (DEFAULT_STIX_NAMESPACES):
                    entity_namespaces[ns] = alias
        except AttributeError:
            # if __input_namespaces__ doesn't exist, move on.
            pass

        entity_ns_dict = {}
        for child in walkns(entity):
            try:
                ns = child._namespace
                ns_alias = None

                try: ns_alias, type_ = child._XSI_TYPE.split(":")
                except: pass

                entity_ns_dict[ns] = ns_alias

            except AttributeError:
                # No _namespace attribute found. move along.
                pass

        for ns, alias in entity_ns_dict.iteritems():
            if alias:
                entity_namespaces[ns] = alias
            elif ns not in entity_namespaces:
                default_alias = DEFAULT_STIX_NAMESPACES[ns]
                entity_namespaces[ns] = default_alias

        # add additional @ns_dict and parsed
        entity_namespaces.update(ns_dict)

        # Remove "http://example.com/" namespace if "http://example.com" exists
        # A bit of a hack to resolve issues with the STIX samples and our
        # own default ID namespace
        if all((entity_namespaces.get('http://example.com/'),
               entity_namespaces.get('http://example.com'))):
            del entity_namespaces['http://example.com/']

        # sanity check namespaces for things like duplicate aliases
        aliases = {}
        for ns, alias in entity_namespaces.iteritems():
            if alias not in aliases:
                aliases[alias] = ns
            else:
                # TODO: Should we just throw an exception here?
                # The XML will be invalid if there is a duplicate ns alias
                warnings.warn("namespace alias '%s' mapped to '%s' and '%s'" %
                              (alias, ns, aliases[alias]))

        return entity_namespaces

    def _get_input_schemalocations(self, entity):
        all_schemalocations = {}

        def apply_input_schemalocations(e):
            try:
                all_schemalocations.update(entity.__input_schemalocations__)
            except AttributeError:
                pass

        apply_input_schemalocations(entity)
        for child in walkns(entity):
           apply_input_schemalocations(child)

        return all_schemalocations

    def get_namespace_schemalocation_dict(self, entity, ns_dict=None, schemaloc_dict=None):
        d = {}
        if not ns_dict:
            ns_dict = self.get_namespaces(entity)

        if not schemaloc_dict:
            schemaloc_dict = {}

        input_schemalocations = self._get_input_schemalocations(entity)
        d.update(input_schemalocations)

        # Iterate over input/discovered namespaces for document and attempt
        # to map them to schemalocations. Warn if unable to map ns to schemaloc.
        id_namespace = get_id_namespace()
        for ns in ns_dict.iterkeys():
            if ns in DEFAULT_STIX_SCHEMALOCATIONS:
                schemalocation = DEFAULT_STIX_SCHEMALOCATIONS[ns]
                d[ns] = schemalocation
            else:
                if not ((ns == id_namespace) or
                        (ns in schemaloc_dict) or
                        (ns in d) or
                        (ns in XML_NAMESPACES)):
                    warnings.warn("Unable to map namespace '%s' to "
                                  "schemaLocation" % ns)

        d.update(schemaloc_dict)
        return d

    def get_xmlns_str(self, ns_dict):
        return "\n\t".join(['xmlns:%s="%s"' %
                            (alias, ns) for ns, alias in sorted(ns_dict.iteritems())])

    def get_schemaloc_str(self, schemaloc_dict):
        if not schemaloc_dict:
            return ""

        schemaloc_str_start = 'xsi:schemaLocation="\n\t'
        schemaloc_str_end = '"'
        schemaloc_str_content = "\n\t".join(["%s %s" %
                                             (ns, loc) for ns, loc in sorted(schemaloc_dict.iteritems())])
        return schemaloc_str_start + schemaloc_str_content + schemaloc_str_end

    def get_namespace_def_str(self, namespaces, schemaloc_dict):
        if not (namespaces or schemaloc_dict):
            return ""

        return ("\n\t" + self.get_xmlns_str(namespaces) + "\n\t" +
               self.get_schemaloc_str(schemaloc_dict))

XML_NAMESPACES = {'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
                  'http://www.w3.org/2001/XMLSchema': 'xs',
                  'http://www.w3.org/1999/xlink': 'xlink',
                  'http://www.w3.org/2000/09/xmldsig#': 'ds'}

# Schema locations for namespaces defined by the STIX language
STIX_NS_TO_SCHEMALOCATION = {
    'http://data-marking.mitre.org/Marking-1': 'http://stix.mitre.org/XMLSchema/data_marking/1.1.1/data_marking.xsd',
    'http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1': 'http://stix.mitre.org/XMLSchema/extensions/marking/simple/1.1.1/simple_marking.xsd',
    'http://data-marking.mitre.org/extensions/MarkingStructure#TLP-1': 'http://stix.mitre.org/XMLSchema/extensions/marking/tlp/1.1.1/tlp_marking.xsd',
    'http://data-marking.mitre.org/extensions/MarkingStructure#Terms_Of_Use-1': 'http://stix.mitre.org/XMLSchema/extensions/marking/terms_of_use/1.0/terms_of_use_marking.xsd',
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
    'http://stix.mitre.org/stix-1': 'http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd'}

CYBOX_NS_TO_SCHEMALOCATION = dict((ns, schemaloc) for ns, _, schemaloc in cybox_nsparser.NS_LIST if schemaloc)

# Schema locations for namespaces not defined by STIX, but hosted on the STIX website     
EXT_NS_TO_SCHEMALOCATION = {'urn:oasis:names:tc:ciq:xal:3': 'http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xAL.xsd',
                            'urn:oasis:names:tc:ciq:xpil:3': 'http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xPIL.xsd',
                            'urn:oasis:names:tc:ciq:xnl:3': 'http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xNL.xsd'}

# Default namespace->alias mappings. These can be overriden by user-provided dictionaries on export
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
    'http://stix.mitre.org/extensions/Vulnerability#CVRF-1': 'stix-cvrf'}

DEFAULT_EXT_TO_PREFIX = {
    'http://capec.mitre.org/capec-2': 'capec',
    'http://maec.mitre.org/XMLSchema/maec-package-2': 'maec',
    'http://oval.mitre.org/XMLSchema/oval-definitions-5': 'oval-def',
    'http://oval.mitre.org/XMLSchema/oval-variables-5': 'oval-var',
    'http://schemas.mandiant.com/2010/ioc': 'ioc',
    'http://schemas.mandiant.com/2010/ioc/TR/': 'ioc-tr',
    'http://www.icasi.org/CVRF/schema/cvrf/1.1': 'cvrf',
    'urn:oasis:names:tc:ciq:xal:3': 'xal',
    'urn:oasis:names:tc:ciq:xpil:3': 'xpil',
    'urn:oasis:names:tc:ciq:xnl:3': 'xnl'}

DEFAULT_CYBOX_NAMESPACES = dict((ns, alias) for (ns, alias, _) in cybox_nsparser.NS_LIST)

DEFAULT_STIX_NAMESPACES  = dict(DEFAULT_CYBOX_NAMESPACES.items() +
                                XML_NAMESPACES.items() +
                                DEFAULT_STIX_NS_TO_PREFIX.items() +
                                DEFAULT_EXT_TO_PREFIX.items())

DEFAULT_STIX_SCHEMALOCATIONS = dict(STIX_NS_TO_SCHEMALOCATION.items() +
                                    EXT_NS_TO_SCHEMALOCATION.items() +
                                    CYBOX_NS_TO_SCHEMALOCATION.items())