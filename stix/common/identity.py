# Copyright (c) 2017, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
from mixbox import entities

# internal
import stix
import stix.bindings.stix_common as common_binding
from stix.bindings.stix_common import IdentityType


class IdentityFactory(entities.EntityFactory):
    @classmethod
    def entity_class(cls, key):
        import stix.extensions.identity.ciq_identity_3_0  # noqa
        return stix.lookup_extension(key, default=Identity)


class Identity(stix.Entity):
    _binding = common_binding
    _binding_class = IdentityType
    _namespace = 'http://stix.mitre.org/common-1'

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

    def to_dict(self):
        d = super(Identity, self).to_dict()

        if self._XSI_TYPE:
            d['xsi:type'] = self._XSI_TYPE

        return d

    @staticmethod
    def lookup_class(xsi_type):
        return stix.lookup_extension(xsi_type, default=Identity)

# We can't import RelatedIdentity until we have defined the Identity class.
from stix.common.related import RelatedIdentity


class RelatedIdentities(stix.EntityList):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.RelatedIdentitiesType

    related_identity = fields.TypedField("Related_Identity", RelatedIdentity, multiple=True, key_name="identities")

    @classmethod
    def _dict_as_list(cls):
        return False


# Backwards compatibility
add_extension = stix.add_extension
