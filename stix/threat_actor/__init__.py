# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.data_marking import Marking
import stix.bindings.threat_actor as threat_actor_binding
from stix.common import vocabs, Confidence, Identity, Statement
from stix.common.related import (
    GenericRelationshipList, RelatedCampaign, RelatedPackageRefs, RelatedTTP,
    RelatedThreatActor
)


class ObservedTTPs(GenericRelationshipList):
    _namespace = 'http://stix.mitre.org/ThreatActor-1'
    _binding = threat_actor_binding
    _binding_class = threat_actor_binding.ObservedTTPsType
    _binding_var = "Observed_TTP"
    _contained_type = RelatedTTP
    _inner_name = "ttps"


class AssociatedActors(GenericRelationshipList):
    _namespace = 'http://stix.mitre.org/ThreatActor-1'
    _binding = threat_actor_binding
    _binding_class = threat_actor_binding.AssociatedActorsType
    _binding_var = "Associated_Actor"
    _contained_type = RelatedThreatActor
    _inner_name = "threat_actors"


class AssociatedCampaigns(GenericRelationshipList):
    _namespace = 'http://stix.mitre.org/ThreatActor-1'
    _binding = threat_actor_binding
    _binding_class = threat_actor_binding.AssociatedCampaignsType
    _binding_var = "Associated_Campaign"
    _contained_type = RelatedCampaign
    _inner_name = "campaigns"


