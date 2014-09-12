# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.ttp import TTP

import stix.bindings.stix_core as core_binding
from stix.common.kill_chains import KillChains

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
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_ttp(v)
        else:
            self.add_ttp(value)
    
    def add_ttp(self, ttp):
        if not ttp:
            return
        elif isinstance(ttp, TTP):
            self.ttps.append(ttp)
        else:
            raise ValueError('Cannot add type %s to ttp list' % type(ttp))
        
    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()
        
        super(TTPs, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        
        if self.kill_chains:
            return_obj.set_Kill_Chains(self.kill_chains.to_obj(ns_info=ns_info))
        
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        super(TTPs, cls).from_obj(obj, return_obj)
        return_obj.kill_chains = KillChains.from_obj(obj.get_Kill_Chains())
        return return_obj
    
    def to_dict(self):
        d = super(TTPs, self).to_dict()
        if self.kill_chains:
            d['kill_chains'] = self.kill_chains.to_dict()
        
        return d
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()
        
        super(TTPs, cls).from_dict(dict_repr, return_obj)
        return_obj.kill_chains = KillChains.from_dict(dict_repr.get('kill_chains'))
        return return_obj
