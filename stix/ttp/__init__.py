# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.bindings.ttp as ttp_binding
from stix.common import vocabs, Statement
from stix.common.kill_chains import KillChainPhasesReference
from stix.common.related import RelatedPackageRefs
from stix.ttp.related_ttps import RelatedTTPs
from stix.ttp.exploit_targets import ExploitTargets

# relative
from .behavior import Behavior
from .resource import Resource
from .victim_targeting import VictimTargeting
from stix.base import ElementField
from stix.common.vocabs import IntendedEffect


class TTP(stix.BaseCoreComponent):
    """Implementation of the STIX TTP.

    Args:
        id_ (optional): An identifier. If ``None``, a value will be generated
            via ``stix.utils.create_id()``. If set, this will unset the
            ``idref`` property.
        idref (optional): An identifier reference. If set this will unset the
            ``id_`` property.
        timestamp (optional): A timestamp value. Can be an instance of
            ``datetime.datetime`` or ``str``.
        description: A description of the purpose or intent of this object.
        short_description: A short description of the intent
            or purpose of this object.
        title: The title of this object.

    """
    _binding = ttp_binding
    _binding_class = _binding.TTPType
    _namespace = "http://stix.mitre.org/TTP-1"
    _version = "1.2"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1", "1.2")
    _ID_PREFIX = "ttp"

    behavior = ElementField("Behavior", Behavior)
    related_ttps = ElementField("Related_TTPs", RelatedTTPs)
    intended_effects = ElementField("Intended_Effect", IntendedEffect, multiple=True)
    resources = ElementField("Resources", Resource)
    victim_targeting = ElementField("Victim_Targeting", VictimTargeting)
    exploit_targets = ElementField("Exploit_Targets", ExploitTargets)
    related_packages = ElementField("Related_Pacakges", RelatedPackageRefs)
    kill_chain_phases = ElementField("Kill_Chain_Phases", KillChainPhasesReference)

    def __init__(self, id_=None, idref=None, timestamp=None, title=None,
                 description=None, short_description=None):

        super(TTP, self).__init__(
            id_=id_,
            idref=idref,
            timestamp=timestamp,
            title=title,
            description=description,
            short_description=short_description
        )

        self.behavior = None
        self.related_ttps = None
        self.intended_effects = None
        self.resources = None
        self.victim_targeting = None
        self.related_packages = None
        self.kill_chain_phases = None


    def add_related_ttp(self, value):
        """Adds an Related TTP to the :attr:`related_ttps` list
        property of this :class:`TTP`.

        The `TTP` parameter must be an instance of
        :class:`.RelatedTTP` or :class:`TTP`.

        If the `TTP` parameter is ``None``, no item wil be added to the
        ``related_ttps`` list property.

        Calling this method is the same as calling ``append()`` on the
        ``related_ttps`` property.

        See Also:
            The :class:`RelatedTTPs` documentation.

        Note:
            If the `TTP` parameter is not an instance of
            :class:`.RelatedTTP` an attempt will be
            made to convert it to one.

        Args:
            TTP: An instance of :class:`TTP` or
                :class:`.RelatedTTP`.

        Raises:
            ValueError: If the `TTP` parameter cannot be converted into
                an instance of :class:`.RelatedTTP`

        """
        self.related_ttps.append(value)

    def add_exploit_target(self, value):
        """Adds a :class:`.ExploitTarget` object to the :attr:`exploit_targets`
        collection.

        """
        self.exploit_targets.append(value)

    def add_intended_effect(self, value):
        """Adds a :class:`.Statement` object to the :attr:`intended_effects`
        collection.

        If `value` is a string, an attempt will be made to convert it into an
        instance of :class:`.Statement`.

        """
        self.intended_effects.append(value)

    def add_kill_chain_phase(self, value):
        """Adds a :class:`.KillChainPhaseReference` to the
        :attr:`kill_chain_phases` collection.

        Args:
            value: A :class:`.KillChainPhase`, :class:`.KillChainPhaseReference`
                or a ``str`` representing the phase_id of. Note that you if you
                are defining a custom Kill Chain, you need to add it to the
                STIX package separately.
        """
        self.kill_chain_phases.append(value)

    @property
    def related_packages(self):
        """**DEPRECATED**: A collection of :class:`.RelatedPackageRef`
        objects. This behaves like a ``MutableSequence``.

        """
        return self._related_packages

    @related_packages.setter
    def related_packages(self, value):
        self._related_packages = RelatedPackageRefs(value)

    def add_related_package(self, value):
        """Adds a :class:`.RelatedPackageRef` object to the
        :attr:`related_packages` collection.

        Args:
            value: A :class:`.RelatedPackageRef` or a :class:`.STIXPackage`
                object.

        """
        self.related_packages.append(value)

    """
    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(TTP, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if self.behavior:
            return_obj.Behavior = self.behavior.to_obj(ns_info=ns_info)
        if self.related_ttps:
            return_obj.Related_TTPs = self.related_ttps.to_obj(ns_info=ns_info)
        if self.exploit_targets:
            return_obj.Exploit_Targets = self.exploit_targets.to_obj(ns_info=ns_info)
        if self.intended_effects:
            return_obj.Intended_Effect = self.intended_effects.to_obj(ns_info=ns_info)
        if self.resources:
            return_obj.Resources = self.resources.to_obj(ns_info=ns_info)
        if self.victim_targeting:
            return_obj.Victim_Targeting = self.victim_targeting.to_obj(ns_info=ns_info)
        if self.kill_chain_phases:
            return_obj.Kill_Chain_Phases = self.kill_chain_phases.to_obj(ns_info=ns_info)
        if self.related_packages:
            return_obj.Related_Packages = self.related_packages.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(TTP, cls).from_obj(obj, return_obj=return_obj)

        if isinstance(obj, cls._binding_class):
            return_obj.behavior = Behavior.from_obj(obj.Behavior)
            return_obj.related_ttps = RelatedTTPs.from_obj(obj.Related_TTPs)
            return_obj.exploit_targets = ExploitTargets.from_obj(obj.Exploit_Targets)
            return_obj.resources = Resource.from_obj(obj.Resources)
            return_obj.victim_targeting = VictimTargeting.from_obj(obj.Victim_Targeting)
            return_obj.intended_effects = _IntendedEffects.from_obj(obj.Intended_Effect)
            return_obj.kill_chain_phases = KillChainPhasesReference.from_obj(obj.Kill_Chain_Phases)
            return_obj.related_packages = RelatedPackageRefs.from_obj(obj.Related_Packages)

        return return_obj

    def to_dict(self):
        return super(TTP, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(TTP, cls).from_dict(dict_repr, return_obj=return_obj)

        get = dict_repr.get
        return_obj.behavior = Behavior.from_dict(get('behavior'))
        return_obj.related_ttps = RelatedTTPs.from_dict(get('related_ttps'))
        return_obj.exploit_targets = ExploitTargets.from_dict(get('exploit_targets'))
        return_obj.intended_effects = _IntendedEffects.from_dict(get('intended_effects'))
        return_obj.resources = Resource.from_dict(get('resources'))
        return_obj.victim_targeting = VictimTargeting.from_dict(get('victim_targeting'))
        return_obj.related_packages = RelatedPackageRefs.from_dict(get('related_packages'))
        return_obj.kill_chain_phases = KillChainPhasesReference.from_dict(get('kill_chain_phases'))

        return return_obj
    """

# NOT ACTUAL STIX TYPE
class _IntendedEffects(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        intended_effect = vocabs.IntendedEffect(value)
        return Statement(value=intended_effect)


# Avoid circular imports
from .related_ttps import RelatedTTPs
from .exploit_targets import ExploitTargets
