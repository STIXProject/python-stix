# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.stix_common as common_binding
import dateutil
from stix.utils.dates import parse_value, serialize_value

DATE_PRECISION_VALUES = ("year", "month", "day")
TIME_PRECISION_VALUES = ("hour", "minute", "second")
DATETIME_PRECISION_VALUES = DATE_PRECISION_VALUES + TIME_PRECISION_VALUES

class DateTimeWithPrecision(stix.Entity):
    _binding = common_binding
    _binding_class = _binding.DateTimeWithPrecisionType
    _namespace = 'http://stix.mitre.org/common-1'

    def __init__(self, value=None, precision='second'):
        super(DateTimeWithPrecision, self).__init__()
        self.value = value
        self.precision = precision

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = parse_value(value)

    @property
    def precision(self):
        return self._precision

    @precision.setter
    def precision(self, value):
        if value not in DATETIME_PRECISION_VALUES:
            raise ValueError("value must be one of [%s]" % ", ".join(x for x in DATETIME_PRECISION_VALUES))

        self._precision = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(DateTimeWithPrecision, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        obj = self._binding_class()
        obj.valueOf_ = serialize_value(self.value)
        obj.precision = self.precision
        return obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.value = obj.valueOf_
        return_obj.precision = obj.precision
        return return_obj

    def to_dict(self):    
        if self.precision == 'second':
            return serialize_value(self.value)
       
        d  = {}
        d['value'] = serialize_value(self.value)
        d['precision'] = self.precision
        return d

    @classmethod
    def from_dict(cls, dict_, return_obj=None):
        if not dict_:
            return None

        if not return_obj:
            return_obj = cls()

        if not isinstance(dict_, dict):
            return_obj.value = dict_
        else:
            return_obj.precision = dict_.get('precision')
            return_obj.value = dict_.get('value')

        return return_obj
