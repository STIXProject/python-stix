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

#     def to_obj(self, return_obj=None, ns_info=None):
#         super(Time, self).to_obj(return_obj=return_obj, ns_info=ns_info)
# 
#         if not return_obj:
#             return_obj = self._binding_class()
# 
#         if self.first_malicious_action:
#             return_obj.First_Malicious_Action = self.first_malicious_action.to_obj(ns_info=ns_info)
#         if self.initial_compromise:
#             return_obj.Initial_Compromise = self.initial_compromise.to_obj(ns_info=ns_info)
#         if self.first_data_exfiltration:
#             return_obj.First_Data_Exfiltration = self.first_data_exfiltration.to_obj(ns_info=ns_info)
#         if self._incident_discovery:
#             return_obj.Incident_Discovery = self.incident_discovery.to_obj(ns_info=ns_info)
#         if self.incident_opened:
#             return_obj.Incident_Opened = self.incident_opened.to_obj(ns_info=ns_info)
#         if self.containment_achieved:
#             return_obj.Containment_Achieved = self.containment_achieved.to_obj(ns_info=ns_info)
#         if self.restoration_achieved:
#             return_obj.Restoration_Achieved = self.restoration_achieved.to_obj(ns_info=ns_info)
#         if self.incident_reported:
#             return_obj.Incident_Reported = self.incident_reported.to_obj(ns_info=ns_info)
#         if self.incident_closed:
#             return_obj.Incident_Closed = self.incident_closed.to_obj(ns_info=ns_info)
# 
#         return return_obj
# 
#     @classmethod
#     def from_obj(cls, obj, return_obj=None):
#         if not obj:
#             return None
# 
#         if not return_obj:
#             return_obj = cls()
# 
#         return_obj.first_malicious_action = DateTimeWithPrecision.from_obj(obj.First_Malicious_Action)
#         return_obj.initial_compromise = DateTimeWithPrecision.from_obj(obj.Initial_Compromise)
#         return_obj.first_data_exfiltration = DateTimeWithPrecision.from_obj(obj.First_Data_Exfiltration)
#         return_obj.incident_discovery = DateTimeWithPrecision.from_obj(obj.Incident_Discovery)
#         return_obj.incident_opened = DateTimeWithPrecision.from_obj(obj.Incident_Opened)
#         return_obj.containment_achieved  = DateTimeWithPrecision.from_obj(obj.Containment_Achieved)
#         return_obj.restoration_achieved = DateTimeWithPrecision.from_obj(obj.Restoration_Achieved)
#         return_obj.incident_reported = DateTimeWithPrecision.from_obj(obj.Incident_Reported)
#         return_obj.incident_closed = DateTimeWithPrecision.from_obj(obj.Incident_Closed)
# 
#         return return_obj
# 
#     def to_dict(self):
#         return super(Time, self).to_dict()
# 
#     @classmethod
#     def from_dict(cls, dict_repr, return_obj=None):
#         if not dict_repr:
#             return None
# 
#         if not return_obj:
#             return_obj = cls()
# 
#         return_obj.first_malicious_action = DateTimeWithPrecision.from_dict(dict_repr.get('first_malicious_action'))
#         return_obj.initial_compromise = DateTimeWithPrecision.from_dict(dict_repr.get('initial_compromise'))
#         return_obj.first_data_exfiltration = DateTimeWithPrecision.from_dict(dict_repr.get('first_data_exfiltration'))
#         return_obj.incident_discovery = DateTimeWithPrecision.from_dict(dict_repr.get('incident_discovery'))
#         return_obj.incident_opened = DateTimeWithPrecision.from_dict(dict_repr.get('incident_opened'))
#         return_obj.containment_achieved = DateTimeWithPrecision.from_dict(dict_repr.get('containment_achieved'))
#         return_obj.restoration_achieved = DateTimeWithPrecision.from_dict(dict_repr.get('restoration_achieved'))
#         return_obj.incident_reported = DateTimeWithPrecision.from_dict(dict_repr.get('incident_reported'))
#         return_obj.incident_closed = DateTimeWithPrecision.from_dict(dict_repr.get('incident_closed'))
# 
#         return return_obj
