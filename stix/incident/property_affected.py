# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import stix
from stix.common import vocabs, VocabString, StructuredTextList
import stix.bindings.incident as incident_binding
from mixbox import fields, entities
from stix.common.vocabs import VocabField

class NonPublicDataCompromised(VocabString):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.NonPublicDataCompromisedType
    
    data_encrypted = fields.TypedField("data_encrypted")
    
    def __init__(self, value=None, data_encrypted=None):
        self.data_encrypted = data_encrypted
        super(NonPublicDataCompromised, self).__init__(value)
 
    def is_plain(self):
        return False
  
#     def to_dict(self):
#         d = super(NonPublicDataCompromised, self).to_dict()
# 
#         if self.data_encrypted:
#             d['data_encrypted'] = self.data_encrypted
# 
#         return d


class PropertyAffected(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.PropertyAffectedType
    
    property_ = VocabField("Property", vocabs.LossProperty, key_name="property")
    descriptions_of_effect = fields.TypedField("Description_Of_Effect", StructuredTextList)
    type_of_availability_loss = VocabField("Type_Of_Availability_Loss", vocabs.AvailabilityLossType)
    duration_of_availability_loss = VocabField("Duration_Of_Availability_Loss", vocabs.LossDuration)
    non_public_data_compromised = VocabField("Non_Public_Data_Compromised", NonPublicDataCompromised)
    
    def __init__(self):
        super(PropertyAffected, self).__init__()

    @property
    def description_of_effect(self):
        """A :class:`.StructuredTextList` object, containing descriptions about
        the purpose or intent of this object.

        Iterating over this object will yield its contents sorted by their
        ``ordinality`` value.

        Default Value: Empty :class:`.StructuredTextList` object.

        Note:
            IF this is set to a value that is not an instance of
            :class:`.StructuredText`, an effort will ne made to convert it.
            If this is set to an iterable, any values contained that are not
            an instance of :class:`.StructuredText` will be be converted.

        Returns:
            An instance of
            :class:`.StructuredTextList`

        """
        return next(iter(self.descriptions_of_effect), None)

    @description_of_effect.setter
    def description_of_effect(self, value):
        self.descriptions_of_effect = value
    
#     @classmethod
#     def from_obj(cls, obj, return_obj=None):
#         if not obj:
#             return None
#         if not return_obj:
#             return_obj = cls()
#             
#         return_obj.property_ = VocabString.from_obj(obj.Property)
#         return_obj.descriptions_of_effect = StructuredTextList.from_obj(obj.Description_Of_Effect)
#         return_obj.type_of_availability_loss = VocabString.from_obj(obj.Type_Of_Availability_Loss)
#         return_obj.duration_of_availability_loss = VocabString.from_obj(obj.Duration_Of_Availability_Loss)
#         return_obj.non_public_data_compromised = NonPublicDataCompromised.from_obj(obj.Non_Public_Data_Compromised)
#         return return_obj
#     
#     def to_obj(self, return_obj=None, ns_info=None):
#         super(PropertyAffected, self).to_obj(return_obj=return_obj, ns_info=ns_info)
# 
#         if not return_obj:
#             return_obj = self._binding_class()
#             
#         if self.property_:
#             return_obj.Property = self.property_.to_obj(ns_info=ns_info)
#         if self.descriptions_of_effect:
#             return_obj.Description_Of_Effect = self.descriptions_of_effect.to_obj(ns_info=ns_info)
#         if self.type_of_availability_loss:
#             return_obj.Type_Of_Availability_Loss = self.type_of_availability_loss.to_obj(ns_info=ns_info)
#         if self.duration_of_availability_loss:
#             return_obj.Duration_Of_Availability_Loss = self.duration_of_availability_loss.to_obj(ns_info=ns_info)
#         if self.non_public_data_compromised:
#             return_obj.Non_Public_Data_Compromised = self.non_public_data_compromised.to_obj(ns_info=ns_info)
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
#         return_obj.property_ = VocabString.from_dict(d.get('property'))
#         return_obj.descriptions_of_effect = StructuredTextList.from_dict(d.get('description_of_effect'))
#         return_obj.type_of_availability_loss = VocabString.from_dict(d.get('type_of_availability_loss'))
#         return_obj.duration_of_availability_loss = VocabString.from_dict(d.get('duration_of_availability_loss'))
#         return_obj.non_public_data_compromised = NonPublicDataCompromised.from_dict(d.get('non_public_data_compromised'))
#         
#         return return_obj
#     
#     def to_dict(self):
#         return super(PropertyAffected, self).to_dict()
