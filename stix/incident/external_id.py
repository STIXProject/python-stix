# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from mixbox import fields, entities

class ExternalID(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.ExternalIDType

    value = fields.TypedField("valueOf_", key_name="value")
    source = fields.TypedField("source")

    def __init__(self, value=None, source=None):
        super(ExternalID, self).__init__()
        self.value = value
        self.source = source

#     def to_obj(self, return_obj=None, ns_info=None):
#         super(ExternalID, self).to_obj(return_obj=return_obj, ns_info=ns_info)
# 
#         obj = self._binding_class()
#         obj.valueOf_ = self.value
#         obj.source = self.source
#         return obj
# 
#     @classmethod
#     def from_obj(cls, obj, return_obj=None):
#         if not obj:
#             return None
# 
#         if not return_obj:
#             return_obj = cls()
# 
#         return_obj.value = obj.valueOf_
#         return_obj.source = obj.source
#         return return_obj
# 
#     def to_dict(self):    
#         d  = {
#             'value': self.value,
#             'source': self.source
#         }
#         return d
# 
#     @classmethod
#     def from_dict(cls, dict_, return_obj=None):
#         if not dict_:
#             return None
# 
#         if not return_obj:
#             return_obj = cls()
# 
#         if not isinstance(dict_, dict):
#             return_obj.value = dict_
#         else:
#             return_obj.source = dict_.get('source')
#             return_obj.value = dict_.get('value')
# 
#         return return_obj
