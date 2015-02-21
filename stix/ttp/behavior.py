# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
import stix

from .malware_instance import MalwareInstance
from .exploit import Exploit
from .attack_pattern import AttackPattern

import stix.bindings.ttp as ttp_binding

class Behavior(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.BehaviorType
    _namespace = "http://stix.mitre.org/TTP-1"

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
        elif isinstance(value, list):
            for v in value:
                self.add_malware_instance(v)
        else:
            self.add_malware_instance(value)

    def add_malware_instance(self, malware):
        if not malware:
            return
        elif isinstance(malware, MalwareInstance):
            self._malware_instances.append(malware)
        else:
            raise ValueError("Unable to add item to malware instance list: %s" % type(malware))

    @property
    def attack_patterns(self):
        return self._attack_patterns

    @attack_patterns.setter
    def attack_patterns(self, value):
        self._attack_patterns = []

        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_attack_pattern(v)
        else:
            self.add_attack_pattern(value)

    def add_attack_pattern(self, attack_pattern):
        if not attack_pattern:
            return
        elif isinstance(attack_pattern, AttackPattern):
            self.attack_patterns.append(attack_pattern)
        else:
            raise ValueError("Unable to add item to attack pattern list: %s" % type(attack_pattern))

    @property
    def exploits(self):
        return self._exploits

    @exploits.setter
    def exploits(self, value):
        self._exploits = []

        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_exploit(v)
        else:
            self.add_exploit(value)

    def add_exploit(self, exploit):
        if not exploit:
            return
        elif isinstance(exploit, Exploit):
            self._exploits.append(exploit)
        else:
            raise ValueError("Unable to add item to exploit list: %s" % type(exploit))

    def to_obj(self, return_obj=None, ns_info=None):
        super(Behavior, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.malware_instances:
            malware_obj = self._binding.MalwareType(Malware_Instance=[x.to_obj(ns_info=ns_info) for x in self.malware_instances])
            return_obj.Malware = malware_obj
        if self.exploits:
            exploits_obj = self._binding.ExploitsType(Exploit=[x.to_obj(ns_info=ns_info) for x in self.exploits])
            return_obj.Exploits = exploits_obj
        if self.attack_patterns:
            attack_patterns_obj = self._binding.AttackPatternsType(Attack_Pattern=[x.to_obj(ns_info=ns_info) for x in self.attack_patterns])
            return_obj.Attack_Patterns = attack_patterns_obj

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        if obj.Malware:
            return_obj.malware_instances = [MalwareInstance.from_obj(x) for x in obj.Malware.Malware_Instance]
        if obj.Exploits:
            return_obj.exploits = [Exploit.from_obj(x) for x in obj.Exploits.Exploit]
        if obj.Attack_Patterns:
            return_obj.attack_patterns = [AttackPattern.from_obj(x) for x in obj.Attack_Patterns.Attack_Pattern]
        return return_obj

    def to_dict(self):
        d = {}
        if self.malware_instances:
            d['malware_instances'] = [x.to_dict() for x in self.malware_instances]
        if self.exploits:
            d['exploits'] = [x.to_dict() for x in self.exploits]
        if self.attack_patterns:
            d['attack_patterns'] = [x.to_dict() for x in self.attack_patterns]
        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.malware_instances = [MalwareInstance.from_dict(x) for x in dict_repr.get('malware_instances', [])]
        return_obj.exploits = [Exploit.from_dict(x) for x in dict_repr.get('exploits', [])]
        return_obj.attack_patterns = [AttackPattern.from_dict(x) for x in dict_repr.get('attack_patterns', [])]
        return return_obj
