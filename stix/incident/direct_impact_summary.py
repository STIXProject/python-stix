# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import VocabString
from stix.common.vocabs import ImpactRating
import stix.bindings.incident as incident_binding
from mixbox import fields, entities

class DirectImpactSummary(entities.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.DirectImpactSummaryType

    asset_losses = fields.TypedField("Asset_Losses", ImpactRating)
    business_mission_disruption = fields.TypedField("Business_Mission_Disruption", ImpactRating)
    response_and_recovery_costs = fields.TypedField("Response_And_Recovery_Costs", ImpactRating)

    def __init__(self):
        super(DirectImpactSummary, self).__init__()
            
#     def to_obj(self, return_obj=None, ns_info=None):
#         super(DirectImpactSummary, self).to_obj(return_obj=return_obj, ns_info=ns_info)
# 
#         obj = self._binding_class()
#         if self.asset_losses:
#             obj.Asset_Losses = self.asset_losses.to_obj(ns_info=ns_info)
#         if self.business_mission_disruption:
#             obj.Business_Mission_Disruption = self.business_mission_disruption.to_obj(ns_info=ns_info)
#         if self.response_and_recovery_costs:
#             obj.Response_And_Recovery_Costs = self.response_and_recovery_costs.to_obj(ns_info=ns_info)
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
#         return_obj.asset_losses = VocabString.from_obj(obj.Asset_Losses)
#         return_obj.business_mission_disruption = VocabString.from_obj(obj.Business_Mission_Disruption)
#         return_obj.response_and_recovery_costs = VocabString.from_obj(obj.Response_And_Recovery_Costs)
#         return return_obj
# 
#     def to_dict(self):    
#         return super(DirectImpactSummary, self).to_dict()
# 
#     @classmethod
#     def from_dict(cls, dict_, return_obj=None):
#         if not dict_:
#             return None
# 
#         if not return_obj:
#             return_obj = cls()
# 
#         return_obj.asset_losses = VocabString.from_dict(dict_.get('asset_losses'))
#         return_obj.business_mission_disruption = VocabString.from_dict(dict_.get('business_mission_disruption'))
#         return_obj.response_and_recovery_costs = VocabString.from_dict(dict_.get('response_and_recovery_costs'))
# 
#         return return_obj
