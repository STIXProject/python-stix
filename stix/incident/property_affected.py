# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import stix
from stix.common import VocabString, StructuredText
import stix.bindings.incident as incident_binding
from stix.common.vocabs import LossProperty, LossDuration
from stix.common.vocabs import AvailabilityLossType as AvailabilityLoss


class NonPublicDataCompromised(VocabString):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.NonPublicDataCompromisedType
    
    def __init__(self, value=None, data_encrypted=None):
        self.data_encrypted = data_encrypted
        super(NonPublicDataCompromised, self).__init__(value)
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        super(NonPublicDataCompromised, cls).from_obj(obj, return_obj=return_obj)
        return_obj.data_encrypted = obj.get_data_encrypted()
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if not return_obj:
            return_obj = self._binding_class()
        
        super(NonPublicDataCompromised, self).to_obj(return_obj=return_obj)
        return_obj.set_data_encrypted(self.data_encrypted)
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        super(NonPublicDataCompromised, cls).from_dict(d, return_obj=return_obj)
        return_obj.data_encrypted = d.get('data_encrypted')
        return return_obj
    
    def to_dict(self):
        d = super(NonPublicDataCompromised, self).to_dict()
        if self.data_encrypted:
            d['data_encrypted'] = self.data_encrypted
        return d

class PropertyAffected(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.PropertyAffectedType
    
    def __init__(self):
        self.property_ = None
        self.description_of_effect = None
        self.type_of_availability_loss = None
        self.duration_of_availability_loss = None
        self.non_public_data_compromised = None
        
    @property
    def property_(self):
        return self._property
    
    @property_.setter
    def property_(self, value):
        if not value:
            self._property = None
        elif isinstance(value, VocabString):
            self._property = value
        else:
            self._property = LossProperty(value)
        
    @property
    def description_of_effect(self):
        return self._description_of_effect
    
    @description_of_effect.setter
    def description_of_effect(self, value):
        if not value:
            self._description_of_effect = None
        elif isinstance(value, StructuredText):
            self._description_of_effect = value
        else:
            self._description_of_effect = StructuredText(value)

    @property
    def type_of_availability_loss(self):
        return self._type_of_availability_loss
    
    @type_of_availability_loss.setter
    def type_of_availability_loss(self, value):
        if not value:
            self._type_of_availability_loss = None
        elif isinstance(value, VocabString):
            self._type_of_availability_loss = value
        else:
            self._type_of_availability_loss = AvailabilityLoss(value)
            
    @property
    def duration_of_availability_loss(self):
        return self._duration_of_availability_loss
    
    @duration_of_availability_loss.setter
    def duration_of_availability_loss(self, value):
        if not value:
            self._duration_of_availability_loss = None
        elif isinstance(value, VocabString):
            self._duration_of_availability_loss = value
        else:
            self._duration_of_availability_loss = LossDuration(value)
    
    @property
    def non_public_data_compromised(self):
        return self._non_public_data_compromised
    
    @non_public_data_compromised.setter
    def non_public_data_compromised(self, value):
        if not value:
            self._non_public_data_compromised = None
        elif isinstance(value, NonPublicDataCompromised):
            self._non_public_data_compromised = value
        else:
            self._non_public_data_compromised = NonPublicDataCompromised(value)
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.property_ = VocabString.from_obj(obj.get_Property())
        return_obj.description_of_effect = StructuredText.from_obj(obj.get_Description_Of_Effect())
        return_obj.type_of_availability_loss = VocabString.from_obj(obj.get_Type_Of_Availability_Loss())
        return_obj.duration_of_availability_loss = VocabString.from_obj(obj.get_Duration_Of_Availability_Loss())
        return_obj.non_public_data_compromised = NonPublicDataCompromised.from_obj(obj.get_Non_Public_Data_Compromised())
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if not return_obj:
            return_obj = self._binding_class()
            
        if self.property_:
            return_obj.set_Property(self.property_.to_obj(ns_info=ns_info))
        if self.description_of_effect:
            return_obj.set_Description_Of_Effect(self.description_of_effect.to_obj(ns_info=ns_info))
        if self.type_of_availability_loss:
            return_obj.set_Type_Of_Availability_Loss(self.type_of_availability_loss.to_obj(ns_info=ns_info))
        if self.duration_of_availability_loss:
            return_obj.set_Duration_Of_Availability_Loss(self.duration_of_availability_loss.to_obj(ns_info=ns_info))
        if self.non_public_data_compromised:
            return_obj.set_Non_Public_Data_Compromised(self.non_public_data_compromised.to_obj(ns_info=ns_info))
        
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.property_ = VocabString.from_dict(d.get(('property')))
        return_obj.description_of_effect = StructuredText.from_dict(d.get('description_of_effect'))
        return_obj.type_of_availability_loss = VocabString.from_dict(d.get('type_of_availability_loss'))
        return_obj.duration_of_availability_loss = VocabString.from_dict(d.get('duration_of_availability_loss'))
        return_obj.non_public_data_compromised = NonPublicDataCompromised.from_dict(d.get('non_public_data_compromised'))
        
        return return_obj
    
    def to_dict(self):
        d = {}
        if self.property_:
            d['property'] = self.property_.to_dict()
        if self.description_of_effect:
            d['description_of_effect'] = self.description_of_effect.to_dict()
        if self.type_of_availability_loss:
            d['type_of_availability_loss'] = self.type_of_availability_loss.to_dict()
        if self.duration_of_availability_loss:
            d['duration_of_availability_loss'] = self.duration_of_availability_loss.to_dict()
        if self.non_public_data_compromised:
            d['non_public_data_compromised'] = self.non_public_data_compromised.to_dict()
        return d
    
