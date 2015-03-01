# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils as utils
from stix.common import ToolInformation, Identity
from .infrastructure import Infrastructure
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
        elif utils.is_sequence(value):
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
        self._infrastructure = value

    @property
    def personas(self):
        return self._personas

    @personas.setter
    def personas(self, value):
        self._personas = []

        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_persona(v)
        else:
            self.add_persona(value)

    def add_persona(self, persona):
        if not persona:
            return
        elif isinstance(persona, Identity):
            self._personas.append(persona)
        else:
            self._personas.append(Identity(name=persona))

    def to_obj(self, return_obj=None, ns_info=None):
        super(Resource, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.tools:
            tools_obj = self._binding.ToolsType(Tool=[x.to_obj(ns_info=ns_info) for x in self.tools])
            return_obj.Tools = tools_obj
        if self.infrastructure:
            return_obj.Infrastructure = self.infrastructure.to_obj(ns_info=ns_info)
        if self.personas:
            personas_obj = self._binding.PersonasType(Persona=[x.to_obj(ns_info=ns_info) for x in self.personas])
            return_obj.Personas = personas_obj

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.infrastructure = Infrastructure.from_obj(obj.Infrastructure)

        if obj.Tools:
            return_obj.tools = [ToolInformation.from_obj(x) for x in obj.Tools.Tool]
        if obj.Personas:
            return_obj.personas = [Identity.from_obj(x) for x in obj.Personas.Persona]

        return return_obj

    def to_dict(self):
        d = {}

        if self.tools:
            d['tools'] = [x.to_dict() for x in self.tools]
        if self.infrastructure:
            d['infrastructure'] = self.infrastructure.to_dict()
        if self.personas:
            d['personas'] = [x.to_dict() for x in self.personas]

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.tools = [ToolInformation.from_dict(x) for x in dict_repr.get('tools', [])] 
        return_obj.infrastructure = Infrastructure.from_dict(dict_repr.get('infrastructure'))
        return_obj.personas = [Identity.from_dict(x) for x in dict_repr.get('personas', [])]

        return return_obj


