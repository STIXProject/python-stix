# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

import cybox.common

import stix
import stix.bindings.stix_common as stix_common_binding
from stix.common import VocabString
from stix.common.vocabs import InformationSourceRole

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
        self._contributing_sources = ContributingSources()
        if not value:
            return
        elif isinstance(value, ContributingSources):
            self._contributing_sources = value
        elif isinstance(value, list):
            for v in value:
                self.add_contributing_source(v)
        else:
            self.add_contributing_source(value)
    
    def add_contributing_source(self, value):
        if not value:
            return
        else:
            self.contributing_sources.append(value) # input checks performed by stix.EntityList
    
    @property
    def references(self):
        return self._references
    
    @references.setter
    def references(self, value):
        self._references = []
        if not value:
            return
        elif isinstance(value, list):
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
        '''Sets the value of the description property.

        If the value is an instance of basestring, it will be coerced into an
        instance of StructuredText, with its 'text' property set to the input
        value.
        '''

        if value and isinstance(value, basestring):
            st = StructuredText()
            st.value = value
            self._description = st
        elif isinstance(value, StructuredText):
            self._description = value
        elif not value:
            self._description = None
        else:
            raise ValueError('value must be instance of StructuredText or basestring')

    @property
    def identity(self):
        return self._identity

    @identity.setter
    def identity(self, value):
        if value and not isinstance(value, Identity):
            raise ValueError('value must be instance of Identity')

        self._identity = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if value and not isinstance(value, cybox.common.Time):
            raise ValueError('value must be instance of Time')

        self._time = value

    @property
    def tools(self):
        return self._tools

    @tools.setter
    def tools(self, value):
        if value and not isinstance(value, cybox.common.ToolInformationList):
            raise ValueError('value must be instance of cybox.common.ToolInformationList')

        self._tools = value

    @property
    def roles(self):
        return self._roles

    @roles.setter
    def roles(self, value):
        self._roles = Roles()

        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_role(v)
        else:
            self.add_role(value)

    def add_role(self, value):
        if not value:
            return
        elif isinstance(value, VocabString):
            self.roles.append(value)
        else:
            role = InformationSourceRole(value)
            self.roles.append(value=role)

    def to_obj(self, return_obj=None, ns_info=None):
        super(InformationSource, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()
            
        if self.description is not None:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.references:
            references_obj = stix_common_binding.ReferencesType(Reference=self.references)
            return_obj.References = references_obj
        if self.contributing_sources:
            return_obj.Contributing_Sources = self.contributing_sources.to_obj(ns_info=ns_info)
        if self.identity:
            return_obj.Identity = self.identity.to_obj(ns_info=ns_info)
        if self.time:
            return_obj.Time = self.time.to_obj(ns_info=ns_info)
        if self.tools:
            return_obj.Tools = self.tools.to_obj(ns_info=ns_info)
        if self.roles:
            return_obj.Role = [x.to_obj(ns_info=ns_info) for x in self.roles]
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
        
        if obj.References:
            return_obj.references = obj.References.Reference
        if obj.Time:
            return_obj.time = cybox.common.Time.from_obj(obj.Time)
        if obj.Tools:
            return_obj.tools = cybox.common.ToolInformationList.from_obj(obj.Tools)
        if obj.Role:
            return_obj.roles = [VocabString.from_obj(x) for x in obj.Role]
        
        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        # To resolve circular dependency
        # TODO: Improve how this extension is handled.

        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))
        return_obj.references = dict_repr.get('references')
        return_obj.contributing_sources = ContributingSources.from_dict(dict_repr.get('contributing_sources'))
        return_obj.identity = Identity.from_dict(dict_repr.get('identity'))
        return_obj.time = cybox.common.Time.from_dict(dict_repr.get('time'))
        return_obj.tools = cybox.common.ToolInformationList.from_list(dict_repr.get('tools'))
        return_obj.roles = [VocabString.from_dict(x) for x in dict_repr.get('roles', [])]

        return return_obj

    def to_dict(self):
        d = {}
        if self.description:
            d['description'] = self.description.to_dict()
        if self.identity:
            d['identity'] = self.identity.to_dict()
        if self.time:
            d['time']  = self.time.to_dict()
        if self.tools:
            d['tools'] = self.tools.to_list()
        if self.references:
            d['references'] = self.references
        if self.contributing_sources:
            d['contributing_sources'] = self.contributing_sources.to_dict()
        if self.roles:
            d['roles'] = [x.to_dict() for x in self.roles]
        return d

class ContributingSources(stix.EntityList):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = stix_common_binding
    _binding_class = stix_common_binding.ContributingSourcesType
    _binding_var = "Source"
    _contained_type = InformationSource
    _inner_name = "sources"


class Roles(stix.EntityList):
    _namespace = "http://stix.mitre.org/common-1"
    _contained_type = VocabString

    def _fix_value(self, value):
        return InformationSourceRole(value)