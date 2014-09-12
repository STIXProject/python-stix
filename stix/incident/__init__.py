# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


import stix
import stix.bindings.incident as incident_binding
from stix.common import (Identity, Statement, StructuredText, VocabString, 
                         InformationSource, Confidence)
from stix.common.related import (GenericRelationshipList, RelatedIndicator,
        RelatedThreatActor, RelatedTTP, RelatedObservable, RelatedIncident)
from stix.indicator import Indicator
from stix.threat_actor import ThreatActor
from stix.ttp import TTP
from stix.data_marking import Marking
import stix.utils
from stix.utils import dates
from .affected_asset import AffectedAsset
from .property_affected import PropertyAffected
from .time import Time
from .external_id import ExternalID
from .impact_assessment import ImpactAssessment
from .coa import COATaken, COATime, CourseOfAction
from .history import History
from stix.common.vocabs import (IncidentCategory, IntendedEffect, 
                                DiscoveryMethod, SecurityCompromise, 
                                IncidentStatus)

from datetime import datetime
from dateutil.tz import tzutc

class Incident(stix.Entity):
    _binding = incident_binding
    _binding_class = _binding.IncidentType
    _namespace = "http://stix.mitre.org/Incident-1"
    _version = "1.1.1"

    def __init__(self, id_=None, idref=None, timestamp=None, title=None, description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("incident")
        self.idref = idref
        self.version = None # self._version
        self.description = description
        self.short_description = short_description
        self.title = title
        self.status = None
        self.time = None
        self.victims = None
        self.attributed_threat_actors = AttributedThreatActors()
        self.related_indicators = RelatedIndicators()
        self.related_observables = RelatedObservables()
        self.related_incidents = RelatedIncidents()
        self.affected_assets = None
        self.categories = None
        self.intended_effects = None
        self.leveraged_ttps = LeveragedTTPs()
        self.discovery_methods = None
        self.reporter = None
        self.responders = None
        self.coordinators = None
        self.external_ids = None
        self.impact_assessment = None
        self.information_source = None
        self.security_compromise = None
        self.confidence = None
        self.coa_taken = None
        self.handling = None
        self.history = History()
    
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
    def version(self):
        return self._version
    
    @version.setter
    def version(self, value):
        if not value:
            self._version = None
        else:
            if value != Incident._version:
                self._version = value
            else:
                self._version = None
    
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
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if not value:
            self._status = None
        elif isinstance(value, VocabString):
            self._status = value
        else:
            self._status = IncidentStatus(value=value)

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if value and not isinstance(value, Time):
            raise ValueError("value must be instance of stix.incident.time.Time")

        self._time = value

    @property
    def handling(self):
        return self._handling
    
    @handling.setter
    def handling(self, value):
        if not value:
            self._handling = None
        elif isinstance(value, Marking):
            self._handling = value
        else:
            raise ValueError('unable to set handling to type %s' % type(value))
    @property
    def intended_effects(self):
        return self._intended_effects

    @intended_effects.setter
    def intended_effects(self, value):
        self._intended_effects = IntendedEffects()
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
        self._categories = IncidentCategories()
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

    @property
    def affected_assets(self):
        return self._affected_assets
    
    @affected_assets.setter
    def affected_assets(self, value):
        self._affected_assets = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_affected_asset(v)
        else:
            self.add_affected_asset(value)
    
    def add_affected_asset(self, v):
        if not v:
            return
        elif isinstance(v, AffectedAsset):
            self.affected_assets.append(v)
        else:
            raise ValueError('Cannot add type %s to affected asset list' % type(v))

    @property
    def discovery_methods(self):
        return self._discovery_methods

    @discovery_methods.setter
    def discovery_methods(self, value):
        self._discovery_methods = DiscoveryMethods()
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_discovery_method(v)
        else:
            self.add_discovery_method(value)

    def add_discovery_method(self, value):
        if not value:
            return
        elif isinstance(value, VocabString):
            self.discovery_methods.append(value)
        else:
            self.discovery_methods.append(DiscoveryMethod(value))

    @property
    def reporter(self):
        return self._reporter

    @reporter.setter
    def reporter(self, value):
        if not value:
            self._reporter = None
        elif isinstance(value, InformationSource):
            self._reporter = value
        else:
            raise ValueError('value must be instance of InformationSource')

    @property
    def responders(self):
        return self._responders

    @responders.setter
    def responders(self, value):
        self._responders = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_responder(v)
        else:
            self.add_responder(value)

    def add_responder(self, value):
        if not value:
            return
        elif isinstance(value, InformationSource):
            self.responders.append(value)
        else:
            raise ValueError('value must be instance of InformationSource')

    @property
    def coordinators(self):
        return self._coordinators

    @coordinators.setter
    def coordinators(self, value):
        self._coordinators = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_coordinator(v)
        else:
            self.add_coordinator(value)

    def add_coordinator(self, value):
        if not value:
            return
        elif isinstance(value, InformationSource):
            self.coordinators.append(value)
        else:
            raise ValueError('value must be instance of InformationSource')

    @property
    def external_ids(self):
        return self._external_ids

    @external_ids.setter
    def external_ids(self, value):
        self._external_ids = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_external_id(v)
        else:
            self.add_external_id(value)

    def add_external_id(self, value):
        if not value:
            return
        elif isinstance(value, ExternalID):
            self.external_ids.append(value)
        else:
            raise ValueError('value must be instance of ExternalID')

    @property
    def impact_assessment(self):
        return self._impact_assessment

    @impact_assessment.setter
    def impact_assessment(self, value):
        if not value:
            self._impact_assessment = None
        elif isinstance(value, ImpactAssessment):
            self._impact_assessment = value
        else:
            raise ValueError('value must be instance of ImpactAssessment')

    @property
    def information_source(self):
        return self._information_source

    @information_source.setter
    def information_source(self, value):
        if not value:
            self._information_source = None
        elif isinstance(value, InformationSource):
            self._information_source = value
        else:
            raise ValueError('value must be instance of InformationSource')

    @property
    def security_compromise(self):
        return self._security_compromise

    @security_compromise.setter
    def security_compromise(self, value):
        if not value:
            self._security_compromise = None
        elif isinstance(value, VocabString):
            self._security_compromise = value
        else:
            self._security_compromise = SecurityCompromise(value=value)

    @property
    def confidence(self):
        return self._confidence
    
    @confidence.setter
    def confidence(self, value):
        if not value:
            self._confidence = None
        elif isinstance(value, Confidence):
            self._confidence = value
        else:
            self._confidence = Confidence(value)

    @property
    def coa_taken(self):
        return self._coa_taken
    
    @coa_taken.setter
    def coa_taken(self, value):
        self._coa_taken = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_coa_taken(v)
        else:
            self.add_coa_taken(value)

    def add_coa_taken(self, value):
        if isinstance(value, COATaken):
            self.coa_taken.append(value)
        elif isinstance(value, CourseOfAction):
            self.coa_taken.append(COATaken(course_of_action=value))
        else:
            raise ValueError("Cannot add coa_taken of type %s" % type(value))

    def to_obj(self, return_obj=None, ns_info=None):

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.idref = self.idref
        return_obj.timestamp = dates.serialize_value(self.timestamp)
        return_obj.version = self.version
        return_obj.Title = self.title
        
        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.short_description:
            return_obj.Short_Description = self.short_description.to_obj(ns_info=ns_info)
        if self.time:
            return_obj.Time = self.time.to_obj(ns_info=ns_info)
        if self.victims:
            return_obj.Victim = [x.to_obj(ns_info=ns_info) for x in self.victims]
        if self.attributed_threat_actors:
            return_obj.Attributed_Threat_Actors = self.attributed_threat_actors.to_obj(ns_info=ns_info)
        if self.related_indicators:
            return_obj.Related_Indicators = self.related_indicators.to_obj(ns_info=ns_info)
        if self.related_observables:
            return_obj.Related_Observables = self.related_observables.to_obj(ns_info=ns_info)
        if self.related_incidents:
            return_obj.Related_Incidents = self.related_incidents.to_obj(ns_info=ns_info)
        if self.categories:
            return_obj.Categories = self._binding.CategoriesType(Category=[x.to_obj(ns_info=ns_info) for x in self.categories])
        if self.intended_effects:
            return_obj.Intended_Effect = [x.to_obj(ns_info=ns_info) for x in self.intended_effects]
        if self.leveraged_ttps:
            return_obj.Leveraged_TTPs = self.leveraged_ttps.to_obj(ns_info=ns_info)
        if self.affected_assets:
            a = self._binding.AffectedAssetsType(Affected_Asset=[x.to_obj(ns_info=ns_info) for x in self.affected_assets])
            return_obj.Affected_Assets = a
        if self.discovery_methods:
            return_obj.Discovery_Method = [x.to_obj(ns_info=ns_info) for x in self.discovery_methods]
        if self.reporter:
            return_obj.Reporter = self.reporter.to_obj(ns_info=ns_info)
        if self.responders:
            return_obj.Responder = [x.to_obj(ns_info=ns_info) for x in self.responders]
        if self.coordinators:
            return_obj.Coordinator = [x.to_obj(ns_info=ns_info) for x in self.coordinators]
        if self.external_ids:
            return_obj.External_ID = [x.to_obj(ns_info=ns_info) for x in self.external_ids]
        if self.impact_assessment:
            return_obj.Impact_Assessment = self.impact_assessment.to_obj(ns_info=ns_info)
        if self.information_source:
            return_obj.Information_Source = self.information_source.to_obj(ns_info=ns_info)
        if self.security_compromise:
            return_obj.Security_Compromise = self.security_compromise.to_obj(ns_info=ns_info)
        if self.confidence:
            return_obj.Confidence = self.confidence.to_obj(ns_info=ns_info)
        if self.coa_taken:
            return_obj.COA_Taken = [x.to_obj(ns_info=ns_info) for x in self.coa_taken]
        if self.status:
            return_obj.Status = self.status.to_obj(ns_info=ns_info)
        if self.handling:
            return_obj.Handling = self.handling.to_obj(ns_info=ns_info)
        if self.history:
            return_obj.History = self.history.to_obj(ns_info=ns_info)

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
        
        if isinstance(obj, cls._binding_class):
            return_obj.version = obj.version or cls._version
            return_obj.title = obj.Title
            return_obj.description = StructuredText.from_obj(obj.Description)
            return_obj.short_description = StructuredText.from_obj(obj.Short_Description)
            return_obj.time = Time.from_obj(obj.Time)
    
            if obj.Victim:
                return_obj.victims = [Identity.from_obj(x) for x in obj.Victim]
            if obj.Categories:
                return_obj.categories = [IncidentCategory.from_obj(x) for x in obj.Categories.Category]
            if obj.Intended_Effect:
                return_obj.intended_effects = [Statement.from_obj(x) for x in obj.Intended_Effect]
            if obj.Affected_Assets:
                return_obj.affected_assets = [AffectedAsset.from_obj(x) for x in obj.Affected_Assets.Affected_Asset]
            if obj.Discovery_Method:
                return_obj.discovery_methods = [DiscoveryMethod.from_obj(x) for x in obj.Discovery_Method]
            if obj.Reporter:
                return_obj.reporter = InformationSource.from_obj(obj.Reporter)
            if obj.Responder:
                return_obj.responders = [InformationSource.from_obj(x) for x in obj.Responder]
            if obj.Coordinator:
                return_obj.coordinators = [InformationSource.from_obj(x) for x in obj.Coordinator]
            if obj.External_ID:
                return_obj.external_ids = [ExternalID.from_obj(x) for x in obj.External_ID]
            if obj.Impact_Assessment:
                return_obj.impact_assessment = ImpactAssessment.from_obj(obj.Impact_Assessment)
            if obj.Information_Source:
                return_obj.information_source = InformationSource.from_obj(obj.Information_Source)
            if obj.Security_Compromise:
                return_obj.security_compromise = SecurityCompromise.from_obj(obj.Security_Compromise)
            
            return_obj.coa_taken = [COATaken.from_obj(x) for x in obj.COA_Taken]
            return_obj.confidence = Confidence.from_obj(obj.Confidence)
            return_obj.attributed_threat_actors = AttributedThreatActors.from_obj(obj.Attributed_Threat_Actors)
            return_obj.related_indicators = RelatedIndicators.from_obj(obj.Related_Indicators)
            return_obj.related_observables = RelatedObservables.from_obj(obj.Related_Observables)
            return_obj.leveraged_ttps = LeveragedTTPs.from_obj(obj.Leveraged_TTPs)
            return_obj.related_incidents = RelatedIncidents.from_obj(obj.Related_Incidents)
            return_obj.status = VocabString.from_obj(obj.Status)
            return_obj.handling = Marking.from_obj(obj.Handling)
            return_obj.history = History.from_obj(obj.History)
            
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
            d['version'] = self.version or self._version
        if self.title:
            d['title'] = self.title
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
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
        if self.related_observables:
            d['related_observables'] = self.related_observables.to_dict()
        if self.related_incidents:
            d['related_incidents'] = self.related_incidents.to_dict()
        if self.intended_effects:
            d['intended_effects'] = [x.to_dict() for x in self.intended_effects]
        if self.leveraged_ttps:
            d['leveraged_ttps'] = self.leveraged_ttps.to_dict()
        if self.affected_assets:
            d['affected_assets'] = [x.to_dict() for x in self.affected_assets]
        if self.discovery_methods:
            d['discovery_methods'] = [x.to_dict() for x in self.discovery_methods]
        if self.reporter:
            d['reporter'] = self.reporter.to_dict()
        if self.responders:
            d['responders'] = [x.to_dict() for x in self.responders]
        if self.coordinators:
            d['coordinators'] = [x.to_dict() for x in self.coordinators]
        if self.external_ids:
            d['external_ids'] = [x.to_dict() for x in self.external_ids]
        if self.impact_assessment:
            d['impact_assessment'] = self.impact_assessment.to_dict()
        if self.information_source:
            d['information_source'] = self.information_source.to_dict()
        if self.security_compromise:
            d['security_compromise'] = self.security_compromise.to_dict()
        if self.confidence:
            d['confidence'] = self.confidence.to_dict()
        if self.coa_taken:
            d['coa_taken'] = [x.to_dict() for x in self.coa_taken]
        if self.status:
            d['status'] = self.status.to_dict()
        if self.handling:
            d['handling'] = self.handling.to_dict()
        if self.history:
            d['history'] = self.history.to_dict()
        
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
        return_obj.time = Time.from_dict(dict_repr.get('time'))
        return_obj.victims = [Identity.from_dict(x) for x in dict_repr.get('victims', [])]
        return_obj.categories = [IncidentCategory.from_dict(x) for x in dict_repr.get('categories', [])]
        return_obj.attributed_threat_actors = AttributedThreatActors.from_dict(dict_repr.get('attributed_threat_actors'))
        return_obj.related_indicators = RelatedIndicators.from_dict(dict_repr.get('related_indicators'))
        return_obj.related_observables = RelatedObservables.from_dict(dict_repr.get('related_observables'))
        return_obj.related_incidents = RelatedIncidents.from_dict(dict_repr.get('related_incidents'))
        return_obj.intended_effects = [Statement.from_dict(x) for x in dict_repr.get('intended_effects', [])]
        return_obj.leveraged_ttps = LeveragedTTPs.from_dict(dict_repr.get('leveraged_ttps'))
        return_obj.affected_assets = [AffectedAsset.from_dict(x) for x in dict_repr.get('affected_assets', [])]
        return_obj.discovery_methdos = [DiscoveryMethod.from_dict(x) for x in dict_repr.get('discovery_methods', [])]
        return_obj.reporter = InformationSource.from_dict(dict_repr.get('reporter'))
        return_obj.responders = [InformationSource.from_dict(x) for x in dict_repr.get('responders', [])]
        return_obj.coordinators = [InformationSource.from_dict(x) for x in dict_repr.get('coordinators', [])]
        return_obj.external_ids = [ExternalID.from_dict(x) for x in dict_repr.get('external_ids', [])]
        return_obj.impact_assessment = ImpactAssessment.from_dict(dict_repr.get('impact_assessment'))
        return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))
        return_obj.security_compromise = SecurityCompromise.from_dict(dict_repr.get('security_compromise'))
        return_obj.confidence = Confidence.from_dict(dict_repr.get('confidence'))
        return_obj.coa_taken = [COATaken.from_dict(x) for x in dict_repr.get('coa_taken', [])]
        return_obj.status = VocabString.from_dict(dict_repr.get('status'))
        return_obj.handling = Marking.from_obj(dict_repr.get('handling'))
        return_obj.history = History.from_dict(dict_repr.get('history'))
        
        return return_obj


class AttributedThreatActors(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.AttributedThreatActorsType
    _binding_var = "Threat_Actor"
    _contained_type = RelatedThreatActor
    _inner_name = "threat_actors"


class RelatedIndicators(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedIndicatorsType
    _binding_var = "Related_Indicator"
    _contained_type = RelatedIndicator
    _inner_name = "indicators"


class RelatedObservables(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedObservablesType
    _binding_var = "Related_Observable"
    _contained_type = RelatedObservable
    _inner_name = "observables"


class LeveragedTTPs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.LeveragedTTPsType
    _binding_var = "Leveraged_TTP"
    _contained_type = RelatedTTP
    _inner_name = "ttps"
    

class RelatedIncidents(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedIncidentsType
    _binding_var = "Related_Incident"
    _contained_type = RelatedIncident
    _inner_name = "incidents"


class DiscoveryMethods(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _contained_type = VocabString

    def _fix_value(self, value):
        return DiscoveryMethod(value)


class IncidentCategories(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _contained_type = VocabString

    def _fix_value(self, value):
        return IncidentCategory(value)

class IntendedEffects(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _contained_type = Statement

    def _fix_value(self, value):
        return Statement(value=IntendedEffect(value))

