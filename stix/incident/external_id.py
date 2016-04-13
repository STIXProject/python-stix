# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from mixbox import fields, entities

class ExternalID(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.ExternalIDType

    value = fields.TypedField("valueOf_", key_name="value")
    source = fields.TypedField("source")

    def __init__(self, value=None, source=None):
        super(ExternalID, self).__init__()
        self.value = value
        self.source = source
