# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# mixbox
from mixbox import fields
from mixbox import typedlist

# internal
import stix
from stix.common import ToolInformation, Identity
import stix.bindings.ttp as ttp_binding

# relative
from .infrastructure import Infrastructure

from mixbox import entities, fields

class _IdentityList(typedlist.TypedList):
    def __init__(self, *args):
        super(_IdentityList, self).__init__(type=Identity, *args)

    def _fix_value(self, value):
        return Identity(name=value)


class Personas(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _binding = ttp_binding
    _binding_class = _binding.PersonasType

    persona = fields.TypedField("Persona", Identity, multiple=True, listfunc=_IdentityList)


class Tools(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _binding = ttp_binding
    _binding_class = _binding.ToolsType

    tool = fields.TypedField("Tool", ToolInformation, multiple=True)

    @classmethod
    def _dict_as_list(cls):
        return True


class Resource(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.ResourceType
    _namespace = "http://stix.mitre.org/TTP-1"

    tools = fields.TypedField("Tools", Tools)
    infrastructure = fields.TypedField("Infrastructure", Infrastructure)
    personas = fields.TypedField("Personas", Personas)

    def __init__(self, tools=None, infrastructure=None, personas=None):
        super(Resource, self).__init__()
        self.tools = tools
        self.infrastructure = infrastructure
        self.personas = personas

    # @property
    # def tools(self):
    #     return self._tools
    #
    # @tools.setter
    # def tools(self, value):
    #     self._tools = Tools(value)

    def add_tool(self, tool):
        self.tools.append(tool)

    # @property
    # def infrastructure(self):
    #     return self._infrastructure
    #
    # @infrastructure.setter
    # def infrastructure(self, value):
    #     self._infrastructure = value
    #
    # @property
    # def personas(self):
    #     return self._personas
    #
    # @personas.setter
    # def personas(self, value):
    #     self._personas = Personas(value)

    def add_persona(self, persona):
        self.personas.append(persona)
    #
    # def to_obj(self, return_obj=None, ns_info=None):
    #     super(Resource, self).to_obj(return_obj=return_obj, ns_info=ns_info)
    #
    #     if not return_obj:
    #         return_obj = self._binding_class()
    #
    #     if self.tools:
    #         return_obj.Tools = self.tools.to_obj(ns_info=ns_info)
    #     if self.infrastructure:
    #         return_obj.Infrastructure = self.infrastructure.to_obj(ns_info=ns_info)
    #     if self.personas:
    #         return_obj.Personas = self.personas.to_obj(ns_info=ns_info)
    #
    #     return return_obj
    #
    # @classmethod
    # def from_obj(cls, obj, return_obj=None):
    #     if not obj:
    #         return None
    #
    #     if not return_obj:
    #         return_obj = cls()
    #
    #     return_obj.infrastructure = Infrastructure.from_obj(obj.Infrastructure)
    #     return_obj.tools = Tools.from_obj(obj.Tools)
    #     return_obj.personas = Personas.from_obj(obj.Personas)
    #
    #     return return_obj
    #
    # def to_dict(self):
    #     return super(Resource, self).to_dict()
    #
    # @classmethod
    # def from_dict(cls, dict_repr, return_obj=None):
    #     if not dict_repr:
    #         return None
    #
    #     if not return_obj:
    #         return_obj = cls()
    #
    #     get = dict_repr.get
    #
    #     return_obj.tools = Tools.from_dict(get('tools'))
    #     return_obj.infrastructure = Infrastructure.from_dict(get('infrastructure'))
    #     return_obj.personas = Personas.from_dict(get('personas'))
    #
    #     return return_obj
