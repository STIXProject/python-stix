# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
import cybox.common

# internal
import stix
import stix.bindings.stix_common as common_binding

# relative
from .structured_text import StructuredText


class ToolInformation(stix.Entity, cybox.common.ToolInformation):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.ToolInformationType

    title = fields.TypedField("Title")
    short_description = fields.TypedField("Short_Description", StructuredText)

    def __init__(self, title=None, short_description=None, tool_name=None, tool_vendor=None):
        super(ToolInformation, self).__init__(tool_name=tool_name, tool_vendor=tool_vendor)
        self.title = title
        self.short_description = short_description
