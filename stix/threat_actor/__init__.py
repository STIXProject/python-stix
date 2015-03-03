# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils as utils
import stix.bindings.threat_actor as threat_actor_binding
from stix.common import (
    vocabs, Confidence, Identity, InformationSource, Statement,
    StructuredText
)
from stix.common.related import (
    GenericRelationshipList, RelatedCampaign, RelatedPackageRefs, RelatedTTP,
    RelatedThreatActor
)
from stix.data_marking import Marking

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


class ThreatActor(stix.Entity):
    _binding = threat_actor_binding
    _binding_class = threat_actor_binding.ThreatActorType
    _namespace = 'http://stix.mitre.org/ThreatActor-1'
    _version = "1.1.1"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1")

    def __init__(self, id_=None, idref=None, timestamp=None, title=None, description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("threatactor")
        self.idref = idref
        self.version = None
        self.title = title
        self.description = description
        self.short_description = short_description
        self.identity = None
        self.types = None
        self.motivations = None
        self.sophistications = None
        self.intended_effects = None
        self.planning_and_operational_supports = None
        self.handling = None
        self.confidence = None
        self.information_source = None
        self.observed_ttps = ObservedTTPs()
        self.associated_campaigns = AssociatedCampaigns()
        self.associated_actors = AssociatedActors()
        self.related_packages = RelatedPackageRefs()

        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = utils.dates.now() if not idref else None

    @property
    def id_(self):
        return self._id
    
    @id_.setter
    def id_(self, value):
        if not value:
            self._id = None
        else:
            self._id = value
            self.idref = None
    
    @property
    def version(self):
        return self._version
    
    @version.setter
    def version(self, value):
        if not value:
            self._version = None
        else:
            utils.check_version(self._ALL_VERSIONS, value)
            self._version = value
    
    @property
    def idref(self):
        return self._idref
    
    @idref.setter
    def idref(self, value):
        if not value:
            self._idref = None
        else:
            self._idref = value
            self.id_ = None # unset id_ if idref is present
    
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = utils.dates.parse_value(value)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._description = value
            else:
                self._description = StructuredText(value=value)
        else:
            self._description = None

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._short_description = value
            else:
                self._short_description = StructuredText(value=value)
        else:
            self._short_description = None

    @property
    def identity(self):
        return self._identity
    
    @identity.setter
    def identity(self, value):
        if not value:
            self._identity = None
        elif isinstance(value, Identity):
            self._identity = value
        else:
            raise ValueError("identity must be instance of stix.common.Identity")

    @property
    def types(self):
        return self._types
    
    @types.setter
    def types(self, value):
        self._types = Types(value)
            
    def add_type(self, value):
        self.types.append(value)

    @property
    def motivations(self):
        return self._motivations
    
    @motivations.setter
    def motivations(self, value):
        self._motivations = Motivations(value)
            
    def add_motivation(self, value):
        self.motivations.append(value)

    @property
    def sophistications(self):
        return self._sophistications
    
    @sophistications.setter
    def sophistications(self, value):
        self._sophistications = Sophistications(value)
            
    def add_sophistication(self, value):
        self._sophistications.append(value)

    @property
    def intended_effects(self):
        return self._intended_effects
    
    @intended_effects.setter
    def intended_effects(self, value):
        self._intended_effects = IntendedEffects(value)
            
    def add_intended_effect(self, value):
        self.intended_effects.append(value)

    @property
    def planning_and_operational_supports(self):
        return self._planning_and_operational_supports
    
    @planning_and_operational_supports.setter
    def planning_and_operational_supports(self, value):
        self._planning_and_operational_supports = PlanningAndOperationalSupports(value)
            
    def add_planning_and_operational_support(self, value):
        self.planning_and_operational_supports.append(value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(ThreatActor, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.idref = self.idref
        return_obj.version = self.version
        return_obj.Title = self.title

        if self.timestamp:
            return_obj.timestamp = utils.dates.serialize_value(self.timestamp)
        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.short_description:
            return_obj.Short_Description = self.short_description.to_obj(ns_info=ns_info)
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
        if self.information_source:
            return_obj.Information_Source = self.information_source.to_obj(ns_info=ns_info)
        if self.related_packages:
            return_obj.Related_Packages = self.related_packages.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.id
        return_obj.idref = obj.idref
        return_obj.timestamp = obj.timestamp

        if isinstance(obj, cls._binding_class): # ThreatActorType properties
            return_obj.version = obj.version
            return_obj.title = obj.Title
            return_obj.description = StructuredText.from_obj(obj.Description)
            return_obj.short_description = StructuredText.from_obj(obj.Short_Description)
            return_obj.identity = Identity.from_obj(obj.Identity)
            return_obj.types = Types.from_obj(obj.Type)
            return_obj.motivations = Motivations.from_obj(obj.Motivation)
            return_obj.sophistications = Sophistications.from_obj(obj.Sophistication)
            return_obj.intended_effects = IntendedEffects.from_obj( obj.Intended_Effect)
            return_obj.planning_and_operational_supports = \
                PlanningAndOperationalSupports.from_obj(obj.Planning_And_Operational_Support)
            return_obj.observed_ttps = ObservedTTPs.from_obj(obj.Observed_TTPs)
            return_obj.associated_campaigns = AssociatedCampaigns.from_obj(obj.Associated_Campaigns)
            return_obj.associated_actors = AssociatedActors.from_obj(obj.Associated_Actors)
            return_obj.handling = Marking.from_obj(obj.Handling)
            return_obj.confidence = Confidence.from_obj(obj.Confidence)
            return_obj.information_source = InformationSource.from_obj(obj.Information_Source)
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
            
        get = dict_repr.get

        return_obj.id_ = get('id')
        return_obj.idref = get('idref')
        return_obj.timestamp = get('timestamp')
        return_obj.version = get('version')
        return_obj.title = get('title')
        return_obj.description = StructuredText.from_dict(get('description'))
        return_obj.short_description = StructuredText.from_dict(get('short_description'))
        return_obj.identity = Identity.from_dict(get('identity'))
        return_obj.types = Types.from_dict(get('types'))
        return_obj.motivations = Motivations.from_dict(get('motivations'))
        return_obj.sophistications = Sophistications.from_dict(get('sophistications'))
        return_obj.intended_effects = IntendedEffects.from_dict(get('intended_effects'))
        return_obj.planning_and_operational_supports = \
            PlanningAndOperationalSupports.from_dict(get('planning_and_operational_supports'))
        return_obj.observed_ttps = ObservedTTPs.from_dict(get('observed_ttps'))
        return_obj.associated_campaigns = AssociatedCampaigns.from_dict(get('associated_campaigns'))
        return_obj.associated_actors = AssociatedActors.from_dict(get('associated_actors'))
        return_obj.handling = Marking.from_dict(get('handling'))
        return_obj.confidence = Confidence.from_dict(get('confidence'))
        return_obj.information_source = InformationSource.from_dict(get('information_source'))
        return_obj.related_packages = RelatedPackageRefs.from_dict(get('related_packages'))

        return return_obj


class Sophistications(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        sophistication = vocabs.ThreatActorSophistication(value)
        return Statement(value=sophistication)


class Motivations(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        motivation = vocabs.Motivation(value)
        return Statement(value=motivation)


class IntendedEffects(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        intended_effect = vocabs.IntendedEffect(value)
        return Statement(value=intended_effect)


class PlanningAndOperationalSupports(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        pos = vocabs.PlanningAndOperationalSupport(value)
        return Statement(value=pos)


class Types(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        type_ = vocabs.ThreatActorType(value)
        return Statement(value=type_)

