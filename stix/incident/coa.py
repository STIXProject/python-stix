# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.bindings.incident as incident_binding
from stix.common import DateTimeWithPrecision
from .contributors import Contributors
from stix.coa import CourseOfAction

class COATaken(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.COATakenType
    
    def __init__(self):
        self.time = None
        self.contributors = Contributors()
        self.course_of_action = None
        
    
    def add_contributor(self, value):
        if not value:
            return
        elif isinstance(value, Contributors):
            self.contributors.append(value)
        else:
            raise ValueError("Cannot add type %s to contributors" % type(value))
    
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, value):
        if not value:
            self._time = None
        elif isinstance(value, COATime):
            self._time = value
        else:
            raise ValueError("Cannot set time to type %s" % type(value))
    
    @property
    def course_of_action(self):
        return self._course_of_action
    
    @course_of_action.setter
    def course_of_action(self, value):
        if not value:
            self._course_of_action = None
        elif isinstance(value, CourseOfAction):
            self._course_of_action = value
        else:
            raise ValueError("Cannot set course_of_action to type %s" % type(value))
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.time = COATime.from_obj(obj.get_Time())
        return_obj.contributors = Contributors.from_obj(obj.get_Contributors())
        return_obj.course_of_action = CourseOfAction.from_obj(obj.get_Course_Of_Action())
        
        return return_obj

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()
            
        if self.time:
            return_obj.set_Time(self.time.to_obj())
        if self.contributors:
            return_obj.set_Contributors(self.contributors.to_obj())
        if self.course_of_action:
            return_obj.set_Course_Of_Action(self.course_of_action.to_obj())
        
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
        d = {}

        if self.time:
            d['time'] = self.time.to_dict()
        if self.contributors:
            d['contributors'] = self.contributors.to_dict()
        if self.course_of_action:
            d['course_of_action'] = self.course_of_action.to_dict()

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
        if not value:
            self._start = None
        elif isinstance(value, DateTimeWithPrecision):
            self._start = value
        else:
            self._start = DateTimeWithPrecision(value)
    
    @property
    def end(self):
        return self._end
    
    @end.setter
    def end(self, value):
        if not value:
            self._end = None
        elif isinstance(value, DateTimeWithPrecision):
            self._end = value
        else:
            self._end = DateTimeWithPrecision(value)
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.start = DateTimeWithPrecision.from_obj(obj.get_Start())
        return_obj.end = DateTimeWithPrecision.from_obj(obj.get_End())
        return return_obj
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()
            
        if self.start:
            return_obj.set_Start(self.start.to_obj())
        if self.end:
            return_obj.set_End(self.end.to_obj())
        
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
