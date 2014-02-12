# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import inspect
import stix
from cybox.core import Observables, Observable
import cybox.utils.nsparser as cybox_nsparser

class NamespaceParser(object):
    def __init__(self):
        pass
    
    def _get_observable_namespaces(self, obs):
        '''Returns namespaces used within a CybOX Observable'''
        cybox_parser = cybox_nsparser.NamespaceParser([obs.to_obj()])
        d = cybox_parser.get_namespace_dict()
        d['http://cybox.mitre.org/default_vocabularies-2'] = 'cyboxVocabs' # this is just added by default in python-cybox
        return [ns for ns in d.iterkeys()]
    
    def get_namespaces(self, entity):
        all_namespaces = set()
        
        if not (isinstance(entity, stix.Entity) or isinstance(entity, Observable)):
            raise ValueError("Must provide an instance of stix.Entity or cybox.core.Observable")
        
        entity.nsparser_touched = True
        if isinstance(entity, Observable):
            all_namespaces.update(self._get_observable_namespaces(entity))
        elif isinstance(entity, Observables):
            for child in self._get_children(entity):
                all_namespaces.update(self.get_namespaces(child))
        elif hasattr(entity, "_namespace"):
            all_namespaces.add(entity._namespace)
        
            for child in self._get_children(entity):
                if not hasattr(child, "nsparser_touched"):
                    if hasattr(child, "_namespace") or isinstance(child, Observable):
                        all_namespaces.update(self.get_namespaces(child))
        
        del entity.nsparser_touched
        return all_namespaces
    
    def _get_children(self, entity):
        for (name, obj) in inspect.getmembers(entity):
            if isinstance(obj, stix.Entity):
                yield obj
            elif isinstance(obj, Observable):
                yield obj
            elif isinstance(obj, Observables):
                for obs in obj.observables:
                    yield obs
            elif isinstance(obj, list):
                for item in obj:
                    if isinstance(item, stix.Entity) or isinstance(item, Observable):
                        yield item
    
    def get_namespace_schemalocation_dict(self, entity):
        d = {}
        ns_set = self.get_namespaces(entity)
        for ns in ns_set:
            if ns in XML_NAMESPACES:
                continue
            elif ns in STIX_NS_TO_SCHEMALOCATION:
                schemalocation = STIX_NS_TO_SCHEMALOCATION[ns]
                d[ns] = schemalocation
            elif ns in EXT_NS_TO_SCHEMALOCATION:
                schemalocation = EXT_NS_TO_SCHEMALOCATION[ns]
                d[ns] = schemalocation
            elif ns.startswith("http://cybox.mitre.org"):
                for cybox_ns_tup in cybox_nsparser.NS_LIST:
                    if cybox_ns_tup[0] == ns:
                        d[ns] = cybox_ns_tup[2]
            else:
                print "! Cannot map %s to a schemalocation." % (ns)
                
        return d
    
    def _get_xmlns_str(self, ns_dict):
        return "\n\t".join(['xmlns:%s="%s"' % (alias,ns) for ns,alias in sorted(ns_dict.iteritems())])
    
    def _get_schemaloc_str(self, schemaloc_dict):
        schemaloc_str_start = 'xsi:schemaLocation="\n\t'
        schemaloc_str_end = '"'
        schemaloc_str_content = "\n\t".join(["%s %s" % (ns, loc) for ns,loc in sorted(schemaloc_dict.iteritems())])
        return schemaloc_str_start + schemaloc_str_content + schemaloc_str_end
    
    def get_namespace_def_str(self, ns_dict, schemaloc_dict):
        return "\n\t" + self._get_xmlns_str(ns_dict) + "\n\t" + self._get_schemaloc_str(schemaloc_dict)

XML_NAMESPACES = {'http://www.w3.org/2001/XMLSchema-instance' : 'xsi', 
                  'http://www.w3.org/2001/XMLSchema' : 'xs',
                  'http://www.w3.org/1999/xlink' : 'xlink',
                  'http://www.w3.org/2000/09/xmldsig#': 'ds'}

