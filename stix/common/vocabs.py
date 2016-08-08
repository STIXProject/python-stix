# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
from functools import partial

# mixbox
from mixbox import fields
from mixbox import entities
from mixbox import typedlist

# stix
import stix
import stix.bindings.stix_common as stix_common_binding


def validate_value(instance, value):
    allowed = instance._ALLOWED_VALUES

    if not value:
        return
    elif not allowed:
        return
    elif value in allowed:
        return
    else:
        error = "Value must be one of {allowed}. Received '{value}'"
        error = error.format(**locals())
        raise ValueError(error)

class VocabList(typedlist.TypedList):
    """VocabString fields can be any type of VocabString, though there is often
    a preferred/default VocabString type.

    The TypedList will attempt to make sure that every input item is an instance
    of the default VocabString and throw an error if it isn't. This sublcass
    overrides that behavior and allows any instance of VocabString to be
    inserted.
    """

    def _is_valid(self, value):
        return isinstance(value, VocabString)


class VocabField(fields.TypedField):
    """TypedField subclass for VocabString fields."""

    def __init__(self, *args, **kwargs):
        """Intercepts the __init__() call to TypedField.

        Set the type that will be used in from_dict and from_obj calls to
        :class:`VocabString`.

        Set the type that will be used in ``__set__`` for casting as the
        original ``type_`` argument, or :class:`VocabString` if no `type_`
        argument was provided.

        """
        super(VocabField, self).__init__(*args, **kwargs)
        self.factory = VocabFactory  # force this factory

        if self._unresolved_type is None:
            self.type_ = VocabString

        self._listfunc = partial(VocabList, type=self._unresolved_type)

    def check_type(self, value):
        return isinstance(value, VocabString)


class VocabFactory(entities.EntityFactory):
    _convert_strings = True
    
    @classmethod
    def entity_class(cls, key):
        try:
            return stix.lookup_extension(key, default=VocabString)
        except ValueError:
            return VocabString


class VocabString(stix.Entity):
    _binding = stix_common_binding
    _binding_class = stix_common_binding.ControlledVocabularyStringType
    _namespace = 'http://stix.mitre.org/common-1'

    # All subclasses should override these
    _XSI_TYPE = None
    _ALLOWED_VALUES = None

    value = fields.TypedField("valueOf_", key_name="value", preset_hook=validate_value)
    vocab_name = fields.TypedField("vocab_name")
    vocab_reference = fields.TypedField("vocab_reference")
    xsi_type = fields.TypedField("xsi_type", key_name="xsi:type")

    def __init__(self, value=None):
        super(VocabString, self).__init__()
        self.value = value
        self.xsi_type = self._XSI_TYPE

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        # Check to make sure the values are identical.
        if isinstance(other, VocabString):
            other = other.value

        return other == self.value

    def is_plain(self):
        """Whether the VocabString can be represented as a single value."""
        return (
            self.xsi_type is None and
            self.vocab_name is None and
            self.vocab_reference is None
        )

    def to_dict(self):
        if self.is_plain():
            return self.value
        return super(VocabString, self).to_dict()


    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            vocab =  None
        elif not isinstance(cls_dict, dict):
            vocab = cls()
            vocab.value = cls_dict
        else:
            vocab = super(VocabString, cls).from_dict(cls_dict)

        return vocab


def _get_terms(vocab_class):
    """Helper function used by register_vocab."""
    for k, v in vars(vocab_class).items():
        if k.startswith("TERM_"):
            yield v


def add_vocab(cls):
    """Registers a VocabString subclass.

    Note:
        The :meth:`register_vocab` class decorator has replaced this method.

    """
    stix.add_extension(cls)


def register_vocab(cls):
    """Class decorator that registers a VocabString subclass.

    Also, calculate all the permitted values for class being decorated by
    adding an ``_ALLOWED_VALUES`` tuple of all the values of class members
    beginning with ``TERM_``.

    """
    add_vocab(cls)

    cls._ALLOWED_VALUES = tuple(_get_terms(cls))
    return cls


@register_vocab
class AvailabilityLossType_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:AvailabilityLossTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ACCELERATION = 'Acceleration'
    TERM_DEGREDATION = 'Degredation'
    TERM_DESTRUCTION = 'Destruction'
    TERM_INTERRUPTION = 'Interruption'
    TERM_LOSS = 'Loss'
    TERM_OBSCURATION = 'Obscuration'
    TERM_UNKNOWN = 'Unknown'


