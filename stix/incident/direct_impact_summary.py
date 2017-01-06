# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
from stix.common import VocabString
from stix.common.vocabs import ImpactRating
import stix.bindings.incident as incident_binding


class DirectImpactSummary(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.DirectImpactSummaryType

    asset_losses = fields.TypedField("Asset_Losses", ImpactRating)
    business_mission_disruption = fields.TypedField("Business_Mission_Disruption", ImpactRating)
    response_and_recovery_costs = fields.TypedField("Response_And_Recovery_Costs", ImpactRating)

    def __init__(self):
        super(DirectImpactSummary, self).__init__()
