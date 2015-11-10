# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from stix.common import vocabs, VocabString
from mixbox import entities, fields

class IndirectImpactSummary(entities.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.IndirectImpactSummaryType

    loss_of_competitive_advantage = fields.TypedField("Loss_Of_Competitive_Advantage", vocabs.SecurityCompromise)
    brand_and_market_damage = fields.TypedField("Brand_And_Market_Damage", vocabs.SecurityCompromise)
    increased_operating_costs = fields.TypedField("Increased_Operating_Costs", vocabs.SecurityCompromise)
    legal_and_regulatory_costs = fields.TypedField("Legal_And_Regulatory_Costs", vocabs.SecurityCompromise)

    def __init__(self):
        super(IndirectImpactSummary, self).__init__()

#     def to_obj(self, return_obj=None, ns_info=None):
#         super(IndirectImpactSummary, self).to_obj(return_obj=return_obj, ns_info=ns_info)
# 
#         obj = self._binding_class()
#         if self.loss_of_competitive_advantage:
#             obj.Loss_Of_Competitive_Advantage = self.loss_of_competitive_advantage.to_obj(ns_info=ns_info)
#         if self.brand_and_market_damage:
#             obj.Brand_And_Market_Damage = self.brand_and_market_damage.to_obj(ns_info=ns_info)
#         if self.increased_operating_costs:
#             obj.Increased_Operating_Costs = self.increased_operating_costs.to_obj(ns_info=ns_info)
#         if self.legal_and_regulatory_costs:
#             obj.Legal_And_Regulatory_Costs = self.legal_and_regulatory_costs.to_obj(ns_info=ns_info)
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
#         return_obj.loss_of_competitive_advantage = VocabString.from_obj(obj.Loss_Of_Competitive_Advantage)
#         return_obj.brand_and_market_damage = VocabString.from_obj(obj.Brand_And_Market_Damage)
#         return_obj.increased_operating_costs = VocabString.from_obj(obj.Increased_Operating_Costs)
#         return_obj.legal_and_regulatory_costs = VocabString.from_obj(obj.Legal_And_Regulatory_Costs)
#         return return_obj
# 
#     def to_dict(self):    
#         return super(IndirectImpactSummary, self).to_dict()
# 
#     @classmethod
#     def from_dict(cls, dict_, return_obj=None):
#         if not dict_:
#             return None
# 
#         if not return_obj:
#             return_obj = cls()
# 
#         return_obj.loss_of_competitive_advantage = VocabString.from_dict(dict_.get('loss_of_competitive_advantage'))
#         return_obj.brand_and_market_damage = VocabString.from_dict(dict_.get('brand_and_market_damage'))
#         return_obj.increased_operating_costs = VocabString.from_dict(dict_.get('increased_operating_costs'))
#         return_obj.legal_and_regulatory_costs = VocabString.from_dict(dict_.get('legal_and_regulatory_costs'))
# 
#         return return_obj
