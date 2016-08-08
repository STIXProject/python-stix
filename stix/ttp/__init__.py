# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
from mixbox import fields

# internal
import stix
import stix.bindings.ttp as ttp_binding
from stix.common import vocabs
from stix.common import Statement
from stix.common.kill_chains import KillChainPhasesReference
from stix.common.related import RelatedPackageRefs
from stix.common.statement import StatementField
from stix.ttp.related_ttps import RelatedTTPs
from stix.ttp.exploit_targets import ExploitTargets

# relative
from .behavior import Behavior
from .resource import Resource
from .victim_targeting import VictimTargeting
from stix.common.information_source import InformationSource


class TTP(stix.BaseCoreComponent):
    """Implementation of the STIX TTP.

    Args:
        id_ (optional): An identifier. If ``None``, a value will be generated
            via ``mixbox.idgen.create_id()``. If set, this will unset the
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

    behavior = fields.TypedField("Behavior", Behavior)
    related_ttps = fields.TypedField("Related_TTPs", RelatedTTPs)
    intended_effects = StatementField("Intended_Effect", Statement, vocab_type=vocabs.IntendedEffect, multiple=True)
    resources = fields.TypedField("Resources", Resource)
    victim_targeting = fields.TypedField("Victim_Targeting", VictimTargeting)
    exploit_targets = fields.TypedField("Exploit_Targets", ExploitTargets)
    related_packages = fields.TypedField("Related_Packages", RelatedPackageRefs)
    kill_chain_phases = fields.TypedField("Kill_Chain_Phases", KillChainPhasesReference)
    information_source = fields.TypedField("Information_Source", InformationSource)

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

        self.related_packages = RelatedPackageRefs()
        self.exploit_targets = ExploitTargets()
        self.related_ttps = RelatedTTPs()
        self.kill_chain_phases = KillChainPhasesReference()


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

    def add_related_package(self, value):
        """Adds a :class:`.RelatedPackageRef` object to the
        :attr:`related_packages` collection.

        Args:
            value: A :class:`.RelatedPackageRef` or a :class:`.STIXPackage`
                object.

        """
        self.related_packages.append(value)

# Avoid circular imports
from .related_ttps import RelatedTTPs
from .exploit_targets import ExploitTargets
