# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix.bindings.extensions.marking.ais as ais_binding
import stix.data_marking
from stix.data_marking import MarkingStructure


class AISConsentType(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.AISConsentType
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'
    _ALLOWED_VALUES = ('EVERYONE', 'USG', 'NONE')

    def __init__(self, consent=None):
        self.consent = consent

    @property
    def consent(self):
        return self._consent

    @consent.setter
    def consent(self, value):
        if value is not None and value not in self._ALLOWED_VALUES:
            msg = "consent should be one of: %s. Received %s"
            raise ValueError(msg % (self._ALLOWED_VALUES, value))
        else:
            self._consent = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(AISConsentType, self).to_obj(return_obj=return_obj,
                                           ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.consent:
            return_obj.consent = self.consent

        return return_obj

    def to_dict(self):
        return super(AISConsentType, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.consent = obj.consent

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.consent = d.get('consent')

        return return_obj


class TLPMarkingType(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.TLPMarkingType
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'
    _ALLOWED_VALUES = ('WHITE', 'GREEN', 'AMBER')

    def __init__(self, color=None):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if value is not None and value not in self._ALLOWED_VALUES:
            msg = "color should be one of: %s. Received %s"
            raise ValueError(msg % (self._ALLOWED_VALUES, value))
        else:
            self._color = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(TLPMarkingType, self).to_obj(return_obj=return_obj,
                                           ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.color = self.color

        return return_obj

    def to_dict(self):
        return super(TLPMarkingType, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.color = obj.color

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.color = d.get('color')

        return return_obj


class NotProprietary(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.NotProprietary
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'

    def __init__(self, cisa_proprietary='false', ais_consent=None,
                 tlp_marking=None):
        super(NotProprietary, self).__init__()
        self.cisa_proprietary = cisa_proprietary
        self.ais_consent = ais_consent
        self.tlp_marking = tlp_marking

    @property
    def ais_consent(self):
        return self._ais_consent

    @ais_consent.setter
    def ais_consent(self, value):
        self._set_var(AISConsentType, try_cast=False, ais_consent=value)

    @property
    def tlp_marking(self):
        return self._tlp_marking

    @tlp_marking.setter
    def tlp_marking(self, value):
        self._set_var(TLPMarkingType, try_cast=False, tlp_marking=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(NotProprietary, self).to_obj(return_obj=return_obj,
                                           ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.cisa_proprietary is not None:
            return_obj.CISA_Proprietary = self.cisa_proprietary
        if self.ais_consent:
            return_obj.AISConsent = self.ais_consent.to_obj(ns_info=ns_info)
        if self.tlp_marking:
            return_obj.TLPMarking = self.tlp_marking.to_obj(ns_info=ns_info)

        return return_obj

    def to_dict(self):
        d = {}

        if self.cisa_proprietary is not None:
            d['cisa_proprietary'] = self.cisa_proprietary
        if self.ais_consent:
            d['ais_consent'] = self.ais_consent.to_dict()
        if self.tlp_marking:
            d['tlp_marking'] = self.tlp_marking.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.cisa_proprietary = obj.CISA_Proprietary
        return_obj.ais_consent = AISConsentType.from_obj(obj.AISConsent)
        return_obj.tlp_marking = TLPMarkingType.from_obj(obj.TLPMarking)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.cisa_proprietary = d.get('cisa_proprietary')
        return_obj.ais_consent = AISConsentType.from_dict(d.get('ais_consent'))
        return_obj.tlp_marking = TLPMarkingType.from_dict(d.get('tlp_marking'))

        return return_obj


class IsProprietary(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.IsProprietary
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'

    def __init__(self, cisa_proprietary='true', ais_consent=None,
                 tlp_marking=None):
        super(IsProprietary, self).__init__()
        self.cisa_proprietary = cisa_proprietary
        self.ais_consent = ais_consent
        self.tlp_marking = tlp_marking

    @property
    def ais_consent(self):
        return self._ais_consent

    @ais_consent.setter
    def ais_consent(self, value):
        self._set_var(AISConsentType, try_cast=False, ais_consent=value)

    @property
    def tlp_marking(self):
        return self._tlp_marking

    @tlp_marking.setter
    def tlp_marking(self, value):
        self._set_var(TLPMarkingType, try_cast=False, tlp_marking=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(IsProprietary, self).to_obj(return_obj=return_obj,
                                          ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.cisa_proprietary is not None:
            return_obj.CISA_Proprietary = self.cisa_proprietary
        if self.ais_consent:
            return_obj.AISConsent = self.ais_consent.to_obj(ns_info=ns_info)
        if self.tlp_marking:
            return_obj.TLPMarking = self.tlp_marking.to_obj(ns_info=ns_info)

        return return_obj

    def to_dict(self):
        d = {}

        if self.cisa_proprietary is not None:
            d['cisa_proprietary'] = self.cisa_proprietary
        if self.ais_consent:
            d['ais_consent'] = self.ais_consent.to_dict()
        if self.tlp_marking:
            d['tlp_marking'] = self.tlp_marking.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.cisa_proprietary = obj.CISA_Proprietary
        return_obj.ais_consent = AISConsentType.from_obj(obj.AISConsent)
        return_obj.tlp_marking = TLPMarkingType.from_obj(obj.TLPMarking)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.cisa_proprietary = d.get('cisa_proprietary')
        return_obj.ais_consent = AISConsentType.from_dict(d.get('ais_consent'))
        return_obj.tlp_marking = TLPMarkingType.from_dict(d.get('tlp_marking'))

        return return_obj


class AISMarkingStructure(MarkingStructure):
    _binding = ais_binding
    _binding_class = _binding.AISMarkingStructure
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'
    _XSI_TYPE = "AIS:AISMarkingStructure"

    def __init__(self, is_proprietary=None, not_proprietary=None):
        super(AISMarkingStructure, self).__init__()
        self.is_proprietary = is_proprietary
        self.not_proprietary = not_proprietary

    @property
    def not_proprietary(self):
        return self._not_proprietary

    @not_proprietary.setter
    def not_proprietary(self, value):
        if isinstance(value, NotProprietary):
            self._not_proprietary = value
        else:
            self._set_var(NotProprietary, try_cast=False, not_proprietary=value)

    @property
    def is_proprietary(self):
        return self._is_proprietary

    @is_proprietary.setter
    def is_proprietary(self, value):
        if isinstance(value, IsProprietary):
            self._is_proprietary = value
        else:
            self._set_var(IsProprietary, try_cast=False, is_proprietary=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(AISMarkingStructure, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        MarkingStructure.to_obj(self, return_obj=return_obj, ns_info=ns_info)
        if self.is_proprietary:
            return_obj.Is_Proprietary = self.is_proprietary.to_obj(ns_info=ns_info)
        if self.not_proprietary:
            return_obj.Not_Proprietary = self.not_proprietary.to_obj(ns_info=ns_info)

        return return_obj

    def to_dict(self):
        d = MarkingStructure.to_dict(self)

        if self.is_proprietary:
            d['is_proprietary'] = self.is_proprietary.to_dict()

        if self.not_proprietary:
            d['not_proprietary'] = self.not_proprietary.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        MarkingStructure.from_obj(obj, return_obj=return_obj)
        return_obj.is_proprietary = IsProprietary.from_obj(obj.Is_Proprietary)
        return_obj.not_proprietary = NotProprietary.from_obj(obj.Not_Proprietary)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        MarkingStructure.from_dict(d, return_obj=return_obj)
        return_obj.is_proprietary = IsProprietary.from_dict(d.get('is_proprietary'))
        return_obj.not_proprietary = NotProprietary.from_dict(d.get('not_proprietary'))

        return return_obj


NAMESPACES = {
    'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2': 'AIS'
}

SCHEMALOCATIONS = {
    'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2': 'http://www.us-cert.gov/sites/default/files/STIX_Namespace/AIS_Bundle_Marking_1.1.1_v1.0.xsd'
}


def _update_namespaces():
    # Update the python-stix namespace dictionary
    import stix.utils.nsparser as nsparser

    # Register the extension namespaces
    nsparser.DEFAULT_EXT_TO_PREFIX.update(NAMESPACES)

    # Update the default dict
    nsparser.DEFAULT_STIX_NAMESPACES.update(NAMESPACES)


def _update_schemalocations():
    # Update the python-stix schemalocation dictionary
    import stix.utils.nsparser as nsparser

    # Register the extension schemalocations
    nsparser.EXT_NS_TO_SCHEMALOCATION.update(SCHEMALOCATIONS)

    # Update the default dict
    nsparser.DEFAULT_STIX_SCHEMALOCATIONS.update(SCHEMALOCATIONS)


# Register extension
stix.data_marking.add_extension(AISMarkingStructure)
_update_namespaces()
_update_schemalocations()


# IndustryType allowed sectors
CHEMICAL_SECTOR = 'CHEMICAL SECTOR'
COMMERCIAL_FACILITIES_SECTOR = 'COMMERCIAL FACILITIES SECTOR'
COMMUNICATIONS_SECTOR = 'COMMUNICATIONS SECTOR'
CRITICAL_MANUFACTURING_SECTOR = 'CRITICAL MANUFACTURING SECTOR'
DAMS_SECTOR = 'DAMS SECTOR'
DEFENSE_INDUSTRIAL_BASE_SECTOR = 'DEFENSE INDUSTRIAL BASE SECTOR'
EMERGENCY_SERVICES_SECTOR = 'EMERGENCY SERVICES SECTOR'
ENERGY_SECTOR = 'ENERGY SECTOR'
FINANCIAL_SERVICES_SECTOR = 'FINANCIAL SERVICES SECTOR'
FOOD_AND_AGRICULTURE_SECTOR = 'FOOD AND AGRICULTURE SECTOR'
GOVERNMENT_FACILITIES_SECTOR = 'GOVERNMENT FACILITIES SECTOR'
HEALTH_CARE_AND_PUBLIC_HEALTH_SECTOR = 'HEALTHCARE AND PUBLIC HEALTH SECTOR'
INFORMATION_TECHNOLOGY_SECTOR = 'INFORMATION TECHNOLOGY SECTOR'
NUCLEAR_REACTORS_MATERIALS_AND_WASTE_SECTOR = 'NUCLEAR REACTORS MATERIALS, AND WASTE SECTOR'
TRANSPORTATION_SYSTEMS_SECTOR = 'TRANSPORTATION SYSTEMS SECTOR'
WATER_AND_WASTEWATER_SYSTEMS_SECTOR = 'WATER AND WASTEWATER SYSTEMS SECTOR'


def _validate_and_create_industry_type(industry_type):
    INDUSTRY_TYPE_SECTORS = (CHEMICAL_SECTOR, COMMERCIAL_FACILITIES_SECTOR,
                             COMMUNICATIONS_SECTOR,
                             CRITICAL_MANUFACTURING_SECTOR,
                             DAMS_SECTOR, DEFENSE_INDUSTRIAL_BASE_SECTOR,
                             EMERGENCY_SERVICES_SECTOR, ENERGY_SECTOR,
                             FINANCIAL_SERVICES_SECTOR,
                             FOOD_AND_AGRICULTURE_SECTOR,
                             GOVERNMENT_FACILITIES_SECTOR,
                             HEALTH_CARE_AND_PUBLIC_HEALTH_SECTOR,
                             INFORMATION_TECHNOLOGY_SECTOR,
                             NUCLEAR_REACTORS_MATERIALS_AND_WASTE_SECTOR,
                             TRANSPORTATION_SYSTEMS_SECTOR,
                             WATER_AND_WASTEWATER_SYSTEMS_SECTOR)

    if isinstance(industry_type, str):
        if industry_type.split(" | ") > 1:
            val = industry_type.split(" | ")

            # Pipe-delimited string supplied.
            if all(x in INDUSTRY_TYPE_SECTORS for x in val):
                return industry_type

        # Single string supplied.
        if industry_type in INDUSTRY_TYPE_SECTORS:
            return industry_type

    elif isinstance(industry_type, list):
        # Create pipe-delimited string when list of strings is provided.
        if all(x in INDUSTRY_TYPE_SECTORS for x in industry_type):
            return " | ".join(industry_type)

    msg = 'IndustryType must be one of the following: {0}. Received \'{1}\'.'
    raise ValueError(msg.format(INDUSTRY_TYPE_SECTORS, industry_type))


def add_ais_marking(stix_package, proprietary, consent, color, **kwargs):
    """
    This utility functions aids in the creation of an AIS marking and appends
    it to the provided STIX package.

    Args:
        stix_package: A stix.core.STIXPackage object.
        proprietary: True if marking uses IsProprietary, False for
        NotProprietary.
        consent: A string with one of the following values: "EVERYONE", "NONE"
            or "USG".
        color: A string that corresponds to TLP values: "WHITE", "GREEN" or
            "AMBER".
        **kwargs: Six required keyword arguments that are used to create a CIQ
            identity object. These are: country_name_code,
            country_name_code_type, admin_area_name_code,
            admin_area_name_code_type, organisation_name, industry_type.

    Raises:
        ValueError: When keyword arguments are missing. User did not supply
            correct values for: proprietary, color and consent.

    Note:
        Any Markings under STIX Header will be removed. Please follow the
        guidelines for `AIS`_.

        The industry_type keyword argument accepts: a list of string based on
        defined sectors, a pipe-delimited string of sectors, or a single
        sector.

    .. _AIS:
        https://www.us-cert.gov/ais
    """
    from stix.common import InformationSource
    from stix.extensions.identity.ciq_identity_3_0 import (
        CIQIdentity3_0Instance, STIXCIQIdentity3_0, PartyName, Address,
        Country, NameElement, OrganisationInfo, AdministrativeArea)
    from stix.core.stix_header import STIXHeader
    from stix.data_marking import MarkingSpecification, Marking

    args = ('country_name_code', 'country_name_code_type', 'industry_type',
            'admin_area_name_code', 'admin_area_name_code_type',
            'organisation_name')

    diff = set(args) - set(kwargs.keys())

    if diff:
        msg = 'All keyword arguments must be provided. Missing: {0}'
        raise ValueError(msg.format(tuple(diff)))

    party_name = PartyName()
    party_name.add_organisation_name(kwargs['organisation_name'])

    country = Country()
    country_name = NameElement()
    country_name.name_code = kwargs['country_name_code']
    country_name.name_code_type = kwargs['country_name_code_type']
    country.add_name_element(country_name)

    admin_area = AdministrativeArea()
    admin_area_name = NameElement()
    admin_area_name.name_code = kwargs['admin_area_name_code']
    admin_area_name.name_code_type = kwargs['admin_area_name_code_type']
    admin_area.add_name_element(admin_area_name)

    address = Address()
    address.country = country
    address.administrative_area = admin_area

    org_info = OrganisationInfo()
    org_info.industry_type = _validate_and_create_industry_type(kwargs['industry_type'])

    id_spec = STIXCIQIdentity3_0()
    id_spec.party_name = party_name
    id_spec.add_address(address)
    id_spec.organisation_info = org_info

    identity = CIQIdentity3_0Instance()
    identity.specification = id_spec

    if proprietary is True:
        proprietary_obj = IsProprietary()
        consent = 'EVERYONE'
    elif proprietary is False:
        proprietary_obj = NotProprietary()
    else:
        raise ValueError('proprietary expected True or False.')

    proprietary_obj.ais_consent = AISConsentType(consent=consent)
    proprietary_obj.tlp_marking = TLPMarkingType(color=color)

    ais_marking = AISMarkingStructure()

    if isinstance(proprietary_obj, IsProprietary):
        ais_marking.is_proprietary = proprietary_obj
    else:
        ais_marking.not_proprietary = proprietary_obj

    marking_spec = MarkingSpecification()
    marking_spec.controlled_structure = '//node() | //@*'
    marking_spec.marking_structures.append(ais_marking)
    marking_spec.information_source = InformationSource()
    marking_spec.information_source.identity = identity

    if not stix_package.stix_header:
        stix_package.stix_header = STIXHeader()

    # Removes any other Markings if present.
    stix_package.stix_header.handling = Marking()
    stix_package.stix_header.handling.add_marking(marking_spec)
