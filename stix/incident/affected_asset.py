# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from cybox.core import Observables

# internal
import stix
from stix.common import vocabs, VocabString, StructuredTextList
import stix.bindings.incident as incident_binding

# relative
from .property_affected import PropertyAffected

from mixbox import entities, fields

class AffectedAsset(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.AffectedAssetType
    
    descriptions = fields.TypedField("Description", StructuredTextList)
    business_function_or_roles = fields.TypedField("Business_Function_Or_Role", StructuredTextList)
    ownership_class = vocabs.VocabField("Ownership_Class", vocabs.OwnershipClass)
    management_class = vocabs.VocabField("Management_Class", vocabs.ManagementClass)
    location_class = vocabs.VocabField("Location_Class", vocabs.LocationClass)
    # location = fields.TypedField("Location")
    nature_of_security_effect = fields.TypedField("Nature_Of_Security_Effect", type_="stix.incident.affected_asset.NatureOfSecurityEffect")
    structured_description = fields.TypedField("Structured_Description", Observables)
    type_ = fields.TypedField("Type", type_="stix.incident.affected_asset.AssetType", key_name="type")
    
    def __init__(self):
        super(AffectedAsset, self).__init__()
        self.description = StructuredTextList()
        self.business_function_or_role = StructuredTextList()

    @property
    def description(self):
        """A single description about the contents or purpose of this object.

        Default Value: ``None``

        Note:
            If this object has more than one description set, this will return
            the description with the lowest ordinality value.

        Returns:
            An instance of
            :class:`.StructuredText`

        """
        return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        self.descriptions = value

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        self.descriptions.add(description)

    @property
    def business_function_or_role(self):
        return next(iter(self.business_functions_or_roles), None)

    @business_function_or_role.setter
    def business_function_or_role(self, value):
        self.business_functions_or_roles = value

    def add_property_affected(self, v):
        self.nature_of_security_effect.append(v)


class AssetType(VocabString):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.AssetTypeType
    
    count_affected = fields.IntegerField("count_affected")
    
    def __init__(self, value=None, count_affected=None):
        super(AssetType, self).__init__(value)
        self.count_affected = count_affected
    
    def is_plain(self):
        """Override VocabString.is_plain()"""
        return False


class NatureOfSecurityEffect(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.NatureOfSecurityEffectType
    
    nature_of_security_effect = fields.TypedField("Property_Affected", PropertyAffected, multiple=True, key_name="nature_of_security_effect")
    
    @classmethod
    def _dict_as_list(cls):
        return True
