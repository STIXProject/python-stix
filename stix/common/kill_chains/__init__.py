# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields
from mixbox import typedlist

# internal
import stix
import stix.bindings.stix_common as common_binding

from mixbox.vendor.six import string_types


class KillChain(stix.Entity):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainType

    id_ = fields.TypedField("id")
    name = fields.TypedField("name")
    definer = fields.TypedField("definer")
    reference = fields.TypedField("reference")
    number_of_phases = fields.TypedField("number_of_phases")
    kill_chain_phases = fields.TypedField("Kill_Chain_Phase", type_="stix.common.kill_chains.KillChainPhase", multiple=True, key_name="kill_chain_phases")

    def __init__(self, id_=None, name=None, definer=None, reference=None):
        super(KillChain, self).__init__()

        self.id_ = id_
        self.name = name
        self.definer = definer
        self.reference = reference
        self.number_of_phases = None  # can we just do len(self.kill_chain_phases)?

    def add_kill_chain_phase(self, value):
        self.kill_chain_phases.append(value)

    def __eq__(self, other):
        if self is other:
            return True

        if not isinstance(other, self.__class__):
            return False

        return other.to_dict() == self.to_dict()

    def __ne__(self, other):
        return not self.__eq__(other)


class KillChains(stix.EntityList):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainsType

    kill_chain = fields.TypedField("Kill_Chain", KillChain, multiple=True, key_name="kill_chains")

    @classmethod
    def _dict_as_list(cls):
        return False


class KillChainPhase(stix.Entity):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainPhaseType

    phase_id = fields.TypedField("phase_id")
    name = fields.TypedField("name")
    ordinality = fields.IntegerField("ordinality")

    def __init__(self, phase_id=None, name=None, ordinality=None):
        super(KillChainPhase, self).__init__()

        self.phase_id = phase_id
        self.name = name
        self.ordinality = ordinality

    def __eq__(self, other):
        if other is self:
            return True

        if not isinstance(other, KillChainPhase):
            return False

        return other.to_dict() == self.to_dict()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        # TODO (bworrell): Is all the tuple(sorted(...))) needed?
        return hash(tuple(sorted(self.to_dict().items())))


class KillChainPhaseReference(KillChainPhase):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainPhaseReferenceType

    kill_chain_id = fields.TypedField("kill_chain_id")
    kill_chain_name = fields.TypedField("kill_chain_name")

    def __init__(self, phase_id=None, name=None, ordinality=None, kill_chain_id=None, kill_chain_name=None):
        super(KillChainPhaseReference, self).__init__(phase_id, name, ordinality)
        self.kill_chain_id = kill_chain_id
        self.kill_chain_name = kill_chain_name


class _KillChainPhaseReferenceList(typedlist.TypedList):
    def __init__(self, *args):
        super(_KillChainPhaseReferenceList, self).__init__(type=KillChainPhaseReference, *args)

    def _fix_value(self, value):
        if not isinstance(value, KillChainPhase):
            return super(_KillChainPhaseReferenceList, self)._fix_value(value)

        if value.phase_id:
            return KillChainPhaseReference(phase_id=value.phase_id)

        raise ValueError("KillChainPhase must have a phase_id.")


class KillChainPhasesReference(stix.EntityList):
    _binding = common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.KillChainPhasesReferenceType

    kill_chain_phase = fields.TypedField(
        name="Kill_Chain_Phase",
        type_=KillChainPhaseReference,
        multiple=True,
        listfunc=_KillChainPhaseReferenceList,
        key_name="kill_chain_phases"
    )

    @classmethod
    def _dict_as_list(cls):
        return False


# NOT AN ACTUAL STIX TYPE!
class _KillChainPhases(stix.TypedList):
    _contained_type = KillChainPhase
