# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding


DATE_PRECISION_VALUES = ("year", "month", "day")
TIME_PRECISION_VALUES = ("hour", "minute", "second")
DATETIME_PRECISION_VALUES = DATE_PRECISION_VALUES + TIME_PRECISION_VALUES


def validate_precision(instance, value):
    if value is None:
        return
    elif value in DATETIME_PRECISION_VALUES:
        return
    else:
        error = "The precision must be one of {0}. Received '{1}'"
        error = error.format(DATETIME_PRECISION_VALUES, value)
        raise ValueError(error)


class DateTimeWithPrecision(stix.Entity):
    _binding = common_binding
    _binding_class = _binding.DateTimeWithPrecisionType
    _namespace = 'http://stix.mitre.org/common-1'

    value = fields.DateTimeField("valueOf_", key_name="value")
    precision = fields.TypedField("precision", preset_hook=validate_precision)

    def __init__(self, value=None, precision='second'):
        super(DateTimeWithPrecision, self).__init__()
        self.value = value
        self.precision = precision

    def to_dict(self):
        if self.precision == 'second':
            return utils.dates.serialize_value(self.value)
        return super(DateTimeWithPrecision, self).to_dict()

    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None
        elif not isinstance(cls_dict, dict):
            obj = cls()
            obj.value = cls_dict
        else:
            obj = super(DateTimeWithPrecision, cls).from_dict(cls_dict)

        return obj