# Schema locations for namespaces defined by the STIX language
STIX_NS_TO_SCHEMALOCATION = {
         'http://stix.mitre.org/stix-1': 'http://stix.mitre.org/XMLSchema/core/1.0.1/stix_core.xsd',
         'http://stix.mitre.org/common-1': 'http://stix.mitre.org/XMLSchema/common/1.0.1/stix_common.xsd',
         'http://data-marking.mitre.org/Marking-1': 'http://stix.mitre.org/XMLSchema/data_marking/1.0.1/data_marking.xsd',
         'http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1': 'http://stix.mitre.org/XMLSchema/extensions/marking/simple_marking/1.0.1/simple_marking.xsd',
         'http://data-marking.mitre.org/extensions/MarkingStructure#TLP-1': 'http://stix.mitre.org/XMLSchema/extensions/marking/tlp/1.0.1/tlp.xsd',
         'http://stix.mitre.org/Campaign-1': 'http://stix.mitre.org/XMLSchema/campaign/1.0.1/campaign.xsd',
         'http://stix.mitre.org/CourseOfAction-1': 'http://stix.mitre.org/XMLSchema/course_of_action/1.0.1/course_of_action.xsd',
         'http://stix.mitre.org/ExploitTarget-1': 'http://stix.mitre.org/XMLSchema/exploit_target/1.0.1/exploit_target.xsd',
         'http://stix.mitre.org/Incident-1': 'http://stix.mitre.org/XMLSchema/incident/1.0.1/incident.xsd',
         'http://stix.mitre.org/Indicator-2': 'http://stix.mitre.org/XMLSchema/indicator/2.0.1/indicator.xsd',
         'http://stix.mitre.org/TTP-1': 'http://stix.mitre.org/XMLSchema/ttp/1.0.1/ttp.xsd',
         'http://stix.mitre.org/ThreatActor-1': 'http://stix.mitre.org/XMLSchema/threat_actor/1.0.1/threat_actor.xsd',
         'http://stix.mitre.org/default_vocabularies-1': 'http://stix.mitre.org/XMLSchema/default_vocabularies/1.0.1/stix_default_vocabularies.xsd',
         'http://stix.mitre.org/extensions/AP#CAPEC2.6-1': 'http://stix.mitre.org/XMLSchema/extensions/attack_pattern/capec_2.6.1/1.0.1/capec_2.6.1.xsd',
         'http://stix.mitre.org/extensions/Address#CIQAddress3.0-1': 'http://stix.mitre.org/XMLSchema/extensions/address/ciq_address_3.0/1.0.1/ciq_address_3.0.xsd',
         'http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1': 'http://stix.mitre.org/XMLSchema/extensions/identity/ciq_identity_3.0/1.0.1/ciq_identity_3.0.xsd',
         'http://stix.mitre.org/extensions/Malware#MAEC4.0-1': 'http://stix.mitre.org/XMLSchema/extensions/malware/maec_4.0.1/1.0.1/maec_4.0.1.xsd',
         'http://stix.mitre.org/extensions/StructuredCOA#Generic-1': 'http://stix.mitre.org/XMLSchema/extensions/structured_coa/generic/1.0.1/generic.xsd',
         'http://stix.mitre.org/extensions/TestMechanism#Generic-1': 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/generic/1.0.1/generic.xsd',
         'http://stix.mitre.org/extensions/TestMechanism#OVAL5.10-1': 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/oval_5.10/1.0.1/oval_5.10.xsd',
         'http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1': 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/open_ioc_2010/1.0.1/open_ioc_2010.xsd',
         'http://stix.mitre.org/extensions/TestMechanism#Snort-1': 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/snort/1.0.1/snort.xsd',
         'http://stix.mitre.org/extensions/TestMechanism#YARA-1': 'http://stix.mitre.org/XMLSchema/extensions/test_mechanism/yara/1.0.1/yara.xsd',
         'http://stix.mitre.org/extensions/Vulnerability#CVRF-1': 'http://stix.mitre.org/XMLSchema/extensions/vulnerability/cvrf_1.1/1.0.1/cvrf_1.1.xsd'}

# Schema locations for namespaces not defined by STIX, but hosted on the STIX website     
EXT_NS_TO_SCHEMALOCATION = {'urn:oasis:names:tc:ciq:xpil:3' : 'http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xPIL.xsd',
                            'urn:oasis:names:tc:ciq:xnl:3' : 'http://stix.mitre.org/XMLSchema/external/oasis_ciq_3.0/xNL.xsd'}

# Default namespace->alias mappings. These can be overriden by user-provided dictionaries on export
DEFAULT_STIX_NS_TO_PREFIX = {
     'http://data-marking.mitre.org/Marking-1': 'marking',
     'http://data-marking.mitre.org/extensions/MarkingStructure#TLP-1': 'tlpMarking',
     'http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1': 'simpleMarking',
     'http://stix.mitre.org/Campaign-1': 'campaign',
     'http://stix.mitre.org/CourseOfAction-1': 'coa',
     'http://stix.mitre.org/ExploitTarget-1': 'et',
     'http://stix.mitre.org/Incident-1': 'incident',
     'http://stix.mitre.org/Indicator-2': 'indicator',
     'http://stix.mitre.org/TTP-1': 'ttp',
     'http://stix.mitre.org/ThreatActor-1': 'ta',
     'http://stix.mitre.org/common-1': 'stixCommon',
     'http://stix.mitre.org/default_vocabularies-1': 'stixVocabs',
     'http://stix.mitre.org/extensions/AP#CAPEC2.6-1': 'capecInstance',
     'http://stix.mitre.org/extensions/Address#CIQAddress3.0-1': 'ciqAddress',
     'http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1': 'ciqIdentity',
     'http://stix.mitre.org/extensions/Malware#MAEC4.0-1': 'maecInstance',
     'http://stix.mitre.org/extensions/StructuredCOA#Generic-1': 'genericStructuredCOA',
     'http://stix.mitre.org/extensions/TestMechanism#Generic-1': 'genericTM',
     'http://stix.mitre.org/extensions/TestMechanism#OVAL5.10-1': 'ovalTM',
     'http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1': 'openiocTM',
     'http://stix.mitre.org/extensions/TestMechanism#Snort-1': 'snortTM',
     'http://stix.mitre.org/extensions/TestMechanism#YARA-1': 'yaraTM',
     'http://stix.mitre.org/extensions/Vulnerability#CVRF-1': 'cvrfVuln',
     'http://stix.mitre.org/stix-1': 'stix',
     'http://www.icasi.org/CVRF/schema/common/1.1': 'cvrf-common',
     'http://www.icasi.org/CVRF/schema/cvrf/1.1': 'cvrf',
     'http://www.icasi.org/CVRF/schema/prod/1.1': 'prod',
     'http://www.icasi.org/CVRF/schema/vuln/1.1': 'vuln',
     'http://www.w3.org/1999/xlink': 'xlink',
     'http://www.w3.org/2000/09/xmldsig#': 'ds',
     'http://www.w3.org/2001/XMLSchema': 'xs',
     'http://www.w3.org/2001/XMLSchema-instance': 'xsi'}
             

DEFAULT_EXT_TO_PREFIX = {'urn:oasis:names:tc:ciq:xpil:3' : 'xpil',
                         'urn:oasis:names:tc:ciq:xnl:3' : 'xnl'}
