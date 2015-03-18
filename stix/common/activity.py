# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
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
        self._set_var(DateTimeWithPrecision, date_time=value)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._set_var(StructuredText, description=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(Activity, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.date_time:
            return_obj.Date_Time = self.date_time.to_obj(ns_info=ns_info)
        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.date_time = DateTimeWithPrecision.from_obj(obj.Date_Time)
        return_obj.description = StructuredText.from_obj(obj.Description)

        return return_obj

    def to_dict(self):
        return super(Activity, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        get = dict_repr.get
        return_obj.date_time = DateTimeWithPrecision.from_dict(get('date_time'))
        return_obj.description = StructuredText.from_dict(get('description'))

        return return_obj
