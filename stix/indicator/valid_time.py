# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
from mixbox import fields

import stix
from stix.common import DateTimeWithPrecision
import stix.bindings.indicator as indicator_binding
from mixbox.entities import Entity

class ValidTime(Entity):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.ValidTimeType
    
    start_time = fields.TypedField("Start_Time", DateTimeWithPrecision)
    end_time = fields.TypedField("End_Time", DateTimeWithPrecision)
    
    def __init__(self, start_time=None, end_time=None):
        super(ValidTime, self).__init__()
        self.start_time = start_time
        self.end_time = end_time

