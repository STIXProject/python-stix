# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
import cybox.common

# internal
import stix
import stix.bindings.stix_common as common_binding

# relative
from .structured_text import StructuredTextList


class ToolInformation(stix.Entity, cybox.common.ToolInformation):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.ToolInformationType

    title = fields.TypedField("Title")
    short_descriptions = fields.TypedField("Short_Description", StructuredTextList)

    def __init__(self, title=None, short_description=None, tool_name=None, tool_vendor=None):
        super(ToolInformation, self).__init__(tool_name=tool_name, tool_vendor=tool_vendor)
        self.title = title
        self.short_description = StructuredTextList(short_description)

    @property
    def short_description(self):
        """A single short description about the contents or purpose of this
        object.

        Default Value: ``None``

        Note:
            If this object has more than one short description set, this will
            return the short description with the lowest ordinality value.

        Returns:
            An instance of
            :class:`.StructuredText`

        """
        return next(iter(self.short_descriptions), None)

    @short_description.setter
    def short_description(self, value):
        self.short_descriptions = value

    def add_short_description(self, description):
        """Adds a description to the ``short_descriptions`` collection.

        This is the same as calling "foo.short_descriptions.add(bar)".

        """
        self.short_descriptions.add(description)
