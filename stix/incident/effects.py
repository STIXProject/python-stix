# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import VocabString
from stix.common.vocabs import IncidentEffect
import stix.bindings.incident as incident_binding

class Effects(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.EffectsType

    def __init__(self):
        super(Effects, self).__init__()
        self.effects = None
            
    @property
    def effects(self):
        return self._effects

    @effects.setter
    def effects(self, value):
        self._effects = []

        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_effect(v)
        else:
            self.add_effect(value)

    def add_effect(self, value):
        if not value:
            return
        elif isinstance(value, IncidentEffect):
            self.effects.append(value)
        else:
            effect = IncidentEffect(value)
            self.effects.append(effect)
            
    def to_obj(self):
        obj = self._binding_class()
        if self.effects:
            obj.set_Effect([x.to_obj() for x in self.effects])
        return obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.effects = [IncidentEffect.from_obj(x) for x in obj.get_Effect()]
        return return_obj

    def to_dict(self):    
        d  = {}
        if self.effects:
            d['effects'] = [x.to_dict() for x in self.effects]
        return d

    @classmethod
    def from_dict(cls, dict_, return_obj=None):
        if not dict_:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.effects = [IncidentEffect.from_dict(x) for x in dict_.get('effects')]

        return return_obj
