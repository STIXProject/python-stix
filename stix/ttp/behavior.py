# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
import stix

class Behavior(stix.Entity):
    def __init__(self, malware_instances=None, attack_patterns=None, exploits=None):
        self.malware_instances = malware_instances
        self.attack_patterns = attack_patterns
        self.exploits = exploits
        
    @property
    def malware_instances(self):
        return self._malware_instances
    
    @malware_instances.setter
    def malware_instances(self, value):
        self._malware_instances = []
        
        if not value:
            return
    
    @property
    def attack_patterns(self):
        return self._attack_patterns
    
    @attack_patterns.setter
    def attack_patterns(self, value):
        self._attack_patterns = []
        
        if not value:
            return
    
    @property
    def exploits(self):
        return self._exploits
    
    @exploits.setter
    def exploits(self, value):
        self._exploits = []
    
        if not value:
            return
    
    def to_obj(self, return_obj=None):
        return None
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        return None
    
    def to_dict(self):
        return {}
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        return None