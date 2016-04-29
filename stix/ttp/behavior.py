# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# mixbox
from mixbox import fields

# stix
import stix
import stix.bindings.ttp as ttp_binding

from .malware_instance import MalwareInstance, MalwareInstanceFactory
from .exploit import Exploit
from .attack_pattern import AttackPattern

class Behavior(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.BehaviorType
    _namespace = "http://stix.mitre.org/TTP-1"

    malware_instances = fields.TypedField("Malware", type_="stix.ttp.behavior.MalwareInstances", key_name="malware_instances")
    attack_patterns = fields.TypedField("Attack_Patterns", type_="stix.ttp.behavior.AttackPatterns")
    exploits = fields.TypedField("Exploits", type_="stix.ttp.behavior.Exploits")

    def __init__(self, malware_instances=None, attack_patterns=None, exploits=None):
        super(Behavior, self).__init__()
        self.malware_instances = malware_instances or MalwareInstances()
        self.attack_patterns = attack_patterns or AttackPatterns()
        self.exploits = exploits or Exploits()


    def add_malware_instance(self, malware):
        self.malware_instances.append(malware)

    def add_attack_pattern(self, attack_pattern):
        self.attack_patterns.append(attack_pattern)

    def add_exploit(self, exploit):
        self.exploits.append(exploit)


class Exploits(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _contained_type = Exploit
    _binding = ttp_binding
    _binding_class = _binding.ExploitsType

    exploit = fields.TypedField("Exploit", Exploit, multiple=True, key_name="exploits")


class MalwareInstances(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _binding = ttp_binding
    _binding_class = _binding.MalwareType

    malware_instance = fields.TypedField("Malware_Instance", MalwareInstance, multiple=True, factory=MalwareInstanceFactory, key_name="malware_instances")


class AttackPatterns(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _binding = ttp_binding
    _binding_class = _binding.AttackPatternsType

    attack_pattern = fields.TypedField("Attack_Pattern", AttackPattern, multiple=True, key_name="attack_patterns")
