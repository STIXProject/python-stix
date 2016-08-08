# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# mixbox
from mixbox import fields

# internal
import stix
import stix.bindings.threat_actor as threat_actor_binding
from stix.common import vocabs, Confidence, Identity, Statement
from stix.common.related import (
    GenericRelationshipList, RelatedCampaign, RelatedPackageRefs, RelatedTTP,
    RelatedThreatActor
)

from stix.common.statement import StatementField
from stix.common.information_source import InformationSource


class ObservedTTPs(GenericRelationshipList):
    _namespace = 'http://stix.mitre.org/ThreatActor-1'
    _binding = threat_actor_binding
    _binding_class = threat_actor_binding.ObservedTTPsType

    observed_ttp = fields.TypedField("Observed_TTP", RelatedTTP, multiple=True, key_name="ttps")


class AssociatedActors(GenericRelationshipList):
    _namespace = 'http://stix.mitre.org/ThreatActor-1'
    _binding = threat_actor_binding
    _binding_class = threat_actor_binding.AssociatedActorsType

    associated_actor = fields.TypedField("Associated_Actor", RelatedThreatActor, multiple=True, key_name="threat_actors")


class AssociatedCampaigns(GenericRelationshipList):
    _namespace = 'http://stix.mitre.org/ThreatActor-1'
    _binding = threat_actor_binding
    _binding_class = threat_actor_binding.AssociatedCampaignsType

    associated_campaign = fields.TypedField("Associated_Campaign", RelatedCampaign, multiple=True, key_name="campaigns")


class ThreatActor(stix.BaseCoreComponent):
    """Implementation of the STIX Threat Actor.

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
    _binding = threat_actor_binding
    _binding_class = threat_actor_binding.ThreatActorType
    _namespace = 'http://stix.mitre.org/ThreatActor-1'
    _version = "1.2"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1", "1.2")
    _ID_PREFIX = 'threatactor'

    identity = fields.TypedField("Identity", Identity)
    types = StatementField("Type", Statement, vocab_type=vocabs.ThreatActorType, multiple=True, key_name="types")
    motivations = StatementField("Motivation", Statement, vocab_type=vocabs.Motivation, multiple=True, key_name="motivations")
    sophistications = StatementField("Sophistication", Statement, vocab_type=vocabs.ThreatActorSophistication, multiple=True, key_name="sophistications")
    intended_effects = StatementField("Intended_Effect", Statement, vocab_type=vocabs.IntendedEffect, multiple=True, key_name="intended_effects")
    planning_and_operational_supports = StatementField("Planning_And_Operational_Support", Statement, vocab_type=vocabs.PlanningAndOperationalSupport, multiple=True, key_name="planning_and_operational_supports")
    confidence = fields.TypedField("Confidence", Confidence)
    observed_ttps = fields.TypedField("Observed_TTPs", ObservedTTPs)
    associated_campaigns = fields.TypedField("Associated_Campaigns", AssociatedCampaigns)
    associated_actors = fields.TypedField("Associated_Actors", AssociatedActors)
    related_packages = fields.TypedField("Related_Packages", RelatedPackageRefs)
    information_source = fields.TypedField("Information_Source", InformationSource)

    def __init__(self, id_=None, idref=None, timestamp=None, title=None,
                 description=None, short_description=None):

        super(ThreatActor, self).__init__(
            id_=id_,
            idref=idref,
            timestamp=timestamp,
            title=title,
            description=description,
            short_description=short_description
        )

        self.observed_ttps = ObservedTTPs()
        self.associated_campaigns = AssociatedCampaigns()
        self.associated_actors = AssociatedActors()
        self.related_packages = RelatedPackageRefs()
            
    def add_type(self, value):
        """Adds a :class:`.VocabString` object to the :attr:`types` collection.

        If set to a string, an attempt will be made to convert it into an
        instance of :class:`.ThreatActorType`.

        """
        self.types.append(value)
            
    def add_motivation(self, value):
        """Adds a :class:`.Motivation` object to the :attr:`motivations`
        collection.

        """
        self.motivations.append(value)

    def add_sophistication(self, value):
        """Adds a :class:`.VocabString` object to the :attr:`sophistications`
        collection.

        If `value` is a string, an attempt will be made to convert it to an
        instance of :class:`.ThreatActorSophistication`.

        """
        self.sophistications.append(value)
            
    def add_intended_effect(self, value):
        """Adds a :class:`.Statement` object to the :attr:`intended_effects`
        collection.

        If `value` is a string, an attempt will be made to convert it into an
        instance of :class:`.Statement`.

        """
        self.intended_effects.append(value)

    def add_planning_and_operational_support(self, value):
        """Adds a :class:`.VocabString` object to the
        :attr:`planning_and_operational_supports` collection.

        If `value` is a string, an attempt will be made to convert it to an
        instance of :class:`.PlanningAndOperationalSupport`.

        """
        self.planning_and_operational_supports.append(value)
