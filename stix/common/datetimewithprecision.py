# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox.fields import DateTimeField

import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding

from stix.base import ContentField, AttributeField




DATE_PRECISION_VALUES = ("year", "month", "day")
TIME_PRECISION_VALUES = ("hour", "minute", "second")
DATETIME_PRECISION_VALUES = DATE_PRECISION_VALUES + TIME_PRECISION_VALUES


def _validate_precision(instance, value):
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

    value = DateTimeField("valueOf_", key_name="value")
    precision = AttributeField("precision", preset_hook=_validate_precision)

    def __init__(self, value=None, precision='second'):
        super(DateTimeWithPrecision, self).__init__()

        self.value = value
        self.precision = precision


    def to_dict(self):
        if self.precision == 'second':
            return utils.dates.serialize_value(self.value)

        d  = {
            'value': utils.dates.serialize_value(self.value),
            'precision':self.precision
        }

        return d

    @classmethod
    def from_dict(cls, cls_dict=None, return_obj=None):
        if not cls_dict:
            return None

        if not return_obj:
            return_obj = cls()

        if not isinstance(cls_dict, dict):
            return_obj.value = cls_dict
        else:
            return_obj.precision = cls_dict.get('precision')
            return_obj.value = cls_dict.get('value')

        return return_obj
