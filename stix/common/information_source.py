# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

import cybox.common

import stix
import stix.bindings.stix_common as stix_common_binding

from .identity import Identity
from .structured_text import StructuredText


class InformationSource(stix.Entity):
    _binding = stix_common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    
    def __init__(self, identity=None, time=None, tools=None):
        self.description = None
        self.identity = identity
        #self.contributors = []
        self.time = time
        self.tools = tools
        #self.references = []
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if isinstance(value, StructuredText):
            self._description = value
        else:
            self._description = StructuredText(value=value)
            
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
            
        
    def to_obj(self, return_obj=None):
        if return_obj == None:
            return_obj = self._binding.InformationSourceType()

        if self.description is not None:
            return_obj.set_Description(self.description.to_obj())
        
        identity_obj    = self.identity.to_obj() if self.identity else None
        time_obj        = self.time.to_obj() if self.time else None
        tools_obj       = self.tools.to_obj() if self.tools else None
        
        #=======================================================================
        # contributors_obj = stix_common_binding.ContributorsType() if self.contributors else None
        # for contributor in self.contributors:
        #    contributor_obj = contributor.to_obj()
        #    contributors_obj.add_Contributor(contributor_obj)
        # 
        # 
        #    
        # references_obj = stix_common_binding.ReferencesType() if self.references else None
        # for reference in self.references:
        #    reference_obj = reference.to_obj()
        #    references_obj.add_Reference(reference_obj)
        #=======================================================================
        
        
        return_obj.set_Identity(identity_obj)
        return_obj.set_Time(time_obj)
        return_obj.set_Tools(tools_obj)
        #return_obj.set_Contributors(contributors_obj)
        #return_obj.set_References(references_obj)
    
        return return_obj
        
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        # To resolve circular dependency
        # TODO: Improve how this extension is handled.
        import stix.bindings.extensions.identity.ciq_identity_3_0 as ciq_identity_binding
        from stix.extensions.identity import CIQIdentity3_0Instance

        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()

        return_obj.description = StructuredText.from_obj(obj.get_Description())

        if obj.get_Identity():
            identity_obj = obj.get_Identity()
            if isinstance(identity_obj, ciq_identity_binding.CIQIdentity3_0InstanceType):
                return_obj.identity = CIQIdentity3_0Instance.from_obj(identity_obj)
            elif type(identity_obj) == stix_common_binding.IdentityType:
                return_obj.identity = Identity.from_obj(identity_obj)
        
        if obj.get_Time():
            return_obj.time = cybox.common.Time.from_obj(obj.get_Time())
        
        if obj.get_Tools():
            return_obj.tools = cybox.common.ToolInformationList.from_obj(obj.get_Tools())

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        # To resolve circular dependency
        # TODO: Improve how this extension is handled.
        from stix.extensions.identity import CIQIdentity3_0Instance

        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()

        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))

        identity_dict   = dict_repr.get('identity')
        time_dict       = dict_repr.get('time')
        tools_list      = dict_repr.get('tools')

        if identity_dict:
            xsi_type = identity_dict.get('xsi:type')
            if xsi_type:
                type_name = xsi_type.split(":")[1]
                if  type_name == CIQIdentity3_0Instance._XML_TYPE:
                    return_obj.identity = CIQIdentity3_0Instance.from_dict(identity_dict)
                else:
                    raise TypeError('No known class for xsi:type: %s' % (xsi_type))
            else:
                return_obj.identity = Identity.from_dict(identity_dict)
                
        if time_dict:
            return_obj.time = cybox.common.Time.from_dict(time_dict)
        
        if tools_list:
            return_obj.tools = cybox.common.ToolInformationList.from_list(tools_list)

        return return_obj

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}

        if self.description:
            return_dict['description'] = self.description.to_dict()

        if self.identity:
            return_dict['identity'] = self.identity.to_dict()
            
        if self.time:
            return_dict['time']  = self.time.to_dict()
        
        if self.tools:
            return_dict['tools'] = self.tools.to_list()
        
        return return_dict

