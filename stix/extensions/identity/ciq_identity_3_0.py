# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import lxml.etree as et

import stix
import stix.bindings.extensions.identity.ciq_identity_3_0 as ciq_identity_binding
import stix.common as common
import stix.common.identity as identity
import stix.utils as utils


XML_NS_XPIL     = "urn:oasis:names:tc:ciq:xpil:3"
XML_NS_XNL      = "urn:oasis:names:tc:ciq:xnl:3"
XML_NS_XAL      = "urn:oasis:names:tc:ciq:xal:3"
XML_NS_STIX_EXT = "http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1"

et.register_namespace('xpil', XML_NS_XPIL)
et.register_namespace('xnl', XML_NS_XNL)
et.register_namespace('xal', XML_NS_XAL)
et.register_namespace('stix-ciqidentity', XML_NS_STIX_EXT)


class CIQIdentity3_0Instance(common.Identity):
    _binding = ciq_identity_binding
    _binding_class = _binding.CIQIdentity3_0InstanceType
    _namespace = "http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1"
    _XML_NS_PREFIX = "stix-ciqidentity"
    _XML_TYPE = "CIQIdentity3.0InstanceType"
    _XSI_TYPE = "stix-ciqidentity:CIQIdentity3.0InstanceType"

    def __init__(self, roles=None, specification=None):
        super(CIQIdentity3_0Instance, self).__init__()
        self.roles = roles
        self.specification = specification if specification else STIXCIQIdentity3_0()

    @property
    def roles(self):
        return self._roles

    @roles.setter
    def roles(self, valuelist):
        self._roles = []

        if not valuelist:
            return

        for role in valuelist:
            self.add_role(role)

    def add_role(self, role):
        if not isinstance(role, basestring):
            raise ValueError('role is not instance of basestring')

        self.roles.append(role)

    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        if value and not isinstance(value, STIXCIQIdentity3_0):
            raise ValueError('value not instance of STIXCIQIdentity3_0Type')

        self._specification = value

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(CIQIdentity3_0Instance, self).to_obj(return_obj)

        # return_obj.id = self.id_
        # return_obj.idref = self.idref_
        return_obj.xsi_type = self._XSI_TYPE

        if self.roles:
            for role in self.roles:
                return_obj.add_Role(role)

        if self.specification:
            return_obj.Specification = self.specification.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None
        if not return_obj:
            return_obj = cls()

        super(CIQIdentity3_0Instance, cls).from_obj(obj, return_obj)

        roles = obj.Role
        specification = obj.Specification

        if roles:
            for role in roles:
                return_obj.add_role(role)

        if specification is not None:
            return_obj.specification = STIXCIQIdentity3_0.from_obj(specification)

        return return_obj

    def to_dict(self):
        d = super(CIQIdentity3_0Instance, self).to_dict()
        d['xsi:type'] = self._XSI_TYPE

        if self.roles:
            d['roles'] = [str(x) for x in self.roles]
        if self.specification:
            d['specification'] = self.specification.to_dict()
        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(CIQIdentity3_0Instance, cls).from_dict(dict_repr, return_obj)

        roles = dict_repr.get('roles', [])
        specification = dict_repr.get('specification')

        for role in roles:
            return_obj.add_role(role)

        if specification:
            return_obj.specification = STIXCIQIdentity3_0.from_dict(specification)

        return return_obj


