# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.threat_actor as threat_actor_binding
from stix.common import (Confidence, Identity, InformationSource, Statement,
        StructuredText, VocabString)
from stix.common.related import (GenericRelationshipList, RelatedCampaign,
        RelatedPackageRefs, RelatedTTP, RelatedThreatActor)
from stix.data_marking import Marking
import stix.utils
from stix.utils import dates
from datetime import datetime
from dateutil.tz import tzutc
from stix.common.vocabs import (ThreatActorType, Motivation, ThreatActorSophistication,
                                IntendedEffect, PlanningAndOperationalSupport)

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
    _version = "1.1"

    def __init__(self, id_=None, idref=None, timestamp=None, title=None, description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("threatactor")
        self.idref = idref
        self.version = self._version
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
            self.timestamp = datetime.now(tzutc()) if not idref else None

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
        self._timestamp = dates.parse_value(value)

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
        self._types = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_type(v)
        else:
            self.add_type(value)
            
    def add_type(self, value):
        if not value:
            return
        elif isinstance(value, Statement):
            self.types.append(value)
        else:
            type_ = ThreatActorType(value)
            self.types.append(Statement(value=type_))

    @property
    def motivations(self):
        return self._motivations
    
    @motivations.setter
    def motivations(self, value):
        self._motivations = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_motivation(v)
        else:
            self.add_motivation(value)
            
    def add_motivation(self, value):
        if not value:
            return
        elif isinstance(value, Statement):
            self.motivations.append(value)
        else:
            motivation = Motivation(value)
            self.motivations.append(Statement(value=motivation))

    @property
    def sophistications(self):
        return self._sophistications
    
    @sophistications.setter
    def sophistications(self, value):
        self._sophistications = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_sophistication(v)
        else:
            self.add_sophistication(value)
            
    def add_sophistication(self, value):
        if not value:
            return
        elif isinstance(value, Statement):
            self.sophistications.append(value)
        else:
            sophistication = ThreatActorSophistication(value)
            self.sophistications.append(Statement(value=sophistication))

    @property
    def intended_effects(self):
        return self._intended_effects
    
    @intended_effects.setter
    def intended_effects(self, value):
        self._intended_effects = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_intended_effect(v)
        else:
            self.add_intended_effect(value)
            
    def add_intended_effect(self, value):
        if not value:
            return
        elif isinstance(value, Statement):
            self.intended_effects.append(value)
        else:
            intended_effect = IntendedEffect(value)
            self.intended_effects.append(Statement(value=intended_effect))

    @property
    def planning_and_operational_supports(self):
        return self._planning_and_operational_supports
    
    @planning_and_operational_supports.setter
    def planning_and_operational_supports(self, value):
        self._planning_and_operational_supports = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_planning_and_operational_support(v)
        else:
            self.add_planning_and_operational_support(value)
            
    def add_planning_and_operational_support(self, value):
        if not value:
            return
        elif isinstance(value, Statement):
            self.planning_and_operational_supports.append(value)
        else:
            pos = PlanningAndOperationalSupport(value)
            self.planning_and_operational_supports.append(Statement(value=pos))

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref)
        if self.timestamp:
            return_obj.set_timestamp(dates.serialize_value(self.timestamp))
        return_obj.set_version(self.version)
        return_obj.set_Title(self.title)
        if self.description:
            return_obj.set_Description(self.description.to_obj())
        if self.short_description:
            return_obj.set_Short_Description(self.short_description.to_obj())
        if self.identity:
            return_obj.set_Identity(self.identity.to_obj())
        if self.types:
            return_obj.set_Type([x.to_obj() for x in self.types])
        if self.motivations:
            return_obj.set_Motivation([x.to_obj() for x in self.motivations])
        if self.sophistications:
            return_obj.set_Sophistication([x.to_obj() for x in self.sophistications])
        if self.intended_effects:
            return_obj.set_Intended_Effect([x.to_obj() for x in self.intended_effects])
        if self.planning_and_operational_supports:
            return_obj.set_Planning_And_Operational_Support([x.to_obj()
                    for x in self.planning_and_operational_supports])
        if self.observed_ttps:
            return_obj.set_Observed_TTPs(self.observed_ttps.to_obj())
        if self.associated_campaigns:
            return_obj.set_Associated_Campaigns(self.associated_campaigns.to_obj())
        if self.associated_actors:
            return_obj.set_Associated_Actors(self.associated_actors.to_obj())
        if self.handling:
            return_obj.set_Handling(self.handling.to_obj())
        if self.confidence:
            return_obj.set_Confidence(self.confidence.to_obj())
        if self.information_source:
            return_obj.set_Information_Source(self.information_source.to_obj())
        if self.related_packages:
            return_obj.set_Related_Packages(self.related_packages.to_obj())

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.get_id()
        return_obj.idref = obj.get_idref()
        return_obj.timestamp = obj.get_timestamp()
        if isinstance(obj, cls._binding_class): # ThreatActorType properties
            return_obj.version = obj.get_version() if obj.get_version() else cls._version
            return_obj.title = obj.get_Title()
            return_obj.description = StructuredText.from_obj(obj.get_Description())
            return_obj.short_description = StructuredText.from_obj(obj.get_Short_Description())
            return_obj.identity = Identity.from_obj(obj.get_Identity())
            return_obj.types = [Statement.from_obj(x) for x in obj.get_Type()]
            return_obj.motivations = [Statement.from_obj(x) for x in obj.get_Motivation()]
            return_obj.sophistications = [Statement.from_obj(x) for x in obj.get_Sophistication()]
            return_obj.intended_effects = [Statement.from_obj(x) for x in obj.get_Intended_Effect()]
            return_obj.planning_and_operational_supports = [Statement.from_obj(x) for x in obj.get_Planning_And_Operational_Support()]
            return_obj.observed_ttps = ObservedTTPs.from_obj(obj.get_Observed_TTPs())
            return_obj.associated_campaigns = AssociatedCampaigns.from_obj(obj.get_Associated_Campaigns())
            return_obj.associated_actors = AssociatedActors.from_obj(obj.get_Associated_Actors())
            return_obj.handling = Marking.from_obj(obj.get_Handling())
            return_obj.confidence = Confidence.from_obj(obj.get_Confidence())
            return_obj.information_source = InformationSource.from_obj(obj.get_Information_Source())
            return_obj.related_packages = RelatedPackageRefs.from_obj(obj.get_Related_Packages())

        return return_obj

    def to_dict(self):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.idref:
            d['idref'] = self.idref
        if self.timestamp:
            d['timestamp'] = dates.serialize_value(self.timestamp)
        if self.version:
            d['version'] = self.version
        if self.title:
            d['title'] = self.title
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
        if self.identity:
            d['identity'] = self.identity.to_dict()
        if self.types:
            d['types'] = [x.to_dict() for x in self.types]
        if self.motivations:
            d['motivations'] = [x.to_dict() for x in self.motivations]
        if self.sophistications:
            d['sophistications'] = [x.to_dict() for x in self.sophistications]
        if self.intended_effects:
            d['intended_effects'] = [x.to_dict() for x in self.intended_effects]
        if self.planning_and_operational_supports:
            d['planning_and_operational_supports'] = [x.to_dict()
                    for x in self.planning_and_operational_supports]
        if self.observed_ttps:
            d['observed_ttps'] = self.observed_ttps.to_dict()
        if self.associated_campaigns:
            d['associated_campaigns'] = self.associated_campaigns.to_dict()
        if self.associated_actors:
            d['associated_actors'] = self.associated_actors.to_dict()
        if self.handling:
            d['handling'] = self.handling.to_dict()
        if self.confidence:
            d['confidence'] = self.confidence.to_dict()
        if self.information_source:
            d['information_source'] = self.information_source.to_dict()
        if self.related_packages:
            d['related_packages'] = self.related_packages.to_dict()

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.id_ = dict_repr.get('id')
        return_obj.idref = dict_repr.get('idref')
        return_obj.timestamp = dict_repr.get('timestamp')
        return_obj.version = dict_repr.get('version', cls._version)
        return_obj.title = dict_repr.get('title')
        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))
        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))
        return_obj.identity = Identity.from_dict(dict_repr.get('identity'))
        return_obj.types = [Statement.from_dict(x) for x in dict_repr.get('types', [])]
        return_obj.motivations = [Statement.from_dict(x) for x in dict_repr.get('motivations', [])]
        return_obj.sophistications = [Statement.from_dict(x) for x in dict_repr.get('sophistications', [])]
        return_obj.intended_effects = [Statement.from_dict(x) for x in dict_repr.get('intended_effects', [])]
        return_obj.planning_and_operational_supports = [Statement.from_dict(x)
                for x in dict_repr.get('planning_and_operational_supports', [])]
        return_obj.observed_ttps = ObservedTTPs.from_dict(dict_repr.get('observed_ttps'))
        return_obj.associated_campaigns = AssociatedCampaigns.from_dict(dict_repr.get('associated_campaigns'))
        return_obj.associated_actors = AssociatedActors.from_dict(dict_repr.get('associated_actors'))
        return_obj.handling = Marking.from_dict(dict_repr.get('handling'))
        return_obj.confidence = Confidence.from_dict(dict_repr.get('confidence'))
        return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))
        return_obj.related_packages = RelatedPackageRefs.from_dict(dict_repr.get('related_packages'))

        return return_obj
