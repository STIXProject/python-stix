# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
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
    
    def __init__(self, title=None, short_description=None, tool_name=None, tool_vendor=None):
        super(ToolInformation, self).__init__(tool_name=tool_name, tool_vendor=tool_vendor)
        self.title = title
        self.short_description = short_description
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, value):
        self._set_var(StructuredText, short_description=value)

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        stix.Entity.to_obj(self, return_obj=return_obj, ns_info=ns_info)
        cybox.common.ToolInformation.to_obj(
            self,
            return_obj=return_obj,
            ns_info=ns_info
        )

        return_obj.Title = self.title        
        if self.short_description:
            return_obj.Short_Description = self.short_description.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        cybox.common.ToolInformation.from_obj(obj, return_obj)
        
        return_obj.title = obj.Title
        return_obj.short_description = StructuredText.from_obj(obj.Short_Description)
        
        return return_obj

    def to_dict(self):
        d = cybox.common.ToolInformation.to_dict(self)
        
        if self.title:
            d['title'] = self.title
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
       
        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        cybox.common.ToolInformation.from_dict(dict_repr, return_obj)
        return_obj.title = dict_repr.get('title')
        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))
        
        return return_obj
