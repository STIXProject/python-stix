# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.bindings.stix_common as common_binding

class KillChain(stix.Entity):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainType
    
    def __init__(self, id_=None, name=None):
        self.id_ = id_ or stix.utils.create_id("killchain")
        self.name = name
        self.definer = None
        self.reference = None
        self.number_of_phases = None # can we just do len(self.kill_chain_phases)?
        self.kill_chain_phases = None
    
    @property
    def kill_chain_phases(self):
        return self._kill_chain_phases
    
    @kill_chain_phases.setter
    def kill_chain_phases(self, value):
        self._kill_chain_phases = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_kill_chain_phase(v)
        else:
            self.add_kill_chain_phase(value)
    
    def add_kill_chain_phase(self, value):
        if not value:
            return
        elif isinstance(value, KillChainPhase):
            self.kill_chain_phases.append(value)
        else:
            raise ValueError('value must be instance of KillChainPhase')
            
    
    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if not return_obj:
            return_obj = self._binding_class()
    
        return_obj.set_id(self.id_)
        return_obj.set_name(self.name)
        return_obj.set_definer(self.definer)
        return_obj.set_reference(self.reference)
        return_obj.set_number_of_phases(self.number_of_phases)
        
        if self.kill_chain_phases:
            return_obj.set_Kill_Chain_Phase([x.to_obj(ns_info=ns_info) for x in self.kill_chain_phases])
    
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
    
        return_obj.id_ = obj.get_id()
        return_obj.name = obj.get_name()
        return_obj.definer = obj.get_definer()
        return_obj.reference = obj.get_reference()
        return_obj.number_of_phases = obj.get_number_of_phases()
        
        if obj.get_Kill_Chain_Phase():
            return_obj.kill_chain_phases = [KillChainPhase.from_obj(x) for x in obj.get_Kill_Chain_Phase()]
    
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
    
        return_obj.id_ = d.get('id')
        return_obj.name = d.get('name')
        return_obj.definer = d.get('definer')
        return_obj.reference = d.get('reference')
        return_obj.number_of_phases = d.get('number_of_phases')
        return_obj.kill_chain_phases = [KillChainPhase.from_dict(x) for x in d.get('kill_chain_phases', [])]
    
        return return_obj

class KillChains(stix.EntityList):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainsType
    _contained_type = KillChain
    _binding_var = "Kill_Chain"
    _inner_name = "kill_chains"
    

class KillChainPhase(stix.Entity):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainPhaseType
    
    def __init__(self, phase_id=None, name=None, ordinality=None):
        self.phase_id = phase_id or stix.utils.create_id("killchainphase")
        self.name = name
        self.ordinality = ordinality
    
    @property
    def ordinality(self):
        return self._ordinality
    
    @ordinality.setter
    def ordinality(self, value):
        if value is not None:
            self._ordinality = int(value)
        else:
            self._ordinality = None
    
    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if not return_obj:
            return_obj = self._binding_class()
    
        return_obj.set_phase_id(self.phase_id)
        return_obj.set_name(self.name)
        return_obj.set_ordinality(self.ordinality)
    
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
    
        return_obj.phase_id = obj.get_phase_id()
        return_obj.name = obj.get_name()
        return_obj.ordinality = obj.get_ordinality()
        
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
    
        return_obj.phase_id = d.get('phase_id')
        return_obj.name = d.get('name')
        return_obj.ordinality = d.get('ordinality')
        
        return return_obj

class KillChainPhaseReference(KillChainPhase):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainPhaseReferenceType

    def __init__(self, phase_id=None, name=None, ordinality=None, kill_chain_id=None, kill_chain_name=None):
        super(KillChainPhaseReference, self).__init__(phase_id, name, ordinality)
        self.kill_chain_id = kill_chain_id
        self.kill_chain_name = kill_chain_name

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if not return_obj:
            return_obj = self._binding_class()
    
        super(KillChainPhaseReference, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        return_obj.set_kill_chain_id(self.kill_chain_id)
        return_obj.set_kill_chain_name(self.kill_chain_name)
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
    
        super(KillChainPhaseReference, cls).from_obj(obj, return_obj=return_obj)
        return_obj.kill_chain_id = obj.get_kill_chain_id()
        return_obj.kill_chain_name = obj.get_kill_chain_name()
        return return_obj
    
    def to_dict(self):
        d = super(KillChainPhaseReference, self).to_dict()
        if self.kill_chain_id:
            d['kill_chain_id'] = self.kill_chain_id
        if self.kill_chain_name:
            d['kill_chain_name'] = self.kill_chain_name
        return d
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
    
        super(KillChainPhaseReference, cls).from_dict(d, return_obj=return_obj)
        return_obj.kill_chain_id = d.get('kill_chain_id')
        return_obj.kill_chain_name = d.get('kill_chain_name')
        return return_obj

class KillChainPhasesReference(stix.EntityList):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainPhasesReferenceType
    _contained_type = KillChainPhaseReference
    _binding_var = "Kill_Chain_Phase"
    _inner_name = "kill_chain_phases"
    