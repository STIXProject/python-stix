# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from stix.common import Identity, Statement, StructuredText, VocabString
from stix.common.related import (GenericRelationshipList, RelatedIndicator,
        RelatedThreatActor, RelatedTTP)
from stix.indicator import Indicator
from stix.threat_actor import ThreatActor
from stix.ttp import TTP
import stix.utils

from .time import Time


class IncidentCategory(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IncidentCategoryVocab-1.0'


class Incident(stix.Entity):
    _binding = incident_binding
    _binding_class = _binding.IncidentType
    _namespace = "http://stix.mitre.org/Incident-1"
    _version = "1.1"

    def __init__(self, id_=None, title=None, description=None):
        self.id_ = id_ or stix.utils.create_id("incident")
        self.version = self._version
        self.description = description
        self.title = title
        self.time = None
        self.victims = None
        self.attributed_threat_actors = AttributedThreatActors()
        self.related_indicators = RelatedIndicators()
        self.categories = None
        self.intended_effects = None
        self.leveraged_ttps = LeveragedTTPs()

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
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if value and not isinstance(value, Time):
            raise ValueError("value must be instance of stix.incident.time.Time")

        self._time = value

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

    def add_intended_effect(self, intended_effect):
        if not intended_effect:
            return
        elif isinstance(intended_effect, Statement):
            self._intended_effects.append(intended_effect)
        else:
            self._intended_effects.append(Statement(value=str(intended_effect)))

    @property
    def victims(self):
        return self._victims

    @victims.setter
    def victims(self, value):
        self._victims = []
        if not value:
            return None
        elif isinstance(value, list):
            for v in value:
                self.add_victim(v)
        else:
            self.add_victim(value)

    def add_victim(self, victim):
        if not victim:
            return
        elif isinstance(victim, Identity):
            self.victims.append(victim)
        else:
            self.victims.append(Identity(name=victim))

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        self._categories = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_category(v)
        else:
            self.add_category(value)

    def add_category(self, category):
        if isinstance(category, IncidentCategory):
            self.categories.append(category)
        else:
            cv_item = IncidentCategory(value=category)
            self.categories.append(cv_item)


    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        return_obj.set_id(self.id_)
        return_obj.set_version(self.version)
        return_obj.set_Title(self.title)

        if self.description:
            return_obj.set_Description(self.description.to_obj())
        if self.time:
            return_obj.set_Time(self.time.to_obj())
        if self.victims:
            return_obj.set_Victim([x.to_obj() for x in self.victims])
        if self.attributed_threat_actors:
            return_obj.set_Attributed_Threat_Actors(self.attributed_threat_actors.to_obj())
        if self.related_indicators:
            return_obj.set_Related_Indicators(self.related_indicators.to_obj())
        if self.categories:
            return_obj.set_Categories(self._binding.CategoriesType(Category=[x.to_obj() for x in self.categories]))
        if self.intended_effects:
            return_obj.set_Intended_Effect([x.to_obj() for x in self.intended_effects])
        if self.leveraged_ttps:
            return_obj.set_Leveraged_TTPs(self.leveraged_ttps.to_obj())

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.get_id()
        return_obj.version = obj.get_version() or cls._version
        return_obj.title = obj.get_Title()
        return_obj.description = StructuredText.from_obj(obj.get_Description())
        return_obj.time = Time.from_obj(obj.get_Time())

        if obj.get_Victim():
            return_obj.victims = [Identity.from_obj(x) for x in obj.get_Victim()]

        if obj.get_Categories():
            return_obj.categories = [IncidentCategory.from_obj(x) for x in obj.get_Categories().get_Category()]

        if obj.get_Intended_Effect():
            return_obj.intended_effects = [Statement.from_obj(x) for x in obj.get_Intended_Effect()]

        return_obj.attributed_threat_actors = AttributedThreatActors.from_obj(obj.get_Attributed_Threat_Actors())
        return_obj.related_indicators = RelatedIndicators.from_obj(obj.get_Related_Indicators())
        return_obj.leveraged_ttps = LeveragedTTPs.from_obj(obj.get_Leveraged_TTPs())

        return return_obj

    def to_dict(self):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.version:
            d['version'] = self.version or self._version
        if self.title:
            d['title'] = self.title
        if self.description:
            d['description'] = self.description.to_dict()
        if self.time:
            d['time'] = self.time.to_dict()
        if self.victims:
            d['victims'] = [x.to_dict() for x in self.victims]
        if self.categories:
            d['categories'] = [x.to_dict() for x in self.categories]
        if self.attributed_threat_actors:
            d['attributed_threat_actors'] = self.attributed_threat_actors.to_dict()
        if self.related_indicators:
            d['related_indicators'] = self.related_indicators.to_dict()
        if self.intended_effects:
            d['intended_effects'] = [x.to_dict() for x in self.intended_effects]
        if self.leveraged_ttps:
            d['leveraged_ttps'] = self.leveraged_ttps.to_dict()

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.id_ = dict_repr.get('id')
        return_obj.version = dict_repr.get('version', cls._version)
        return_obj.title = dict_repr.get('title')
        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))
        return_obj.time = Time.from_dict(dict_repr.get('time'))
        return_obj.victims = [Identity.from_dict(x) for x in dict_repr.get('victims', [])]
        return_obj.categories = [IncidentCategory.from_dict(x) for x in dict_repr.get('categories', [])]
        return_obj.attributed_threat_actors = AttributedThreatActors.from_dict(dict_repr.get('attributed_threat_actors'))
        return_obj.related_indicators = RelatedIndicators.from_dict(dict_repr.get('related_indicators'))
        return_obj.intended_effects = [Statement.from_dict(x) for x in dict_repr.get('intended_effects', [])]
        return_obj.leveraged_ttps = LeveragedTTPs.from_dict(dict_repr.get('leveraged_ttps'))

        return return_obj


class AttributedThreatActors(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.AttributedThreatActorsType
    _binding_var = "Threat_Actor"
    _contained_type = RelatedThreatActor
    _inner_name = "threat_actors"

    def __init__(self, threat_actors=None, scope=None):
        if threat_actors is None:
            threat_actors = []
        super(AttributedThreatActors, self).__init__(*threat_actors, scope=scope)


class RelatedIndicators(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedIndicatorsType
    _binding_var = "Related_Indicator"
    _contained_type = RelatedIndicator
    _inner_name = "indicators"

    def __init__(self, indicators=None, scope=None):
        if indicators is None:
            indicators = []
        super(RelatedIndicators, self).__init__(*indicators, scope=scope)


class LeveragedTTPs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.LeveragedTTPsType
    _binding_var = "Leveraged_TTP"
    _contained_type = RelatedTTP
    _inner_name = "ttps"

    def __init__(self, leveraged_ttps=None, scope=None):
        if leveraged_ttps is None:
            leveraged_ttps = []
        super(LeveragedTTPs, self).__init__(*leveraged_ttps, scope=scope)

