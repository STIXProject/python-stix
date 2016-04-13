# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from stix.common import vocabs, VocabString
from mixbox import entities, fields

class IndirectImpactSummary(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.IndirectImpactSummaryType

    loss_of_competitive_advantage = vocabs.VocabField("Loss_Of_Competitive_Advantage", vocabs.SecurityCompromise)
    brand_and_market_damage = vocabs.VocabField("Brand_And_Market_Damage", vocabs.SecurityCompromise)
    increased_operating_costs = vocabs.VocabField("Increased_Operating_Costs", vocabs.SecurityCompromise)
    legal_and_regulatory_costs = vocabs.VocabField("Legal_And_Regulatory_Costs", vocabs.SecurityCompromise)

    def __init__(self):
        super(IndirectImpactSummary, self).__init__()
