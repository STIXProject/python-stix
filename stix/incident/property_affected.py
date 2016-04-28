# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import stix
from stix.common import vocabs, VocabString, StructuredTextList
import stix.bindings.incident as incident_binding
from mixbox import fields, entities

class NonPublicDataCompromised(VocabString):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.NonPublicDataCompromisedType
    
    data_encrypted = fields.TypedField("data_encrypted")
    
    def __init__(self, value=None, data_encrypted=None):
        super(NonPublicDataCompromised, self).__init__(value)
        self.data_encrypted = data_encrypted
 
    def is_plain(self):
        return False


class PropertyAffected(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.PropertyAffectedType
    
    property_ = vocabs.VocabField("Property", vocabs.LossProperty, key_name="property")
    descriptions_of_effect = fields.TypedField("Description_Of_Effect", StructuredTextList)
    type_of_availability_loss = vocabs.VocabField("Type_Of_Availability_Loss", vocabs.AvailabilityLossType)
    duration_of_availability_loss = vocabs.VocabField("Duration_Of_Availability_Loss", vocabs.LossDuration)
    non_public_data_compromised = fields.TypedField("Non_Public_Data_Compromised", NonPublicDataCompromised)
    
    def __init__(self):
        super(PropertyAffected, self).__init__()
        self.descriptions_of_effect = StructuredTextList()

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
