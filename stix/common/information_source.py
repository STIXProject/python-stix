# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
import cybox.common

# internal
import stix
import stix.utils as utils
import stix.bindings.stix_common as stix_common_binding

# relative
from . import vocabs
from .vocabs import VocabString
from .references import References
from .identity import Identity
from .structured_text import StructuredTextList, StructuredTextListField
from stix.base import ElementField

from cybox.common.tools import ToolInformationList


class InformationSource(stix.Entity):
    _binding = stix_common_binding
    _binding_class = stix_common_binding.InformationSourceType
    _namespace = 'http://stix.mitre.org/common-1'

    identity = ElementField("Identity", Identity)
    descriptions = StructuredTextListField("Description", StructuredTextList, key_name="description")
    contributing_sources = ElementField("Contributing_Sources")
    time = ElementField("Time", cybox.common.Time)
    roles = ElementField("Role", VocabString, multiple=True, key_name="roles")
    tools = ElementField("Tools", ToolInformationList)
    references = ElementField("References", References)

    @classmethod
    def initClassFields(cls):
        cls.contributing_sources.type_ = ContributingSources

    def __init__(self, description=None, identity=None, time=None, tools=None, contributing_sources=None, references=None):
        super(InformationSource, self).__init__()

        self.identity = identity
        self.descriptions = StructuredTextList(description)
        self.contributing_sources = contributing_sources
        self.time = time
        self.tools = tools
        self.references = references
        #self.roles = None
    
    def add_contributing_source(self, value):
        self.contributing_sources.append(value)


    def add_reference(self, value):
        if not value:
            return
        # TODO: Check if it's a valid URI?
        self.references.append(value)

    @property
    def description(self):
        """A single description about the contents or purpose of this object.

        Default Value: ``None``

        Note:
            If this object has more than one description set, this will return
            the description with the lowest ordinality value.

        Returns:
            An instance of :class:`.StructuredText`

        """
        return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        from stix.common.structured_text import StructuredTextList
        self.descriptions = StructuredTextList(value)

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        self.descriptions.add(description)


    def add_role(self, value):
        self.roles.append(value)


class ContributingSources(stix.EntityList):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = stix_common_binding
    _binding_class = stix_common_binding.ContributingSourcesType
    _binding_var = "Source"
    _contained_type = InformationSource
    _inner_name = "sources"


# finally, initialize field types that would be circular dependencies
InformationSource.initClassFields()
