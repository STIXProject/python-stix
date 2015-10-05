# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
from mixbox.cache import Cached

# internal
import stix
import stix.bindings.stix_common as common_binding
from stix.base import ElementField
from stix.bindings.stix_common import IdentityType


class Identity(Cached, stix.Entity):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = IdentityType

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    name = ElementField("Name")
    related_identities = fields.TypedField("Related_Identities", type_="stix.common.identity.RelatedIdentities")

    def __init__(self, id_=None, idref=None, name=None, related_identities=None):
        super(Identity, self).__init__()
        
        self.id_ = id_
        self.idref = idref
        self.name = name
        self.related_identities = related_identities

    @staticmethod
    def lookup_class(xsi_type):
        if not xsi_type:
            raise ValueError("xsi:type is required")

        return stix.lookup_extension(xsi_type)

    @classmethod
    def from_obj(cls, obj, partial=None):
        import stix.extensions.identity.ciq_identity_3_0  # noqa
        
        if not obj:
            return None

        if not partial:
            klass = stix.lookup_extension(obj, default=cls)
            partial = klass.from_obj(obj, partial=klass())
        else:
            partial.id_ = obj.id
            partial.idref = obj.idref
            partial.name = obj.Name
            partial.related_identities = RelatedIdentities.from_obj(obj.Related_Identities)

        return partial

    @classmethod
    def from_dict(cls, dict_repr, partial=None):
        import stix.extensions.identity.ciq_identity_3_0  # noqa
        
        if not dict_repr:
            return None

        get = dict_repr.get

        if not partial:
            klass = stix.lookup_extension(get('xsi:type'), default=cls)
            partial = klass.from_dict(dict_repr, klass())
        else:
            partial.name = get('name')
            partial.id_ = get('id')
            partial.idref = get('idref')
            partial.related_identities = \
                RelatedIdentities.from_dict(get('related_identities'))

        return partial


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
