# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix.utils import dates
from stix.utils.parser import EntityParser
from stix_header import STIXHeader
from stix.campaign import Campaign
from stix.coa import CourseOfAction
from stix.exploit_target import ExploitTarget
from stix.indicator import Indicator
from stix.incident import Incident
from stix.threat_actor import ThreatActor
from stix.ttp import TTP
from stix.common.related import RelatedPackages
from .ttps import TTPs
from cybox.core import Observables

import stix.bindings.stix_common as stix_common_binding
import stix.bindings.stix_core as stix_core_binding
import cybox.bindings.cybox_core as cybox_core_binding

from StringIO import StringIO
from datetime import datetime
from dateutil.tz import tzutc

class STIXPackage(stix.Entity):
    _binding = stix_core_binding
    _binding_class = _binding.STIXType
    _namespace = 'http://stix.mitre.org/stix-1'
    _version = "1.1.1"

    def __init__(self, id_=None, idref=None, timestamp=None, stix_header=None, courses_of_action=None, exploit_targets=None, indicators=None, observables=None, incidents=None, threat_actors=None, ttps=None, campaigns=None):
        self.id_ = id_ or stix.utils.create_id("Package")
        self.idref = idref
        self.version = self._version
        self.stix_header = stix_header
        self.campaigns = campaigns
        self.courses_of_action = courses_of_action
        self.exploit_targets = exploit_targets
        self.observables = observables
        self.indicators = indicators
        self.incidents = incidents
        self.threat_actors = threat_actors
        self.ttps = ttps
        self.related_packages = RelatedPackages()
        
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
    def stix_header(self):
        return self._stix_header

    @stix_header.setter
    def stix_header(self, value):
        if value and not isinstance(value, STIXHeader):
            raise ValueError('value must be instance of STIXHeader')

        self._stix_header = value

    @property
    def indicators(self):
        return self._indicators

    @indicators.setter
    def indicators(self, value):
        self._indicators = []

        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_indicator(v)
        else:
            self.add_indicator(value)

    def add_indicator(self, indicator):
        if not indicator:
            return
        elif isinstance(indicator, Indicator):
            self.indicators.append(indicator)
        else:
            raise ValueError('indicator must be instance of stix.indicator.Indicator')

    @property
    def campaigns(self):
        return self._campaigns

    @campaigns.setter
    def campaigns(self, value):
        self._campaigns = []

        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_campaign(v)
        else:
            self.add_campaign(value)

    def add_campaign(self, campaign):
        if not campaign:
            return
        elif isinstance(campaign, Campaign):
            self.campaigns.append(campaign)
        else:
            raise ValueError('indicator must be instance of stix.campaign.Campaign')

    @property
    def observables(self):
        return self._observables

    @observables.setter
    def observables(self, value):
        if value and not isinstance(value, Observables):
            raise ValueError('value must be instance of cybox.core.Observables')

        self._observables = value

    def add_observable(self, observable):
        if not self.observables:
            self.observables = Observables(observables=observable)
        else:
            self.observables.add(observable)


    @property
    def incidents(self):
        return self._incidents
    
    @incidents.setter
    def incidents(self, value):
        self._incidents = []
        
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_incident(v)
        else:
            self.add_incident(value)
    
    def add_incident(self, incident):
        if not incident:
            return
        elif isinstance(incident, Incident):
            self.incidents.append(incident)
        else:
            raise ValueError('Cannot add %s to incident list' % type(incident))

    @property
    def threat_actors(self):
        return self._threat_actors
    
    @threat_actors.setter
    def threat_actors(self, value):
        self._threat_actors = []
        
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_threat_actor(v)
        else:
            self.add_threat_actor(value)

    def add_threat_actor(self, threat_actor):
        if not threat_actor:
            return
        elif isinstance(threat_actor, ThreatActor):
            self._threat_actors.append(threat_actor)
        else:
            raise ValueError('Cannot add %s to threat actor list' % type(threat_actor))

    @property
    def courses_of_action(self):
        return self._courses_of_action
    
    @courses_of_action.setter
    def courses_of_action(self, value):
        self._courses_of_action = []
        
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_course_of_action(v)
        else:
            self.add_course_of_action(value)

    def add_course_of_action(self, course_of_action):
        if not course_of_action:
            return
        elif isinstance(course_of_action, CourseOfAction):
            self._courses_of_action.append(course_of_action)
        else:
            raise ValueError('Cannot add %s to course of action list' % type(course_of_action))

    @property
    def exploit_targets(self):
        return self._exploit_targets
    
    @exploit_targets.setter
    def exploit_targets(self, value):
        self._exploit_targets = []
        
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_exploit_target(v)
        else:
            self.add_exploit_target(value)

    def add_exploit_target(self, exploit_target):
        if not exploit_target:
            return
        elif isinstance(exploit_target, ExploitTarget):
            self._exploit_targets.append(exploit_target)
        else:
            raise ValueError('Cannot add %s to exploit target list' % type(exploit_target))

    @property
    def ttps(self):
        return self._ttps
    
    @ttps.setter
    def ttps(self, value):
        if not value:
            self._ttps = TTPs()
        elif isinstance(value, TTPs):
            self._ttps = value
        elif isinstance(value, list):
            for v in value:
                self.add_ttp(v)
        else:
            self.add_ttp(value)
    
    def add_ttp(self, ttp):
        if not ttp:
            return 
        if not self.ttps:
            self.ttps = TTPs()
        
        self.ttps.append(ttp)
   

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref)
        return_obj.set_version(self.version)
        return_obj.set_timestamp(dates.serialize_value(self.timestamp))

        if self.stix_header:
            return_obj.set_STIX_Header(self.stix_header.to_obj())
        
        if self.campaigns:
            coas_obj = self._binding.CampaignsType()
            coas_obj.set_Campaign([x.to_obj() for x in self.campaigns])
            return_obj.set_Campaigns(coas_obj)
            
        if self.courses_of_action:
            coas_obj = self._binding.CoursesOfActionType()
            coas_obj.set_Course_Of_Action([x.to_obj() for x in self.courses_of_action])
            return_obj.set_Courses_Of_Action(coas_obj)
        
        if self.exploit_targets:
            et_obj = stix_common_binding.ExploitTargetsType()
            et_obj.set_Exploit_Target([x.to_obj() for x in self.exploit_targets])
            return_obj.set_Exploit_Targets(et_obj)
            
        if self.indicators:
            indicators_obj = self._binding.IndicatorsType()
            indicators_obj.set_Indicator([x.to_obj() for x in self.indicators])
            return_obj.set_Indicators(indicators_obj)

        if self.observables:
            return_obj.set_Observables(self.observables.to_obj())

        if self.incidents:
            incidents_obj = self._binding.IncidentsType()
            incidents_obj.set_Incident([x.to_obj() for x in self.incidents])
            return_obj.set_Incidents(incidents_obj)
        if self.threat_actors:
            threat_actors_obj = self._binding.ThreatActorsType()
            threat_actors_obj.set_Threat_Actor([x.to_obj() for x in self.threat_actors])
            return_obj.set_Threat_Actors(threat_actors_obj)
        
        if self.ttps:
            return_obj.set_TTPs(self.ttps.to_obj())
           
        if self.related_packages:
            return_obj.set_Related_Packages(self.related_packages.to_obj())
             
        return return_obj

    def to_dict(self):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.idref:
            d['idref'] = self.idref
        if self.version:
            d['version'] = self.version
        if self.idref:
            d['idref'] = self.idref
        if self.timestamp:
            d['timestamp'] = dates.serialize_value(self.timestamp)
        if self.stix_header:
            d['stix_header'] = self.stix_header.to_dict()
        if self.campaigns:
            d['campaigns'] = [x.to_dict() for x in self.campaigns]
        if self.courses_of_action:
            d['courses_of_action'] = [x.to_dict() for x in self.courses_of_action]
        if self.exploit_targets:
            d['exploit_targets'] = [x.to_dict() for x in self.exploit_targets]
        if self.indicators:
            d['indicators'] = [x.to_dict() for x in self.indicators]
        if self.observables:
            d['observables'] = self.observables.to_dict()
        if self.incidents:
            d['incidents'] = [x.to_dict() for x in self.incidents]
        if self.threat_actors:
            d['threat_actors'] = [x.to_dict() for x in self.threat_actors]
        if self.ttps:
            d['ttps'] = self.ttps.to_dict()
        if self.related_packages:
            d['related_packages'] = self.related_packages.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.get_id()
        return_obj.idref = obj.get_idref()
        return_obj.timestamp = obj.get_timestamp()
        return_obj.stix_header = STIXHeader.from_obj(obj.get_STIX_Header())
        return_obj.related_packages = RelatedPackages.from_obj(obj.get_Related_Packages())

        if obj.get_version():
            return_obj.version = obj.get_version()
        if obj.get_Campaigns():
            return_obj.campaigns = [Campaign.from_obj(x) for x in obj.get_Campaigns().get_Campaign()]
        if obj.get_Courses_Of_Action():
            return_obj.courses_of_action = [CourseOfAction.from_obj(x) for x in obj.get_Courses_Of_Action().get_Course_Of_Action()]
        if obj.get_Exploit_Targets():
            return_obj.exploit_targets = [ExploitTarget.from_obj(x) for x in obj.get_Exploit_Targets().get_Exploit_Target()]
        if obj.get_Indicators():
            return_obj.indicators = [Indicator.from_obj(x) for x in obj.get_Indicators().get_Indicator()]
        if obj.get_Observables():
            return_obj.observables = Observables.from_obj(obj.get_Observables())
        if obj.get_Incidents():
            return_obj.incidents = [Incident.from_obj(x) for x in obj.get_Incidents().get_Incident()]
        if obj.get_Threat_Actors():
            return_obj.threat_actors = [ThreatActor.from_obj(x) for x in obj.get_Threat_Actors().get_Threat_Actor()]
        if obj.get_TTPs():
            return_obj.ttps = TTPs.from_obj(obj.get_TTPs())
            
        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = dict_repr.get('id', None)
        return_obj.idref = dict_repr.get('idref', None)
        return_obj.timestamp = dict_repr.get('timestamp')
        return_obj.version = dict_repr.get('version', cls._version)
        header_dict = dict_repr.get('stix_header', None)
        return_obj.stix_header = STIXHeader.from_dict(header_dict)
        return_obj.campaigns = [Campaign.from_dict(x) for x in dict_repr.get('campaigns', [])]
        return_obj.courses_of_action = [CourseOfAction.from_dict(x) for x in dict_repr.get('courses_of_action', [])]
        return_obj.exploit_targets = [ExploitTarget.from_dict(x) for x in dict_repr.get('exploit_targets', [])]
        return_obj.indicators = [Indicator.from_dict(x) for x in dict_repr.get('indicators', [])]
        return_obj.observables = Observables.from_dict(dict_repr.get('observables'))
        return_obj.incidents = [Incident.from_dict(x) for x in dict_repr.get('incidents', [])]
        return_obj.threat_actors = [ThreatActor.from_dict(x) for x in dict_repr.get('threat_actors', [])]
        return_obj.ttps = TTPs.from_dict(dict_repr.get('ttps'))
        return_obj.related_packages = RelatedPackages.from_dict(dict_repr.get('related_packages'))
        
        return return_obj

    @classmethod
    def from_xml(cls, xml_file):
        parser = EntityParser()
        return parser.parse_xml(xml_file)



