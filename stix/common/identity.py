# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

import stix
import stix.bindings.stix_common as common_binding
import stix.bindings.extensions.identity.ciq_identity_3_0 as ciq_identity_binding
import stix.utils

# import of GenericRelationshipList and RelatedIdentity is below


class Identity(stix.Entity):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'

    def __init__(self, id_=None, idref=None, name=None, related_identities=None):
        self.id_ = id_ or stix.utils.create_id("Identity")
        self.idref = idref
        self.name = name
        self.related_identities = RelatedIdentities()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value if value else None

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding.IdentityType()

        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref)

        if self.name:
            return_obj.set_Name(self.name)
        if self.related_identities:
            return_obj.set_Related_Identities(self.related_identities.to_obj())

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
        return_obj.related_identities = \
                RelatedIdentities.from_obj(obj.get_Related_Identities())

        return return_obj

    def to_dict(self):
        d = {}
        if self.name:
            d['name'] = self.name
        if self.id_:
            d['id'] = self.id_
        if self.idref:
            d['idref'] = self.idref
        if self.related_identities:
            d['related_identities'] = self.related_identities.to_dict()

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.name = dict_repr.get('name')
        return_obj.id_ = dict_repr.get('id')
        return_obj.idref = dict_repr.get('idref')
        return_obj.related_identities = \
                RelatedIdentities.from_dict(dict_repr.get('related_identities'))

        return return_obj


from stix.common.related import GenericRelationshipList, RelatedIdentity

# TODO: This is sort of a hack, since RelatedIdentities is not actually a
# subclass of GenericRelationshipList. As long as you don't try to set the
# 'scope' variable, things should go fine.

class RelatedIdentities(GenericRelationshipList):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.RelatedIdentitiesType
    _binding_var = "Related_Identity"
    _contained_type = RelatedIdentity
    _inner_name = "identities"

    def __init__(self, identities=None, scope=None):
        if identities is None:
            identities = []
        super(RelatedIdentities, self).__init__(*identities, scope=scope)
