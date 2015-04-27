# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.stix_common as stix_common_binding


# TODO: handle normalization
# from cybox.utils import normalize_to_xml, denormalize_from_xml


class VocabString(stix.Entity):
    _binding = stix_common_binding
    _binding_class = stix_common_binding.ControlledVocabularyStringType
    _namespace = 'http://stix.mitre.org/common-1'

    # All subclasses should override these
    _XSI_TYPE = None
    _ALLOWED_VALUES = None

    def __init__(self, value=None):
        super(VocabString, self).__init__()
        self.value = value
        self.xsi_type = self._XSI_TYPE

        self.vocab_name = None
        self.vocab_reference = None

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, v):
        allowed = self._ALLOWED_VALUES

        if not v:
            self._value = None
        elif allowed and (v not in allowed):
            error = "Value must be one of {0}. Received '{1}'"
            error = error.format(allowed, v)
            raise ValueError(error)
        else:
            self._value = v

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
            self._XSI_TYPE is None and
            self.vocab_name is None and
            self.vocab_reference is None
        )

    @staticmethod
    def lookup_class(xsi_type):
        if not xsi_type:
            return VocabString
        
        for (k, v) in _VOCAB_MAP.iteritems():
            # TODO: for now we ignore the prefix and just check for
            # a partial match
            if xsi_type in k:
                return v

        return VocabString

    def to_obj(self, return_obj=None, ns_info=None):
        super(VocabString, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        # TODO: handle normalization
        # vocab_obj.valueOf_ = normalize_to_xml(self.value)
        return_obj.valueOf_ = self.value
        return_obj.xsi_type = self.xsi_type

        if self.vocab_name is not None:
            return_obj.vocab_name = self.vocab_name
        if self.vocab_reference is not None:
            return_obj.vocab_reference = self.vocab_reference

        return return_obj

    def to_dict(self):
        if self.is_plain():
            return self.value

        d = {}
        if self.value is not None:
            d['value'] = self.value
        if self.xsi_type is not None:
            d['xsi:type'] = self.xsi_type
        if self.vocab_name is not None:
            d['vocab_name'] = self.vocab_name
        if self.vocab_reference is not None:
            d['vocab_reference'] = self.vocab_reference

        return d

    @classmethod
    def from_obj(cls, vocab_obj, return_obj=None):
        if not vocab_obj:
            return None
        
        if not return_obj:
            klass = VocabString.lookup_class(vocab_obj.xsi_type)
            return klass.from_obj(vocab_obj, klass())
           
        # xsi_type should be set automatically by the class's constructor.
        
        # TODO: handle denormalization
        # vocab_str.value = denormalize_from_xml(vocab_obj.valueOf_)
        return_obj.value = vocab_obj.valueOf_
        return_obj.vocab_name = vocab_obj.vocab_name
        return_obj.vocab_reference = vocab_obj.vocab_reference
        return_obj.xsi_type = vocab_obj.xsi_type

        return return_obj

    @classmethod
    def from_dict(cls, vocab_dict, return_obj=None):
        if not vocab_dict:
            return None
        
        if not return_obj:
            if isinstance(vocab_dict, dict):
                klass = VocabString.lookup_class(vocab_dict.get('xsi:type'))
                return klass.from_dict(vocab_dict, klass())
            else:
                return_obj = cls()
            
        # xsi_type should be set automatically by the class's constructor.

        # In case this is a "plain" string, just set it.
        if not isinstance(vocab_dict, dict):
            return_obj.value = vocab_dict
        else:
            return_obj.value = vocab_dict.get('value')
            return_obj.vocab_name = vocab_dict.get('vocab_name')
            return_obj.vocab_reference = vocab_dict.get('vocab_reference')
            return_obj.xsi_type = vocab_dict.get('xsi:type')

        return return_obj


#: Mapping of Controlled Vocabulary xsi:type's to their class implementations.
_VOCAB_MAP = {}


def _get_terms(vocab_class):
    """Helper function used by register_vocab."""
    for k, v in vocab_class.__dict__.items():
        if k.startswith("TERM_"):
            yield v


def add_vocab(cls):
    """Registers a VocabString subclass.

    Note:
        The :meth:`register_vocab` class decorator has replaced this method.

    """
    _VOCAB_MAP[cls._XSI_TYPE] = cls


def register_vocab(cls):
    """Register a VocabString subclass.

    Also, calculate all the permitted values for class being decorated by
    adding an ``_ALLOWED_VALUES`` tuple of all the values of class members
    beginning with ``TERM_``.

    """
    add_vocab(cls)

    cls._ALLOWED_VALUES = tuple(_get_terms(cls))
    return cls


@register_vocab
class AvailabilityLossType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:AvailabilityLossTypeVocab-1.1.1'

    TERM_DESTRUCTION = "Destruction"
    TERM_LOSS = "Loss"
    TERM_INTERRUPTION = "Interruption"
    TERM_DEGRADATION = "Degradation"
    TERM_ACCELERATION = "Acceleration"
    TERM_OBSCURATION = "Obscuration"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class ThreatActorType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:ThreatActorTypeVocab-1.0'

    TERM_CYBER_ESPIONAGE_OPERATIONS = "Cyber Espionage Operations"
    TERM_HACKER = "Hacker"
    TERM_HACKER_WHITE_HAT = "Hacker - White hat"
    TERM_HACKER_GRAY_HAT = "Hacker - Gray hat"
    TERM_HACKER_BLACK_HAT = "Hacker - Black hat"
    TERM_HACKTIVIST = "Hacktivist"
    TERM_STATE_ACTOR_OR_AGENCY = "State Actor / Agency"
    TERM_ECRIME_ACTOR_CREDENTIAL_THEFT_BOTNET_OPERATOR = "eCrime Actor - Credential Theft Botnet Operator"
    TERM_ECRIME_ACTOR_CREDENTIAL_THEFT_BOTNET_SERVICE = "eCrime Actor - Credential Theft Botnet Service"
    TERM_ECRIME_ACTOR_MALWARE_DEVELOPER = "eCrime Actor - Malware Developer"
    TERM_ECRIME_ACTOR_MONEY_LAUNDERING_NETWORK = "eCrime Actor - Money Laundering Network"
    TERM_ECRIME_ACTOR_ORGANIZED_CRIME_ACTOR = "eCrime Actor - Organized Crime Actor"
    TERM_ECRIME_ACTOR_SPAM_SERVICE = "eCrime Actor - Spam Service"
    TERM_ECRIME_ACTOR_TRAFFIC_SERVICE = "eCrime Actor - Traffic Service"
    TERM_ECRIME_ACTOR_UNDERGROUND_CALL_SERVICE = "eCrime Actor - Underground Call Service"
    TERM_INSIDER_THREAT = "Insider Threat"
    TERM_DISGRUNTLED_CUSTOMER_OR_USER = "Disgruntled Customer / User"


@register_vocab
class AttackerInfrastructureType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:AttackerInfrastructureTypeVocab-1.0'

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
    TERM_HOSTING = "Hosting"
    TERM_HOSTING_BULLETPROOF_OR_ROGUE_HOSTING = "Hosting - Bulletproof / Rogue Hosting"
    TERM_HOSTING_CLOUD_HOSTING = "Hosting - Cloud Hosting"
    TERM_HOSTING_COMPROMISED_SERVER = "Hosting - Compromised Server"
    TERM_HOSTING_FAST_FLUX_BOTNET_HOSTING = "Hosting - Fast Flux Botnet Hosting"
    TERM_HOSTING_LEGITIMATE_HOSTING = "Hosting - Legitimate Hosting"
    TERM_ELECTRONIC_PAYMENT_METHODS = "Electronic Payment Methods"


@register_vocab
class DiscoveryMethod(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:DiscoveryMethodVocab-1.0'

    TERM_AGENT_DISCLOSURE = "Agent Disclosure"
    TERM_FRAUD_DETECTION = "Fraud Detection"
    TERM_MONITORING_SERVICE = "Monitoring Service"
    TERM_LAW_ENFORCEMENT = "Law Enforcement"
    TERM_CUSTOMER = "Customer"
    TERM_UNRELATED_PARTY = "Unrelated Party"
    TERM_AUDIT = "Audit"
    TERM_ANTIVIRUS = "Antivirus"
    TERM_INCIDENT_RESPONSE = "Incident Response"
    TERM_FINANCIAL_AUDIT = "Financial Audit"
    TERM_HIPS = "HIPS"
    TERM_IT_AUDIT = "IT Audit"
    TERM_LOG_REVIEW = "Log Review"
    TERM_NIDS = "NIDS"
    TERM_SECURITY_ALARM = "Security Alarm"
    TERM_USER = "User"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class AttackerToolType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:AttackerToolTypeVocab-1.0'

    TERM_MALWARE = "Malware"
    TERM_PENETRATION_TESTING = "Penetration Testing"
    TERM_PORT_SCANNER = "Port Scanner"
    TERM_TRAFFIC_SCANNER = "Traffic Scanner"
    TERM_VULNERABILITY_SCANNER = "Vulnerability Scanner"
    TERM_APPLICATION_SCANNER = "Application Scanner"
    TERM_PASSWORD_CRACKING = "Password Cracking"


@register_vocab
class IndicatorType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IndicatorTypeVocab-1.1'

    TERM_MALICIOUS_EMAIL = "Malicious E-mail"
    TERM_IP_WATCHLIST = "IP Watchlist"
    TERM_FILE_HASH_WATCHLIST = "File Hash Watchlist"
    TERM_DOMAIN_WATCHLIST = "Domain Watchlist"
    TERM_URL_WATCHLIST = "URL Watchlist"
    TERM_MALWARE_ARTIFACTS = "Malware Artifacts"
    TERM_C2 = "C2"
    TERM_ANONYMIZATION = "Anonymization"
    TERM_EXFILTRATION = "Exfiltration"
    TERM_HOST_CHARACTERISTICS = "Host Characteristics"
    TERM_COMPROMISED_PKI_CERTIFICATE = "Compromised PKI Certificate"
    TERM_LOGIN_NAME = "Login Name"
    TERM_IMEI_WATCHLIST = "IMEI Watchlist"
    TERM_IMSI_WATCHLIST = "IMSI Watchlist"


@register_vocab
class SystemType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:SystemTypeVocab-1.0'

    TERM_ENTERPRISE_SYSTEMS = "Enterprise Systems"
    TERM_ENTERPRISE_SYSTEMS_APPLICATION_LAYER = "Enterprise Systems - Application Layer"
    TERM_ENTERPRISE_SYSTEMS_DATABASE_LAYER = "Enterprise Systems - Database Layer"
    TERM_ENTERPRISE_SYSTEMS_ENTERPRISE_TECHNOLOGIES_AND_SUPPORT_INFRASTRUCTURE = "Enterprise Systems - Enterprise Technologies and Support Infrastructure"
    TERM_ENTERPRISE_SYSTEMS_NETWORK_SYSTEMS = "Enterprise Systems - Network Systems"
    TERM_ENTERPRISE_SYSTEMS_NETWORKING_DEVICES = "Enterprise Systems - Networking Devices"
    TERM_ENTERPRISE_SYSTEMS_WEB_LAYER = "Enterprise Systems - Web Layer"
    TERM_ENTERPRISE_SYSTEMS_VOIP = "Enterprise Systems - VoIP"
    TERM_INDUSTRIAL_CONTROL_SYSTEMS = "Industrial Control Systems"
    TERM_INDUSTRIAL_CONTROL_SYSTEMS_EQUIPMENT_UNDER_CONTROL = "Industrial Control Systems - Equipment Under Control"
    TERM_INDUSTRIAL_CONTROL_SYSTEMS_OPERATIONS_MANAGEMENT = "Industrial Control Systems - Operations Management"
    TERM_INDUSTRIAL_CONTROL_SYSTEMS_SAFETY_PROTECTION_AND_LOCAL_CONTROL = "Industrial Control Systems - Safety, Protection and Local Control"
    TERM_INDUSTRIAL_CONTROL_SYSTEMS_SUPERVISORY_CONTROL = "Industrial Control Systems - Supervisory Control"
    TERM_MOBILE_SYSTEMS = "Mobile Systems"
    TERM_MOBILE_SYSTEMS_MOBILE_OPERATING_SYSTEMS = "Mobile Systems - Mobile Operating Systems"
    TERM_MOBILE_SYSTEMS_NEAR_FIELD_COMMUNICATIONS = "Mobile Systems - Near Field Communications"
    TERM_MOBILE_SYSTEMS_MOBILE_DEVICES = "Mobile Systems - Mobile Devices"
    TERM_THIRDPARTY_SERVICES = "Third-Party Services"
    TERM_THIRDPARTY_SERVICES_APPLICATION_STORES = "Third-Party Services - Application Stores"
    TERM_THIRDPARTY_SERVICES_CLOUD_SERVICES = "Third-Party Services - Cloud Services"
    TERM_THIRDPARTY_SERVICES_SECURITY_VENDORS = "Third-Party Services - Security Vendors"
    TERM_THIRDPARTY_SERVICES_SOCIAL_MEDIA = "Third-Party Services - Social Media"
    TERM_THIRDPARTY_SERVICES_SOFTWARE_UPDATE = "Third-Party Services - Software Update"
    TERM_USERS = "Users"
    TERM_USERS_APPLICATION_AND_SOFTWARE = "Users - Application And Software"
    TERM_USERS_WORKSTATION = "Users - Workstation"
    TERM_USERS_REMOVABLE_MEDIA = "Users - Removable Media"


@register_vocab
class CampaignStatus(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:CampaignStatusVocab-1.0'

    TERM_ONGOING = "Ongoing"
    TERM_HISTORIC = "Historic"
    TERM_FUTURE = "Future"


@register_vocab
class IncidentStatus(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IncidentStatusVocab-1.0'

    TERM_NEW = "New"
    TERM_OPEN = "Open"
    TERM_STALLED = "Stalled"
    TERM_CONTAINMENT_ACHIEVED = "Containment Achieved"
    TERM_RESTORATION_ACHIEVED = "Restoration Achieved"
    TERM_INCIDENT_REPORTED = "Incident Reported"
    TERM_CLOSED = "Closed"
    TERM_REJECTED = "Rejected"
    TERM_DELETED = "Deleted"


@register_vocab
class ManagementClass(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:ManagementClassVocab-1.0'

    TERM_INTERNALLYMANAGED = "Internally-Managed"
    TERM_EXTERNALLYMANAGEMENT = "Externally-Management"
    TERM_COMANAGEMENT = "Co-Management"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class Motivation(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:MotivationVocab-1.1'

    TERM_IDEOLOGICAL = "Ideological"
    TERM_IDEOLOGICAL_ANTICORRUPTION = "Ideological - Anti-Corruption"
    TERM_IDEOLOGICAL_ANTIESTABLISHMENT = "Ideological - Anti-Establishment"
    TERM_IDEOLOGICAL_ENVIRONMENTAL = "Ideological - Environmental"
    TERM_IDEOLOGICAL_ETHNIC_OR_NATIONALIST = "Ideological - Ethnic / Nationalist"
    TERM_IDEOLOGICAL_INFORMATION_FREEDOM = "Ideological - Information Freedom"
    TERM_IDEOLOGICAL_RELIGIOUS = "Ideological - Religious"
    TERM_IDEOLOGICAL_SECURITY_AWARENESS = "Ideological - Security Awareness"
    TERM_IDEOLOGICAL_HUMAN_RIGHTS = "Ideological - Human Rights"
    TERM_EGO = "Ego"
    TERM_FINANCIAL_OR_ECONOMIC = "Financial or Economic"
    TERM_MILITARY = "Military"
    TERM_OPPORTUNISTIC = "Opportunistic"
    TERM_POLITICAL = "Political"


@register_vocab
class IncidentCategory(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IncidentCategoryVocab-1.0'

    TERM_EXERCISEORNETWORK_DEFENSE_TESTING = "Exercise/Network Defense Testing"
    TERM_UNAUTHORIZED_ACCESS = "Unauthorized Access"
    TERM_DENIAL_OF_SERVICE = "Denial of Service"
    TERM_MALICIOUS_CODE = "Malicious Code"
    TERM_IMPROPER_USAGE = "Improper Usage"
    TERM_SCANSORPROBESORATTEMPTED_ACCESS = "Scans/Probes/Attempted Access"
    TERM_INVESTIGATION = "Investigation"


@register_vocab
class ImpactQualification(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:ImpactQualificationVocab-1.0'

    TERM_INSIGNIFICANT = "Insignificant"
    TERM_DISTRACTING = "Distracting"
    TERM_PAINFUL = "Painful"
    TERM_DAMAGING = "Damaging"
    TERM_CATASTROPHIC = "Catastrophic"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class PlanningAndOperationalSupport(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:PlanningAndOperationalSupportVocab-1.0.1'

    TERM_DATA_EXPLOITATION = "Data Exploitation"
    TERM_DATA_EXPLOITATION_ANALYTIC_SUPPORT = "Data Exploitation - Analytic Support"
    TERM_DATA_EXPLOITATION_TRANSLATION_SUPPORT = "Data Exploitation - Translation Support"
    TERM_FINANCIAL_RESOURCES = "Financial Resources"
    TERM_FINANCIAL_RESOURCES_ACADEMIC = "Financial Resources - Academic"
    TERM_FINANCIAL_RESOURCES_COMMERCIAL = "Financial Resources - Commercial"
    TERM_FINANCIAL_RESOURCES_GOVERNMENT = "Financial Resources - Government"
    TERM_FINANCIAL_RESOURCES_HACKTIVIST_OR_GRASSROOT = "Financial Resources - Hacktivist or Grassroot"
    TERM_FINANCIAL_RESOURCES_NONATTRIBUTABLE_FINANCE = "Financial Resources - Non-Attributable Finance"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT = "Skill Development / Recruitment"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_CONTRACTING_AND_HIRING = "Skill Development / Recruitment - Contracting and Hiring"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_DOCUMENT_EXPLOITATION_DOCEX_TRAINING = "Skill Development / Recruitment - Document Exploitation (DOCEX) Training"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_INTERNAL_TRAINING = "Skill Development / Recruitment - Internal Training"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_MILITARY_PROGRAMS = "Skill Development / Recruitment - Military Programs"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_SECURITY_OR_HACKER_CONFERENCES = "Skill Development / Recruitment - Security / Hacker Conferences"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_UNDERGROUND_FORUMS = "Skill Development / Recruitment - Underground Forums"
    TERM_SKILL_DEVELOPMENT_OR_RECRUITMENT_UNIVERSITY_PROGRAMS = "Skill Development / Recruitment - University Programs"
    TERM_PLANNING = "Planning"
    TERM_PLANNING_OPERATIONAL_COVER_PLAN = "Planning - Operational Cover Plan"
    TERM_PLANNING_OPENSOURCE_INTELLIGENCE_OSINT_GATHERING = "Planning - Open-Source Intelligence (OSINT) Gathering"
    TERM_PLANNING_PREOPERATIONAL_SURVEILLANCE_AND_RECONNAISSANCE = "Planning - Pre-Operational Surveillance and Reconnaissance"
    TERM_PLANNING_TARGET_SELECTION = "Planning - Target Selection"


@register_vocab
class CourseOfActionType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:CourseOfActionTypeVocab-1.0'

    TERM_PERIMETER_BLOCKING = "Perimeter Blocking"
    TERM_INTERNAL_BLOCKING = "Internal Blocking"
    TERM_REDIRECTION = "Redirection"
    TERM_REDIRECTION_HONEY_POT = "Redirection (Honey Pot)"
    TERM_HARDENING = "Hardening"
    TERM_PATCHING = "Patching"
    TERM_ERADICATION = "Eradication"
    TERM_REBUILDING = "Rebuilding"
    TERM_TRAINING = "Training"
    TERM_MONITORING = "Monitoring"
    TERM_PHYSICAL_ACCESS_RESTRICTIONS = "Physical Access Restrictions"
    TERM_LOGICAL_ACCESS_RESTRICTIONS = "Logical Access Restrictions"
    TERM_PUBLIC_DISCLOSURE = "Public Disclosure"
    TERM_DIPLOMATIC_ACTIONS = "Diplomatic Actions"
    TERM_POLICY_ACTIONS = "Policy Actions"
    TERM_OTHER = "Other"


@register_vocab
class SecurityCompromise(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:SecurityCompromiseVocab-1.0'

    TERM_YES = "Yes"
    TERM_SUSPECTED = "Suspected"
    TERM_NO = "No"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class ImpactRating(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:ImpactRatingVocab-1.0'

    TERM_NONE = "None"
    TERM_MINOR = "Minor"
    TERM_MODERATE = "Moderate"
    TERM_MAJOR = "Major"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class AssetType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:AssetTypeVocab-1.0'

    TERM_BACKUP = "Backup"
    TERM_DATABASE = "Database"
    TERM_DHCP = "DHCP"
    TERM_DIRECTORY = "Directory"
    TERM_DCS = "DCS"
    TERM_DNS = "DNS"
    TERM_FILE = "File"
    TERM_LOG = "Log"
    TERM_MAIL = "Mail"
    TERM_MAINFRAME = "Mainframe"
    TERM_PAYMENT_SWITCH = "Payment switch"
    TERM_POS_CONTROLLER = "POS controller"
    TERM_PRINT = "Print"
    TERM_PROXY = "Proxy"
    TERM_REMOTE_ACCESS = "Remote access"
    TERM_SCADA = "SCADA"
    TERM_WEB_APPLICATION = "Web application"
    TERM_SERVER = "Server"
    TERM_ACCESS_READER = "Access reader"
    TERM_CAMERA = "Camera"
    TERM_FIREWALL = "Firewall"
    TERM_HSM = "HSM"
    TERM_IDS = "IDS"
    TERM_BROADBAND = "Broadband"
    TERM_PBX = "PBX"
    TERM_PRIVATE_WAN = "Private WAN"
    TERM_PLC = "PLC"
    TERM_PUBLIC_WAN = "Public WAN"
    TERM_RTU = "RTU"
    TERM_ROUTER_OR_SWITCH = "Router or switch"
    TERM_SAN = "SAN"
    TERM_TELEPHONE = "Telephone"
    TERM_VOIP_ADAPTER = "VoIP adapter"
    TERM_LAN = "LAN"
    TERM_WLAN = "WLAN"
    TERM_NETWORK = "Network"
    TERM_AUTH_TOKEN = "Auth token"
    TERM_ATM = "ATM"
    TERM_DESKTOP = "Desktop"
    TERM_PED_PAD = "PED pad"
    TERM_GAS_TERMINAL = "Gas terminal"
    TERM_LAPTOP = "Laptop"
    TERM_MEDIA = "Media"
    TERM_MOBILE_PHONE = "Mobile phone"
    TERM_PERIPHERAL = "Peripheral"
    TERM_POS_TERMINAL = "POS terminal"
    TERM_KIOSK = "Kiosk"
    TERM_TABLET = "Tablet"
    TERM_VOIP_PHONE = "VoIP phone"
    TERM_USER_DEVICE = "User Device"
    TERM_TAPES = "Tapes"
    TERM_DISK_MEDIA = "Disk media"
    TERM_DOCUMENTS = "Documents"
    TERM_FLASH_DRIVE = "Flash drive"
    TERM_DISK_DRIVE = "Disk drive"
    TERM_SMART_CARD = "Smart card"
    TERM_PAYMENT_CARD = "Payment card"
    TERM_ADMINISTRATOR = "Administrator"
    TERM_AUDITOR = "Auditor"
    TERM_CALL_CENTER = "Call center"
    TERM_CASHIER = "Cashier"
    TERM_CUSTOMER = "Customer"
    TERM_DEVELOPER = "Developer"
    TERM_ENDUSER = "End-user"
    TERM_EXECUTIVE = "Executive"
    TERM_FINANCE = "Finance"
    TERM_FORMER_EMPLOYEE = "Former employee"
    TERM_GUARD = "Guard"
    TERM_HELPDESK = "Helpdesk"
    TERM_HUMAN_RESOURCES = "Human resources"
    TERM_MAINTENANCE = "Maintenance"
    TERM_MANAGER = "Manager"
    TERM_PARTNER = "Partner"
    TERM_PERSON = "Person"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class COAStage(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:COAStageVocab-1.0'

    TERM_REMEDY = "Remedy"
    TERM_RESPONSE = "Response"


@register_vocab
class LocationClass(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:LocationClassVocab-1.0'

    TERM_INTERNALLYLOCATED = "Internally-Located"
    TERM_EXTERNALLYLOCATED = "Externally-Located"
    TERM_COLOCATED = "Co-Located"
    TERM_MOBILE = "Mobile"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class InformationType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:InformationTypeVocab-1.0'

    TERM_INFORMATION_ASSETS = "Information Assets"
    TERM_INFORMATION_ASSETS_CORPORATE_EMPLOYEE_INFORMATION = "Information Assets - Corporate Employee Information"
    TERM_INFORMATION_ASSETS_CUSTOMER_PII = "Information Assets - Customer PII"
    TERM_INFORMATION_ASSETS_EMAIL_LISTS_OR_ARCHIVES = "Information Assets - Email Lists / Archives"
    TERM_INFORMATION_ASSETS_FINANCIAL_DATA = "Information Assets - Financial Data"
    TERM_INFORMATION_ASSETS_INTELLECTUAL_PROPERTY = "Information Assets - Intellectual Property"
    TERM_INFORMATION_ASSETS_MOBILE_PHONE_CONTACTS = "Information Assets - Mobile Phone Contacts"
    TERM_INFORMATION_ASSETS_USER_CREDENTIALS = "Information Assets - User Credentials"
    TERM_AUTHENTICATION_COOKIES = "Authentication Cookies"


@register_vocab
class ThreatActorSophistication(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:ThreatActorSophisticationVocab-1.0'

    TERM_INNOVATOR = "Innovator"
    TERM_EXPERT = "Expert"
    TERM_PRACTITIONER = "Practitioner"
    TERM_NOVICE = "Novice"
    TERM_ASPIRANT = "Aspirant"


@register_vocab
class HighMediumLow(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:HighMediumLowVocab-1.0'

    TERM_HIGH = "High"
    TERM_MEDIUM = "Medium"
    TERM_LOW = "Low"
    TERM_NONE = "None"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class LossProperty(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:LossPropertyVocab-1.0'

    TERM_CONFIDENTIALITY = "Confidentiality"
    TERM_INTEGRITY = "Integrity"
    TERM_AVAILABILITY = "Availability"
    TERM_ACCOUNTABILITY = "Accountability"
    TERM_NONREPUDIATION = "Non-Repudiation"


@register_vocab
class IntendedEffect(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IntendedEffectVocab-1.0'

    TERM_ADVANTAGE = "Advantage"
    TERM_ADVANTAGE_ECONOMIC = "Advantage - Economic"
    TERM_ADVANTAGE_MILITARY = "Advantage - Military"
    TERM_ADVANTAGE_POLITICAL = "Advantage - Political"
    TERM_THEFT = "Theft"
    TERM_THEFT_INTELLECTUAL_PROPERTY = "Theft - Intellectual Property"
    TERM_THEFT_CREDENTIAL_THEFT = "Theft - Credential Theft"
    TERM_THEFT_IDENTITY_THEFT = "Theft - Identity Theft"
    TERM_THEFT_THEFT_OF_PROPRIETARY_INFORMATION = "Theft - Theft of Proprietary Information"
    TERM_ACCOUNT_TAKEOVER = "Account Takeover"
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
    TERM_TRAFFIC_DIVERSION = "Traffic Diversion"
    TERM_UNAUTHORIZED_ACCESS = "Unauthorized Access"


@register_vocab
class PackageIntent(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:PackageIntentVocab-1.0'

    TERM_COLLECTIVE_THREAT_INTELLIGENCE = "Collective Threat Intelligence"
    TERM_THREAT_REPORT = "Threat Report"
    TERM_INDICATORS = "Indicators"
    TERM_INDICATORS_PHISHING = "Indicators - Phishing"
    TERM_INDICATORS_WATCHLIST = "Indicators - Watchlist"
    TERM_INDICATORS_MALWARE_ARTIFACTS = "Indicators - Malware Artifacts"
    TERM_INDICATORS_NETWORK_ACTIVITY = "Indicators - Network Activity"
    TERM_INDICATORS_ENDPOINT_CHARACTERISTICS = "Indicators - Endpoint Characteristics"
    TERM_CAMPAIGN_CHARACTERIZATION = "Campaign Characterization"
    TERM_THREAT_ACTOR_CHARACTERIZATION = "Threat Actor Characterization"
    TERM_EXPLOIT_CHARACTERIZATION = "Exploit Characterization"
    TERM_ATTACK_PATTERN_CHARACTERIZATION = "Attack Pattern Characterization"
    TERM_MALWARE_CHARACTERIZATION = "Malware Characterization"
    TERM_TTP_INFRASTRUCTURE = "TTP - Infrastructure"
    TERM_TTP_TOOLS = "TTP - Tools"
    TERM_COURSES_OF_ACTION = "Courses of Action"
    TERM_INCIDENT = "Incident"
    TERM_OBSERVATIONS = "Observations"
    TERM_OBSERVATIONS_EMAIL = "Observations - Email"
    TERM_MALWARE_SAMPLES = "Malware Samples"


@register_vocab
class LossDuration(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:LossDurationVocab-1.0'

    TERM_PERMANENT = "Permanent"
    TERM_WEEKS = "Weeks"
    TERM_DAYS = "Days"
    TERM_HOURS = "Hours"
    TERM_MINUTES = "Minutes"
    TERM_SECONDS = "Seconds"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class OwnershipClass(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:OwnershipClassVocab-1.0'

    TERM_INTERNALLYOWNED = "Internally-Owned"
    TERM_EMPLOYEEOWNED = "Employee-Owned"
    TERM_PARTNEROWNED = "Partner-Owned"
    TERM_CUSTOMEROWNED = "Customer-Owned"
    TERM_UNKNOWN = "Unknown"


@register_vocab
class MalwareType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:MalwareTypeVocab-1.0'

    TERM_AUTOMATED_TRANSFER_SCRIPTS = "Automated Transfer Scripts"
    TERM_ADWARE = "Adware"
    TERM_DIALER = "Dialer"
    TERM_BOT = "Bot"
    TERM_BOT_CREDENTIAL_THEFT = "Bot - Credential Theft"
    TERM_BOT_DDOS = "Bot - DDoS"
    TERM_BOT_LOADER = "Bot - Loader"
    TERM_BOT_SPAM = "Bot - Spam"
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
class IncidentEffect(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IncidentEffectVocab-1.0'

    TERM_BRAND_OR_IMAGE_DEGRADATION = "Brand or Image Degradation"
    TERM_LOSS_OF_COMPETITIVE_ADVANTAGE = "Loss of Competitive Advantage"
    TERM_LOSS_OF_COMPETITIVE_ADVANTAGE_ECONOMIC = "Loss of Competitive Advantage - Economic"
    TERM_LOSS_OF_COMPETITIVE_ADVANTAGE_MILITARY = "Loss of Competitive Advantage - Military"
    TERM_LOSS_OF_COMPETITIVE_ADVANTAGE_POLITICAL = "Loss of Competitive Advantage - Political"
    TERM_DATA_BREACH_OR_COMPROMISE = "Data Breach or Compromise"
    TERM_DEGRADATION_OF_SERVICE = "Degradation of Service"
    TERM_DESTRUCTION = "Destruction"
    TERM_DISRUPTION_OF_SERVICE_OR_OPERATIONS = "Disruption of Service / Operations"
    TERM_FINANCIAL_LOSS = "Financial Loss"
    TERM_LOSS_OF_CONFIDENTIAL_OR_PROPRIETARY_INFORMATION_OR_INTELLECTUAL_PROPERTY = "Loss of Confidential / Proprietary Information or Intellectual Property"
    TERM_REGULATORY_COMPLIANCE_OR_LEGAL_IMPACT = "Regulatory, Compliance or Legal Impact"
    TERM_UNINTENDED_ACCESS = "Unintended Access"
    TERM_USER_DATA_LOSS = "User Data Loss"


@register_vocab
class InformationSourceRole(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:InformationSourceRoleVocab-1.0'

    TERM_INITIAL_AUTHOR = "Initial Author"
    TERM_CONTENT_ENHANCERORREFINER = "Content Enhancer/Refiner"
    TERM_AGGREGATOR = "Aggregator"
    TERM_TRANSFORMERORTRANSLATOR = "Transformer/Translator"

