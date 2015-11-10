# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from mixbox import entities, fields

class LossEstimation(entities.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.LossEstimationType

    iso_currency_code = fields.TypedField("iso_currency_code")
    amount = fields.TypedField("amount")

    def __init__(self):
        super(LossEstimation, self).__init__()

#     def to_obj(self, return_obj=None, ns_info=None):
#         super(LossEstimation, self).to_obj(return_obj=return_obj, ns_info=ns_info)
# 
#         obj = self._binding_class()
#         if self.amount:
#             obj.amount = self.amount
#         if self.iso_currency_code:
#             obj.iso_currency_code = self.iso_currency_code
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
#         return_obj.amount = obj.amount
#         return_obj.iso_currency_code = obj.iso_currency_code
#         return return_obj
# 
#     def to_dict(self):    
#         return super(LossEstimation, self).to_dict()
# 
#     @classmethod
#     def from_dict(cls, dict_, return_obj=None):
#         if not dict_:
#             return None
# 
#         if not return_obj:
#             return_obj = cls()
# 
#         return_obj.amount = dict_.get('amount')
#         return_obj.iso_currency_code = dict_.get('iso_currency_code')
# 
#         return return_obj
