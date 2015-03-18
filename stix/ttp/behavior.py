# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
import stix
import stix.bindings.ttp as ttp_binding

from .malware_instance import MalwareInstance
from .exploit import Exploit
from .attack_pattern import AttackPattern


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
        self._malware_instances = MalwareInstances(value)

    def add_malware_instance(self, malware):
        self.malware_instances.append(malware)

    @property
    def attack_patterns(self):
        return self._attack_patterns

    @attack_patterns.setter
    def attack_patterns(self, value):
        self._attack_patterns = AttackPatterns(value)

    def add_attack_pattern(self, attack_pattern):
        self.attack_patterns.append(attack_pattern)

    @property
    def exploits(self):
        return self._exploits

    @exploits.setter
    def exploits(self, value):
        self._exploits = Exploits(value)

    def add_exploit(self, exploit):
        self.exploits.append(exploit)

    def to_obj(self, return_obj=None, ns_info=None):
        super(Behavior, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.malware_instances:
            return_obj.Malware = self.malware_instances.to_obj(ns_info=ns_info)
        if self.exploits:
            return_obj.Exploits = self.exploits.to_obj(ns_info=ns_info)
        if self.attack_patterns:
            return_obj.Attack_Patterns = self.attack_patterns.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.malware_instances = MalwareInstances.from_obj(obj.Malware)
        return_obj.exploits = Exploits.from_obj(obj.Exploits)
        return_obj.attack_patterns = AttackPatterns.from_obj(obj.Attack_Patterns)

        return return_obj

    def to_dict(self):
        return super(Behavior, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        get = dict_repr.get

        return_obj.malware_instances = MalwareInstances.from_dict(get('malware_instances'))
        return_obj.exploits = Exploits.from_dict(get('exploits'))
        return_obj.attack_patterns = AttackPatterns.from_dict(get('attack_patterns'))

        return return_obj


class Exploits(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _contained_type = Exploit
    _binding = ttp_binding
    _binding_class = _binding.ExploitsType
    _binding_var = "Exploit"
    _inner_name = "exploits"
    _dict_as_list = True


class MalwareInstances(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _contained_type = MalwareInstance
    _binding = ttp_binding
    _binding_class = _binding.MalwareType
    _binding_var = "Malware_Instance"
    _inner_name = "malware_instances"
    _dict_as_list = True


class AttackPatterns(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _contained_type = AttackPattern
    _binding = ttp_binding
    _binding_class = _binding.AttackPatternsType
    _binding_var = "Attack_Pattern"
    _inner_name = "attack_patterns"
    _dict_as_list = True
