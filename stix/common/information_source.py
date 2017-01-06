# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
import cybox.common
from cybox.common.tools import ToolInformationList

# internal
import stix
import stix.bindings.stix_common as stix_common_binding

# relative
from .vocabs import VocabField
from .references import References
from .identity import Identity, IdentityFactory
from .structured_text import StructuredText


class InformationSource(stix.Entity):
    _binding = stix_common_binding
    _binding_class = stix_common_binding.InformationSourceType
    _namespace = 'http://stix.mitre.org/common-1'

    identity = fields.TypedField("Identity", type_=Identity, factory=IdentityFactory)
    description = fields.TypedField("Description", StructuredText)
    contributing_sources = fields.TypedField("Contributing_Sources", type_="stix.common.information_source.ContributingSources")
    time = fields.TypedField("Time", cybox.common.Time)
    roles = VocabField("Role", multiple=True, key_name="roles")
    tools = fields.TypedField("Tools", ToolInformationList)
    references = fields.TypedField("References", References)

    def __init__(self, description=None, identity=None, time=None, tools=None, contributing_sources=None, references=None):
        super(InformationSource, self).__init__()

        self.identity = identity
        self.description = description
        self.contributing_sources = contributing_sources
        self.time = time
        self.tools = tools
        self.references = references
    
    def add_contributing_source(self, value):
        self.contributing_sources.append(value)

    def add_reference(self, value):
        if not value:
            return
        # TODO: Check if it's a valid URI?
        self.references.append(value)

    def add_role(self, value):
        self.roles.append(value)


class ContributingSources(stix.EntityList):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = stix_common_binding
    _binding_class = stix_common_binding.ContributingSourcesType

    source = fields.TypedField("Source", InformationSource, multiple=True, key_name="sources")

    @classmethod
    def _dict_as_list(cls):
        return False
