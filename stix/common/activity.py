# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.stix_common as common_binding
import stix.utils
from stix.base import ElementField

from .datetimewithprecision import DateTimeWithPrecision
from .structured_text import StructuredTextList, StructuredTextListField


class Activity(stix.Entity):
    _binding = common_binding
    _binding_class = common_binding.ActivityType
    _namespace = 'http://stix.mitre.org/common-1'

    date_time = ElementField("Date_Time", DateTimeWithPrecision)
    descriptions = StructuredTextListField("Description", StructuredTextList, key_name="description")

    def __init__(self):
        super(Activity, self).__init__()
        self.date_time = None
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

