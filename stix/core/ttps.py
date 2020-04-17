# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# mixbox
from mixbox import fields

# stix
import stix
from stix.ttp import TTP
from stix.common.kill_chains import KillChains
from stix.bindings import stix_core as core_binding


class TTPs(stix.Entity):
    _binding = core_binding
    _binding_class = _binding.TTPsType
    _namespace = 'http://stix.mitre.org/stix-1'

    ttp = fields.TypedField("TTP", TTP, multiple=True, key_name="ttps")
    kill_chains = fields.TypedField("Kill_Chains", KillChains)

    def __init__(self, ttps=None):
        super(TTPs, self).__init__()
        self.ttp = ttps
        self.kill_chains = KillChains()

    def add_ttp(self, ttp):
        self.ttp.append(ttp)
