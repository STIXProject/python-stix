# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
from mixbox import entities
from mixbox.cache import Cached

# internal
import stix
import stix.bindings.stix_common as common_binding
from stix.bindings.stix_common import IdentityType


class IdentityFactory(entities.EntityFactory):
    @classmethod
    def entity_class(cls, key):
        import stix.extensions.identity.ciq_identity_3_0  # noqa
        return stix.lookup_extension(key, default=Identity)


class Identity(Cached, stix.Entity):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = IdentityType

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    name = fields.TypedField("Name")
    related_identities = fields.TypedField("Related_Identities", type_="stix.common.identity.RelatedIdentities")

    def __init__(self, id_=None, idref=None, name=None, related_identities=None):
        super(Identity, self).__init__()
        
        self.id_ = id_
        self.idref = idref
        self.name = name
        self.related_identities = related_identities


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
