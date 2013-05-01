# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.bindings.stix_common_0_2 as stix_common_binding
import stix.bindings.oasis.xpil as oasis_xpil_binding


class Identity(stix.Entity):
    def __init__(self, id=None, idref=None, roles=None, related_identities=None):
        self.id_ = id if id else stix.utils.create_id()
        self.idref_ = idref
        self.roles = roles
        self.related_identities = related_identities

    @property
    def roles(self):
        return self._roles
    
    @roles.setter
    def roles(self, valuelist):
        self._roles = []
        
        if valuelist:
            for value in valuelist:
                self.add_role(value)
    
    @property
    def related_identities(self):
        return self._related_identities
    
    @related_identities.setter
    def related_identities(self, valuelist):
        self._related_identities = []
        
        if valuelist:
            for value in valuelist:
                self.add_related_identity(value)
    
    
    def add_role(self, value):
        if not value:
            return
        
        if not isinstance(value, basestring):
            raise ValueError('value must be instance of basestring')
        
        self.roles.append(value)
    
    def add_related_identity(self, value):
        if not value:
            return
        
        if not isinstance(value, RelatedIdentity):
            raise ValueError('value must be instance of RelatedIdentity')
        
        self.roles.append(value)
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = stix_common_binding.IdentityType()
        
        #return_obj.set_id(self.id_)
        #return_obj.set_idref(self.idref_)
        
        if self.roles:
            for role in self.roles:
                return_obj.add_Role(role)
                
        if self.related_identities:
            related_identities_obj = stix_common_binding.RelatedIdentitiesType()
            for identity in self.related_identities:
                related_identities_obj.add_RelatedIdentity(identity.to_obj())
            
            return_obj.set_RelatedIdentities(related_identities_obj)
                
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        roles = obj.get_Role()
        related_identities = obj.get_RelatedIdentities()
        
        if roles:
            for role in roles:
                return_obj.add_role(role)
        
        if related_identities:
            for identity in related_identities.get_RelatedIdentity():
                return_obj.add_related_identity(RelatedIdentity.from_obj(identity))
            
        return return_obj 

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        if self.roles:
            for role in self.roles:
                return_dict.setdefault('roles', []).append(role)
        
        if self.related_identities:
            for identity in self.related_identities:
                return_dict.setdefault('related_identities', []).append(identity.to_dict())
        
        return return_dict

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        roles = dict_repr.get('roles', [])
        related_identities = dict_repr.get('related_identities', [])
        
        for role in roles:
            return_obj.add_role(role)
        
        for related_identity_dict in related_identities:
            return_obj.add_related_identity(RelatedIdentity.from_dict(related_identity_dict))
            
        return return_obj


class STIXCIQIdentity(Identity):
    def __init__(self, party_name=None):
        super(STIXCIQIdentity, self).__init__()
        
        '''
        Constructor
        '''
        #=======================================================================
        # self.party_type = None
        # self.free_text_lines = None
        #=======================================================================
        self.party_name = party_name if party_name else PartyName()
        #=======================================================================
        # self.addresses = None
        # self.accounts = None
        # self.contact_numbers = None
        # self.documents = None
        # self.electronic_address_identifiers = None
        # self.events = None
        # self.identifiers = None
        # self.memberships = None
        # self.relationships = None
        # self.revenues = None
        # self.stocks = None
        # self.vehicles = None
        # self.organisation_info = None
        # self.person_info = None
        # self.birth_info = None
        # self.countries_of_residence = None
        # self.favourites = None
        # self.habits = None
        # self.hobbies = None
        # self.languages = None
        # self.nationalities = None
        # self.occupations = None
        # self.physical_info = None
        # self.preferences = None
        # self.qualifications = None
        # self.visas = None
        #=======================================================================

    @property
    def party_name(self):
        return self._party_name
    
    
    @party_name.setter
    def party_name(self, value):
        if value and not isinstance(value, PartyName):
            raise ValueError("value must be instance of PartyName")
        
        self._party_name = value
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        super(STIXCIQIdentity, cls).from_obj(obj, return_obj)
        
        if obj.get_PartyName():
            party_name_obj = obj.get_PartyName()
            return_obj.party_name = PartyName.from_obj(party_name_obj)
    
        return return_obj
        
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = stix_common_binding.STIX_CIQ_IdentityType()
        
        super(STIXCIQIdentity, self).to_obj(return_obj)
        if self.party_name:
            return_obj.set_PartyName(self.party_name.to_obj())
        
        return return_obj
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        super(STIXCIQIdentity, cls).from_dict(dict_repr, return_obj)
        party_name_dict = dict_repr.get('party_name', None)
        return_obj.party_name = PartyName.from_dict(party_name_dict) if party_name_dict else None
        
        return return_obj
            
            
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        super(STIXCIQIdentity, self).to_dict(return_dict)
        if self.party_name:
            return_dict['party_name'] = self.party_name.to_dict()
        
        return return_dict


