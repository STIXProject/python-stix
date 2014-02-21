# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import Identity
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.extensions.identity.ciq_identity_3_0 as ciq_identity_binding

# xml element tree creation
#from xml.etree import cElementTree as et
import lxml.etree as et

XML_NS_XPIL     = "urn:oasis:names:tc:ciq:xpil:3"
XML_NS_XNL      = "urn:oasis:names:tc:ciq:xnl:3"
XML_NS_STIX_EXT ="http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1"

et.register_namespace('xpil', XML_NS_XPIL)
et.register_namespace('xnl', XML_NS_XNL)
et.register_namespace('ExtSch', XML_NS_STIX_EXT)

class CIQIdentity3_0Instance(Identity):
    _binding        = ciq_identity_binding
    _namespace      = "http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1"
    _XML_NS_PREFIX  = "ciqIdentity"
    _XML_TYPE       = "CIQIdentity3.0InstanceType"

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

        if valuelist:
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


    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding.CIQIdentity3_0InstanceType()

        super(CIQIdentity3_0Instance, self).to_obj(return_obj)

        #return_obj.set_id(self.id_)
        #return_obj.set_idref(self.idref_)

        if self.roles:
            for role in self.roles:
                return_obj.add_Role(role)

        if self.specification:
            return_obj.set_Specification(self.specification.to_obj())

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        super(CIQIdentity3_0Instance, cls).from_obj(obj, return_obj)

        roles = obj.get_Role()
        specification = obj.get_Specification()

        if roles:
            for role in roles:
                return_obj.add_role(role)

        if specification is not None:
            return_obj.specification = STIXCIQIdentity3_0.from_obj(specification)

        return return_obj 

    def to_dict(self):
        d = super(CIQIdentity3_0Instance, self).to_dict()
        d['xsi:type'] = "%s:%s" % (CIQIdentity3_0Instance._XML_NS_PREFIX, CIQIdentity3_0Instance._XML_TYPE)
        
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
    _namespace      = "http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1"
    XML_TAG = "{%s}Specification" % _namespace

    def __init__(self, party_name=None):
        self.party_name = party_name if party_name else PartyName()

    @property
    def party_name(self):
        return self._party_name

    @party_name.setter
    def party_name(self, value):
        if value and not isinstance(value, PartyName):
            raise ValueError('party_name must be instance of PartyName')

        self._party_name = value

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        party_name = obj.findall(PartyName.XML_TAG)
        if party_name:
            return_obj.party_name = PartyName.from_obj(party_name[0])

        return return_obj

    def to_obj(self, return_obj=None):
        if not return_obj:
            root_tag = STIXCIQIdentity3_0.XML_TAG
            return_obj = et.Element(root_tag)

        if self.party_name:
            return_obj.append(self.party_name.to_obj())

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        party_name_dict = dict_repr.get('party_name')
        return_obj.party_name = PartyName.from_dict(party_name_dict) if party_name_dict else None

        return return_obj


    def to_dict(self):
        d = {}

        if self.party_name:
            d['party_name'] = self.party_name.to_dict()

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
            for value in self.organisation_names:
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

    def to_obj(self, return_obj=None):
        if not return_obj:
            root_tag = PartyName.XML_TAG
            return_obj = et.Element(root_tag)

        for name_line in self.name_lines:
            return_obj.append(name_line.to_obj())

        for person_name in self.person_names:
            return_obj.append(person_name.to_obj())

        for organisation_name in self.organisation_names:
            return_obj.append(organisation_name.to_obj())

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

    def to_obj(self, return_obj=None):
        if not return_obj:
            root_tag = NameLine.XML_TAG
            return_obj = et.Element(root_tag)

        if self.type:
            return_obj.attrib = {'Type' : self.type}

        if self.value: 
            return_obj.text = self.value

        return return_obj

    @classmethod
    def from_obj (cls, obj, return_obj=None):
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

    def to_obj(self, return_obj=None):
        if not return_obj:
            root_tag = PersonName.XML_TAG
            return_obj = et.Element(root_tag)

        for name_element in self.name_elements:
            return_obj.append(name_element.to_obj())

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

    def __init__(self, name_elements=None, sub_division_names=None):
        self.name_elements = []
        self.subdivision_names = []

        if name_elements:
            for name_element in name_elements:
                self.add_organisation_name_element(name_element)

        if sub_division_names:
            for name in sub_division_names:
                self.add_subdivision_name(name)


    def add_organisation_name_element(self, value):
        if isinstance(value, basestring):
            self.name_elements.append(OrganisationNameElement(value=value))
        elif isinstance(value, OrganisationNameElement):
            self.name_elements.append(value)
        else:
            raise ValueError('value must be instance of OrganisationNameElement')


    def add_subdivision_name(self, value):
        if not isinstance(value, SubDivisionName):
            raise ValueError('value must be instance of SubDivisionName')

        self.subdivision_names.append(value)


    def to_obj(self, return_obj=None):
        if not return_obj:
            root_tag = OrganisationName.XML_TAG
            return_obj = et.Element(root_tag)

        for name_element in self.name_elements:
            return_obj.append(name_element.to_obj())

        for subdivision_name in self.subdivision_names:
            return_obj.append(subdivision_name.to_obj())

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

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

        for ne_dict in ne_dicts:
            return_obj.add_organisation_name_element(OrganisationNameElement.from_dict(ne_dict))

        for sn_dict in sn_dicts:
            return_obj.add_subdivision_name(SubDivisionName.from_dict(sn_dict))

        return return_obj

