# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from cybox.core import Observables

# internal
import stix
from stix.common import vocabs, VocabString, Identity
import stix.bindings.ttp as ttp_binding
from mixbox import fields

class VictimTargeting(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.VictimTargetingType
    _namespace = "http://stix.mitre.org/TTP-1"

    identity = fields.TypedField("Identity", Identity)
    
    targeted_systems = vocabs.VocabField("Targeted_Systems", vocabs.SystemType, multiple=True)
    targeted_information = vocabs.VocabField("Targeted_Information", vocabs.InformationType, multiple=True)

    def __init__(self):
        super(VictimTargeting, self).__init__()

    def add_targeted_system(self, system):
        self.targeted_systems.append(system)

    def add_targeted_information(self, targeted_information):
        self.targeted_information.append(targeted_information)
