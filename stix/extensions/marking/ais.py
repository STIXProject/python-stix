# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields
from mixbox.namespaces import Namespace

import stix.bindings.extensions.marking.ais as ais_binding
import stix.data_marking
from stix.data_marking import MarkingStructure


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


class AISConsentType(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.AISConsentType
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'
    _ALLOWED_VALUES = ('EVERYONE', 'USG', 'NONE')

    consent = fields.TypedField("consent", preset_hook=validate_value)

    def __init__(self, consent=None):
        super(AISConsentType, self).__init__()
        self.consent = consent


class TLPMarkingType(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.TLPMarkingType
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'
    _ALLOWED_VALUES = ('WHITE', 'GREEN', 'AMBER')

    color = fields.TypedField("color", preset_hook=validate_value)

    def __init__(self, color=None):
        super(TLPMarkingType, self).__init__()
        self.color = color


class NotProprietary(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.NotProprietary
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'

    cisa_proprietary = fields.TypedField("CISA_Proprietary")
    ais_consent = fields.TypedField("AISConsent", AISConsentType, key_name="ais_consent")
    tlp_marking = fields.TypedField("TLPMarking", TLPMarkingType, key_name="tlp_marking")

    def __init__(self, cisa_proprietary='false', ais_consent=None,
                 tlp_marking=None):
        super(NotProprietary, self).__init__()

        self.cisa_proprietary = cisa_proprietary
        self.ais_consent = ais_consent
        self.tlp_marking = tlp_marking


class IsProprietary(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.IsProprietary
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'

    cisa_proprietary = fields.TypedField("CISA_Proprietary")
    ais_consent = fields.TypedField("AISConsent", AISConsentType, key_name="ais_consent")
    tlp_marking = fields.TypedField("TLPMarking", TLPMarkingType, key_name="tlp_marking")

    def __init__(self, cisa_proprietary='true', ais_consent=None,
                 tlp_marking=None):
        super(IsProprietary, self).__init__()

        self.cisa_proprietary = cisa_proprietary
        self.ais_consent = ais_consent
        self.tlp_marking = tlp_marking


@stix.register_extension
class AISMarkingStructure(MarkingStructure):
    _binding = ais_binding
    _binding_class = _binding.AISMarkingStructure
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'
    _XSI_TYPE = "AIS:AISMarkingStructure"

    is_proprietary = fields.TypedField("Is_Proprietary", IsProprietary)
    not_proprietary = fields.TypedField("Not_Proprietary", NotProprietary)

    def __init__(self, is_proprietary=None, not_proprietary=None):
        super(AISMarkingStructure, self).__init__()

        self.is_proprietary = is_proprietary
        self.not_proprietary = not_proprietary


NAMESPACES = [
    Namespace('http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2', 'AIS', 'http://www.us-cert.gov/sites/default/files/STIX_Namespace/AIS_Bundle_Marking_1.1.1_v1.0.xsd')
]


def _update_namespaces():
    # Update the python-stix namespace dictionary
    from stix.utils import nsparser
    import mixbox.namespaces

    nsparser.STIX_NAMESPACES.add_namespace(NAMESPACES[0])
    mixbox.namespaces.register_namespace(NAMESPACES[0])


_update_namespaces()


# IndustryType allowed sectors
CHEMICAL_SECTOR = 'Chemical Sector'
COMMERCIAL_FACILITIES_SECTOR = 'Commercial Facilities Sector'
COMMUNICATIONS_SECTOR = 'Communications Sector'
CRITICAL_MANUFACTURING_SECTOR = 'Critical Manufacturing Sector'
DAMS_SECTOR = 'Dams Sector'
DEFENSE_INDUSTRIAL_BASE_SECTOR = 'Defense Industrial Base Sector'
EMERGENCY_SERVICES_SECTOR = 'Emergency Services Sector'
ENERGY_SECTOR = 'Energy Sector'
FINANCIAL_SERVICES_SECTOR = 'Financial Services Sector'
FOOD_AND_AGRICULTURE_SECTOR = 'Food and Agriculture Sector'
GOVERNMENT_FACILITIES_SECTOR = 'Government Facilities Sector'
HEALTH_CARE_AND_PUBLIC_HEALTH_SECTOR = 'Healthcare and Public Health Sector'
INFORMATION_TECHNOLOGY_SECTOR = 'Information Technology Sector'
NUCLEAR_REACTORS_MATERIALS_AND_WASTE_SECTOR = 'Nuclear Reactors, Materials, and Waste Sector'
OTHER = 'Other'
TRANSPORTATION_SYSTEMS_SECTOR = 'Transportation Systems Sector'
WATER_AND_WASTEWATER_SYSTEMS_SECTOR = 'Water and Wastewater Systems Sector'


def _validate_and_create_industry_type(industry_type):
    INDUSTRY_SECTORS = (CHEMICAL_SECTOR, COMMERCIAL_FACILITIES_SECTOR,
                        COMMUNICATIONS_SECTOR, CRITICAL_MANUFACTURING_SECTOR,
                        DAMS_SECTOR, DEFENSE_INDUSTRIAL_BASE_SECTOR,
                        EMERGENCY_SERVICES_SECTOR, ENERGY_SECTOR,
                        FINANCIAL_SERVICES_SECTOR, FOOD_AND_AGRICULTURE_SECTOR,
                        GOVERNMENT_FACILITIES_SECTOR,
                        HEALTH_CARE_AND_PUBLIC_HEALTH_SECTOR,
                        INFORMATION_TECHNOLOGY_SECTOR,
                        NUCLEAR_REACTORS_MATERIALS_AND_WASTE_SECTOR,
                        TRANSPORTATION_SYSTEMS_SECTOR, OTHER,
                        WATER_AND_WASTEWATER_SYSTEMS_SECTOR)

    lower_case_sectors = tuple(x.lower() for x in INDUSTRY_SECTORS)
    result = ""
    error = False
    val = []

    if isinstance(industry_type, str):
        # Pipe-delimited or single string supplied.
        val = [x.lower().strip() for x in industry_type.split("|")]

    elif isinstance(industry_type, (list, tuple)):
        # Create pipe-delimited string when list of strings is provided.
        val = [x.lower().strip() for x in industry_type]

    else:
        error = True

    for item in val:
        for idx, sector in enumerate(lower_case_sectors):
            if item == sector:
                if not result:
                    result = INDUSTRY_SECTORS[idx]
                else:
                    result = "{0}|{1}".format(result, INDUSTRY_SECTORS[idx])
                break
        else:
            # The sectors collection was exhausted. No match found.
            error = True
            break

    if not error and val:
        return result

    msg = 'IndustryType must be one of the following: {0}. Received \'{1}\'.'
    raise ValueError(msg.format(INDUSTRY_SECTORS, industry_type))


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
        The following line is required to register the AIS extension:
        >>> import stix.extensions.marking.ais
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
