# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils as utils
from stix.ttp import TTP
from stix.common.kill_chains import KillChains
from stix.bindings import stix_core as core_binding

# deprecation warnings
from stix.utils import deprecated

class TTPs(stix.EntityList):
    _binding = core_binding
    _binding_class = _binding.TTPsType
    _namespace = 'http://stix.mitre.org/stix-1'
    _contained_type = TTP
    _binding_var = "TTP"
    _inner_name = "ttps"
    
    def __init__(self, ttps=None):
        super(TTPs, self).__init__(ttps)
        self.kill_chains = KillChains()

    def __nonzero__(self):
        return super(TTPs, self).__nonzero__() or bool(self.kill_chains)

    @property
    def ttps(self):
        return self._inner
    
    @ttps.setter
    def ttps(self, value):
        self._inner = []

        if utils.is_sequence(value):
            self.extend(value)
        else:
            self.append(value)

    def add_ttp(self, ttp):
        self.append(ttp)

    def _is_valid(self, value):
        deprecated.idref(value)
        return stix.EntityList._is_valid(self, value)

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()
        
        super(TTPs, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        
        if self.kill_chains:
            return_obj.Kill_Chains = self.kill_chains.to_obj(ns_info=ns_info)
        
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):  # noqa
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()
        
        super(TTPs, cls).from_obj(obj, return_obj=return_obj)

        return_obj.kill_chains = KillChains.from_obj(obj.Kill_Chains)

        return return_obj
    
    def to_dict(self):
        return super(TTPs, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):  # noqa
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(TTPs, cls).from_dict(dict_repr, return_obj)

        get = dict_repr.get
        return_obj.kill_chains = KillChains.from_dict(get('kill_chains'))

        return return_obj
