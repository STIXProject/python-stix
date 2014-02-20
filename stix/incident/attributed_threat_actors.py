# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from stix.common.generic_relationship import GenericRelationshipList
from stix.threat_actor import ThreatActor

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
        elif isinstance(threat_actor, ThreatActor):
            self.threat_actors.append(threat_actor)
        else:
            raise ValueError('value must be instance of ThreatActor')

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
            return_obj.threat_actors = [ThreatActor.from_obj(x) for x in obj.get_Threat_Actor()]

        return return_obj

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}

        super(AttributedThreatActors, self).to_dict(return_dict)

        if self.threat_actors:
            return_dict['threat_actors'] = [x.to_dict() for x in self.threat_actors()]

        return return_dict

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(AttributedThreatActors, cls).from_dict(dict_repr, return_obj)
        return_obj.threat_actors = [ThreatActor.from_dict(x) for x in dict_repr.get('threat_actors', [])]
        return return_obj
