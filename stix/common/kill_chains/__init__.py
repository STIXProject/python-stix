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
        self.number_of_phases = None  # can we just do len(self.kill_chain_phases)?
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
    def phase_id(self):
        return self._phase_id

    @phase_id.setter
    def phase_id(self, value):
        self._set_var(basestring, try_cast=False, phase_id=value)

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
        if not isinstance(value, KillChainPhase):
            return super(KillChainPhasesReference, self)._fix_value(value)

        if value.phase_id:
            return KillChainPhaseReference(phase_id=value.phase_id)

        raise ValueError("KillChainPhase must have a phase_id.")


# NOT AN ACTUAL STIX TYPE!
class _KillChainPhases(stix.TypedList):
    _contained_type = KillChainPhase
