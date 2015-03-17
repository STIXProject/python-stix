# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.bindings.stix_common as common_binding


class KillChain(stix.Entity):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainType
    
    def __init__(self, id_=None, name=None, definer=None, reference=None):
        self.id_ = id_
        self.name = name
        self.definer = definer
        self.reference = reference
        self.number_of_phases = None # can we just do len(self.kill_chain_phases)?
        self.kill_chain_phases = None
    
    @property
    def kill_chain_phases(self):
        return self._kill_chain_phases
    
    @kill_chain_phases.setter
    def kill_chain_phases(self, value):
        self._kill_chain_phases = _KillChainPhases(value)
    
    def add_kill_chain_phase(self, value):
        self.kill_chain_phases.append(value)
    
    def to_obj(self, return_obj=None, ns_info=None):
        super(KillChain, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()
    
        return_obj.id = self.id_
        return_obj.name = self.name
        return_obj.definer = self.definer
        return_obj.reference = self.reference
        return_obj.number_of_phases = self.number_of_phases
        return_obj.Kill_Chain_Phase = self.kill_chain_phases.to_obj(ns_info=ns_info)
    
        return return_obj

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, self.__class__):
            return False

        return other.to_dict() == self.to_dict()

    def __ne__(self, other):
        return not self.__eq__(other)

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
    
        return_obj.id_ = obj.id
        return_obj.name = obj.name
        return_obj.definer = obj.definer
        return_obj.reference = obj.reference
        return_obj.number_of_phases = obj.number_of_phases
        return_obj.kill_chain_phases = _KillChainPhases.from_obj(obj.Kill_Chain_Phase)
    
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()

        get = d.get
        return_obj.id_ = get('id')
        return_obj.name = get('name')
        return_obj.definer = get('definer')
        return_obj.reference = get('reference')
        return_obj.number_of_phases = get('number_of_phases')
        return_obj.kill_chain_phases = \
            _KillChainPhases.from_dict(get('kill_chain_phases'))
    
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
        self.phase_id = phase_id
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
        if not return_obj:
            return_obj = self._binding_class()

        super(KillChainPhase, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        return_obj.phase_id = self.phase_id
        return_obj.name = self.name
        return_obj.ordinality = self.ordinality
    
        return return_obj

    def __eq__(self, other):
        if other is self:
            return True

        if not isinstance(other, KillChainPhase):
            return False

        return other.to_dict() == self.to_dict()

    def __ne__(self, other):
        return not self.__eq__(other)


    def __hash__(self):
        return hash(tuple(sorted(self.to_dict().items())))

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()
    
        return_obj.phase_id = obj.phase_id
        return_obj.name = obj.name
        return_obj.ordinality = obj.ordinality
        
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

    def to_dict(self):
        return super(KillChainPhase, self).to_dict()


class KillChainPhaseReference(KillChainPhase):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainPhaseReferenceType

    def __init__(self, phase_id=None, name=None, ordinality=None, kill_chain_id=None, kill_chain_name=None):
        super(KillChainPhaseReference, self).__init__(phase_id, name, ordinality)
        self.kill_chain_id = kill_chain_id
        self.kill_chain_name = kill_chain_name

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()
    
        super(KillChainPhaseReference, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        return_obj.kill_chain_id = self.kill_chain_id
        return_obj.kill_chain_name = self.kill_chain_name
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
    
        super(KillChainPhaseReference, cls).from_obj(obj, return_obj=return_obj)

        return_obj.kill_chain_id = obj.kill_chain_id
        return_obj.kill_chain_name = obj.kill_chain_name
        return return_obj
    
    def to_dict(self):
        return super(KillChainPhaseReference, self).to_dict()
    
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

    def _fix_value(self, value):
        def is_lmco(phase):
            return phase.phase_id in LMCO_KILL_CHAIN_PHASES_DICT

        if isinstance(value, KillChainPhase) and is_lmco(value):
            return KillChainPhaseReference(
                phase_id=value.phase_id,
                kill_chain_id=LMCO_KILL_CHAIN.id_
            )

        return super(KillChainPhasesReference, self)._fix_value(value)


# NOT AN ACTUAL STIX TYPE!
class _KillChainPhases(stix.TypedList):
    _contained_type = KillChainPhase


LMCO_KILL_CHAIN = None
LMCO_KILL_CHAIN_PHASES = None
LMCO_KILL_CHAIN_PHASES_DICT = None

def __create_lmco():
    global LMCO_KILL_CHAIN, LMCO_KILL_CHAIN_PHASES, LMCO_KILL_CHAIN_PHASES_DICT
    global PHASE_RECONNAISSANCE, PHASE_WEAPONIZE, PHASE_DELIVERY
    global PHASE_EXPLOITATION, PHASE_INSTALLATION, PHASE_COMMAND_AND_CONTROL
    global PHASE_ACTIONS_AND_OBJECTIVES

    if LMCO_KILL_CHAIN:
        return

    PHASE_RECONNAISSANCE = KillChainPhase(
        phase_id="stix:TTP-af1016d6-a744-4ed7-ac91-00fe2272185a",
        name="Reconnaissance",
        ordinality="1"
    )

    PHASE_WEAPONIZE = KillChainPhase(
        phase_id="stix:TTP-445b4827-3cca-42bd-8421-f2e947133c16",
        name="Weaponization",
        ordinality="2"
    )

    PHASE_DELIVERY  = KillChainPhase(
        phase_id="stix:TTP-79a0e041-9d5f-49bb-ada4-8322622b162d",
        name="Delivery",
        ordinality="3"
    )

    PHASE_EXPLOITATION = KillChainPhase(
        phase_id="stix:TTP-f706e4e7-53d8-44ef-967f-81535c9db7d0",
        name="Exploitation",
        ordinality="4"
    )

    PHASE_INSTALLATION  = KillChainPhase(
        phase_id="stix:TTP-e1e4e3f7-be3b-4b39-b80a-a593cfd99a4f",
        name="Installation",
        ordinality="5"
    )

    PHASE_COMMAND_AND_CONTROL = KillChainPhase(
        phase_id="stix:TTP-d6dc32b9-2538-4951-8733-3cb9ef1daae2",
        name="Command and Control",
        ordinality="6"

    )

    PHASE_ACTIONS_AND_OBJECTIVES  = KillChainPhase(
        phase_id="stix:TTP-786ca8f9-2d9a-4213-b38e-399af4a2e5d6",
        name="Actions on Objectives",
        ordinality="7"
    )

    LMCO_KILL_CHAIN_PHASES = (
        PHASE_RECONNAISSANCE, PHASE_WEAPONIZE, PHASE_DELIVERY,
        PHASE_EXPLOITATION, PHASE_INSTALLATION, PHASE_COMMAND_AND_CONTROL,
        PHASE_ACTIONS_AND_OBJECTIVES
    )

    LMCO_KILL_CHAIN = KillChain(
        id_="stix:TTP-af3e707f-2fb9-49e5-8c37-14026ca0a5ff",
        name="LM Cyber Kill Chain",
        definer="LMCO",
        reference="http://www.lockheedmartin.com/content/dam/lockheed/data/corporate/documents/LM-White-Paper-Intel-Driven-Defense.pdf"
    )

    LMCO_KILL_CHAIN.kill_chain_phases.extend(LMCO_KILL_CHAIN_PHASES)

    LMCO_KILL_CHAIN_PHASES_DICT = dict(
        (x.phase_id, x) for x in LMCO_KILL_CHAIN_PHASES
    )

# Set the module-level LMCO Kill Chain object
__create_lmco()
