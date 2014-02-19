# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.threat_actor import ThreatActor
from . import GenericRelationship
import stix.bindings.stix_common as common_binding

class RelatedThreatActor(GenericRelationship):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.RelatedThreatActorType
    
    def __init__(self, confidence=None, information_source=None, relationship=None, threat_actor=None ):
        super(RelatedThreatActor, self).__init__(confidence=confidence, information_source=information_source, relationship=relationship)
        self.threat_actor = threat_actor
        
    @property
    def threat_actor(self):
        return self._threat_actor
    
    @threat_actor.setter
    def threat_actor(self, value):
        if value and not isinstance(value, ThreatActor):
            raise ValueError("value must be instance of ThreatActor")
        
        self._value = value
        
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
            
        super(RelatedThreatActor, cls).from_obj(obj, return_obj)
        return_obj.threat_actor = ThreatActor.from_obj(obj=obj.get_Threat_Actor())
        return return_obj
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()
        
        super(RelatedThreatActor, self).to_obj(return_obj=return_obj)
        
        if self.threat_actor:
            return_obj.set_Threat_Actor(self.threat_actor.to_obj())
            
        return return_obj
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()
            
        super(RelatedThreatActor, cls).from_dict(dict_repr, return_obj=return_obj)
        return_obj.threat_actor = ThreatActor.from_dict(dict_repr.get('threat_actor'))
    
        return return_obj
    
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
            
        super(RelatedThreatActor, self).to_dict(return_dict=return_dict)
        
        if self.threat_actor:
            return_dict['threat_actor'] = self.threat_actor.to_dict()
        
    