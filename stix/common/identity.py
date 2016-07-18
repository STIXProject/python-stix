# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox.cache import Cached

# internal
import stix
import stix.bindings.stix_common as common_binding


class Identity(Cached, stix.Entity):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'

    def __init__(self, id_=None, idref=None, name=None, related_identities=None):
        self.id_ = id_
        self.idref = idref
        self.name = name
        self.related_identities = related_identities

    @property
    def id_(self):
        return self._id
    
    @id_.setter
    def id_(self, value):
        if not value:
            self._id = None
        else:
            self._id = value
            self.idref = None

    @property
    def id(self):
        """The ``id`` and ``id_`` properties reference the same variable.
        """
        return self.id_

    @id.setter
    def id(self, value):
        self.id_(value)
    
    @property
    def idref(self):
        return self._idref
    
    @idref.setter
    def idref(self, value):
        if not value:
            self._idref = None
        else:
            self._idref = value
            self.id_ = None  # unset id_ if idref is present

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value if value else None

    @property
    def related_identities(self):
        return self._related_identities

    @related_identities.setter
    def related_identities(self, value):
        self._related_identities = RelatedIdentities(value)

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
            return_obj.id_ = obj.id_
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



# Backwards compatibility
add_extension = stix.add_extension
