# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.utils as utils
import stix.bindings.incident as incident_binding
from stix.common import DateTimeWithPrecision
from stix.coa import CourseOfAction

# relative
from .contributors import Contributors

from mixbox import entities, fields

class COATaken(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.COATakenType
    
    course_of_action = fields.TypedField("Course_Of_Action", CourseOfAction)
    contributors = fields.TypedField("Contributors", Contributors)
    time = fields.TypedField("Time", type_="stix.incident.coa.COATime")
    
    def __init__(self, course_of_action=None):
        super(COATaken, self).__init__()
        self.time = None
        self.course_of_action = course_of_action

    def add_contributor(self, value):
        self.contributors.append(value)


class COARequested(COATaken):
    namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.COARequestedType

    priority = fields.TypedField("priority")

    def __init__(self, course_of_action=None):
        super(COARequested, self).__init__(course_of_action=course_of_action)


class COATime(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.COATimeType
    
    start = fields.TypedField("Start", DateTimeWithPrecision)
    end = fields.TypedField("End", DateTimeWithPrecision)
    
    def __init__(self, start=None, end=None):
        super(COATime, self).__init__()
        self.start = start
        self.end = end
