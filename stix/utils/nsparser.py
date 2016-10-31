# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import mixbox.namespaces

Namespace = mixbox.namespaces.Namespace

NS_CAMPAIGN_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/campaign-1", "campaign", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/campaign.xsd")
NS_CAPEC_OBJECT = Namespace("http://capec.mitre.org/capec-2", "capec", "")
NS_CIQIDENTITY_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/identity/ciq-3.0-identity-1", "ciqIdentity", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/identity/ciq-3.0-identity.xsd")
NS_COA_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/course-of-action-1", "coa", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/course-of-action.xsd")
NS_CVRF_OBJECT = Namespace("http://www.icasi.org/CVRF/schema/cvrf/1.1", "cvrf", "")
NS_ET_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/exploit-target-1", "et", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/exploit-target.xsd")
NS_GENERICSTRUCTUREDCOA_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/structured-coa/generic-1", "genericStructuredCOA", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/structured-coa/generic-structured-coa.xsd")
NS_GENERICTM_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/test-mechanism/generic-1", "genericTM", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/test-mechanism/generic-test-mechanism.xsd")
NS_INCIDENT_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/incident-1", "incident", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/incident.xsd")
NS_INDICATOR_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/indicator-1", "indicator", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/indicator.xsd")
NS_IOC_OBJECT = Namespace("http://schemas.mandiant.com/2010/ioc", "ioc", "")
NS_IOCTR_OBJECT = Namespace("http://schemas.mandiant.com/2010/ioc/TR/", "ioc-tr", "")
NS_MARKING_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/data-marking-1", "marking", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/data-marking.xsd")
NS_OVALDEF_OBJECT = Namespace("http://oval.mitre.org/XMLSchema/oval-definitions-5", "oval-def", "")
NS_OVALVAR_OBJECT = Namespace("http://oval.mitre.org/XMLSchema/oval-variables-5", "oval-var", "")
NS_REPORT_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/report-1", "report", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/report.xsd")
NS_SIMPLEMARKING_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/data-marking/simple-1", "simpleMarking", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/marking/simple-marking.xsd")
NS_SNORTTM_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/test-mechanism/snort-1", "snortTM", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/test-mechanism/snort-test-mechanism.xsd")
NS_STIX_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/core-1", "stix", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/core.xsd")
NS_STIXCAPEC_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/attack-pattern/capec-2.7-1", "stix-capec", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/attack-pattern/capec-2.7-attack-pattern.xsd")
NS_STIXCIQADDRESS_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/address/ciq-address-3.0-1", "stix-ciqaddress", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/address/ciq-3.0-address.xsd")
NS_STIXCVRF_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/vulnerability/cvrf-1", "stix-cvrf", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/vulnerability/cvrf-1.1-vulnerability.xsd")
NS_STIXMAEC_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/malware/maec-4.1-1", "stix-maec", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/malware/maec-4.1-malware.xsd")
NS_STIXOPENIOC_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/test-mechanism/openioc-2010-1", "stix-openioc", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/test-mechanism/openioc-2010-test-mechanism.xsd")
NS_STIXOVAL_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/test-mechanism/oval-5.10-1", "stix-oval", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/test-mechanism/oval-5.10-test-mechanism.xsd")
NS_STIXCOMMON_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/common-1", "stixCommon", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/common.xsd")
NS_STIXVOCABS_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/vocabularies-1", "stixVocabs", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/vocabularies.xsd")
NS_TA_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/threat-actor-1", "ta", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/threat-actor.xsd")
NS_TLPMARKING_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/data-marking/tlp-1", "tlpMarking", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/marking/tlp-marking.xsd")
NS_TOUMARKING_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/data-marking/terms-of-use-1", "TOUMarking", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/marking/terms-of-use-marking.xsd")
NS_TTP_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/ttp-1", "ttp", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/ttp.xsd")
NS_XAL_OBJECT = Namespace("urn:oasis:names:tc:ciq:xal:3", "xal", "http://docs.oasis-open.org/ciq/v3.0/prd03/xsd/default/xsd/xAL.xsd")
NS_XNL_OBJECT = Namespace("urn:oasis:names:tc:ciq:xnl:3", "xnl", "http://docs.oasis-open.org/ciq/v3.0/prd03/xsd/default/xsd/xNL.xsd")
NS_XPIL_OBJECT = Namespace("urn:oasis:names:tc:ciq:xpil:3", "xpil", "http://docs.oasis-open.org/ciq/v3.0/prd03/xsd/default/xsd/xPIL.xsd")
NS_YARATM_OBJECT = Namespace("http://docs.oasis-open.org/cti/ns/stix/extensions/test-mechanism/yara-1", "yaraTM", "http://docs.oasis-open.org/cti/stix/v1.2.1/csd01/xml-schemas/extensions/test-mechanism/yara-test-mechanism.xsd")

STIX_NAMESPACES = mixbox.namespaces.NamespaceSet()

# Magic to automatically register all Namespaces defined in this module.
for k, v in list(globals().items()):
    if k.startswith('NS_'):
        mixbox.namespaces.register_namespace(v)
        STIX_NAMESPACES.add_namespace(v)