class STIXCIQIdentity3_0(stix.Entity):
    _namespace = "http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1"
    XML_TAG = "{%s}Specification" % _namespace

    def __init__(self, party_name=None, languages=None, addresses=None,
                 organisation_info=None, electronic_address_identifiers=None,
                 free_text_lines=None, contact_numbers=None,
                 nationalities=None):
        self.party_name = party_name
        self.languages = languages
        self.addresses = addresses
        self.organisation_info = organisation_info
        self.electronic_address_identifiers = electronic_address_identifiers
        self.free_text_lines = free_text_lines
        self.contact_numbers = contact_numbers
        self.nationalities = nationalities

    @property
    def addresses(self):
        return self._addresses

    @addresses.setter
    def addresses(self, value):
        self._addresses = []
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_address(v)
        else:
            self.add_address(value)

    def add_address(self, value):
        if not value:
            return
        elif isinstance(value, Address):
            self.addresses.append(value)
        else:
            raise ValueError('value must be instance of Address')

    @property
    def languages(self):
        return self._languages

    @languages.setter
    def languages(self, value):
        self._languages = []
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_language(v)
        else:
            self.add_language(value)

    def add_language(self, value):
        if not value:
            return
        elif isinstance(value, Language):
            self.languages.append(value)
        else:
            self.languages.append(Language(value))

    @property
    def party_name(self):
        return self._party_name

    @party_name.setter
    def party_name(self, value):
        if not value:
            self._party_name = None
        elif isinstance(value, PartyName):
            self._party_name = value
        else:
            raise ValueError('party_name must be instance of PartyName')

    @property
    def electronic_address_identifiers(self):
        return self._electronic_address_identifiers

    @electronic_address_identifiers.setter
    def electronic_address_identifiers(self, value):
        self._electronic_address_identifiers = []
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_electronic_address_identifier(v)
        else:
            self.add_electronic_address_identifier(value)

    def add_electronic_address_identifier(self, value):
        if not value:
            return
        elif isinstance(value, ElectronicAddressIdentifier):
            self.electronic_address_identifiers.append(value)
        else:
            self.electronic_address_identifiers.append(ElectronicAddressIdentifier(value))

    @property
    def free_text_lines(self):
        return self._free_text_lines

    @free_text_lines.setter
    def free_text_lines(self, value):
        self._free_text_lines = []
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_free_text_line(v)
        else:
            self.add_free_text_line(value)

    def add_free_text_line(self, value):
        if not value:
            return
        elif isinstance(value, FreeTextLine):
            self.free_text_lines.append(value)
        else:
            self.free_text_lines.append(FreeTextLine(value))

    @property
    def contact_numbers(self):
        return self._contact_numbers

    @contact_numbers.setter
    def contact_numbers(self, value):
        self._contact_numbers = []
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_contact_number(v)
        else:
            self.add_contact_number(value)

    def add_contact_number(self, value):
        if not value:
            return
        elif isinstance(value, ContactNumber):
            self.contact_numbers.append(value)
        else:
            self.contact_numbers.append(ContactNumber(value))

    @property
    def nationalities(self):
        return self._nationalities

    @nationalities.setter
    def nationalities(self, value):
        self._nationalities = []
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_nationality(v)
        else:
            self.add_nationality(value)

    def add_nationality(self, value):
        if not value:
            return
        elif isinstance(value, Country):
            self.nationalities.append(value)
        else:
            self.nationalities.append(Country(value))

    @property
    def organisation_info(self):
        return self._organisation_info

    @organisation_info.setter
    def organisation_info(self, value):
        if not value:
            self._organisation_info = None
        elif isinstance(value, OrganisationInfo):
            self._organisation_info = value
        else:
            raise ValueError('organisation_info must be instance of OrganisationInfo')

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None
        if not return_obj:
            return_obj = cls()

        party_name = obj.findall(PartyName.XML_TAG)
        if party_name is not None and len(party_name) > 0:
            return_obj.party_name = PartyName.from_obj(party_name[0])

        languages = obj.findall("{%s}Languages" % XML_NS_XPIL)
        if languages is not None and len(languages) > 0:
            return_obj.languages = [Language.from_obj(x) for x in languages[0]]

        addresses = obj.findall("{%s}Addresses" % XML_NS_XPIL)
        if addresses is not None and len(addresses) > 0:
            return_obj.addresses = [Address.from_obj(x) for x in addresses[0]]

        nationalities = obj.findall("{%s}Nationalities" % XML_NS_XPIL)
        if nationalities is not None and len(nationalities) > 0:
            return_obj.nationalities = [Country.from_obj(x) for x in nationalities[0]]

        organisation_info = obj.findall(OrganisationInfo.XML_TAG)
        if organisation_info is not None and len(organisation_info) > 0:
            return_obj.organisation_info = OrganisationInfo.from_obj(organisation_info[0])

        electronic_address_identifiers = obj.findall("{%s}ElectronicAddressIdentifiers" % XML_NS_XPIL)
        if electronic_address_identifiers is not None and len(electronic_address_identifiers) > 0:
            return_obj.electronic_address_identifiers = [ElectronicAddressIdentifier.from_obj(x) for x in electronic_address_identifiers[0]]

        free_text_lines = obj.findall("{%s}FreeTextLines" % XML_NS_XPIL)
        if free_text_lines is not None and len(free_text_lines) > 0:
            return_obj.free_text_lines = [FreeTextLine.from_obj(x) for x in free_text_lines[0]]

        contact_numbers = obj.findall("{%s}ContactNumbers" % XML_NS_XPIL)
        if contact_numbers is not None and len(contact_numbers) > 0:
            return_obj.contact_numbers = [ContactNumber.from_obj(x) for x in contact_numbers[0]]

        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        super(STIXCIQIdentity3_0, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            root_tag = STIXCIQIdentity3_0.XML_TAG
            return_obj = et.Element(root_tag)

        if self.free_text_lines:
            ftl_root = et.Element("{%s}FreeTextLines" % XML_NS_XPIL)
            return_obj.append(ftl_root)
            for ftl in self.free_text_lines:
                ftl_root.append(ftl.to_obj(ns_info=ns_info))

        if self.party_name:
            return_obj.append(self.party_name.to_obj(ns_info=ns_info))

        if self.addresses:
            addresses_root = et.Element("{%s}Addresses" % XML_NS_XPIL)
            return_obj.append(addresses_root)
            for address in self.addresses:
                addresses_root.append(address.to_obj(ns_info=ns_info))

        if self.contact_numbers:
            contact_numbers_root = et.Element("{%s}ContactNumbers" % XML_NS_XPIL)
            return_obj.append(contact_numbers_root)
            for contact_number in self.contact_numbers:
                contact_numbers_root.append(contact_number.to_obj(ns_info=ns_info))

        if self.electronic_address_identifiers:
            eai_root = et.Element("{%s}ElectronicAddressIdentifiers" % XML_NS_XPIL)
            return_obj.append(eai_root)
            for eai in self.electronic_address_identifiers:
                eai_root.append(eai.to_obj(ns_info=ns_info))

        if self.organisation_info:
            return_obj.append(self.organisation_info.to_obj(ns_info=ns_info))

        if self.languages:
            languages_root = et.Element("{%s}Languages" % XML_NS_XPIL)
            return_obj.append(languages_root)
            for language in self.languages:
                languages_root.append(language.to_obj(ns_info=ns_info))

        if self.nationalities:
            nationalities_root = et.Element("{%s}Nationalities" % XML_NS_XPIL)
            return_obj.append(nationalities_root)
            for country in self.nationalities:
                country_obj = country.to_obj(ns_info=ns_info)
                country_obj.tag = "{%s}Country" % XML_NS_XPIL
                nationalities_root.append(country_obj)

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.party_name = PartyName.from_dict(dict_repr.get('party_name'))
        return_obj.languages = [Language.from_dict(x) for x in dict_repr.get('languages', [])]
        return_obj.addresses = [Address.from_dict(x) for x in dict_repr.get('addresses', [])]
        return_obj.electronic_address_identifiers = [ElectronicAddressIdentifier.from_dict(x) for x in dict_repr.get('electronic_address_identifiers', [])]
        return_obj.free_text_lines = [FreeTextLine.from_dict(x) for x in dict_repr.get('free_text_lines', [])]
        return_obj.contact_numbers = [ContactNumber.from_dict(x) for x in dict_repr.get('contact_numbers', [])]
        return_obj.nationalities = [Country.from_dict(x) for x in dict_repr.get('nationalities', [])]
        return_obj.organisation_info = OrganisationInfo.from_dict(dict_repr.get('organisation_info'))

        return return_obj

    def to_dict(self):
        d = {}

        if self.party_name:
            d['party_name'] = self.party_name.to_dict()
        if self.languages:
            d['languages'] = [x.to_dict() for x in self.languages]
        if self.addresses:
            d['addresses'] = [x.to_dict() for x in self.addresses]
        if self.electronic_address_identifiers:
            d['electronic_address_identifiers'] = [x.to_dict() for x in self.electronic_address_identifiers]
        if self.free_text_lines:
            d['free_text_lines'] = [x.to_dict() for x in self.free_text_lines]
        if self.contact_numbers:
            d['contact_numbers'] = [x.to_dict() for x in self.contact_numbers]
        if self.nationalities:
            d['nationalities'] = [x.to_dict() for x in self.nationalities]
        if self.organisation_info:
            d['organisation_info'] = self.organisation_info.to_dict()

        return d


class Address(stix.Entity):
    _namespace = XML_NS_XPIL
    XML_TAG = "{%s}Address" % _namespace

    def __init__(self, free_text_address=None, country=None,
                 administrative_area=None):
        self.free_text_address = free_text_address
        self.country = country
        self.administrative_area = administrative_area

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._set_var(Country, country=value)

    @property
    def administrative_area(self):
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, value):
        self._set_var(AdministrativeArea, administrative_area=value)

    @property
    def free_text_address(self):
        return self._free_text_address

    @free_text_address.setter
    def free_text_address(self, value):
        self._set_var(FreeTextAddress, free_text_address=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(Address, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = et.Element(self.XML_TAG)

        if self.free_text_address:
            return_obj.append(self.free_text_address.to_obj(ns_info=ns_info))
        if self.country:
            return_obj.append(self.country.to_obj(ns_info=ns_info))
        if self.administrative_area:
            return_obj.append(self.administrative_area.to_obj(ns_info=ns_info))

        return return_obj

    def to_dict(self):
        d = {}
        if self.free_text_address:
            d['free_text_address'] = self.free_text_address.to_dict()
        if self.country:
            d['country'] = self.country.to_dict()
        if self.administrative_area:
            d['administrative_area'] = self.administrative_area.to_dict()
        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None
        if not return_obj:
            return_obj = cls()

        free_text_address = obj.findall("{%s}FreeTextAddress" % XML_NS_XAL)
        if len(free_text_address) > 0:
            return_obj.free_text_address = FreeTextAddress.from_obj(free_text_address[0])

        country = obj.findall("{%s}Country" % XML_NS_XAL)
        if len(country) > 0:
            return_obj.country = Country.from_obj(country[0])

        administrative_area = obj.findall("{%s}AdministrativeArea" % XML_NS_XAL)
        if len(administrative_area) > 0:
            return_obj.administrative_area = AdministrativeArea.from_obj(administrative_area[0])

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.free_text_address = FreeTextAddress.from_dict(d.get('free_text_address'))
        return_obj.country = Country.from_dict(d.get('country'))
        return_obj.administrative_area = AdministrativeArea.from_dict(d.get('administrative_area'))
        return return_obj


class AdministrativeArea(stix.Entity):
    _namespace = XML_NS_XAL
    XML_TAG = "{%s}AdministrativeArea" % _namespace

    def __init__(self, name_elements=None):
        self.name_elements = name_elements

    @property
    def name_elements(self):
        return self._name_elements

    @name_elements.setter
    def name_elements(self, value):
        self._name_elements = []
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_name_element(v)
        else:
            self.add_name_element(value)

    def add_name_element(self, value):
        if not value:
            return
        elif isinstance(value, NameElement):
            self.name_elements.append(value)
        else:
            self.name_elements.append(NameElement(value))

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None
        if not return_obj:
            return_obj = cls()

        name_elements = obj.findall(NameElement.XML_TAG)
        if name_elements:
            for name_element in name_elements:
                return_obj.name_elements.append(NameElement.from_obj(name_element))

        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        super(AdministrativeArea, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = et.Element(self.XML_TAG)

        for name_element in self.name_elements:
            return_obj.append(name_element.to_obj(ns_info=ns_info))

        return return_obj

    def to_dict(self):
        d = {}
        if self.name_elements:
            d['name_elements'] = [x.to_dict() for x in self.name_elements]
        return d

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.name_elements = [NameElement.from_dict(x) for x in d.get('name_elements', [])]
        return return_obj


class Country(stix.Entity):
    _namespace = XML_NS_XAL
    XML_TAG = "{%s}Country" % _namespace

    def __init__(self, name_elements=None):
        self.name_elements = name_elements

    @property
    def name_elements(self):
        return self._name_elements

    @name_elements.setter
    def name_elements(self, value):
        self._name_elements = []
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_name_element(v)
        else:
            self.add_name_element(value)

    def add_name_element(self, value):
        if not value:
            return
        elif isinstance(value, NameElement):
            self.name_elements.append(value)
        else:
            self.name_elements.append(NameElement(value))

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None
        if not return_obj:
            return_obj = cls()

        name_elements = obj.findall("{%s}NameElement" % XML_NS_XAL)
        if name_elements:
            for name_element in name_elements:
                return_obj.name_elements.append(NameElement.from_obj(name_element))

        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        super(Country, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = et.Element(self.XML_TAG)

        for name_element in self.name_elements:
            return_obj.append(name_element.to_obj(ns_info=ns_info))

        return return_obj

    def to_dict(self):
        d = {}
        if self.name_elements:
            d['name_elements'] = [x.to_dict() for x in self.name_elements]
        return d

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.name_elements = [NameElement.from_dict(x) for x in d.get('name_elements', [])]
        return return_obj


class NameElement(stix.Entity):
    _namespace = XML_NS_XAL
    XML_TAG = "{%s}NameElement" % XML_NS_XAL

    def __init__(self, value=None, name_type=None, name_code=None, name_code_type=None):
        self.value = value
        self.name_type = name_type
        self.name_code = name_code
        self.name_code_type = name_code_type

    def to_obj(self, return_obj=None, ns_info=None):
        super(NameElement, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        return_obj = et.Element(self.XML_TAG)
        return_obj.text = self.value

        if self.name_type:
            return_obj.set('{%s}NameType' % self._namespace, self.name_type)
        if self.name_code:
            return_obj.set('{%s}NameCode' % self._namespace, self.name_code)
        if self.name_code_type:
            return_obj.set('{%s}NameCodeType' % self._namespace, self.name_code_type)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.value = obj.text
        return_obj.name_type = obj.get('{%s}NameType' % cls._namespace)
        return_obj.name_code = obj.get('{%s}NameCode' % cls._namespace)
        return_obj.name_code_type = obj.get('{%s}NameCodeType' % cls._namespace)

        return return_obj

    def to_dict(self):
        d = {}
        if self.value:
            d['value'] = self.value
        if self.name_type:
            d['name_type'] = self.name_type
        if self.name_code:
            d['name_code'] = self.name_code
        if self.name_code_type:
            d['name_code_type'] = self.name_code_type
        return d

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.value = d.get('value')
        return_obj.name_type = d.get('name_type')
        return_obj.name_code = d.get('name_code')
        return_obj.name_code_type = d.get('name_code_type')
        return return_obj


class FreeTextAddress(stix.Entity):
    _namespace = XML_NS_XAL
    XML_TAG = "{%s}FreeTextAddress" % XML_NS_XAL

    def __init__(self, address_lines=None):
        self.address_lines = address_lines

    @property
    def address_lines(self):
        return self._address_lines

    @address_lines.setter
    def address_lines(self, value):
        self._address_lines = []

        if value is None or len(value) == 0:
            return
        elif utils.is_sequence(value):
            self._address_lines = value
        else:
            self._address_lines.append(value)

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None or len(obj) == 0:
            return None
        if not return_obj:
            return_obj = cls()

        address_line_tag = "{%s}AddressLine" % XML_NS_XAL
        address_lines = obj.findall(address_line_tag)
        if address_lines:
            for address_line in address_lines:
                return_obj.address_lines.append(address_line.text)

        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        super(FreeTextAddress, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = et.Element(self.XML_TAG)

        for address in self.address_lines:
            address_line = et.Element("{%s}AddressLine" % XML_NS_XAL)
            address_line.text = address
            return_obj.append(address_line)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.address_lines = d.get('address_lines', [])
        return return_obj

    def to_dict(self):
        d = {}
        if self.address_lines:
            d['address_lines'] = self.address_lines
        return d


class PartyName(stix.Entity):
    _namespace = XML_NS_XPIL
    XML_TAG = "{%s}PartyName" % _namespace

    def __init__(self, name_lines=None, person_names=None, organisation_names=None):
        self.name_lines = []
        self.person_names = []
        self.organisation_names = []

        if name_lines:
            for value in name_lines:
                self.add_name_line(value)

        if person_names:
            for value in person_names:
                self.add_person_name(value)

        if organisation_names:
            for value in organisation_names:
                self.add_organisation_name(value)

    def add_name_line(self, value):
        if isinstance(value, basestring):
            self.name_lines.append(NameLine(value))
        elif isinstance(value, NameLine):
            self.name_lines.append(value)
        else:
            raise ValueError('value must be a basestring or NameLine instance')

    def add_person_name(self, value):
        if isinstance(value, basestring):
            self.person_names.append(PersonName(name_elements=[value]))
        elif isinstance(value, PersonName):
            self.person_names.append(value)
        else:
            raise ValueError('value must be instance of PersonName or basestring')

    def add_organisation_name(self, value):
        if isinstance(value, basestring):
            self.organisation_names.append(OrganisationName(name_elements=[value]))
        elif isinstance(value, OrganisationName):
            self.organisation_names.append(value)
        else:
            raise ValueError('value must be instance of OrganisationName')

    def to_obj(self, return_obj=None, ns_info=None):
        super(PartyName, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            root_tag = PartyName.XML_TAG
            return_obj = et.Element(root_tag)

        for name_line in self.name_lines:
            return_obj.append(name_line.to_obj(ns_info=ns_info))

        for person_name in self.person_names:
            return_obj.append(person_name.to_obj(ns_info=ns_info))

        for organisation_name in self.organisation_names:
            return_obj.append(organisation_name.to_obj(ns_info=ns_info))

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        name_lines = obj.findall(NameLine.XML_TAG)
        if name_lines:
            for name_line_obj in name_lines:
                name_line = NameLine.from_obj(name_line_obj)
                return_obj.add_name_line(name_line)

        person_names = obj.findall(PersonName.XML_TAG)
        if person_names:
            for person_name_obj in person_names:
                person_name = PersonName.from_obj(person_name_obj)
                return_obj.add_person_name(person_name)

        org_names = obj.findall(OrganisationName.XML_TAG)
        if org_names:
            for organisation_name_obj in org_names:
                org_name = OrganisationName.from_obj(organisation_name_obj)
                return_obj.add_organisation_name(org_name)

        return return_obj

    def to_dict(self):
        d = {}

        if self.name_lines:
            for name_line in self.name_lines:
                d.setdefault('name_lines', []).append(name_line.to_dict())

        if self.organisation_names:
            for on in self.organisation_names:
                d.setdefault('organisation_names', []).append(on.to_dict())

        if self.person_names:
            for pn in self.person_names:
                d.setdefault('person_names', []).append(pn.to_dict())

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        nl_dicts = dict_repr.get('name_lines', [])
        on_dicts = dict_repr.get('organisation_names', [])
        pn_dicts = dict_repr.get('person_names', [])

        for nl in nl_dicts:
            name_line = NameLine.from_dict(nl)
            return_obj.add_name_line(name_line)

        for on in on_dicts:
            organisation_name = OrganisationName.from_dict(on)
            return_obj.add_organisation_name(organisation_name)

        for pn in pn_dicts:
            person_name = PersonName.from_dict(pn)
            return_obj.add_person_name(person_name)

        return return_obj


class NameLine(stix.Entity):
    _namespace = XML_NS_XNL
    XML_TAG = "{%s}NameLine" % _namespace

    def __init__(self, value=None, type_=None):
        self.value = value
        self.type = type_

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value and not isinstance(value, basestring):
            raise ValueError('value must be instance of basestring')

        self._value = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(NameLine, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            root_tag = NameLine.XML_TAG
            return_obj = et.Element(root_tag)

        if self.type:
            return_obj.attrib['Type'] = self.type

        if self.value:
            return_obj.text = self.value

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.value = obj.text
        return_obj.type = obj.get('Type')

        return return_obj

    def to_dict(self):
        d = {}
        d['value'] = self.value

        if self.type:
            d['type'] = self.type

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.value = dict_repr.get('value', None)
        return_obj.type = dict_repr.get('type', None)

        return return_obj


class PersonName(stix.Entity):
    _namespace = XML_NS_XNL
    XML_TAG = "{%s}PersonName" % _namespace

    def __init__(self, name_elements=None):
        self.name_elements = []

        if name_elements:
            for name_element in name_elements:
                self.add_name_element(name_element)

    def add_name_element(self, value):
        if isinstance(value, basestring):
            self.name_elements.append(PersonNameElement(value=value))
        elif isinstance(value, PersonNameElement):
            self.name_elements.append(value)
        else:
            raise ValueError('value must be instance of PersonNameElement')

    def to_obj(self, return_obj=None, ns_info=None):
        super(PersonName, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            root_tag = PersonName.XML_TAG
            return_obj = et.Element(root_tag)

        for name_element in self.name_elements:
            return_obj.append(name_element.to_obj(ns_info=ns_info))

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        name_elements = obj.findall(PersonNameElement.XML_TAG)
        if name_elements:
            for name_element_obj in name_elements:
                person_name_element = PersonNameElement.from_obj(name_element_obj)
                return_obj.add_name_element(person_name_element)

        return return_obj

    def to_dict(self):
        d = {}

        if self.name_elements:
            for ne in self.name_elements:
                d.setdefault('name_elements', []).append(ne.to_dict())

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        ne_dicts = dict_repr.get('name_elements', [])

        for ne_dict in ne_dicts:
            return_obj.add_name_element(PersonNameElement.from_dict(ne_dict))

        return return_obj


class OrganisationName(stix.Entity):
    _namespace = XML_NS_XNL
    XML_TAG = "{%s}OrganisationName" % _namespace

    def __init__(self, name_elements=None, subdivision_names=None, type_=None):
        self.type_ = type_
        self.name_elements = name_elements
        self.subdivision_names = subdivision_names

    @property
    def name_elements(self):
        return self._name_elements

    @name_elements.setter
    def name_elements(self, value):
        self._name_elements = []
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_organisation_name_element(v)
        else:
            self.add_organisation_name_element(value)

    def add_organisation_name_element(self, value):
        if isinstance(value, basestring):
            self.name_elements.append(OrganisationNameElement(value=value))
        elif isinstance(value, OrganisationNameElement):
            self.name_elements.append(value)
        else:
            raise ValueError('value must be instance of OrganisationNameElement')

    @property
    def subdivision_names(self):
        return self._subdivision_names

    @subdivision_names.setter
    def subdivision_names(self, value):
        self._subdivision_names = []
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_subdivision_name(v)
        else:
            self.add_subdivision_name(value)

    def add_subdivision_name(self, value):
        if not isinstance(value, SubDivisionName):
            raise ValueError('value must be instance of SubDivisionName')

        self.subdivision_names.append(value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(OrganisationName, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            root_tag = OrganisationName.XML_TAG
            return_obj = et.Element(root_tag)

        if self.type_:
            return_obj.attrib['{%s}Type' % XML_NS_XNL] = self.type_
        for name_element in self.name_elements:
            return_obj.append(name_element.to_obj(ns_info=ns_info))
        for subdivision_name in self.subdivision_names:
            return_obj.append(subdivision_name.to_obj(ns_info=ns_info))

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.type_ = obj.attrib.get('{%s}Type' % XML_NS_XNL)

        name_elements = obj.findall(OrganisationNameElement.XML_TAG)
        if name_elements:
            for name_element_obj in name_elements:
                name_element = OrganisationNameElement.from_obj(name_element_obj)
                return_obj.add_organisation_name_element(name_element)

        sub_division_names = obj.findall(SubDivisionName.XML_TAG)
        if sub_division_names:
            for sub_division_name_obj in sub_division_names:
                sub_division_name = SubDivisionName.from_obj(sub_division_name_obj)
                return_obj.add_subdivision_name(sub_division_name)

        return return_obj

    def to_dict(self):
        d = {}

        if self.type_:
            d['type'] = self.type_
        if self.name_elements:
            for ne in self.name_elements:
                d.setdefault('name_elements', []).append(ne.to_dict())
        if self.subdivision_names:
            for sn in self.subdivision_names:
                d.setdefault('subdivision_names', []).append(sn.to_dict())

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        ne_dicts = dict_repr.get('name_elements', [])
        sn_dicts = dict_repr.get('subdivision_names', [])

        return_obj.type_ = dict_repr.get('type')
        for ne_dict in ne_dicts:
            return_obj.add_organisation_name_element(OrganisationNameElement.from_dict(ne_dict))
        for sn_dict in sn_dicts:
            return_obj.add_subdivision_name(SubDivisionName.from_dict(sn_dict))

        return return_obj


class _BaseNameElement(stix.Entity):
    """Do not instantiate directly: use PersonNameElement or
    OrganisationNameElement

    """
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        # if not value:
        #    raise ValueError('value cannot be None')

        self._value = value

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not return_obj:
            raise ValueError("Must supply return_obj")

        return_obj.value = obj.valueOf_
        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        super(_BaseNameElement, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        return_obj.text = self.value
        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not return_obj:
            raise ValueError("Must supply return_obj")

        return_obj.value = dict_repr.get('value', None)
        return return_obj

    def to_dict(self):
        return dict(value=self.value)


class PersonNameElement(_BaseNameElement):
    _namespace = XML_NS_XNL
    XML_TAG = "{%s}NameElement" % _namespace

    TYPE_TITLE = 'Title'
    TYPE_PRECEDING_TITLE = 'PrecedingTitle'
    TYPE_FIRST_NAME = 'FirstName'
    TYPE_MIDDLE_NAME = 'MiddleName'
    TYPE_LAST_NAME = 'LastName'
    TYPE_OTHER_NAME = 'OtherName'
    TYPE_ALIAS = 'Alias'
    TYPE_GENERATION_IDENTIFIER = 'GenerationIdentifier'
    TYPE_DEGREE = 'Degree'

    TYPES = (
        TYPE_TITLE, TYPE_PRECEDING_TITLE, TYPE_FIRST_NAME, TYPE_LAST_NAME,
        TYPE_MIDDLE_NAME, TYPE_OTHER_NAME, TYPE_ALIAS,
        TYPE_GENERATION_IDENTIFIER, TYPE_DEGREE
    )

    def __init__(self, value=None, element_type=None):
        super(PersonNameElement, self).__init__(value)
        self.element_type = element_type

    @property
    def element_type(self):
        return self._element_type

    @element_type.setter
    def element_type(self, value):
        if value and value not in self.TYPES:
            raise ValueError('value must be one of %s: ' % (self.TYPES,))

        self._element_type = value

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            root_tag = PersonNameElement.XML_TAG
            return_obj = et.Element(root_tag)

        super(PersonNameElement, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if self.element_type:
            return_obj.attrib['ElementType'] = self.element_type

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.element_type = obj.get('ElementType')
        return_obj.value = obj.text

        return return_obj

    def to_dict(self):
        d = {}
        d['value'] = self.value

        if self.element_type:
            d['element_type'] = self.element_type

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.value = dict_repr.get('value', None)
        return_obj.element_type = dict_repr.get('element_type', None)

        return return_obj


class OrganisationNameElement(_BaseNameElement):
    _namespace = XML_NS_XNL
    XML_TAG = "{%s}NameElement" % _namespace

    TYPE_NAME_ONLY = "NameOnly"
    TYPE_TYPE_ONLY = "TypeOnly"
    TYPE_FULL_NAME = "FullName"

    TYPES = (TYPE_NAME_ONLY, TYPE_TYPE_ONLY, TYPE_FULL_NAME)

    def __init__(self, value=None, element_type=None):
        super(OrganisationNameElement, self).__init__(value)
        self.value = value
        self.element_type = element_type

    @property
    def element_type(self):
        return self._element_type

    @element_type.setter
    def element_type(self, value):
        if value and value not in self.TYPES:
            raise ValueError('value must be one of: %s ' % (self.TYPES,))

        self._element_type = value

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            root_tag = OrganisationNameElement.XML_TAG
            return_obj = et.Element(root_tag)

        super(OrganisationNameElement, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if self.element_type:
            return_obj.attrib['{%s}ElementType' % XML_NS_XNL] = self.element_type

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.element_type = obj.get('{%s}ElementType' % XML_NS_XNL)
        return_obj.value = obj.text

        return return_obj

    def to_dict(self):
        d = {}
        if self.element_type:
            d['element_type'] = self.element_type
        if self.value:
            d['value'] = self.value

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.value = dict_repr.get('value')
        return_obj.element_type = dict_repr.get('element_type')

        return return_obj


class SubDivisionName(stix.Entity):
    _namespace = XML_NS_XNL
    XML_TAG = "{%s}SubDivisionName" % _namespace

    TYPE_DEPARTMENT = 'Department'
    TYPE_DIVISION = 'Division'
    TYPE_BRANCH = 'Branch'
    TYPE_BUSINESS_UNIT = 'BusinessUnit'
    TYPE_SCHOOL = 'School'
    TYPE_SECTION = 'Section'

    TYPES = (
        TYPE_DEPARTMENT, TYPE_DIVISION, TYPE_BRANCH, TYPE_BUSINESS_UNIT,
        TYPE_SCHOOL, TYPE_SECTION
    )

    def __init__(self, value=None, type_=None):
        self.value = value
        self.type = type_

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value and value not in self.TYPES:
            raise ValueError('value must be one of: %s' % (self.TYPES,))

        self._type = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(SubDivisionName, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            root_tag = SubDivisionName.XML_TAG
            return_obj = et.Element(root_tag)

        if self.type:
            return_obj.attrib['{%s}Type' % XML_NS_XNL] = self.type

        return_obj.text = self.value
        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.type = obj.get('{%s}Type' % XML_NS_XNL)
        return_obj.value = obj.text

        return return_obj

    def to_dict(self):
        d = {}
        d['value'] = self.value
        if self.type:
            d['type'] = self.type

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.value = dict_repr.get('value')
        return_obj.type = dict_repr.get('type')
        return return_obj


class Language(stix.Entity):
    _namespace = XML_NS_XPIL
    XML_TAG = "{%s}Language" % _namespace

    def __init__(self, value=None):
        self.value = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(Language, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        return_obj = et.Element(self.XML_TAG)
        return_obj.text = self.value
        return return_obj

    @classmethod
    def from_obj(cls, obj):
        if obj is None:
            return None

        return_obj = cls()
        return_obj.value = obj.text
        return return_obj

    def to_dict(self):
        d = {}
        if self.value:
            d['value'] = self.value
        return d

    @classmethod
    def from_dict(cls, d):
        if not d:
            return None

        return_obj = cls()
        return_obj.value = d.get('value')
        return return_obj


class ElectronicAddressIdentifier(stix.Entity):
    _namespace = XML_NS_XPIL
    XML_TAG = "{%s}ElectronicAddressIdentifier" % _namespace

    def __init__(self, value=None, type_=None):
        self.type_ = type_
        self.value = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(ElectronicAddressIdentifier, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        return_obj = et.Element(self.XML_TAG)
        return_obj.text = self.value

        if self.type_:
            return_obj.attrib['{%s}Type' % XML_NS_XPIL] = self.type_

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.type_ = obj.attrib.get('{%s}Type' % XML_NS_XPIL)
        return_obj.value = obj.text
        return return_obj

    def to_dict(self):
        d = {}
        if self.value:
            d['value'] = self.value
        if self.type_:
            d['type'] = self.type_
        return d

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.value = d.get('value')
        return_obj.type_ = d.get('type')
        return return_obj


class OrganisationInfo(stix.Entity):
    _namespace = XML_NS_XPIL
    XML_TAG = "{%s}OrganisationInfo" % _namespace

    def __init__(self, industry_type=None):
        self.industry_type = industry_type

    def to_obj(self, return_obj=None, ns_info=None):
        super(OrganisationInfo, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        return_obj = et.Element(self.XML_TAG)
        if self.industry_type:
            return_obj.attrib['{%s}IndustryType' % self._namespace] = self.industry_type

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.industry_type = obj.get('{%s}IndustryType' % cls._namespace)
        return return_obj

    def to_dict(self):
        d = {}
        if self.industry_type:
            d['industry_type'] = self.industry_type
        return d

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.industry_type = d.get('industry_type')
        return return_obj


class FreeTextLine(stix.Entity):
    _namespace = XML_NS_XPIL
    XML_TAG = "{%s}FreeTextLine" % _namespace

    def __init__(self, value=None, type_=None):
        self.value = value
        self.type_ = type_

    def to_obj(self, return_obj=None, ns_info=None):
        super(FreeTextLine, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        return_obj = et.Element(self.XML_TAG)
        if self.type_:
            return_obj.attrib['{%s}Type' % self._namespace] = self.type_
        if self.value:
            return_obj.text = self.value

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.type_ = obj.get('{%s}Type' % cls._namespace)
        return_obj.value = obj.text
        return return_obj

    def to_dict(self):
        d = {}
        if self.type_:
            d['type'] = self.type_
        if self.value:
            d['value'] = self.value
        return d

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.type_ = d.get('type')
        return_obj.value = d.get('value')
        return return_obj


class ContactNumber(stix.Entity):
    _namespace = XML_NS_XPIL
    XML_TAG = "{%s}ContactNumber" % _namespace

    COM_MEDIA_TYPE_CELLPHONE = "Cellphone"
    COM_MEDIA_TYPE_FAX = "Fax"
    COM_MEDIA_TYPE_PAGER = "Pager"
    COM_MEDIA_TYPE_TELEPHONE = "Telephone"
    COM_MEDIA_TYPE_VOIP = "VOIP"

    ALLOWED_COM_MEDIA_TYPES = (
        COM_MEDIA_TYPE_CELLPHONE, COM_MEDIA_TYPE_FAX, COM_MEDIA_TYPE_PAGER,
        COM_MEDIA_TYPE_TELEPHONE, COM_MEDIA_TYPE_VOIP
    )

    def __init__(self, contact_number_elements=None, communication_media_type=None):
        self.communication_media_type = communication_media_type
        self.contact_number_elements = contact_number_elements

    @property
    def contact_number_elements(self):
        return self._contact_number_elements

    @contact_number_elements.setter
    def contact_number_elements(self, value):
        self._contact_number_elements = []
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_contact_number_element(v)
        else:
            self.add_contact_number_element(value)

    def add_contact_number_element(self, value):
        if not value:
            return
        elif isinstance(value, ContactNumberElement):
            self.contact_number_elements.append(value)
        else:
            self.contact_number_elements.append(ContactNumberElement(value))

    @property
    def communication_media_type(self):
        return self._communication_media_type

    @communication_media_type.setter
    def communication_media_type(self, value):
        if not value:
            self._communication_media_type = None
        elif value not in self.ALLOWED_COM_MEDIA_TYPES:
            raise ValueError('value must be one of %s' % (self.ALLOWED_COM_MEDIA_TYPES,))
        else:
            self._communication_media_type = value

    def to_obj(self, return_obj=None, ns_info=None):
        return_obj = et.Element(self.XML_TAG)
        if self.communication_media_type:
            return_obj.attrib['{%s}CommunicationMediaType' % self._namespace] = self.communication_media_type
        if self.contact_number_elements:
            for contact_number_element in self.contact_number_elements:
                return_obj.append(contact_number_element.to_obj(ns_info=ns_info))

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.communication_media_type = obj.get('{%s}CommunicationMediaType' % cls._namespace)

        contact_number_elements = obj.findall("{%s}ContactNumberElement" % XML_NS_XPIL)
        if contact_number_elements is not None and len(contact_number_elements) > 0:
            return_obj.contact_number_elements = [ContactNumberElement.from_obj(x) for x in contact_number_elements]

        return return_obj

    def to_dict(self):
        d = {}
        if self.communication_media_type:
            d['communication_media_type'] = self.communication_media_type
        if self.contact_number_elements:
            d['contact_number_elements'] = [x.to_dict() for x in self.contact_number_elements]

        return d

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.communication_media_type = d.get('communication_media_type')
        return_obj.contact_number_elements = [ContactNumberElement.from_dict(x) for x in d.get('contact_number_elements', [])]

        return return_obj


class ContactNumberElement(stix.Entity):
    _namespace = XML_NS_XPIL
    XML_TAG = "{%s}ContactNumberElement" % _namespace

    TYPE_COUNTRY_CODE = "CountryCode"
    TYPE_AREA_CODE = "AreaCode"
    TYPE_LOCAL_NUMBER = "LocalNumber"
    TYPE_EXTENSION = "Extension"
    TYPE_PIN = "Pin"
    TYPE_SEPARATOR = "Separator"
    TYPE_NATIONAL_NUMBER = "NationalNumber"
    TYPE_INTERNATIONAL_NUMBER = "InternationalNumber"

    ALLOWED_TYPES = (
        TYPE_AREA_CODE, TYPE_COUNTRY_CODE, TYPE_EXTENSION,
        TYPE_INTERNATIONAL_NUMBER, TYPE_LOCAL_NUMBER, TYPE_NATIONAL_NUMBER,
        TYPE_SEPARATOR, TYPE_PIN
    )

    def __init__(self, value=None, type_=None):
        self.value = value
        self.type_ = type_

    @property
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, value):
        if not value:
            self._type = None
        elif value not in self.ALLOWED_TYPES:
            raise ValueError('value must be one of %s' % (self.ALLOWED_TYPES,))
        else:
            self._type = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(ContactNumberElement, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        return_obj = et.Element(self.XML_TAG)
        if self.type_:
            return_obj.attrib['{%s}Type' % self._namespace] = self.type_
        if self.value:
            return_obj.text = self.value

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.type_ = obj.get('{%s}Type' % cls._namespace)
        return_obj.value = obj.text
        return return_obj

    def to_dict(self):
        d = {}
        if self.type_:
            d['type'] = self.type_
        if self.value:
            d['value'] = self.value
        return d

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.type_ = d.get('type')
        return_obj.value = d.get('value')
        return return_obj


# Register the extension
identity.add_extension(CIQIdentity3_0Instance)
