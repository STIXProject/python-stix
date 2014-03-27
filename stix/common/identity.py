# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

import stix
import stix.bindings.stix_common as common_binding
import stix.bindings.extensions.identity.ciq_identity_3_0 as ciq_identity_binding
import stix.utils

# import of RelatedIdentity is below


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

    @staticmethod
    def lookup_class(xsi_type):
        if not xsi_type:
            raise ValueError("xsi:type is required")
        for (k, v) in _EXTENSION_MAP.iteritems():
            # TODO: for now we ignore the prefix and just check for
            # a partial match
            if xsi_type in k:
                return v

        raise ValueError("Unregistered xsi:type %s" % xsi_type)

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        import stix.extensions.identity.ciq_identity_3_0
        
        if not obj:
            return None

        if not return_obj:
            try:
                klass = Identity.lookup_class(obj.xml_type)
                return_obj = klass.from_obj(obj)
            except AttributeError:
                return_obj = Identity.from_obj(obj, cls())
        else:
            return_obj.id_ = obj.get_id()
            return_obj.idref = obj.get_idref()
            return_obj.name = obj.get_Name()
            return_obj.related_identities = RelatedIdentities.from_obj(obj.get_Related_Identities())

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
        import stix.extensions.identity.ciq_identity_3_0
        
        if not dict_repr:
            return None

        if not return_obj:
            xsi_type = dict_repr.get('xsi:type')
            if xsi_type:
                klass = Identity.lookup_class(dict_repr.get('xsi:type'))
                return_obj = klass.from_dict(dict_repr)
            else:
                return_obj = Identity.from_dict(dict_repr, cls())
        else:
            return_obj.name = dict_repr.get('name')
            return_obj.id_ = dict_repr.get('id')
            return_obj.idref = dict_repr.get('idref')
            return_obj.related_identities = RelatedIdentities.from_dict(dict_repr.get('related_identities'))

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


_EXTENSION_MAP = {}
def add_extension(cls):
    _EXTENSION_MAP[cls._XSI_TYPE] = cls

