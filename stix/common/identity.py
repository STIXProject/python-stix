# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

import stix
import stix.bindings.stix_common as common_binding
from stix.base import ElementField, IdField
from stix.bindings.stix_common import IdentityType

class Identity(stix.Entity):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = IdentityType

    id_ = IdField("id")
    idref = IdField("idref")
    name = ElementField("Name")
    related_identities = ElementField("Related_Identities")

    @classmethod
    def initializeClassFields(cls):
        cls.related_identities.type = RelatedIdentities

    def __init__(self, id_=None, idref=None, name=None, related_identities=None):
        super(Identity, self).__init__()
        
        self.id_ = id_
        self.idref = idref
        self.name = name
        self.related_identities = related_identities

    def to_obj(self, return_obj=None, ns_info=None):
        super(Identity, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding.IdentityType()

        return_obj.id = self.id_
        return_obj.idref = self.idref

        if self.name:
            return_obj.Name = self.name
        if self.related_identities:
            return_obj.Related_Identities = \
                self.related_identities.to_obj(ns_info=ns_info)

        return return_obj

    @staticmethod
    def lookup_class(xsi_type):
        if not xsi_type:
            raise ValueError("xsi:type is required")

        return stix.lookup_extension(xsi_type)

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        import stix.extensions.identity.ciq_identity_3_0  # noqa
        
        if not obj:
            return None

        if not return_obj:
            klass = stix.lookup_extension(obj, default=cls)
            return_obj = klass.from_obj(obj, return_obj=klass())
        else:
            return_obj.id_ = obj.id
            return_obj.idref = obj.idref
            return_obj.name = obj.Name
            return_obj.related_identities = \
                RelatedIdentities.from_obj(obj.Related_Identities)

        return return_obj

    def to_dict(self):
        return super(Identity, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        import stix.extensions.identity.ciq_identity_3_0  # noqa
        
        if not dict_repr:
            return None

        get = dict_repr.get

        if not return_obj:
            klass = stix.lookup_extension(get('xsi:type'), default=cls)
            return_obj = klass.from_dict(dict_repr, klass())
        else:
            return_obj.name = get('name')
            return_obj.id_ = get('id')
            return_obj.idref = get('idref')
            return_obj.related_identities = \
                RelatedIdentities.from_dict(get('related_identities'))

        return return_obj


# We can't import RelatedIdentity until we have defined the Identity class.
from stix.common.related import RelatedIdentity


class RelatedIdentities(stix.EntityList):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.RelatedIdentitiesType
    _binding_var = "Related_Identity"
    _contained_type = RelatedIdentity
    _inner_name = "identities"

# this must come after RelatedIdentities definition
Identity.initializeClassFields()

# Backwards compatibility
add_extension = stix.add_extension
