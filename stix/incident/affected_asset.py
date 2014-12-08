# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import stix
from stix.common import VocabString, StructuredText
import stix.bindings.incident as incident_binding
from .property_affected import PropertyAffected
from cybox.core import Observables
from stix.common.vocabs import OwnershipClass, ManagementClass, LocationClass

class AffectedAsset(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.AffectedAssetType
    
    def __init__(self):
        self.type_ = None
        self.description = None
        self.business_function_or_role = None
        self.ownership_class = None
        self.management_class = None
        self.location_class = None
        #self.location = None
        self.nature_of_security_effect = None
        self.structured_description =  None
        
    @property
    def type_(self):
        return self._type
    
    @type_.setter
    def type_(self, value):
        if not value:
            self._type = None
        elif isinstance(value, AssetType):
            self._type = value
        else:
            self._type = AssetType(value=value)
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not value:
            self._description = None
        elif isinstance(value, StructuredText):
            self._description = value
        else:
            self._description = StructuredText(value)
    
    @property
    def business_function_or_role(self):
        return self._business_function_or_role
    
    @business_function_or_role.setter
    def business_function_or_role(self, value):
        if not value:
            self._business_function_or_role = None
        elif isinstance(value, StructuredText):
            self._business_function_or_role = value
        else:
            self._business_function_or_role = StructuredText(value)
            
    @property
    def ownership_class(self):
        return self._ownership_class
    
    @ownership_class.setter
    def ownership_class(self, value):
        if not value:
            self._ownership_class = None
        elif isinstance(value, VocabString):
            self._ownership_class = value
        else:
            self._ownership_class = OwnershipClass(value)
    
    @property
    def management_class(self):
        return self._management_class
    
    @management_class.setter
    def management_class(self, value):
        if not value:
            self._management_class = None
        elif isinstance(value, VocabString):
            self._management_class = value
        else:
            self._management_class = ManagementClass(value)
    
    @property
    def location_class(self):
        return self._location_class
    
    @location_class.setter
    def location_class(self, value):
        if not value:
            self._location_class = None
        elif isinstance(value, VocabString):
            self._location_class = value
        else:
            self._location_class = LocationClass(value)
    
    @property
    def nature_of_security_effect(self):
        return self._nature_of_security_effect
    
    @nature_of_security_effect.setter
    def nature_of_security_effect(self, value):
        self._nature_of_security_effect = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_property_affected(v)
        else:
            self.add_property_affected(value)
            
    def add_property_affected(self, v):
        if not v:
            return
        elif isinstance(v, PropertyAffected):
            self.nature_of_security_effect.append(v)
        else:
            raise ValueError('Cannot add type %s to nature_of_security_effect list' % type(v))
    
    @property
    def structured_description(self):
        return self._structured_description
    
    @structured_description.setter
    def structured_description(self, value):
        if not value:
            self._structured_description = None
        elif isinstance(value, Observables):
            self._structured_description = value
        else:
            self._structured_description = Observables(value)
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.type_ = AssetType.from_obj(obj.Type)
        return_obj.description = StructuredText.from_obj(obj.Description)
        return_obj.business_function_or_role = StructuredText.from_obj(obj.Business_Function_Or_Role)
        return_obj.ownership_class = VocabString.from_obj(obj.Ownership_Class)
        return_obj.management_class = VocabString.from_obj(obj.Management_Class)
        return_obj.location_class = VocabString.from_obj(obj.Location_Class)
        #return_obj.location = None 
        
        if obj.Nature_Of_Security_Effect:
            n = obj.Nature_Of_Security_Effect
            return_obj.nature_of_security_effect = [PropertyAffected.from_obj(x) for x in n.Property_Affected]
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        super(AffectedAsset, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()
        
        if self.type_:
            return_obj.Type = self.type_.to_obj(ns_info=ns_info)
        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.business_function_or_role:
            return_obj.Business_Function_Or_Role = self.business_function_or_role.to_obj(ns_info=ns_info)
        if self.ownership_class:
            return_obj.Ownership_Class = self.ownership_class.to_obj(ns_info=ns_info)
        if self.management_class:
            return_obj.Management_Class = self.management_class.to_obj(ns_info=ns_info)
        if self.location_class:
            return_obj.Location_Class = self.location_class.to_obj(ns_info=ns_info)
#         if self.location:
#             return_obj.Location = self.location.to_obj(ns_info=ns_info)
        if self.nature_of_security_effect:
            property_affected_list = [x.to_obj(ns_info=ns_info) for x in self.nature_of_security_effect]
            n = self._binding.NatureOfSecurityEffectType(Property_Affected=property_affected_list)
            return_obj.Nature_Of_Security_Effect = n
        if self.structured_description:
            return_obj.Structured_Description = self.structured_description.to_obj(ns_info=ns_info)
       
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
        
        return_obj.type_ = AssetType.from_dict(d.get('type'))
        return_obj.description = StructuredText.from_dict(d.get('description'))
        return_obj.business_function_or_role = StructuredText.from_dict(d.get('business_function_or_role'))
        return_obj.ownership_class = OwnershipClass.from_dict(d.get('ownership_class'))
        return_obj.management_class = ManagementClass.from_dict(d.get('management_class'))
        return_obj.location_class = LocationClass.from_dict(d.get('location_class'))
        #return_obj.location = Location.from_dict(d.get('location'))
        return_obj.nature_of_security_effect = [PropertyAffected.from_dict(x) for x in d.get('nature_of_security_effect')]
        return_obj.structured_description = Observables.from_dict(d.get('structured_description'))
        return return_obj
    
    def to_dict(self):
        d = {}
        if self.type_:
            d['type'] = self.type_.to_dict()
        if self.description:
            d['description'] = self.description.to_dict()
        if self.business_function_or_role:
            d['business_function_or_role'] = self.business_function_or_role.to_dict()
        if self.ownership_class:
            d['ownership_class'] = self.ownership_class.to_dict()
        if self.management_class:
            d['management_class'] = self.management_class.to_dict()
        if self.location_class:
            d['location_class'] = self.location_class.to_dict()
#         if self.location:
#             d['location'] = self.location.to_dict()
        if self.nature_of_security_effect:
            d['nature_of_security_effect'] = [x.to_dict() for x in self.nature_of_security_effect]
        if self.structured_description:
            d['structured_description'] = self.structured_description.to_dict()
        return d
    
#from stix.common.vocabs import AssetType as DefaultAssetType

class AssetType(VocabString):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.AssetTypeType
    
    def __init__(self, value=None, count_affected=None):
        self.count_affected = count_affected
        super(AssetType, self).__init__(value)
    
    def is_plain(self):
        '''Override VocabString.is_plain()'''
        return False

    @property
    def count_affected(self):
        return self._count_affected

    @count_affected.setter
    def count_affected(self, value):
        if value is None:
            self._count_affected = None
            return

        self._count_affected = int(value)

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        super(AssetType, cls).from_obj(obj, return_obj=return_obj)
        return_obj.count_affected = obj.count_affected
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()
        
        super(AssetType, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        return_obj.count_affected = self.count_affected
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        super(AssetType, cls).from_dict(d, return_obj=return_obj)
        return_obj.count_affected = d.get('count_affected')
        return return_obj
    
    def to_dict(self):
        d = super(AssetType, self).to_dict()
        if self.count_affected:
            d['count_affected'] = self.count_affected
        return d
        
        