class NameElement(stix.Entity):
    '''Do not instantiate directly: use PersonNameElement or OrganisationNameElement'''
    def __init__(self, value=None):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        #if not value:
        #    raise ValueError('value cannot be None')

        self._value = value

    @classmethod
    def from_obj(cls, obj, return_obj):
        return_obj.value = obj.get_valueOf_()
        return return_obj

    def to_obj(self, return_obj):
        return_obj.text = self.value
        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj):
        return_obj.value = dict_repr.get('value', None)
        return return_obj

    def to_dict(self, d):
        d['value'] = self.value
        return d

class PersonNameElement(NameElement):
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

    TYPES = (TYPE_TITLE, TYPE_PRECEDING_TITLE, TYPE_FIRST_NAME, TYPE_LAST_NAME,
             TYPE_MIDDLE_NAME, TYPE_OTHER_NAME, TYPE_ALIAS, TYPE_GENERATION_IDENTIFIER,
             TYPE_DEGREE)


    def __init__(self, value=None, element_type=None):
        super(PersonNameElement, self).__init__(value)
        self.element_type = element_type


    @property
    def element_type(self):
        return self._element_type


    @element_type.setter
    def element_type(self, value):
        if value and value not in self.TYPES:
            raise ValueError('value must be one of %s: ' % ' '.join(self.TYPES) )

        self._element_type = value    

    def to_obj(self, return_obj=None):
        if not return_obj:
            root_tag = PersonNameElement.XML_TAG
            return_obj = et.Element(root_tag)

        if self.element_type:
            return_obj.attrib = {'ElementType' : self.element_type}

        return_obj.text = self.value
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

class OrganisationNameElement(NameElement):
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
            raise ValueError('value must be one of: %s ' % ' '.join(self.TYPES) )

        self._element_type = value

    def to_obj(self, return_obj=None):
        if not return_obj:
            root_tag = OrganisationNameElement.XML_TAG
            return_obj = et.Element(root_tag)

        if self.element_type:
            return_obj.attrib['ElementType'] = self.element_type

        return_obj.text = self.value
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

    TYPES = (TYPE_DEPARTMENT, TYPE_DIVISION, TYPE_BRANCH, TYPE_BUSINESS_UNIT, TYPE_SCHOOL, TYPE_SECTION)

    def __init__(self, value=None, type_=None):
        self.value = value
        self.type = type_

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value and value not in self.TYPES:
            raise ValueError('value must be one of: %s' % ' '.join(self.TYPES))

        self._type = value

    def to_obj(self, return_obj=None):
        if not return_obj:
            root_tag = SubDivisionName.XML_TAG
            return_obj = et.Element(root_tag)

        if self.type:
            return_obj.attrib['Type'] = self.type

        return_obj.text = self.value
        return return_obj


    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if obj is None:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.type= obj.get('Type')    
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
