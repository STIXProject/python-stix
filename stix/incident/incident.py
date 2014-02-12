# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.bindings.incident as incident_binding
from . import time
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
    _namespace = "http://stix.mitre.org/Incident-1"
    
    def __init__(self, id_=None, title=None, description=None):
        self.id_ = id_ or stix.utils.create_id()
        self.description = description
        self.title = title
        self.time = None
        self.victim = None
        self.attributed_threat_actors = []
        self.threat_actors = []
        self.related_indicators = []
        self.leveraged_ttps = []
        self.categories = []
        self.incident_reported = None
        self.intended_effect = None
        
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
        if value and not isinstance(time, time.Time): # try to cast this?
            raise ValueError("value must be instance of stix.incident.time.Time")
    
        self._time = value
        
    @property
    def victim(self):
        return self._victim
    
    @victim.setter
    def victim(self, value):
        if not value:
            return None
        elif isinstance(value, Identity):
            self._victim = value
        else:
            self._victim = Identity(name=value)
    
    def add_related_indicator(self, indicator):
        if isinstance(indicator, Indicator):
            self.related_indicators.append(indicator)
        elif isinstance(indicator, Object):
            object_ = indicator
            tmp_indicator = Indicator()
            tmp_indicator.add_object(object_)
            self.related_indicators.append(tmp_indicator)
        elif isinstance(indicator, Observable):
            obs = indicator
            tmp_indicator = Indicator()
            tmp_indicator.add_observable(obs)
            self.related_indicators.append(tmp_indicator)
        else:
            raise ValueError("Cannot add %s to related_indicators list" % type(indicator))
    
    def add_category(self, category):
        if isinstance(category, IncidentCategory):
            self.categories.append(category)
        else:
            cv_item = IncidentCategory(value=category)
            self.categories.append(cv_item)
    
        
      
    