# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
from stix.common import vocabs, VocabString, StructuredText
import stix.bindings.incident as incident_binding


class NonPublicDataCompromised(VocabString):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
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
    descriptions_of_effect = fields.TypedField("Description_Of_Effect", StructuredText)
    type_of_availability_loss = vocabs.VocabField("Type_Of_Availability_Loss", vocabs.AvailabilityLossType)
    duration_of_availability_loss = vocabs.VocabField("Duration_Of_Availability_Loss", vocabs.LossDuration)
    non_public_data_compromised = fields.TypedField("Non_Public_Data_Compromised", NonPublicDataCompromised)

    def __init__(self):
        super(PropertyAffected, self).__init__()
