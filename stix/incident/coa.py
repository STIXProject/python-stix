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


class COATaken(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.COATakenType
    
    def __init__(self, course_of_action=None):
        self.time = None
        self.course_of_action = course_of_action
        self.contributors = Contributors()

    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, value):
        self._set_var(COATime, try_cast=False, time=value)
    
    @property
    def course_of_action(self):
        return self._course_of_action
    
    @course_of_action.setter
    def course_of_action(self, value):
        self._set_var(CourseOfAction, try_cast=False, course_of_action=value)

    @property
    def contributors(self):
        return self._contributors

    @contributors.setter
    def contributors(self, value):
        self._contributors = Contributors(value)

    def add_contributor(self, value):
        self.contributors.append(value)

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.time = COATime.from_obj(obj.Time)
        return_obj.contributors = Contributors.from_obj(obj.Contributors)
        return_obj.course_of_action = CourseOfAction.from_obj(obj.Course_Of_Action)
        
        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        super(COATaken, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()
            
        if self.time:
            return_obj.Time = self.time.to_obj(ns_info=ns_info)
        if self.contributors:
            return_obj.Contributors = self.contributors.to_obj(ns_info=ns_info)
        if self.course_of_action:
            return_obj.Course_Of_Action = self.course_of_action.to_obj(ns_info=ns_info)
        
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.time = COATime.from_dict(d.get('time'))
        return_obj.contributors = Contributors.from_dict(d.get('contributors'))
        return_obj.course_of_action = CourseOfAction.from_dict(d.get('course_of_action'))
        
        return return_obj
    
    def to_dict(self):
        return super(COATaken, self).to_dict()


class COARequested(COATaken):
    namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.COARequestedType

    def __init__(self, course_of_action=None):
        super(COARequested, self).__init__(course_of_action=course_of_action)
        self.priority = None

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, value):
        if value is None:
            self._priority = None
        else:
            self._priority = value

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        super(COARequested, cls).from_obj(obj, return_obj=return_obj)
        return_obj.priority = obj.priority

        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(COARequested, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        return_obj.priority = self.priority

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()

        super(COARequested, cls).from_dict(d, return_obj=return_obj)
        return_obj.priority = d.get('priority')

        return return_obj

    def to_dict(self):
        d = utils.to_dict(self)
        return d


class COATime(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.COATimeType
    
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        
    @property
    def start(self):
        return self._start
    
    @start.setter
    def start(self, value):
        self._set_var(DateTimeWithPrecision, start=value)
    
    @property
    def end(self):
        return self._end
    
    @end.setter
    def end(self, value):
        self._set_var(DateTimeWithPrecision, end=value)
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.start = DateTimeWithPrecision.from_obj(obj.Start)
        return_obj.end = DateTimeWithPrecision.from_obj(obj.End)
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(COATime, self).to_obj(return_obj=return_obj, ns_info=ns_info)
            
        if self.start:
            return_obj.Start = self.start.to_obj(ns_info=ns_info)
        if self.end:
            return_obj.End = self.end.to_obj(ns_info=ns_info)
        
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.start = DateTimeWithPrecision.from_dict(d.get('start'))
        return_obj.end = DateTimeWithPrecision.from_dict(d.get('end'))
        return return_obj
    
    def to_dict(self):
        d = {}
        
        if self.start:
            d['start'] = self.start.to_dict()
        if self.end:
            d['end'] = self.end.to_dict()
        
        return d
