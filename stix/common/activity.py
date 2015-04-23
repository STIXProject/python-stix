# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding

from .datetimewithprecision import DateTimeWithPrecision
from .structured_text import StructuredTextList


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
        """A single description about the contents or purpose of this object.

        Default Value: ``None``

        Note:
            If this object has more than one description set, this will return
            the description with the lowest ordinality value.

        Returns:
            An instance of
            :class:`.StructuredText`

        """
        return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        self.descriptions = value

    @property
    def descriptions(self):
        """A :class:`.StructuredTextList` object, containing descriptions about
        the purpose or intent of this object.

        Iterating over this object will yield its contents sorted by their
        ``ordinality`` value.

        Default Value: Empty :class:`StructuredTextList` object.

        Note:
            IF this is set to a value that is not an instance of
            :class:`.StructuredText`, an effort will ne made to convert it.
            If this is set to an iterable, any values contained that are not
            an instance of :class:`StructuredText` will be be converted.

        Returns:
            An instance of
            :class:`.StructuredTextList`

        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, value):
        self._descriptions = StructuredTextList(value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(Activity, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.date_time:
            return_obj.Date_Time = self.date_time.to_obj(ns_info=ns_info)
        if self.descriptions:
            return_obj.Description = self.descriptions.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.date_time = DateTimeWithPrecision.from_obj(obj.Date_Time)
        return_obj.descriptions = StructuredTextList.from_obj(obj.Description)

        return return_obj

    def to_dict(self):
        d = utils.to_dict(self)

        # Rename 'descriptions' key.
        utils.fix_descriptions(d)

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        get = dict_repr.get
        return_obj.date_time = DateTimeWithPrecision.from_dict(get('date_time'))
        return_obj.descriptions = StructuredTextList.from_dict(get('description'))

        return return_obj
