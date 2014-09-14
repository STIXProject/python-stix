# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common.vocabs import SecurityCompromise
import stix.bindings.incident as incident_binding
from stix.common import VocabString

class IndirectImpactSummary(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.IndirectImpactSummaryType

    def __init__(self):
        super(IndirectImpactSummary, self).__init__()
        self.loss_of_competitive_advantage = None
        self.brand_and_market_damage = None
        self.increased_operating_costs = None
        self.legal_and_regulatory_costs = None

    @property
    def loss_of_competitive_advantage(self):
        return self._loss_of_competitive_advantage

    @loss_of_competitive_advantage.setter
    def loss_of_competitive_advantage(self, value):
        if not value:
            self._loss_of_competitive_advantage = None
        elif isinstance(value, VocabString):
            self._loss_of_competitive_advantage = value
        else:
            self._loss_of_competitive_advantage = SecurityCompromise(value=value)

    @property
    def brand_and_market_damage(self):
        return self._brand_and_market_damage

    @brand_and_market_damage.setter
    def brand_and_market_damage(self, value):
        if not value:
            self._brand_and_market_damage = None
        elif isinstance(value, VocabString):
            self._brand_and_market_damage = value
        else:
            self._brand_and_market_damage = SecurityCompromise(value=value)

    @property
    def increased_operating_costs(self):
        return self._increased_operating_costs

    @increased_operating_costs.setter
    def increased_operating_costs(self, value):
        if not value:
            self._increased_operating_costs = None
        elif isinstance(value, VocabString):
            self._increased_operating_costs = value
        else:
            self._increased_operating_costs = SecurityCompromise(value=value)

    @property
    def legal_and_regulatory_costs(self):
        return self._legal_and_regulatory_costs

    @legal_and_regulatory_costs.setter
    def legal_and_regulatory_costs(self, value):
        if not value:
            self._legal_and_regulatory_costs = None
        elif isinstance(value, VocabString):
            self._legal_and_regulatory_costs = value
        else:
            self._legal_and_regulatory_costs = SecurityCompromise(value=value)
            
    def to_obj(self, return_obj=None, ns_info=None):
        super(IndirectImpactSummary, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        obj = self._binding_class()
        if self.loss_of_competitive_advantage:
            obj.Loss_Of_Competitive_Advantage = self.loss_of_competitive_advantage.to_obj(ns_info=ns_info)
        if self.brand_and_market_damage:
            obj.Brand_And_Market_Damage = self.brand_and_market_damage.to_obj(ns_info=ns_info)
        if self.increased_operating_costs:
            obj.Increased_Operating_Costs = self.increased_operating_costs.to_obj(ns_info=ns_info)
        if self.legal_and_regulatory_costs:
            obj.Legal_And_Regulatory_Costs = self.legal_and_regulatory_costs.to_obj(ns_info=ns_info)
        return obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.loss_of_competitive_advantage = VocabString.from_obj(obj.Loss_Of_Competitive_Advantage)
        return_obj.brand_and_market_damage = VocabString.from_obj(obj.Brand_And_Market_Damage)
        return_obj.increased_operating_costs = VocabString.from_obj(obj.Increased_Operating_Costs)
        return_obj.legal_and_regulatory_costs = VocabString.from_obj(obj.Legal_And_Regulatory_Costs)
        return return_obj

    def to_dict(self):    
        d  = {}
        if self.loss_of_competitive_advantage:
            d['loss_of_competitive_advantage'] = self.loss_of_competitive_advantage.to_dict()
        if self.brand_and_market_damage:
            d['brand_and_market_damage'] = self.brand_and_market_damage.to_dict()
        if self.increased_operating_costs:
            d['increased_operating_costs'] = self.increased_operating_costs.to_dict()
        if self.legal_and_regulatory_costs:
            d['legal_and_regulatory_costs'] = self.legal_and_regulatory_costs.to_dict()
        return d

    @classmethod
    def from_dict(cls, dict_, return_obj=None):
        if not dict_:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.loss_of_competitive_advantage = VocabString.from_dict(dict_.get('loss_of_competitive_advantage'))
        return_obj.brand_and_market_damage = VocabString.from_dict(dict_.get('brand_and_market_damage'))
        return_obj.increased_operating_costs = VocabString.from_dict(dict_.get('increased_operating_costs'))
        return_obj.legal_and_regulatory_costs = VocabString.from_dict(dict_.get('legal_and_regulatory_costs'))

        return return_obj
