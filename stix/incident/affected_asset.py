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
    ownership_class = fields.TypedField("Ownership_Class", vocabs.OwnershipClass)
    management_class = fields.TypedField("Management_Class", vocabs.ManagementClass)
    location_class = fields.TypedField("Location_Class", vocabs.LocationClass)
    # location = fields.TypedField("Location")
    nature_of_security_effect = fields.TypedField("Nature_Of_Security_Effect", type_="stix.incident.affected_asset.NatureOfSecurityEffect")
    structured_description = fields.TypedField("Structured_Description", Observables)
    type_ = fields.TypedField("Type", type_="stix.incident.affected_asset.AssetType", key_name="type")
    
    def __init__(self):
        super(AffectedAsset, self).__init__()

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
    
#     @classmethod
#     def from_obj(cls, obj, return_obj=None):
#         if not obj:
#             return None
#         if not return_obj:
#             return_obj = cls()
# 
#         return_obj.type_ = AssetType.from_obj(obj.Type)
#         return_obj.descriptions = StructuredTextList.from_obj(obj.Description)
#         return_obj.business_functions_or_roles = StructuredTextList.from_obj(obj.Business_Function_Or_Role)
#         return_obj.ownership_class = VocabString.from_obj(obj.Ownership_Class)
#         return_obj.management_class = VocabString.from_obj(obj.Management_Class)
#         return_obj.location_class = VocabString.from_obj(obj.Location_Class)
#         # return_obj.location = None
#         
#         if obj.Nature_Of_Security_Effect:
#             n = obj.Nature_Of_Security_Effect
#             return_obj.nature_of_security_effect = [PropertyAffected.from_obj(x) for x in n.Property_Affected]
# 
#         return return_obj
#     
#     def to_obj(self, return_obj=None, ns_info=None):
#         super(AffectedAsset, self).to_obj(return_obj=return_obj, ns_info=ns_info)
# 
#         if not return_obj:
#             return_obj = self._binding_class()
#         
#         if self.type_:
#             return_obj.Type = self.type_.to_obj(ns_info=ns_info)
#         if self.descriptions:
#             return_obj.Description = self.descriptions.to_obj(ns_info=ns_info)
#         if self.business_functions_or_roles:
#             return_obj.Business_Function_Or_Role = self.business_functions_or_roles.to_obj(ns_info=ns_info)
#         if self.ownership_class:
#             return_obj.Ownership_Class = self.ownership_class.to_obj(ns_info=ns_info)
#         if self.management_class:
#             return_obj.Management_Class = self.management_class.to_obj(ns_info=ns_info)
#         if self.location_class:
#             return_obj.Location_Class = self.location_class.to_obj(ns_info=ns_info)
#         # if self.location:
#         #     return_obj.Location = self.location.to_obj(ns_info=ns_info)
#         if self.nature_of_security_effect:
#             property_affected_list = [x.to_obj(ns_info=ns_info) for x in self.nature_of_security_effect]
#             n = self._binding.NatureOfSecurityEffectType(Property_Affected=property_affected_list)
#             return_obj.Nature_Of_Security_Effect = n
#         if self.structured_description:
#             return_obj.Structured_Description = self.structured_description.to_obj(ns_info=ns_info)
#        
#         return return_obj
#     
#     @classmethod
#     def from_dict(cls, d, return_obj=None):
#         if not d:
#             return None
#         if not return_obj:
#             return_obj = cls()
# 
#         get = d.get
#         return_obj.type_ = AssetType.from_dict(get('type'))
#         return_obj.descriptions = StructuredTextList.from_dict(get('description'))
#         return_obj.business_functions_or_roles = StructuredTextList.from_dict(get('business_function_or_role'))
#         return_obj.ownership_class = VocabString.from_dict(get('ownership_class'))
#         return_obj.management_class = VocabString.from_dict(get('management_class'))
#         return_obj.location_class = VocabString.from_dict(get('location_class'))
#         # return_obj.location = Location.from_dict(get('location'))
#         return_obj.nature_of_security_effect = NatureOfSecurityEffect.from_dict(get('nature_of_security_effect'))
#         return_obj.structured_description = Observables.from_dict(get('structured_description'))
#         return return_obj
#     
#     def to_dict(self):
#         return super(AffectedAsset, self).to_dict()

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

#     @classmethod
#     def from_obj(cls, obj, return_obj=None):
#         if not obj:
#             return None
#         if not return_obj:
#             return_obj = cls()
#         
#         super(AssetType, cls).from_obj(obj, return_obj=return_obj)
#         return_obj.count_affected = obj.count_affected
#         return return_obj
#     
#     def to_obj(self, return_obj=None, ns_info=None):
#         if not return_obj:
#             return_obj = self._binding_class()
#         
#         super(AssetType, self).to_obj(return_obj=return_obj, ns_info=ns_info)
#         return_obj.count_affected = self.count_affected
#         return return_obj
#     
#     @classmethod
#     def from_dict(cls, d, return_obj=None):
#         if not d:
#             return None
#         if not return_obj:
#             return_obj = cls()
#             
#         super(AssetType, cls).from_dict(d, return_obj=return_obj)
#         return_obj.count_affected = d.get('count_affected')
#         return return_obj
#     
#     def to_dict(self):
#         d = super(AssetType, self).to_dict()
#         if self.count_affected:
#             d['count_affected'] = self.count_affected
#         return d
        

class NatureOfSecurityEffect(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.NatureOfSecurityEffectType
    
    nature_of_security_effect = fields.TypedField("Property_Affected", PropertyAffected, multiple=True, key_name="nature_of_security_effect")
    
    @classmethod
    def _dict_as_list(cls):
        return True
