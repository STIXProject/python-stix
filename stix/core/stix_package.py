# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
from datetime import datetime

# external
from dateutil.tz import tzutc
from cybox.core import Observables

# internal
import stix
import stix.utils
from stix.utils import dates
from stix.utils import parser
from stix_header import STIXHeader
from stix.campaign import Campaign
from stix.coa import CourseOfAction
from stix.exploit_target import ExploitTarget
from stix.indicator import Indicator
from stix.incident import Incident
from stix.threat_actor import ThreatActor
from stix.common.related import RelatedPackages
from .ttps import TTPs

import stix.bindings.stix_common as stix_common_binding
import stix.bindings.stix_core as stix_core_binding


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
        if isinstance(value, Indicators):
            self._indicators = value
            return

        self._indicators = Indicators()

        if not value:
            return
        elif isinstance(value, (list, tuple)):
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
        if isinstance(value, Campaigns):
            self._campaigns = value
            return

        self._campaigns = Campaigns()

        if not value:
            return
        elif isinstance(value, (list, tuple)):
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
        if isinstance(value, Incidents):
            self._incidents = value
            return

        self._incidents = Incidents()
        
        if not value:
            return
        elif isinstance(value, (list, tuple)):
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
        if isinstance(value, ThreatActors):
            self._threat_actors = value
            return

        self._threat_actors = ThreatActors()
        
        if not value:
            return
        elif isinstance(value, (list, tuple)):
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
        if isinstance(value, CoursesOfAction):
            self._courses_of_action = value
            return

        self._courses_of_action = CoursesOfAction()
        
        if not value:
            return
        elif isinstance(value, (list, tuple)):
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
        if isinstance(value, ExploitTargets):
            self._exploit_targets = value
            return

        self._exploit_targets = ExploitTargets()
        
        if not value:
            return
        elif isinstance(value, (list, tuple)):
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
        if isinstance(value, TTPs):
            self._ttps = value
            return

        if not value:
            self._ttps = TTPs()
        elif isinstance(value, (list, tuple)):
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
   

    def to_obj(self, return_obj=None, ns_info=None):
        super(STIXPackage, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.idref = self.idref
        return_obj.version = self.version
        return_obj.timestamp = dates.serialize_value(self.timestamp)

        if self.stix_header:
            return_obj.STIX_Header = self.stix_header.to_obj(ns_info=ns_info)

        if self.campaigns:
            return_obj.Campaigns = self.campaigns.to_obj(ns_info=ns_info)
            
        if self.courses_of_action:
            return_obj.Courses_Of_Action = self.courses_of_action.to_obj(ns_info=ns_info)
        
        if self.exploit_targets:
            return_obj.Exploit_Targets = self.exploit_targets.to_obj(ns_info=ns_info)
            
        if self.indicators:
            return_obj.Indicators = self.indicators.to_obj(ns_info=ns_info)

        if self.observables:
            return_obj.Observables = self.observables.to_obj(ns_info=ns_info)

        if self.incidents:
            return_obj.Incidents = self.incidents.to_obj(ns_info=ns_info)

        if self.threat_actors:
            return_obj.Threat_Actors = self.threat_actors.to_obj(ns_info=ns_info)
        
        if self.ttps:
            return_obj.TTPs = self.ttps.to_obj(ns_info=ns_info)
           
        if self.related_packages:
            return_obj.Related_Packages = self.related_packages.to_obj(ns_info=ns_info)
             
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
            d['campaigns'] = self.campaigns.to_dict()
        if self.courses_of_action:
            d['courses_of_action'] = self.courses_of_action.to_dict()
        if self.exploit_targets:
            d['exploit_targets'] = self.exploit_targets.to_dict()
        if self.indicators:
            d['indicators'] = self.indicators.to_dict()
        if self.observables:
            d['observables'] = self.observables.to_dict()
        if self.incidents:
            d['incidents'] = self.incidents.to_dict()
        if self.threat_actors:
            d['threat_actors'] = self.threat_actors.to_dict()
        if self.ttps:
            d['ttps'] = self.ttps.to_dict()
        if self.related_packages:
            d['related_packages'] = self.related_packages.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.id
        return_obj.idref = obj.idref
        return_obj.timestamp = obj.timestamp
        return_obj.stix_header = STIXHeader.from_obj(obj.STIX_Header)
        return_obj.related_packages = RelatedPackages.from_obj(obj.Related_Packages)

        if obj.version:
            return_obj.version = obj.version
        if obj.Campaigns:
            return_obj.campaigns = Campaigns.from_obj(obj.Campaigns)
        if obj.Courses_Of_Action:
            return_obj.courses_of_action = CoursesOfAction.from_obj(obj.Courses_Of_Action)
        if obj.Exploit_Targets:
            return_obj.exploit_targets = ExploitTargets.from_obj(obj.Exploit_Targets)
        if obj.Indicators:
            return_obj.indicators = Indicators.from_obj(obj.Indicators)
        if obj.Observables:
            return_obj.observables = Observables.from_obj(obj.Observables)
        if obj.Incidents:
            return_obj.incidents = Incident.from_obj(obj.Incidents)
        if obj.Threat_Actors:
            return_obj.threat_actors = ThreatActors.from_obj(obj.Threat_Actors)
        if obj.TTPs:
            return_obj.ttps = TTPs.from_obj(obj.TTPs)
            
        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = dict_repr.get('id')
        return_obj.idref = dict_repr.get('idref')
        return_obj.timestamp = dict_repr.get('timestamp')
        return_obj.version = dict_repr.get('version', cls._version)
        return_obj.stix_header = STIXHeader.from_dict(dict_repr.get('stix_header'))
        return_obj.campaigns = Campaigns.from_dict(dict_repr.get('campaigns'))
        return_obj.courses_of_action = CoursesOfAction.from_dict(dict_repr.get('courses_of_action'))
        return_obj.exploit_targets = ExploitTargets.from_dict(dict_repr.get('exploit_targets'))
        return_obj.indicators = Indicators.from_dict(dict_repr.get('indicators'))
        return_obj.observables = Observables.from_dict(dict_repr.get('observables'))
        return_obj.incidents = Incidents.from_dict(dict_repr.get('incidents'))
        return_obj.threat_actors = ThreatActors.from_dict(dict_repr.get('threat_actors'))
        return_obj.ttps = TTPs.from_dict(dict_repr.get('ttps'))
        return_obj.related_packages = RelatedPackages.from_dict(dict_repr.get('related_packages'))
        
        return return_obj

    @classmethod
    def from_xml(cls, xml_file, encoding=None):
        """Parses the `xml_file` file-like object and returns a
        :class:`STIXPackage` instance.

        Args:
            xml_file: A file, file-like object, etree._Element, or
                etree._ElementTree instance.
            encoding: The character encoding of the `xml_file` input. If
                ``None``, an attempt will be made to determine the input
                character encoding. Default is ``None``.

        Returns:
            An instance of :class:`STIXPackage`.

        """
        entity_parser = parser.EntityParser()
        return entity_parser.parse_xml(xml_file, encoding=encoding)


class Campaigns(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.CampaignsType
    _contained_type = Campaign
    _binding_var = "Campaign"
    _inner_name = "campaigns"
    _dict_as_list = True


class CoursesOfAction(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.CoursesOfActionType
    _contained_type = CourseOfAction
    _binding_var = "Course_Of_Action"
    _inner_name = "courses_of_action"
    _dict_as_list = True


class ExploitTargets(stix.EntityList):
    _binding = stix_common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.ExploitTargetsType
    _contained_type = ExploitTarget
    _binding_var = "Exploit_Target"
    _inner_name = "exploit_targets"
    _dict_as_list = True


class Incidents(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.IncidentsType
    _contained_type = Incident
    _binding_var = "Incident"
    _inner_name = "incidents"
    _dict_as_list = True


class Indicators(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.IndicatorsType
    _contained_type = Indicator
    _binding_var = "Indicator"
    _inner_name = "indicators"
    _dict_as_list = True


class ThreatActors(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.ThreatActorsType
    _contained_type = ThreatActor
    _binding_var = "Threat_Actor"
    _inner_name = "threat_actors"
    _dict_as_list = True

