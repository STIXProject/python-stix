# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix.bindings.incident as incident_binding
from stix.common.generic_relationship import GenericRelationshipList
from stix.common.related import RelatedThreatActor


class AttributedThreatActors(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.AttributedThreatActorsType
    _binding_var = "Threat_Actor"
    _contained_type = RelatedThreatActor
    _inner_name = "threat_actors"

    def __init__(self, threat_actors=None, scope=None):
        if threat_actors is None:
            threat_actors = []
        super(AttributedThreatActors, self).__init__(*threat_actors, scope=scope)
