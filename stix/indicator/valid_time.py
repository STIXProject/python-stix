# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix.utils import dates
from stix.common import DateTimeWithPrecision
import stix.bindings.indicator as indicator_binding
from datetime import datetime

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
        if isinstance(value, DateTimeWithPrecision):
            self._start_time = value
        else:
            self._start_time = DateTimeWithPrecision(value)

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        if isinstance(value, DateTimeWithPrecision):
            self._end_time = value
        else:
            self._end_time = DateTimeWithPrecision(value)
    
    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if not return_obj:
            return_obj = self._binding_class()
        
        if self.start_time:
            return_obj.Start_Time = self.start_time.to_obj(ns_info=ns_info)
        if self.end_time:
            return_obj.End_Time = self.end_time.to_obj(ns_info=ns_info)
        
        return return_obj

    def to_dict(self):
        d = {}
        if self.start_time:
            d['start_time'] = self.start_time.to_dict()
        if self.end_time:
            d['end_time'] = self.end_time.to_dict()
         
        return d

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
