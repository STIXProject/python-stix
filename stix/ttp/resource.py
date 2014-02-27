# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import ToolInformation
import stix.bindings.ttp as ttp_binding

class Resource(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.ResourceType
    _namespace = "http://stix.mitre.org/TTP-1"
    
    def __init__(self, tools=None, infrastructure=None, personas=None):
        self.tools = tools
        self.infrastructure = infrastructure
        self.personas = personas
        
    @property
    def tools(self):
        return self._tools
    
    @tools.setter
    def tools(self, value):
        self._tools = []
        
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_tool(v)
        else:
            self.add_tool(value)
    
    def add_tool(self, tool):
        if not tool:
            return
        elif isinstance(tool, ToolInformation):
            self._tools.append(tool)
        else:
            raise ValueError('Cannot add type %s to tools list' % type(tool))
    
    @property
    def infrastructure(self):
        return self._infrastructure
    
    @infrastructure.setter
    def infrastructure(self, value):
        self._infrastructure = None
        
    @property
    def personas(self):
        return self._personas
    
    @personas.setter
    def personas(self, value):
        self._personas = []
        return
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()
        
        if self.tools:
            tools_obj = self._binding.ToolsType(Tool=[x.to_obj() for x in self.tools])
            return_obj.set_Tools(tools_obj)
        
        return return_obj
        
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
            
        if obj.get_Tools():
            return_obj.tools = [ToolInformation.from_obj(x) for x in obj.get_Tools().get_Tool()]
    
        return return_obj
            
    def to_dict(self):
        d = {}
        
        if self.tools:
            d['tools'] = [x.to_dict() for x in self.tools]
            
        return d
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.tools = [ToolInformation.from_dict(x) for x in dict_repr.get('tools', [])] 
        
        return return_obj
        
        