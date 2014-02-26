# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from stix.common.generic_relationship import GenericRelationshipList
from stix.threat_actor import ThreatActor
from stix.common.related import RelatedThreatActor

class AttributedThreatActors(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.AttributedThreatActorsType

    def __init__(self, threat_actors=None, scope=None):
        super(AttributedThreatActors, self).__init__(scope=scope)
        self.threat_actors = threat_actors

    @property
    def threat_actors(self):
        return self._threat_actors

    @threat_actors.setter
    def threat_actors(self, value):
        self._threat_actors = []

        if isinstance(value, list):
            for v in value:
                self.add_threat_actor(v)
        else:
            self.add_threat_actor(value)

    def add_threat_actor(self, threat_actor):
        if not threat_actor:
            return
        elif isinstance(threat_actor, RelatedThreatActor):
            self.threat_actors.append(threat_actor)
        elif isinstance(threat_actor, ThreatActor):
            self.threat_actors.append(RelatedThreatActor(threat_actor=threat_actor))
        else:
            raise ValueError('value must be instance of RelatedThreatActor')

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(AttributedThreatActors, self).to_obj(return_obj)
        return_obj.set_Threat_Actor([x.to_obj() for x in self.threat_actors])
        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(AttributedThreatActors, cls).from_obj(obj, return_obj)

        if obj.get_Threat_Actor():
            return_obj.threat_actors = [RelatedThreatActor.from_obj(x) for x in obj.get_Threat_Actor()]

        return return_obj

    def to_dict(self):
        d = super(AttributedThreatActors, self).to_dict()
        if self.threat_actors:
            d['threat_actors'] = [x.to_dict() for x in self.threat_actors]

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(AttributedThreatActors, cls).from_dict(dict_repr, return_obj)
        return_obj.threat_actors = [RelatedThreatActor.from_dict(x) for x in dict_repr.get('threat_actors', [])]
        return return_obj
