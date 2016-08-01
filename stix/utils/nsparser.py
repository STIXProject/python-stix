# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import mixbox.namespaces

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
for k, v in list(globals().items()):
    if k.startswith('NS_'):
        mixbox.namespaces.register_namespace(v)
        STIX_NAMESPACES.add_namespace(v)
