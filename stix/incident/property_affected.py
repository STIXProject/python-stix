# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import stix
from stix.common import vocabs, VocabString, StructuredText
import stix.bindings.incident as incident_binding


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
        return_obj.data_encrypted = obj.data_encrypted
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()
        
        super(NonPublicDataCompromised, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        return_obj.data_encrypted = self.data_encrypted
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

    def is_plain(self):
        return False

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
        self._set_vocab(vocabs.LossProperty, property=value)

    @property
    def description_of_effect(self):
        return self._description_of_effect
    
    @description_of_effect.setter
    def description_of_effect(self, value):
        self._set_var(StructuredText, description_of_effect=value)

    @property
    def type_of_availability_loss(self):
        return self._type_of_availability_loss
    
    @type_of_availability_loss.setter
    def type_of_availability_loss(self, value):
        self._set_vocab(vocabs.AvailabilityLossType, type_of_availability_loss=value)
            
    @property
    def duration_of_availability_loss(self):
        return self._duration_of_availability_loss
    
    @duration_of_availability_loss.setter
    def duration_of_availability_loss(self, value):
        self._set_vocab(vocabs.LossDuration, duration_of_availability_loss=value)
    
    @property
    def non_public_data_compromised(self):
        return self._non_public_data_compromised
    
    @non_public_data_compromised.setter
    def non_public_data_compromised(self, value):
        self._set_var(NonPublicDataCompromised, non_public_data_compromised=value)
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.property_ = VocabString.from_obj(obj.Property)
        return_obj.description_of_effect = StructuredText.from_obj(obj.Description_Of_Effect)
        return_obj.type_of_availability_loss = VocabString.from_obj(obj.Type_Of_Availability_Loss)
        return_obj.duration_of_availability_loss = VocabString.from_obj(obj.Duration_Of_Availability_Loss)
        return_obj.non_public_data_compromised = NonPublicDataCompromised.from_obj(obj.Non_Public_Data_Compromised)
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        super(PropertyAffected, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()
            
        if self.property_:
            return_obj.Property = self.property_.to_obj(ns_info=ns_info)
        if self.description_of_effect:
            return_obj.Description_Of_Effect = self.description_of_effect.to_obj(ns_info=ns_info)
        if self.type_of_availability_loss:
            return_obj.Type_Of_Availability_Loss = self.type_of_availability_loss.to_obj(ns_info=ns_info)
        if self.duration_of_availability_loss:
            return_obj.Duration_Of_Availability_Loss = self.duration_of_availability_loss.to_obj(ns_info=ns_info)
        if self.non_public_data_compromised:
            return_obj.Non_Public_Data_Compromised = self.non_public_data_compromised.to_obj(ns_info=ns_info)
        
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.property_ = VocabString.from_dict(d.get('property'))
        return_obj.description_of_effect = StructuredText.from_dict(d.get('description_of_effect'))
        return_obj.type_of_availability_loss = VocabString.from_dict(d.get('type_of_availability_loss'))
        return_obj.duration_of_availability_loss = VocabString.from_dict(d.get('duration_of_availability_loss'))
        return_obj.non_public_data_compromised = NonPublicDataCompromised.from_dict(d.get('non_public_data_compromised'))
        
        return return_obj
    
    def to_dict(self):
        return super(PropertyAffected, self).to_dict()
