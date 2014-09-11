# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.stix_common as common_binding

from .datetimewithprecision import DateTimeWithPrecision
from .structured_text import StructuredText


class Activity(stix.Entity):
    _binding = common_binding
    _binding_class = common_binding.ActivityType
    _namespace = 'http://stix.mitre.org/common-1'

    def __init__(self):
        self.date_time = None
        self.description = None

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, value):
        if value:
            if isinstance(value, DateTimeWithPrecision):
                self._date_time = value
            else:
                self._date_time = DateTimeWithPrecision(value=value)
        else:
            self._date_time = None

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if isinstance(value, StructuredText):
            self._description = value
        else:
            self._description = StructuredText(value=value)

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.date_time:
            return_obj.set_Date_Time(self.date_time.to_obj(ns_info=ns_info))
        if self.description:
            return_obj.set_Description(self.description.to_obj(ns_info=ns_info))

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.date_time = \
                DateTimeWithPrecision.from_obj(obj.get_Date_Time())
        return_obj.description = StructuredText.from_obj(obj.get_Description())

        return return_obj

    def to_dict(self):
        d = {}

        if self.date_time:
            d['date_time'] = self.date_time.to_dict()
        if self.description:
            d['description'] = self.description.to_dict()

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.date_time = \
                DateTimeWithPrecision.from_dict(dict_repr.get('date_time'))
        return_obj.description = \
                StructuredText.from_dict(dict_repr.get('description'))

        return return_obj

