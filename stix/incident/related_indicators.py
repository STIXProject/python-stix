# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix.bindings.incident as incident_binding
from stix.common.generic_relationship import GenericRelationshipList
from stix.common.related import RelatedIndicator


class RelatedIndicators(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedIndicatorsType
    _binding_var = "Related_Indicator"
    _contained_type = RelatedIndicator
    _inner_name = "indicators"

    def __init__(self, indicators=None, scope=None):
        if indicators is None:
            indicators = []
        super(RelatedIndicators, self).__init__(*indicators, scope=scope)
