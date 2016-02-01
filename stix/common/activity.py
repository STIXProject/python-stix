# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
import stix.bindings.stix_common as common_binding
import stix.utils

from .datetimewithprecision import DateTimeWithPrecision
from .structured_text import StructuredTextList


class Activity(stix.Entity):
    _binding = common_binding
    _binding_class = common_binding.ActivityType
    _namespace = 'http://stix.mitre.org/common-1'

    date_time = fields.TypedField("Date_Time", DateTimeWithPrecision)
    descriptions = fields.TypedField("Description", StructuredTextList)

    def __init__(self):
        super(Activity, self).__init__()
        self.descriptions = StructuredTextList()

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
        self.descriptions = StructuredTextList(value)

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        self.descriptions.add(description)