class RelatedIdentity(STIXCIQIdentity):
    def __init__(self, relationship=None):
        super(RelatedIdentity, self).__init__()
        self.relationship = relationship
        
    @property
    def relationship(self):
        return self._relationship
    
    @relationship.setter
    def relationship(self, value):
        if value and not isinstance(value, basestring):
            raise ValueError('value must be instance of basestring')
        
        self._relationship = value
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = stix_common_binding.RelatedIdentityType()
            
        super(RelatedIdentity, self).to_obj(return_obj)
        return_obj.set_relationshipType(self.relationship)
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
            
        super(RelatedIdentity, cls).from_obj(obj, return_obj)
        return_obj.relationship = obj.get_relationshipType()
        return return_obj
    
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        super(RelatedIdentity, self).to_dict(return_dict)
        return_dict['relationship'] = self.relationship
        return return_dict
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()
            
        super(RelatedIdentity, cls).from_dict(dict_repr, return_obj)
        return_obj.relationship = dict_repr.get('relationship', None)
        return return_obj
    


class PartyName(stix.Entity):
    def __init__(self):
        self.name_lines = []
        self.person_names = []
        self.organisation_names = []
        

    def add_name_line(self, value):
        if isinstance(value, basestring):
            self.name_lines.append(NameLine(value))
    
        elif isinstance(value, NameLine):
            self.name_lines.append(value)
            
        else:
            raise ValueError('value must be a string or NameLine instance')
        
    def add_person_name(self, value):
        if not isinstance(value, PersonName):
            raise ValueError('value must be instance of PersonName')
        
        self.person_names.append(value) 
    
    def add_organisation_name(self, value):
        if not isinstance(value, OrganisationName):
            raise ValueError('value must be instance of OrganisationName')
        
        self.organisation_names.append(value)

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = oasis_xpil_binding.PartyNameType()
            
        for name_line in self.name_lines:
            return_obj.add_NameLine(name_line.to_obj())
        
        for person_name in self.person_names:
            return_obj.add_PersonName(person_name.to_obj())
        
        for organisation_name in self.organisation_names:
            return_obj.add_OrganisationName(organisation_name.to_obj())

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        if obj.get_NameLine():
            for name_line_obj in obj.get_NameLine():
                name_line = NameLine.from_obj(name_line_obj)
                return_obj.add_name_line(name_line)
        
        if obj.get_PersonName():
            for person_name_obj in obj.get_PersonName():
                person_name = PersonName.from_obj(person_name_obj)
                return_obj.add_person_name(person_name)
                
        if obj.get_OrganisationName():
            for organisation_name_obj in obj.get_OrganisationName():
                org_name = OrganisationName.from_obj(organisation_name_obj)
                return_obj.add_organisation_name(org_name)
                
        return return_obj

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        if self.name_lines:
            for name_line in self.name_lines:
                return_dict.setdefault('name_lines', []).append(name_line.to_dict())
        
        if self.organisation_names:
            for on in self.organisation_names:
                return_dict.setdefault('organisation_names', []).append(on.to_dict())
        
        if self.person_names:
            for pn in self.person_names:
                return_dict.setdefault('person_names', []).append(pn.to_dict())
                
        return return_dict

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
    def __init__(self, value=None, type=None):
        self.value = value
        self.type = type
    
    @property
    def value(self):
        return self._value    
    
    @value.setter
    def value(self, value):
        if not (value and isinstance(value, basestring)):
            raise ValueError('value must be instance of basestring')
        
        self._value = value
        
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = oasis_xpil_binding.NameLine()
        
        if self.type:
            return_obj.set_Type(self.type)
        
        return_obj.set_valueOf_(self.value)
        
        return return_obj
    
    @classmethod
    def from_obj (cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        return_obj.value = obj.get_valueOf_()
        return_obj.type = obj.get_Type()        
          
        return return_obj
    
    
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
            
        return_dict['value'] = self.value
        
        if self.type:
            return_dict['type'] = self.type
        
        return return_dict
    
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
    def __init__(self, name_elements=None):
        self.name_elements = []
        
        if name_elements:
            for name_element in name_elements:
                self.add_name_element(name_element)


    def add_name_element(self, value):
        if not isinstance(value, PersonNameElement):
            raise ValueError('value must be instance of PersonNameElement')
        
        self.name_elements.append(value)

        
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = oasis_xpil_binding.PersonNameType()
        
        for name_element in self.name_elements:
            return_obj.add_NameElement(name_element.to_obj())
            
        return return_obj
    
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        if obj.get_NameElement():
            for name_element_obj in obj.get_NameElement():
                person_name_element = PersonNameElement.from_obj(name_element_obj)
                return_obj.add_name_element(person_name_element)
        
        return return_obj

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        if self.name_elements:
            for ne in self.name_elements:
                return_dict.setdefault('name_elements', []).append(ne.to_dict())
    
        return return_dict
    
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
        if not isinstance(value, OrganisationNameElement):
            raise ValueError('value must be instance of OrganisationNameElement')
        
        self.name_elements.append(value)


    def add_subdivision_name(self, value):
        if not isinstance(value, SubDivisionName):
            raise ValueError('value must be instance of SubDivisionName')
        
        self.subdivision_names.append(value)


    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = oasis_xpil_binding.OrganisationNameType()
        
        for name_element in self.name_elements:
            return_obj.add_NameElement(name_element.to_obj())
        
        for subdivision_name in self.subdivision_names:
            return_obj.add_SubDivisionName(subdivision_name.to_obj())
            
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        if obj.get_NameElement():
            for name_element_obj in obj.get_NameElement():
                name_element = OrganisationNameElement.from_obj(name_element_obj)
                return_obj.add_organisation_name_element(name_element)
                
        if obj.get_SubDivisionName():
            for sub_division_name_obj in obj.get_SubDivisionName():
                sub_division_name = SubDivisionName.from_obj(sub_division_name_obj)
                return_obj.add_subdivision_name(sub_division_name)
            
        return return_obj

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        if self.name_elements:
            for ne in self.name_elements:
                return_dict.setdefault('name_elements', []).append(ne.to_dict())
        
        if self.subdivision_names:
            for sn in self.subdivision_names:
                return_dict.setdefault('subdivision_names', []).append(sn.to_dict())
        
        return return_dict

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
        return_obj.set_valueOf_(self.value)
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj):
        return_obj.value = dict_repr.get('value', None)

    def to_dict(self, return_dict):
        return_dict['value'] = self.value
        

