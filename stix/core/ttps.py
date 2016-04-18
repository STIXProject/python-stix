# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
from functools import partial

# mixbox
from mixbox import entities
from mixbox import fields

# stix
import stix
from stix import utils
from stix.ttp import TTP
from stix.common.kill_chains import KillChains
from stix.bindings import stix_core as core_binding

# deprecation warnings
from stix.utils.deprecated import IdrefDeprecatedList


class TTPs(stix.EntityList):
    _binding = core_binding
    _binding_class = _binding.TTPsType
    _namespace = 'http://stix.mitre.org/stix-1'

    ttps = fields.TypedField(
        name="TTP",
        type_=TTP,
        multiple=True,
        key_name="ttps",
        listfunc=partial(IdrefDeprecatedList, type=TTP)
    )

    kill_chains = fields.TypedField("Kill_Chains", KillChains)

    def __init__(self, ttps=None):
        super(TTPs, self).__init__(ttps)
        self.kill_chains = KillChains()

    def add_ttp(self, ttp):
        self.append(ttp)
