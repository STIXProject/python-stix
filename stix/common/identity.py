# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.extensions.identity.ciq_identity_3_0 as ciq_identity_binding

from stix.common.generic_relationship import GenericRelationship

class Identity(stix.Entity):
    _binding = stix_common_binding
    _namespace = 'http://stix.mitre.org/common-1'

    def __init__(self, id_=None, idref=None, name=None, related_identities=None):
        self.id_ = id_ or stix.utils.create_id("Identity")
        self.idref = idref
        self.name = name
        #self.related_identities = related_identities

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = unicode(value) if value else None

#    @property
#    def related_identities(self):
#        return self._related_identities
#    
#    @related_identities.setter
#    def related_identities(self, valuelist):
#        self._related_identities = []
#        
#        if valuelist:
#            for value in valuelist:
#                self.add_related_identity(value)

#    
#    def add_related_identity(self, value):
#        if not value:
#            return
#        
#        if not isinstance(value, RelatedIdentity):
#            raise ValueError('value must be instance of RelatedIdentity')
#        
#        self.roles.append(value)

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding.IdentityType()

        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref)

        if self.name:
            return_obj.set_Name(self.name)

#        if self.related_identities:
#            related_identities_obj = stix_common_binding.RelatedIdentitiesType()
#            for identity in self.related_identities:
#                related_identities_obj.add_RelatedIdentity(identity.to_obj())
#            
#            return_obj.set_RelatedIdentities(related_identities_obj)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.get_id()
        return_obj.idref = obj.get_idref()
        return_obj.name = obj.get_Name()
        #related_identities = obj.get_RelatedIdentities()

#        if related_identities:
#            for identity in related_identities.get_RelatedIdentity():
#                return_obj.add_related_identity(RelatedIdentity.from_obj(identity))

        return return_obj 

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}

        if self.name:
            return_dict['name'] = self.name
        if self.id_:
            return_dict['id'] = self.id_
        if self.idref:
            return_dict['idref'] = self.idref

#        if self.related_identities:
#            for identity in self.related_identities:
#                return_dict.setdefault('related_identities', []).append(identity.to_dict())

        return return_dict

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.name = dict_repr.get('name')
        return_obj.id_ = dict_repr.get('id')
        return_obj.idref = dict_repr.get('idref')
        #related_identities = dict_repr.get('related_identities', [])


#        for related_identity_dict in related_identities:
#            return_obj.add_related_identity(RelatedIdentity.from_dict(related_identity_dict))

        return return_obj


class RelatedIdentity(GenericRelationship):
    _binding = stix_common_binding
    _namespace = 'http://stix.mitre.org/common-1'

    def __init__(self, identity=None, relationship=None):
        super(RelatedIdentity, self).__init__()
        self.identity = identity


    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        if value and not isinstance(value, Identity):
            raise ValueError('value must be instance of Identity')

        self._identity = value


    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding.RelatedIdentityType()

        super(RelatedIdentity, self).to_obj(return_obj)

        if self.identity:
            return_obj.set_Identity(self.identity.to_obj())

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(RelatedIdentity, cls).from_obj(obj, return_obj)

        if obj.get_Identity():
            identity_obj = obj.get_Identity()
            if isinstance(identity_obj, ciq_identity_binding.CIQIdentity3_0InstanceType):
                from stix.extensions.identity import CIQIdentity3_0Instance
                return_obj.identity = CIQIdentity3_0Instance.from_obj(identity_obj)
            elif isinstance(identity_obj, stix_common_binding.IdentityType):
                return_obj.identity = Identity.from_obj(identity_obj)
            else:
                raise ValueError('unable to instantiate the correct type for identity')

        return return_obj

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}

        super(RelatedIdentity, self).to_dict(return_dict)
        return_dict['identity'] = self.identity.to_dict()
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

