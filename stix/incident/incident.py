# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.bindings.incident as incident_binding
from .time import Time
from .attributed_threat_actors import AttributedThreatActors
from .related_indicators import RelatedIndicators
from stix.threat_actor import ThreatActor
from stix.indicator import Indicator
from stix.common import StructuredText
from stix.common import Identity
from cybox.core import Observable, Object
from stix.common import VocabString

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
        self.attributed_threat_actors = None
        self.related_indicators = None
        self.categories = []
        #self.leveraged_ttps = []
        #self.incident_reported = None
        #self.intended_effect = None

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = unicode(value)

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
    def attributed_threat_actors(self):
        return self._attributed_threat_actors

    @attributed_threat_actors.setter
    def attributed_threat_actors(self, value):
        if not value:
            self.attributed_threat_actors = None
        elif isinstance(value, AttributedThreatActors):
            self.attributed_threat_actors = value
        elif isinstance(value, ThreatActor):
            self.attributed_threat_actors = AttributedThreatActors(threat_actors=value)
        else:
            raise ValueError('Cannot cast value to type: AttributedThreatActors')

    @property
    def related_indicators(self):
        return self._related_indicators

    @related_indicators.setter
    def related_indicators(self, value):
        if not value:
            self._related_indicators = None
        elif isinstance(value, RelatedIndicators):
            self._related_indicators = value
        else:
            raise ValueError("Unable to set related_indcators to instance of %s" % type(value))

    @property
    def categories(self):
        return self._categories

    @categories.setter
    def categories(self, value):
        self._catetories = []
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

        return_obj.set_id(self.id)
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
            return_obj.categories = [IncidentCategory.from_obj(x) for x in obj.get_Categories.get_Category()]

        return_obj.attributed_threat_actors = AttributedThreatActors.from_obj(obj.get_Attributed_Threat_Actors())
        return_obj.related_indicators = RelatedIndicators.from_obj(obj.get_Related_Indicators())

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}

        if self.id_:
            return_dict['id'] = self.id_
        if self.version:
            return_dict['version'] = self.version or self._version
        if self.title:
            return_dict['title'] = self.title
        if self.description:
            return_dict['description'] = self.description.to_dict()
        if self.time:
            return_dict['time'] = self.time.to_dict()
        if self.victims:
            return_dict['victims'] = [x.to_dict() for x in self.victims]
        if self.categories:
            return_dict['categories'] = [x.to_dict() for x in self.categories]
        if self.attributed_threat_actors:
            return_dict['attributed_threat_actors'] = self.attributed_threat_actors.to_dict()
        if self.related_indicators:
            return_dict['related_indicators'] = self.related_indicators.to_dict()

        return return_dict

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

        return return_obj
