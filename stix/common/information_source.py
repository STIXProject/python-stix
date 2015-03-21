# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

# external
import cybox.common

# internal
import stix
import stix.utils as utils
import stix.bindings.stix_common as stix_common_binding

# relative
from . import vocabs, VocabString
from .identity import Identity
from .structured_text import StructuredText


class InformationSource(stix.Entity):
    _binding = stix_common_binding
    _binding_class = stix_common_binding.InformationSourceType
    _namespace = 'http://stix.mitre.org/common-1'

    def __init__(self, description=None, identity=None, time=None, tools=None, contributing_sources=None, references=None):
        self.description = description
        self.identity = identity
        self.contributing_sources = contributing_sources
        self.time = time
        self.tools = tools
        self.references = references
        self.roles = None
    
    @property
    def contributing_sources(self):
        return self._contributing_sources
    
    @contributing_sources.setter
    def contributing_sources(self, value):
        self._contributing_sources = ContributingSources(value)
    
    def add_contributing_source(self, value):
        self.contributing_sources.append(value)
    
    @property
    def references(self):
        return self._references
    
    @references.setter
    def references(self, value):
        self._references = []

        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_reference(v)
        else:
            self.add_reference(value)
    
    def add_reference(self, value):
        if not value:
            return
        # TODO: Check if it's a valid URI?
        self.references.append(value)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        """Sets the value of the description property.

        If the value is an instance of basestring, it will be coerced into an
        instance of StructuredText, with its 'text' property set to the input
        value.

        """
        self._set_var(StructuredText, description=value)

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        self._set_var(Identity, try_cast=False, identity=value)

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        self._set_var(cybox.common.Time, try_cast=False, time=value)

    @property
    def tools(self):
        return self._tools

    @tools.setter
    def tools(self, value):
        self._set_var(cybox.common.ToolInformationList, try_cast=False, tools=value)

    @property
    def roles(self):
        return self._roles

    @roles.setter
    def roles(self, value):
        self._roles = _Roles(value)

    def add_role(self, value):
        self.roles.append(value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(InformationSource, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        if not return_obj:
            return_obj = self._binding_class()
            
        if self.description is not None:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.references:
            return_obj.References = stix_common_binding.ReferencesType(Reference=self.references)
        if self.contributing_sources:
            return_obj.Contributing_Sources = self.contributing_sources.to_obj(ns_info=ns_info)
        if self.identity:
            return_obj.Identity = self.identity.to_obj(ns_info=ns_info)
        if self.time:
            return_obj.Time = self.time.to_obj(ns_info=ns_info)
        if self.tools:
            return_obj.Tools = self.tools.to_obj(ns_info=ns_info)
        if self.roles:
            return_obj.Role = self.roles.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.description = StructuredText.from_obj(obj.Description)
        return_obj.identity = Identity.from_obj(obj.Identity)
        return_obj.contributing_sources = ContributingSources.from_obj(obj.Contributing_Sources)
        return_obj.roles = _Roles.from_obj(obj.Role)

        if obj.References:
            return_obj.references = obj.References.Reference
        if obj.Time:
            return_obj.time = cybox.common.Time.from_obj(obj.Time)
        if obj.Tools:
            return_obj.tools = cybox.common.ToolInformationList.from_obj(obj.Tools)

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        # To resolve circular dependency
        # TODO: Improve how this extension is handled.

        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        get = dict_repr.get
        return_obj.description = StructuredText.from_dict(get('description'))
        return_obj.references = get('references')
        return_obj.contributing_sources = ContributingSources.from_dict(get('contributing_sources'))
        return_obj.identity = Identity.from_dict(get('identity'))
        return_obj.time = cybox.common.Time.from_dict(get('time'))
        return_obj.tools = cybox.common.ToolInformationList.from_list(get('tools'))
        return_obj.roles = _Roles.from_dict(get('roles'))

        return return_obj

    def to_dict(self):
        return super(InformationSource, self).to_dict()


class ContributingSources(stix.EntityList):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = stix_common_binding
    _binding_class = stix_common_binding.ContributingSourcesType
    _binding_var = "Source"
    _contained_type = InformationSource
    _inner_name = "sources"


# NOT AN ACTUAL STIX TYPE!
class _Roles(stix.TypedList):
    _contained_type = VocabString

    def _fix_value(self, value):
        return vocabs.InformationSourceRole(value)
