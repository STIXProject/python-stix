# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.ttp import TTP

import stix.bindings.stix_core as core_binding

class TTPs(stix.Entity):
    _binding = core_binding
    _binding_class = _binding.TTPsType
    _namespace = 'http://stix.mitre.org/stix-1'
    
    def __init__(self, ttps=None, kill_chain=None):
        self.ttps = ttps
        #self.kill_chain = kill_chain
        
    @property
    def ttps(self):
        return self._ttps
    
    @ttps.setter
    def ttps(self, value):
        self._ttps = []
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
        
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()
        
        if self.ttps:
            return_obj.set_TTP([x.to_obj() for x in self.ttps])
        
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        if obj.get_TTP():
            return_obj.ttps = [TTP.from_obj(x) for x in obj.get_TTP()]

        return return_obj
    
    def to_dict(self):
        d = {}
        if self.ttps:
            d['ttps'] = [x.to_dict() for x in self.ttps]
        
        return d
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()
        
        return_obj.ttps = [TTP.from_dict(x) for x in dict_repr.get('ttps', [])]
        return return_obj