class ThreatActor(stix.BaseCoreComponent):
    _binding = threat_actor_binding
    _binding_class = threat_actor_binding.ThreatActorType
    _namespace = 'http://stix.mitre.org/ThreatActor-1'
    _version = "1.1.1"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1")
    _ID_PREFIX = 'threatactor'

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

        self.identity = None
        self.types = None
        self.motivations = None
        self.sophistications = None
        self.intended_effects = None
        self.planning_and_operational_supports = None
        self.handling = None
        self.confidence = None
        self.observed_ttps = ObservedTTPs()
        self.associated_campaigns = AssociatedCampaigns()
        self.associated_actors = AssociatedActors()
        self.related_packages = RelatedPackageRefs()

    @property
    def identity(self):
        return self._identity
    
    @identity.setter
    def identity(self, value):
        self._set_var(Identity, try_cast=False, identity=value)

    @property
    def types(self):
        return self._types
    
    @types.setter
    def types(self, value):
        self._types = _Types(value)
            
    def add_type(self, value):
        self.types.append(value)

    @property
    def motivations(self):
        return self._motivations
    
    @motivations.setter
    def motivations(self, value):
        self._motivations = _Motivations(value)
            
    def add_motivation(self, value):
        self.motivations.append(value)

    @property
    def sophistications(self):
        return self._sophistications
    
    @sophistications.setter
    def sophistications(self, value):
        self._sophistications = _Sophistications(value)
            
    def add_sophistication(self, value):
        self._sophistications.append(value)

    @property
    def intended_effects(self):
        return self._intended_effects
    
    @intended_effects.setter
    def intended_effects(self, value):
        self._intended_effects = _IntendedEffects(value)
            
    def add_intended_effect(self, value):
        self.intended_effects.append(value)

    @property
    def planning_and_operational_supports(self):
        return self._planning_and_operational_supports
    
    @planning_and_operational_supports.setter
    def planning_and_operational_supports(self, value):
        self._planning_and_operational_supports = _PlanningAndOperationalSupports(value)
            
    def add_planning_and_operational_support(self, value):
        self.planning_and_operational_supports.append(value)

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(ThreatActor, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if self.identity:
            return_obj.Identity = self.identity.to_obj(ns_info=ns_info)
        if self.types:
            return_obj.Type = self.types.to_obj(ns_info=ns_info)
        if self.motivations:
            return_obj.Motivation = self.motivations.to_obj(ns_info=ns_info)
        if self.sophistications:
            return_obj.Sophistication = self.sophistications.to_obj(ns_info=ns_info)
        if self.intended_effects:
            return_obj.Intended_Effect = self.intended_effects.to_obj(ns_info=ns_info)
        if self.planning_and_operational_supports:
            return_obj.Planning_And_Operational_Support = \
                self.planning_and_operational_supports.to_obj(ns_info=ns_info)
        if self.observed_ttps:
            return_obj.Observed_TTPs = self.observed_ttps.to_obj(ns_info=ns_info)
        if self.associated_campaigns:
            return_obj.Associated_Campaigns = self.associated_campaigns.to_obj(ns_info=ns_info)
        if self.associated_actors:
            return_obj.Associated_Actors = self.associated_actors.to_obj(ns_info=ns_info)
        if self.handling:
            return_obj.Handling = self.handling.to_obj(ns_info=ns_info)
        if self.confidence:
            return_obj.Confidence = self.confidence.to_obj(ns_info=ns_info)
        if self.related_packages:
            return_obj.Related_Packages = self.related_packages.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        super(ThreatActor, cls).from_obj(obj, return_obj=return_obj)

        if isinstance(obj, cls._binding_class):  # ThreatActorType properties
            return_obj.identity = Identity.from_obj(obj.Identity)
            return_obj.types = _Types.from_obj(obj.Type)
            return_obj.motivations = _Motivations.from_obj(obj.Motivation)
            return_obj.sophistications = _Sophistications.from_obj(obj.Sophistication)
            return_obj.intended_effects = _IntendedEffects.from_obj(obj.Intended_Effect)
            return_obj.planning_and_operational_supports = \
                _PlanningAndOperationalSupports.from_obj(obj.Planning_And_Operational_Support)
            return_obj.observed_ttps = ObservedTTPs.from_obj(obj.Observed_TTPs)
            return_obj.associated_campaigns = AssociatedCampaigns.from_obj(obj.Associated_Campaigns)
            return_obj.associated_actors = AssociatedActors.from_obj(obj.Associated_Actors)
            return_obj.handling = Marking.from_obj(obj.Handling)
            return_obj.confidence = Confidence.from_obj(obj.Confidence)
            return_obj.related_packages = RelatedPackageRefs.from_obj(obj.Related_Packages)

        return return_obj

    def to_dict(self):
        return super(ThreatActor, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(ThreatActor, cls).from_dict(dict_repr, return_obj=return_obj)

        get = dict_repr.get
        return_obj.identity = Identity.from_dict(get('identity'))
        return_obj.types = _Types.from_dict(get('types'))
        return_obj.motivations = _Motivations.from_dict(get('motivations'))
        return_obj.sophistications = _Sophistications.from_dict(get('sophistications'))
        return_obj.intended_effects = _IntendedEffects.from_dict(get('intended_effects'))
        return_obj.planning_and_operational_supports = \
            _PlanningAndOperationalSupports.from_dict(get('planning_and_operational_supports'))
        return_obj.observed_ttps = ObservedTTPs.from_dict(get('observed_ttps'))
        return_obj.associated_campaigns = AssociatedCampaigns.from_dict(get('associated_campaigns'))
        return_obj.associated_actors = AssociatedActors.from_dict(get('associated_actors'))
        return_obj.handling = Marking.from_dict(get('handling'))
        return_obj.confidence = Confidence.from_dict(get('confidence'))
        return_obj.related_packages = RelatedPackageRefs.from_dict(get('related_packages'))

        return return_obj


# NOT ACTUAL STIX TYPES!
class _Sophistications(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        sophistication = vocabs.ThreatActorSophistication(value)
        return Statement(value=sophistication)


class _Motivations(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        motivation = vocabs.Motivation(value)
        return Statement(value=motivation)


class _IntendedEffects(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        intended_effect = vocabs.IntendedEffect(value)
        return Statement(value=intended_effect)


class _PlanningAndOperationalSupports(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        pos = vocabs.PlanningAndOperationalSupport(value)
        return Statement(value=pos)


class _Types(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        type_ = vocabs.ThreatActorType(value)
        return Statement(value=type_)
