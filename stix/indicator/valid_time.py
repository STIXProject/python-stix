# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import DateTimeWithPrecision
import stix.bindings.indicator as indicator_binding


class ValidTime(stix.Entity):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.ValidTimeType
    
    def __init__(self, start_time=None, end_time=None):
        self.start_time = start_time
        self.end_time = end_time
        
    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._set_var(DateTimeWithPrecision, start_time=value)

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._set_var(DateTimeWithPrecision, end_time=value)
    
    def to_obj(self, return_obj=None, ns_info=None):
        super(ValidTime, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()
        
        if self.start_time:
            return_obj.Start_Time = self.start_time.to_obj(ns_info=ns_info)
        if self.end_time:
            return_obj.End_Time = self.end_time.to_obj(ns_info=ns_info)
        
        return return_obj

    def to_dict(self):
        return super(ValidTime, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if return_obj is None:
            return_obj = cls()

        return_obj.start_time = DateTimeWithPrecision.from_obj(obj.Start_Time)
        return_obj.end_time = DateTimeWithPrecision.from_obj(obj.End_Time)
        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if return_obj is None:
            return_obj = cls()

        return_obj.start_time = DateTimeWithPrecision.from_dict(d.get('start_time'))
        return_obj.end_time = DateTimeWithPrecision.from_dict(d.get('end_time'))
        
        return return_obj


# NOT AN ACTUAL STIX TYPE
class _ValidTimePositions(stix.TypedList):
    _contained_type = ValidTime
