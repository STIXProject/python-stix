# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from stix.common import DateTimeWithPrecision
from mixbox import entities, fields

class Time(stix.Entity):
    _binding = incident_binding
    _binding_class = _binding.TimeType
    _namespace = "http://stix.mitre.org/Incident-1"

    first_malicious_action = fields.TypedField("First_Malicious_Action", DateTimeWithPrecision)
    initial_compromise = fields.TypedField("Initial_Compromise", DateTimeWithPrecision)
    first_data_exfiltration = fields.TypedField("First_Data_Exfiltration", DateTimeWithPrecision)
    incident_discovery = fields.TypedField("Incident_Discovery", DateTimeWithPrecision)
    incident_opened = fields.TypedField("Incident_Opened", DateTimeWithPrecision)
    containment_achieved = fields.TypedField("Containment_Achieved", DateTimeWithPrecision)
    restoration_achieved = fields.TypedField("Restoration_Achieved", DateTimeWithPrecision)
    incident_reported = fields.TypedField("Incident_Reported", DateTimeWithPrecision)
    incident_closed = fields.TypedField("Incident_Closed", DateTimeWithPrecision)

    def __init__(self, first_malicious_action=None, initial_compromise=None,
                 first_data_exfiltration=None, incident_discovery=None,
                 incident_opened=None, containment_achieved=None,
                 restoration_achieved=None, incident_reported=None,
                 incident_closed=None):
        super(Time, self).__init__()
        self.first_malicious_action = first_malicious_action
        self.initial_compromise = initial_compromise
        self.first_data_exfiltration = first_data_exfiltration
        self.incident_discovery = incident_discovery
        self.incident_opened = incident_opened
        self.containment_achieved = containment_achieved
        self.restoration_achieved = restoration_achieved
        self.incident_reported = incident_reported
        self.incident_closed = incident_closed