@register_vocab
class AvailabilityLossType_1_1_1(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:AvailabilityLossTypeVocab-1.1.1'
    _VOCAB_VERSION = '1.1.1'

    TERM_ACCELERATION = 'Acceleration'
    TERM_DEGRADATION = 'Degradation'
    TERM_DESTRUCTION = 'Destruction'
    TERM_INTERRUPTION = 'Interruption'
    TERM_LOSS = 'Loss'
    TERM_OBSCURATION = 'Obscuration'
    TERM_UNKNOWN = 'Unknown'


@register_vocab
class ThreatActorType_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:ThreatActorTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_CYBER_ESPIONAGE_OPERATIONS = "Cyber Espionage Operations"
    TERM_DISGRUNTLED_CUSTOMER_OR_USER = "Disgruntled Customer / User"
    TERM_ECRIME_ACTOR_CREDENTIAL_THEFT_BOTNET_OPERATOR = "eCrime Actor - Credential Theft Botnet Operator"
    TERM_ECRIME_ACTOR_CREDENTIAL_THEFT_BOTNET_SERVICE = "eCrime Actor - Credential Theft Botnet Service"
    TERM_ECRIME_ACTOR_MALWARE_DEVELOPER = "eCrime Actor - Malware Developer"
    TERM_ECRIME_ACTOR_MONEY_LAUNDERING_NETWORK = "eCrime Actor - Money Laundering Network"
    TERM_ECRIME_ACTOR_ORGANIZED_CRIME_ACTOR = "eCrime Actor - Organized Crime Actor"
    TERM_ECRIME_ACTOR_SPAM_SERVICE = "eCrime Actor - Spam Service"
    TERM_ECRIME_ACTOR_TRAFFIC_SERVICE = "eCrime Actor - Traffic Service"
    TERM_ECRIME_ACTOR_UNDERGROUND_CALL_SERVICE = "eCrime Actor - Underground Call Service"
    TERM_HACKER = "Hacker"
    TERM_HACKER_BLACK_HAT = "Hacker - Black hat"
    TERM_HACKER_GRAY_HAT = "Hacker - Gray hat"
    TERM_HACKER_WHITE_HAT = "Hacker - White hat"
    TERM_HACKTIVIST = "Hacktivist"
    TERM_INSIDER_THREAT = "Insider Threat"
    TERM_STATE_ACTOR_OR_AGENCY = "State Actor / Agency"


@register_vocab
class AttackerInfrastructureType_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:AttackerInfrastructureTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ANONYMIZATION = "Anonymization"
    TERM_ANONYMIZATION_PROXY = "Anonymization - Proxy"
    TERM_ANONYMIZATION_TOR_NETWORK = "Anonymization - TOR Network"
    TERM_ANONYMIZATION_VPN = "Anonymization - VPN"
    TERM_COMMUNICATIONS = "Communications"
    TERM_COMMUNICATIONS_BLOGS = "Communications - Blogs"
    TERM_COMMUNICATIONS_FORUMS = "Communications - Forums"
    TERM_COMMUNICATIONS_INTERNET_RELAY_CHAT = "Communications - Internet Relay Chat"
    TERM_COMMUNICATIONS_MICROBLOGS = "Communications - Micro-Blogs"
    TERM_COMMUNICATIONS_MOBILE_COMMUNICATIONS = "Communications - Mobile Communications"
    TERM_COMMUNICATIONS_SOCIAL_NETWORKS = "Communications - Social Networks"
    TERM_COMMUNICATIONS_USERGENERATED_CONTENT_WEBSITES = "Communications - User-Generated Content Websites"
    TERM_DOMAIN_REGISTRATION = "Domain Registration"
    TERM_DOMAIN_REGISTRATION_DYNAMIC_DNS_SERVICES = "Domain Registration - Dynamic DNS Services"
    TERM_DOMAIN_REGISTRATION_LEGITIMATE_DOMAIN_REGISTRATION_SERVICES = "Domain Registration - Legitimate Domain Registration Services"
    TERM_DOMAIN_REGISTRATION_MALICIOUS_DOMAIN_REGISTRARS = "Domain Registration - Malicious Domain Registrars"
    TERM_DOMAIN_REGISTRATION_TOPLEVEL_DOMAIN_REGISTRARS = "Domain Registration - Top-Level Domain Registrars"
    TERM_ELECTRONIC_PAYMENT_METHODS = "Electronic Payment Methods"
    TERM_HOSTING = "Hosting"
    TERM_HOSTING_BULLETPROOF_OR_ROGUE_HOSTING = "Hosting - Bulletproof / Rogue Hosting"
    TERM_HOSTING_CLOUD_HOSTING = "Hosting - Cloud Hosting"
    TERM_HOSTING_COMPROMISED_SERVER = "Hosting - Compromised Server"
    TERM_HOSTING_FAST_FLUX_BOTNET_HOSTING = "Hosting - Fast Flux Botnet Hosting"
    TERM_HOSTING_LEGITIMATE_HOSTING = "Hosting - Legitimate Hosting"


@register_vocab
class DiscoveryMethod_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:DiscoveryMethodVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_AGENT_DISCLOSURE = "Agent Disclosure"
    TERM_ANTIVIRUS = "Antivirus"
    TERM_AUDIT = "Audit"
    TERM_CUSTOMER = "Customer"
    TERM_FINANCIAL_AUDIT = "Financial Audit"
    TERM_FRAUD_DETECTION = "Fraud Detection"
    TERM_HIPS = "HIPS"
    TERM_INCIDENT_RESPONSE = "Incident Response"
    TERM_IT_AUDIT = "IT Audit"
    TERM_LAW_ENFORCEMENT = "Law Enforcement"
    TERM_LOG_REVIEW = "Log Review"
    TERM_MONITORING_SERVICE = "Monitoring Service"
    TERM_NIDS = "NIDS"
    TERM_SECURITY_ALARM = "Security Alarm"
    TERM_UNKNOWN = "Unknown"
    TERM_UNRELATED_PARTY = "Unrelated Party"
    TERM_USER = "User"

@register_vocab
class DiscoveryMethod_2_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:DiscoveryMethodVocab-2.0'
    _VOCAB_VERSION = '2.0'

    TERM_AGENT_DISCLOSURE = "Agent Disclosure"
    TERM_ANTIVIRUS = "Antivirus"
    TERM_AUDIT = "Audit"
    TERM_CUSTOMER = "Customer"
    TERM_EXTERNAL_FRAUD_DETECTION = "External - Fraud Detection"
    TERM_FINANCIAL_AUDIT = "Financial Audit"
    TERM_HIPS = "HIPS"
    TERM_INCIDENT_RESPONSE = "Incident Response"
    TERM_INTERNAL_FRAUD_DETECTION = "Internal - Fraud Detection"
    TERM_IT_AUDIT = "IT Audit"
    TERM_LAW_ENFORCEMENT = "Law Enforcement"
    TERM_LOG_REVIEW = "Log Review"
    TERM_MONITORING_SERVICE = "Monitoring Service"
    TERM_NIDS = "NIDS"
    TERM_SECURITY_ALARM = "Security Alarm"
    TERM_UNKNOWN = "Unknown"
    TERM_UNRELATED_PARTY = "Unrelated Party"
    TERM_USER = "User"


@register_vocab
class AttackerToolType_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:AttackerToolTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_APPLICATION_SCANNER = "Application Scanner"
    TERM_MALWARE = "Malware"
    TERM_PASSWORD_CRACKING = "Password Cracking"
    TERM_PENETRATION_TESTING = "Penetration Testing"
    TERM_PORT_SCANNER = "Port Scanner"
    TERM_TRAFFIC_SCANNER = "Traffic Scanner"
    TERM_VULNERABILITY_SCANNER = "Vulnerability Scanner"


@register_vocab
class IndicatorType_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IndicatorTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ANONYMIZATION = 'Anonymization'
    TERM_C2 = 'C2'
    TERM_DOMAIN_WATCHLIST = 'Domain Watchlist'
    TERM_EXFILTRATION = 'Exfiltration'
    TERM_FILE_HASH_WATCHLIST = 'File Hash Watchlist'
    TERM_HOST_CHARACTERISTICS = 'Host Characteristics'
    TERM_IP_WATCHLIST = 'IP Watchlist'
    TERM_MALICIOUS_EMAIL = 'Malicious E-mail'
    TERM_MALWARE_ARTIFACTS = 'Malware Artifacts'
    TERM_URL_WATCHLIST = 'URL Watchlist'


@register_vocab
class IndicatorType_1_1(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IndicatorTypeVocab-1.1'
    _VOCAB_VERSION = '1.1'

    TERM_ANONYMIZATION = 'Anonymization'
    TERM_C2 = 'C2'
    TERM_COMPROMISED_PKI_CERTIFICATE = 'Compromised PKI Certificate'
    TERM_DOMAIN_WATCHLIST = 'Domain Watchlist'
    TERM_EXFILTRATION = 'Exfiltration'
    TERM_FILE_HASH_WATCHLIST = 'File Hash Watchlist'
    TERM_HOST_CHARACTERISTICS = 'Host Characteristics'
    TERM_IMEI_WATCHLIST = 'IMEI Watchlist'
    TERM_IMSI_WATCHLIST = 'IMSI Watchlist'
    TERM_IP_WATCHLIST = 'IP Watchlist'
    TERM_LOGIN_NAME = 'Login Name'
    TERM_MALICIOUS_EMAIL = 'Malicious E-mail'
    TERM_MALWARE_ARTIFACTS = 'Malware Artifacts'
    TERM_URL_WATCHLIST = 'URL Watchlist'


@register_vocab
class SystemType_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:SystemTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ENTERPRISE_SYSTEMS = "Enterprise Systems"
    TERM_ENTERPRISE_SYSTEMS_APPLICATION_LAYER = "Enterprise Systems - Application Layer"
    TERM_ENTERPRISE_SYSTEMS_DATABASE_LAYER = "Enterprise Systems - Database Layer"
    TERM_ENTERPRISE_SYSTEMS_ENTERPRISE_TECHNOLOGIES_AND_SUPPORT_INFRASTRUCTURE = "Enterprise Systems - Enterprise Technologies and Support Infrastructure"
    TERM_ENTERPRISE_SYSTEMS_NETWORKING_DEVICES = "Enterprise Systems - Networking Devices"
    TERM_ENTERPRISE_SYSTEMS_NETWORK_SYSTEMS = "Enterprise Systems - Network Systems"
    TERM_ENTERPRISE_SYSTEMS_VOIP = "Enterprise Systems - VoIP"
    TERM_ENTERPRISE_SYSTEMS_WEB_LAYER = "Enterprise Systems - Web Layer"
    TERM_INDUSTRIAL_CONTROL_SYSTEMS = "Industrial Control Systems"
    TERM_INDUSTRIAL_CONTROL_SYSTEMS_EQUIPMENT_UNDER_CONTROL = "Industrial Control Systems - Equipment Under Control"
    TERM_INDUSTRIAL_CONTROL_SYSTEMS_OPERATIONS_MANAGEMENT = "Industrial Control Systems - Operations Management"
    TERM_INDUSTRIAL_CONTROL_SYSTEMS_SAFETY_PROTECTION_AND_LOCAL_CONTROL = "Industrial Control Systems - Safety, Protection and Local Control"
    TERM_INDUSTRIAL_CONTROL_SYSTEMS_SUPERVISORY_CONTROL = "Industrial Control Systems - Supervisory Control"
    TERM_MOBILE_SYSTEMS = "Mobile Systems"
    TERM_MOBILE_SYSTEMS_MOBILE_DEVICES = "Mobile Systems - Mobile Devices"
    TERM_MOBILE_SYSTEMS_MOBILE_OPERATING_SYSTEMS = "Mobile Systems - Mobile Operating Systems"
    TERM_MOBILE_SYSTEMS_NEAR_FIELD_COMMUNICATIONS = "Mobile Systems - Near Field Communications"
    TERM_THIRDPARTY_SERVICES = "Third-Party Services"
    TERM_THIRDPARTY_SERVICES_APPLICATION_STORES = "Third-Party Services - Application Stores"
    TERM_THIRDPARTY_SERVICES_CLOUD_SERVICES = "Third-Party Services - Cloud Services"
    TERM_THIRDPARTY_SERVICES_SECURITY_VENDORS = "Third-Party Services - Security Vendors"
    TERM_THIRDPARTY_SERVICES_SOCIAL_MEDIA = "Third-Party Services - Social Media"
    TERM_THIRDPARTY_SERVICES_SOFTWARE_UPDATE = "Third-Party Services - Software Update"
    TERM_USERS = "Users"
    TERM_USERS_APPLICATION_AND_SOFTWARE = "Users - Application And Software"
    TERM_USERS_REMOVABLE_MEDIA = "Users - Removable Media"
    TERM_USERS_WORKSTATION = "Users - Workstation"


@register_vocab
class CampaignStatus_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:CampaignStatusVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_FUTURE = "Future"
    TERM_HISTORIC = "Historic"
    TERM_ONGOING = "Ongoing"


@register_vocab
class IncidentStatus_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IncidentStatusVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_CLOSED = "Closed"
    TERM_CONTAINMENT_ACHIEVED = "Containment Achieved"
    TERM_DELETED = "Deleted"
    TERM_INCIDENT_REPORTED = "Incident Reported"
    TERM_NEW = "New"
    TERM_OPEN = "Open"
    TERM_REJECTED = "Rejected"
    TERM_RESTORATION_ACHIEVED = "Restoration Achieved"
    TERM_STALLED = "Stalled"


@register_vocab
class ManagementClass_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:ManagementClassVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_COMANAGEMENT = "Co-Management"
    TERM_EXTERNALLYMANAGEMENT = "Externally-Management"
    TERM_INTERNALLYMANAGED = "Internally-Managed"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class Motivation_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:MotivationVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_EGO = 'Ego'
    TERM_FINANCIAL_OR_ECONOMIC = 'Financial or Economic'
    TERM_IDEOLOGICAL = 'Ideological'
    TERM_IDEOLOGICAL_ANTICORRUPTION = 'Ideological - Anti-Corruption'
    TERM_IDEOLOGICAL_ANTIESTABLISMENT = 'Ideological - Anti-Establisment'
    TERM_IDEOLOGICAL_ENVIRONMENTAL = 'Ideological - Environmental'
    TERM_IDEOLOGICAL_ETHNIC_NATIONALIST = 'Ideological - Ethnic / Nationalist'
    TERM_IDEOLOGICAL_HUMAN_RIGHTS = 'Ideological - Human Rights'
    TERM_IDEOLOGICAL_INFORMATION_FREEDOM = 'Ideological - Information Freedom'
    TERM_IDEOLOGICAL_RELIGIOUS = 'Ideological - Religious'
    TERM_IDEOLOGICAL_SECURITY_AWARENESS = 'Ideological - Security Awareness'
    TERM_MILITARY = 'Military'
    TERM_OPPORTUNISTIC = 'Opportunistic'
    TERM_POLICITAL = 'Policital'


@register_vocab
class Motivation_1_0_1(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:MotivationVocab-1.0.1'
    _VOCAB_VERSION = '1.0.1'

    TERM_EGO = 'Ego'
    TERM_FINANCIAL_OR_ECONOMIC = 'Financial or Economic'
    TERM_IDEOLOGICAL = 'Ideological'
    TERM_IDEOLOGICAL_ANTI_CORRUPTION = 'Ideological - Anti-Corruption'
    TERM_IDEOLOGICAL_ANTI_ESTABLISHMENT = 'Ideological - Anti-Establishment'
    TERM_IDEOLOGICAL_ENVIRONMENTAL = 'Ideological - Environmental'
    TERM_IDEOLOGICAL_ETHNIC_NATIONALIST = 'Ideological - Ethnic / Nationalist'
    TERM_IDEOLOGICAL_HUMAN_RIGHTS = 'Ideological - Human Rights'
    TERM_IDEOLOGICAL_INFORMATION_FREEDOM = 'Ideological - Information Freedom'
    TERM_IDEOLOGICAL_SECURITY_AWARENESS = 'Ideological - Security Awareness'
    TERM_IDEOLOGICAL__RELIGIOUS = 'Ideological - Religious'
    TERM_MILITARY = 'Military'
    TERM_OPPORTUNISTIC = 'Opportunistic'
    TERM_POLICITAL = 'Policital'


@register_vocab
class Motivation_1_1(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:MotivationVocab-1.1'
    _VOCAB_VERSION = '1.1'

    TERM_EGO = 'Ego'
    TERM_FINANCIAL_OR_ECONOMIC = 'Financial or Economic'
    TERM_IDEOLOGICAL = 'Ideological'
    TERM_IDEOLOGICAL_ANTICORRUPTION = 'Ideological - Anti-Corruption'
    TERM_IDEOLOGICAL_ANTIESTABLISHMENT = 'Ideological - Anti-Establishment'
    TERM_IDEOLOGICAL_ENVIRONMENTAL = 'Ideological - Environmental'
    TERM_IDEOLOGICAL_ETHNIC_NATIONALIST = 'Ideological - Ethnic / Nationalist'
    TERM_IDEOLOGICAL_HUMAN_RIGHTS = 'Ideological - Human Rights'
    TERM_IDEOLOGICAL_INFORMATION_FREEDOM = 'Ideological - Information Freedom'
    TERM_IDEOLOGICAL_RELIGIOUS = 'Ideological - Religious'
    TERM_IDEOLOGICAL_SECURITY_AWARENESS = 'Ideological - Security Awareness'
    TERM_MILITARY = 'Military'
    TERM_OPPORTUNISTIC = 'Opportunistic'
    TERM_POLITICAL = 'Political'


@register_vocab
class IncidentCategory_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IncidentCategoryVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_DENIAL_OF_SERVICE = "Denial of Service"
    TERM_EXERCISEORNETWORK_DEFENSE_TESTING = "Exercise/Network Defense Testing"
    TERM_IMPROPER_USAGE = "Improper Usage"
    TERM_INVESTIGATION = "Investigation"
    TERM_MALICIOUS_CODE = "Malicious Code"
    TERM_SCANSORPROBESORATTEMPTED_ACCESS = "Scans/Probes/Attempted Access"
    TERM_UNAUTHORIZED_ACCESS = "Unauthorized Access"


@register_vocab
class ImpactQualification_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:ImpactQualificationVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_CATASTROPHIC = "Catastrophic"
    TERM_DAMAGING = "Damaging"
    TERM_DISTRACTING = "Distracting"
    TERM_INSIGNIFICANT = "Insignificant"
    TERM_PAINFUL = "Painful"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class PlanningAndOperationalSupport_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:PlanningAndOperationalSupportVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_DATA_EXPLOITATION = 'Data Exploitation'
    TERM_DATA_EXPLOITATION_ANALYTIC_SUPPORT = 'Data Exploitation - Analytic Support'
    TERM_DATA_EXPLOITATION_TRANSLATION_SUPPORT = 'Data Exploitation - Translation Support'
    TERM_FINANCIAL_RESOURCES = 'Financial Resources'
    TERM_FINANCIAL_RESOURCES_ACADEMIC = 'Financial Resources - Academic'
    TERM_FINANCIAL_RESOURCES_COMMERCIAL = 'Financial Resources - Commercial'
    TERM_FINANCIAL_RESOURCES_GOVERNMENT = 'Financial Resources - Government'
    TERM_FINANCIAL_RESOURCES_HACKTIVIST_OR_GRASSROOT = 'Financial Resources - Hacktivist or Grassroot'
    TERM_FINANCIAL_RESOURCES_NONATTRIBUTABLE_FINANCE = 'Financial Resources - Non-Attributable Finance'
    TERM_PLANNING = 'Planning '
    TERM_PLANNING_OPEN_SOURCE_INTELLIGENCE_OSINT_GETHERING = 'Planning - Open-Source Intelligence (OSINT) Gethering'
    TERM_PLANNING_OPERATIONAL_COVER_PLAN = 'Planning - Operational Cover Plan'
    TERM_PLANNING_PRE_OPERATIONAL_SURVEILLANCE_AND_RECONNAISSANCE = 'Planning - Pre-Operational Surveillance and Reconnaissance'
    TERM_PLANNING_TARGET_SELECTION = 'Planning - Target Selection'
    TERM_SKILL_DEVELOPMENT_RECRUITMENT = 'Skill Development / Recruitment'
    TERM_SKILL_DEVELOPMENT_RECRUITMENT_CONTRACTING_AND_HIRING = 'Skill Development / Recruitment - Contracting and Hiring'
    TERM_SKILL_DEVELOPMENT_RECRUITMENT_DOCUMENT_EXPLOITATION_DOCEX_TRAINING = 'Skill Development / Recruitment - Document Exploitation (DOCEX) Training'
    TERM_SKILL_DEVELOPMENT_RECRUITMENT_INTERNAL_TRAINING = 'Skill Development / Recruitment - Internal Training'
    TERM_SKILL_DEVELOPMENT_RECRUITMENT_MILITARY_PROGRAMS = 'Skill Development / Recruitment - Military Programs'
    TERM_SKILL_DEVELOPMENT_RECRUITMENT_SECURITY_HACKER_CONFERENCES = 'Skill Development / Recruitment - Security / Hacker Conferences'
    TERM_SKILL_DEVELOPMENT_RECRUITMENT_UNDERGROUND_FORUMS = 'Skill Development / Recruitment - Underground Forums'
    TERM_SKILL_DEVELOPMENT_RECRUITMENT_UNIVERSITY_PROGRAMS = 'Skill Development / Recruitment - University Programs'


@register_vocab
class PlanningAndOperationalSupport_1_0_1(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:PlanningAndOperationalSupportVocab-1.0.1'
    _VOCAB_VERSION = '1.0.1'

    TERM_DATA_EXPLOITATION = "Data Exploitation"
    TERM_DATA_EXPLOITATION_ANALYTIC_SUPPORT = "Data Exploitation - Analytic Support"
    TERM_DATA_EXPLOITATION_TRANSLATION_SUPPORT = "Data Exploitation - Translation Support"
    TERM_FINANCIAL_RESOURCES = "Financial Resources"
    TERM_FINANCIAL_RESOURCES_ACADEMIC = "Financial Resources - Academic"
    TERM_FINANCIAL_RESOURCES_COMMERCIAL = "Financial Resources - Commercial"
    TERM_FINANCIAL_RESOURCES_GOVERNMENT = "Financial Resources - Government"
    TERM_FINANCIAL_RESOURCES_HACKTIVIST_OR_GRASSROOT = "Financial Resources - Hacktivist or Grassroot"
    TERM_FINANCIAL_RESOURCES_NONATTRIBUTABLE_FINANCE = "Financial Resources - Non-Attributable Finance"
    TERM_PLANNING = "Planning"
    TERM_PLANNING_OPENSOURCE_INTELLIGENCE_OSINT_GATHERING = "Planning - Open-Source Intelligence (OSINT) Gathering"
    TERM_PLANNING_OPERATIONAL_COVER_PLAN = "Planning - Operational Cover Plan"
    TERM_PLANNING_PREOPERATIONAL_SURVEILLANCE_AND_RECONNAISSANCE = "Planning - Pre-Operational Surveillance and Reconnaissance"
    TERM_PLANNING_TARGET_SELECTION = "Planning - Target Selection"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT = "Skill Development / Recruitment"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_CONTRACTING_AND_HIRING = "Skill Development / Recruitment - Contracting and Hiring"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_DOCUMENT_EXPLOITATION_DOCEX_TRAINING = "Skill Development / Recruitment - Document Exploitation (DOCEX) Training"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_INTERNAL_TRAINING = "Skill Development / Recruitment - Internal Training"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_MILITARY_PROGRAMS = "Skill Development / Recruitment - Military Programs"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_SECURITY_OR_HACKER_CONFERENCES = "Skill Development / Recruitment - Security / Hacker Conferences"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_UNDERGROUND_FORUMS = "Skill Development / Recruitment - Underground Forums"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_UNIVERSITY_PROGRAMS = "Skill Development / Recruitment - University Programs"


@register_vocab
class CourseOfActionType_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:CourseOfActionTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_DIPLOMATIC_ACTIONS = "Diplomatic Actions"
    TERM_ERADICATION = "Eradication"
    TERM_HARDENING = "Hardening"
    TERM_INTERNAL_BLOCKING = "Internal Blocking"
    TERM_LOGICAL_ACCESS_RESTRICTIONS = "Logical Access Restrictions"
    TERM_MONITORING = "Monitoring"
    TERM_OTHER = "Other"
    TERM_PATCHING = "Patching"
    TERM_PERIMETER_BLOCKING = "Perimeter Blocking"
    TERM_PHYSICAL_ACCESS_RESTRICTIONS = "Physical Access Restrictions"
    TERM_POLICY_ACTIONS = "Policy Actions"
    TERM_PUBLIC_DISCLOSURE = "Public Disclosure"
    TERM_REBUILDING = "Rebuilding"
    TERM_REDIRECTION = "Redirection"
    TERM_REDIRECTION_HONEY_POT = "Redirection (Honey Pot)"
    TERM_TRAINING = "Training"


@register_vocab
class SecurityCompromise_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:SecurityCompromiseVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_NO = "No"
    TERM_SUSPECTED = "Suspected"
    TERM_UNKNOWN = "Unknown"
    TERM_YES = "Yes"


@register_vocab
class ImpactRating_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:ImpactRatingVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_MAJOR = "Major"
    TERM_MINOR = "Minor"
    TERM_MODERATE = "Moderate"
    TERM_NONE = "None"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class AssetType_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:AssetTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'


    TERM_ACCESS_READER = "Access reader"
    TERM_ADMINISTRATOR = "Administrator"
    TERM_ATM = "ATM"
    TERM_AUDITOR = "Auditor"
    TERM_AUTH_TOKEN = "Auth token"
    TERM_BACKUP = "Backup"
    TERM_BROADBAND = "Broadband"
    TERM_CALL_CENTER = "Call center"
    TERM_CAMERA = "Camera"
    TERM_CASHIER = "Cashier"
    TERM_CUSTOMER = "Customer"
    TERM_DATABASE = "Database"
    TERM_DCS = "DCS"
    TERM_DESKTOP = "Desktop"
    TERM_DEVELOPER = "Developer"
    TERM_DHCP = "DHCP"
    TERM_DIRECTORY = "Directory"
    TERM_DISK_DRIVE = "Disk drive"
    TERM_DISK_MEDIA = "Disk media"
    TERM_DNS = "DNS"
    TERM_DOCUMENTS = "Documents"
    TERM_ENDUSER = "End-user"
    TERM_EXECUTIVE = "Executive"
    TERM_FILE = "File"
    TERM_FINANCE = "Finance"
    TERM_FIREWALL = "Firewall"
    TERM_FLASH_DRIVE = "Flash drive"
    TERM_FORMER_EMPLOYEE = "Former employee"
    TERM_GAS_TERMINAL = "Gas terminal"
    TERM_GUARD = "Guard"
    TERM_HELPDESK = "Helpdesk"
    TERM_HSM = "HSM"
    TERM_HUMAN_RESOURCES = "Human resources"
    TERM_IDS = "IDS"
    TERM_KIOSK = "Kiosk"
    TERM_LAN = "LAN"
    TERM_LAPTOP = "Laptop"
    TERM_LOG = "Log"
    TERM_MAIL = "Mail"
    TERM_MAINFRAME = "Mainframe"
    TERM_MAINTENANCE = "Maintenance"
    TERM_MANAGER = "Manager"
    TERM_MEDIA = "Media"
    TERM_MOBILE_PHONE = "Mobile phone"
    TERM_NETWORK = "Network"
    TERM_PARTNER = "Partner"
    TERM_PAYMENT_CARD = "Payment card"
    TERM_PAYMENT_SWITCH = "Payment switch"
    TERM_PBX = "PBX"
    TERM_PED_PAD = "PED pad"
    TERM_PERIPHERAL = "Peripheral"
    TERM_PERSON = "Person"
    TERM_PLC = "PLC"
    TERM_POS_CONTROLLER = "POS controller"
    TERM_POS_TERMINAL = "POS terminal"
    TERM_PRINT = "Print"
    TERM_PRIVATE_WAN = "Private WAN"
    TERM_PROXY = "Proxy"
    TERM_PUBLIC_WAN = "Public WAN"
    TERM_REMOTE_ACCESS = "Remote access"
    TERM_ROUTER_OR_SWITCH = "Router or switch"
    TERM_RTU = "RTU"
    TERM_SAN = "SAN"
    TERM_SCADA = "SCADA"
    TERM_SERVER = "Server"
    TERM_SMART_CARD = "Smart card"
    TERM_TABLET = "Tablet"
    TERM_TAPES = "Tapes"
    TERM_TELEPHONE = "Telephone"
    TERM_UNKNOWN = "Unknown"
    TERM_USER_DEVICE = "User Device"
    TERM_VOIP_ADAPTER = "VoIP adapter"
    TERM_VOIP_PHONE = "VoIP phone"
    TERM_WEB_APPLICATION = "Web application"
    TERM_WLAN = "WLAN"

@register_vocab
class COAStage_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:COAStageVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_REMEDY = "Remedy"
    TERM_RESPONSE = "Response"


@register_vocab
class LocationClass_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:LocationClassVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_COLOCATED = "Co-Located"
    TERM_EXTERNALLYLOCATED = "Externally-Located"
    TERM_INTERNALLYLOCATED = "Internally-Located"
    TERM_MOBILE = "Mobile"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class InformationType_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:InformationTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_AUTHENTICATION_COOKIES = "Authentication Cookies"
    TERM_INFORMATION_ASSETS = "Information Assets"
    TERM_INFORMATION_ASSETS_CORPORATE_EMPLOYEE_INFORMATION = "Information Assets - Corporate Employee Information"
    TERM_INFORMATION_ASSETS_CUSTOMER_PII = "Information Assets - Customer PII"
    TERM_INFORMATION_ASSETS_EMAIL_LISTS_OR_ARCHIVES = "Information Assets - Email Lists / Archives"
    TERM_INFORMATION_ASSETS_FINANCIAL_DATA = "Information Assets - Financial Data"
    TERM_INFORMATION_ASSETS_INTELLECTUAL_PROPERTY = "Information Assets - Intellectual Property"
    TERM_INFORMATION_ASSETS_MOBILE_PHONE_CONTACTS = "Information Assets - Mobile Phone Contacts"
    TERM_INFORMATION_ASSETS_USER_CREDENTIALS = "Information Assets - User Credentials"


@register_vocab
class ThreatActorSophistication_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:ThreatActorSophisticationVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ASPIRANT = "Aspirant"
    TERM_EXPERT = "Expert"
    TERM_INNOVATOR = "Innovator"
    TERM_NOVICE = "Novice"
    TERM_PRACTITIONER = "Practitioner"


@register_vocab
class HighMediumLow_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:HighMediumLowVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_HIGH = "High"
    TERM_LOW = "Low"
    TERM_MEDIUM = "Medium"
    TERM_NONE = "None"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class LossProperty_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:LossPropertyVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ACCOUNTABILITY = "Accountability"
    TERM_AVAILABILITY = "Availability"
    TERM_CONFIDENTIALITY = "Confidentiality"
    TERM_INTEGRITY = "Integrity"
    TERM_NONREPUDIATION = "Non-Repudiation"


@register_vocab
class IntendedEffect_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IntendedEffectVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ACCOUNT_TAKEOVER = "Account Takeover"
    TERM_ADVANTAGE = "Advantage"
    TERM_ADVANTAGE_ECONOMIC = "Advantage - Economic"
    TERM_ADVANTAGE_MILITARY = "Advantage - Military"
    TERM_ADVANTAGE_POLITICAL = "Advantage - Political"
    TERM_BRAND_DAMAGE = "Brand Damage"
    TERM_COMPETITIVE_ADVANTAGE = "Competitive Advantage"
    TERM_DEGRADATION_OF_SERVICE = "Degradation of Service"
    TERM_DENIAL_AND_DECEPTION = "Denial and Deception"
    TERM_DESTRUCTION = "Destruction"
    TERM_DISRUPTION = "Disruption"
    TERM_EMBARRASSMENT = "Embarrassment"
    TERM_EXPOSURE = "Exposure"
    TERM_EXTORTION = "Extortion"
    TERM_FRAUD = "Fraud"
    TERM_HARASSMENT = "Harassment"
    TERM_ICS_CONTROL = "ICS Control"
    TERM_THEFT = "Theft"
    TERM_THEFT_CREDENTIAL_THEFT = "Theft - Credential Theft"
    TERM_THEFT_IDENTITY_THEFT = "Theft - Identity Theft"
    TERM_THEFT_INTELLECTUAL_PROPERTY = "Theft - Intellectual Property"
    TERM_THEFT_THEFT_OF_PROPRIETARY_INFORMATION = "Theft - Theft of Proprietary Information"
    TERM_TRAFFIC_DIVERSION = "Traffic Diversion"
    TERM_UNAUTHORIZED_ACCESS = "Unauthorized Access"


@register_vocab
class PackageIntent_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:PackageIntentVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ATTACK_PATTERN_CHARACTERIZATION = "Attack Pattern Characterization"
    TERM_CAMPAIGN_CHARACTERIZATION = "Campaign Characterization"
    TERM_COLLECTIVE_THREAT_INTELLIGENCE = "Collective Threat Intelligence"
    TERM_COURSES_OF_ACTION = "Courses of Action"
    TERM_EXPLOIT_CHARACTERIZATION = "Exploit Characterization"
    TERM_INCIDENT = "Incident"
    TERM_INDICATORS = "Indicators"
    TERM_INDICATORS_ENDPOINT_CHARACTERISTICS = "Indicators - Endpoint Characteristics"
    TERM_INDICATORS_MALWARE_ARTIFACTS = "Indicators - Malware Artifacts"
    TERM_INDICATORS_NETWORK_ACTIVITY = "Indicators - Network Activity"
    TERM_INDICATORS_PHISHING = "Indicators - Phishing"
    TERM_INDICATORS_WATCHLIST = "Indicators - Watchlist"
    TERM_MALWARE_CHARACTERIZATION = "Malware Characterization"
    TERM_MALWARE_SAMPLES = "Malware Samples"
    TERM_OBSERVATIONS = "Observations"
    TERM_OBSERVATIONS_EMAIL = "Observations - Email"
    TERM_THREAT_ACTOR_CHARACTERIZATION = "Threat Actor Characterization"
    TERM_THREAT_REPORT = "Threat Report"
    TERM_TTP_INFRASTRUCTURE = "TTP - Infrastructure"
    TERM_TTP_TOOLS = "TTP - Tools"


@register_vocab
class ReportIntent_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:ReportIntentVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ATTACK_PATTERN_CHARACTERIZATION = "Attack Pattern Characterization"
    TERM_CAMPAIGN_CHARACTERIZATION = "Campaign Characterization"
    TERM_COLLECTIVE_THREAT_INTELLIGENCE = "Collective Threat Intelligence"
    TERM_COURSES_OF_ACTION = "Courses of Action"
    TERM_EXPLOIT_CHARACTERIZATION = "Exploit Characterization"
    TERM_INCIDENT = "Incident"
    TERM_INDICATORS = "Indicators"
    TERM_INDICATORS_ENDPOINT_CHARACTERISTICS = "Indicators - Endpoint Characteristics"
    TERM_INDICATORS_MALWARE_ARTIFACTS = "Indicators - Malware Artifacts"
    TERM_INDICATORS_NETWORK_ACTIVITY = "Indicators - Network Activity"
    TERM_INDICATORS_PHISHING = "Indicators - Phishing"
    TERM_INDICATORS_WATCHLIST = "Indicators - Watchlist"
    TERM_MALWARE_CHARACTERIZATION = "Malware Characterization"
    TERM_MALWARE_SAMPLES = "Malware Samples"
    TERM_OBSERVATIONS = "Observations"
    TERM_OBSERVATIONS_EMAIL = "Observations - Email"
    TERM_THREAT_ACTOR_CHARACTERIZATION = "Threat Actor Characterization"
    TERM_THREAT_REPORT = "Threat Report"
    TERM_TTP_INFRASTRUCTURE = "TTP - Infrastructure"
    TERM_TTP_TOOLS = "TTP - Tools"


@register_vocab
class LossDuration_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:LossDurationVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_DAYS = "Days"
    TERM_HOURS = "Hours"
    TERM_MINUTES = "Minutes"
    TERM_PERMANENT = "Permanent"
    TERM_SECONDS = "Seconds"
    TERM_UNKNOWN = "Unknown"
    TERM_WEEKS = "Weeks"


@register_vocab
class OwnershipClass_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:OwnershipClassVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_CUSTOMEROWNED = "Customer-Owned"
    TERM_EMPLOYEEOWNED = "Employee-Owned"
    TERM_INTERNALLYOWNED = "Internally-Owned"
    TERM_PARTNEROWNED = "Partner-Owned"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class MalwareType_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:MalwareTypeVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_ADWARE = "Adware"
    TERM_AUTOMATED_TRANSFER_SCRIPTS = "Automated Transfer Scripts"
    TERM_BOT = "Bot"
    TERM_BOT_CREDENTIAL_THEFT = "Bot - Credential Theft"
    TERM_BOT_DDOS = "Bot - DDoS"
    TERM_BOT_LOADER = "Bot - Loader"
    TERM_BOT_SPAM = "Bot - Spam"
    TERM_DIALER = "Dialer"
    TERM_DOS_OR_DDOS = "DoS / DDoS"
    TERM_DOS_OR_DDOS_PARTICIPATORY = "DoS / DDoS - Participatory"
    TERM_DOS_OR_DDOS_SCRIPT = "DoS / DDoS - Script"
    TERM_DOS_OR_DDOS_STRESS_TEST_TOOLS = "DoS / DDoS - Stress Test Tools"
    TERM_EXPLOIT_KITS = "Exploit Kits"
    TERM_POS_OR_ATM_MALWARE = "POS / ATM Malware"
    TERM_RANSOMWARE = "Ransomware"
    TERM_REMOTE_ACCESS_TROJAN = "Remote Access Trojan"
    TERM_ROGUE_ANTIVIRUS = "Rogue Antivirus"
    TERM_ROOTKIT = "Rootkit"


@register_vocab
class IncidentEffect_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IncidentEffectVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_BRAND_OR_IMAGE_DEGRADATION = "Brand or Image Degradation"
    TERM_DATA_BREACH_OR_COMPROMISE = "Data Breach or Compromise"
    TERM_DEGRADATION_OF_SERVICE = "Degradation of Service"
    TERM_DESTRUCTION = "Destruction"
    TERM_DISRUPTION_OF_SERVICE_OR_OPERATIONS = "Disruption of Service / Operations"
    TERM_FINANCIAL_LOSS = "Financial Loss"
    TERM_LOSS_OF_COMPETITIVE_ADVANTAGE = "Loss of Competitive Advantage"
    TERM_LOSS_OF_COMPETITIVE_ADVANTAGE_ECONOMIC = "Loss of Competitive Advantage - Economic"
    TERM_LOSS_OF_COMPETITIVE_ADVANTAGE_MILITARY = "Loss of Competitive Advantage - Military"
    TERM_LOSS_OF_COMPETITIVE_ADVANTAGE_POLITICAL = "Loss of Competitive Advantage - Political"
    TERM_LOSS_OF_CONFIDENTIAL_OR_PROPRIETARY_INFORMATION_OR_INTELLECTUAL_PROPERTY = "Loss of Confidential / Proprietary Information or Intellectual Property"
    TERM_REGULATORY_COMPLIANCE_OR_LEGAL_IMPACT = "Regulatory, Compliance or Legal Impact"
    TERM_UNINTENDED_ACCESS = "Unintended Access"
    TERM_USER_DATA_LOSS = "User Data Loss"


@register_vocab
class InformationSourceRole_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:InformationSourceRoleVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_AGGREGATOR = "Aggregator"
    TERM_CONTENT_ENHANCERORREFINER = "Content Enhancer/Refiner"
    TERM_INITIAL_AUTHOR = "Initial Author"
    TERM_TRANSFORMERORTRANSLATOR = "Transformer/Translator"


@register_vocab
class Versioning_1_0(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:VersioningVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_REVOKES = "Revokes"
    TERM_UPDATES_REVISES = "Updates - Revises"
    TERM_UPDATE_CORRECTS = "Updates - Corrects"


# Vocab aliases which resolve to the most recent version of the
# associated VocabString.
AssetType = AssetType_1_0
AttackerInfrastructureType = AttackerInfrastructureType_1_0
AttackerToolType = AttackerToolType_1_0
AvailabilityLossType = AvailabilityLossType_1_1_1
CampaignStatus = CampaignStatus_1_0
COAStage = COAStage_1_0
CourseOfActionType = CourseOfActionType_1_0
DiscoveryMethod = DiscoveryMethod_2_0
HighMediumLow = HighMediumLow_1_0
ImpactQualification = ImpactQualification_1_0
ImpactRating = ImpactRating_1_0
IncidentCategory = IncidentCategory_1_0
IncidentEffect = IncidentEffect_1_0
IncidentStatus = IncidentStatus_1_0
IndicatorType = IndicatorType_1_1
InformationSourceRole = InformationSourceRole_1_0
InformationType = InformationType_1_0
IntendedEffect = IntendedEffect_1_0
LocationClass = LocationClass_1_0
LossDuration = LossDuration_1_0
LossProperty = LossProperty_1_0
MalwareType = MalwareType_1_0
ManagementClass = ManagementClass_1_0
Motivation = Motivation_1_1
OwnershipClass = OwnershipClass_1_0
PackageIntent = PackageIntent_1_0
PlanningAndOperationalSupport = PlanningAndOperationalSupport_1_0_1
ReportIntent = ReportIntent_1_0
SecurityCompromise = SecurityCompromise_1_0
SystemType = SystemType_1_0
ThreatActorSophistication = ThreatActorSophistication_1_0
ThreatActorType = ThreatActorType_1_0
Versioning = Versioning_1_0
