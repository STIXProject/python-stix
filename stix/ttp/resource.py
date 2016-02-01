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