class PersonNameElement(NameElement):
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
            return_obj = oasis_xpil_binding.NameElementType()
            
        if self.element_type:
            return_obj.set_ElementType(self.element_type)
            
        return_obj.set_valueOf_(self.value)
        return return_obj    
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        if obj.get_ElementType():
            return_obj.element_type = obj.get_ElementType()
            
        if obj.get_valueOf_():
            return_obj.value = obj.get_valueOf_()
            
        return return_obj
    
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        return_dict['value'] = self.value
        
        if self.element_type:
            return_dict['element_type'] = self.element_type
            
        return return_dict
    
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
    TYPE_NAME_ONLY = "NameOnly"
    TYPE_TYPE_ONLY = "TypeOnly"
    TYPE_FULL_NAME = "FullName"
    
    TYPES = (TYPE_NAME_ONLY, TYPE_TYPE_ONLY, TYPE_FULL_NAME)
    
    def __init__(self, value=None, element_type=None):
        super(OrganisationNameElement, self).__init__(value)
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
            return_obj = oasis_xpil_binding.NameElementType()
            
        if self.element_type:
            return_obj.set_ElementType(self.element_type)
            
        return_obj.set_valueOf_(self.value)
        return return_obj
        
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
              
        if obj.get_ElementType():
            return_obj.element_type = obj.get_ElementType()
            
        return_obj.value = obj.get_valueOf_()
            
        return return_obj
        
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        if self.element_type:
            return_dict['element_type'] = self.element_type
            
        if self.value:
            return_dict['value'] = self.value
        
        return return_dict
            
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        return_obj.value = dict_repr.get('value', None)
        return_obj.element_type = dict_repr.get('element_type', None)
        
        return return_obj
        

class SubDivisionName(stix.Entity):
    TYPE_DEPARTMENT = 'Department'
    TYPE_DIVISION = 'Division'
    TYPE_BRANCH = 'Branch'
    TYPE_BUSINESS_UNIT = 'BusinessUnit'
    TYPE_SCHOOL = 'School'
    TYPE_SECTION = 'Section'
    
    TYPES = (TYPE_DEPARTMENT, TYPE_DIVISION, TYPE_BRANCH, TYPE_BUSINESS_UNIT, TYPE_SCHOOL, TYPE_SECTION)
    
    def __init__(self, value=None, type=None):
        self.value = value
        self.type = type
    
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
            return_obj = oasis_xpil_binding.SubDivisionNameType()
            
        if self.type:
            return_obj.set_Type(self.type)
            
        return_obj.set_valueOf_(self.value)
        return return_obj
        
        
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
                    
        return_obj.value = obj.get_valueOf_()
        
        if obj.get_Type():
            return_obj.type = obj.get_Type()
            
        return return_obj
    
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        return_dict['value'] = self.value
        
        if self.type:
            return_dict['type'] = self.type
            
        return return_dict
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()
            
        return_obj.value = dict_repr.get('value', None)
        return_obj.type = dict_repr.get('type', None)
        return return_obj



