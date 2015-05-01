# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from cybox.core import Observable, Observables

# base
import stix

# utility imports
import stix.utils as utils
import stix.utils.parser as parser

# component imports
from stix.campaign import Campaign
from stix.coa import CourseOfAction
from stix.exploit_target import ExploitTarget
from stix.indicator import Indicator
from stix.incident import Incident
from stix.threat_actor import ThreatActor
from stix.ttp import TTP
from stix.report import Report

# relationship imports
from stix.common.related import RelatedPackages

# relative imports
from .stix_header import STIXHeader
from .ttps import TTPs
from . import (Campaigns, CoursesOfAction, ExploitTargets, Incidents,
               Indicators, ThreatActors, Reports)

# binding imports
import stix.bindings.stix_core as stix_core_binding


class STIXPackage(stix.Entity):
    _binding = stix_core_binding
    _binding_class = _binding.STIXType
    _namespace = 'http://stix.mitre.org/stix-1'
    _version = "1.2"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1", "1.2")

    def __init__(self, id_=None, idref=None, timestamp=None, stix_header=None,
                 courses_of_action=None, exploit_targets=None, indicators=None,
                 observables=None, incidents=None, threat_actors=None,
                 ttps=None, campaigns=None, related_packages=None,
                 reports=None):
        
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
        self.related_packages = related_packages
        self.reports = reports
        
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
    def idref(self):
        return self._idref
    
    @idref.setter
    def idref(self, value):
        if not value:
            self._idref = None
        else:
            self._idref = value
            self.id_ = None  # unset id_ if idref is present
    
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = utils.dates.parse_value(value)

    @property
    def stix_header(self):
        return self._stix_header

    @stix_header.setter
    def stix_header(self, value):
        self._set_var(STIXHeader, try_cast=False, stix_header=value)

    @property
    def indicators(self):
        return self._indicators

    @indicators.setter
    def indicators(self, value):
        self._indicators = Indicators(value)

    def add_indicator(self, indicator):
        self.indicators.append(indicator)

    @property
    def campaigns(self):
        return self._campaigns

    @campaigns.setter
    def campaigns(self, value):
        self._campaigns = Campaigns(value)

    def add_campaign(self, campaign):
        self.campaigns.append(campaign)

    @property
    def observables(self):
        return self._observables

    @observables.setter
    def observables(self, value):
        self._set_var(Observables, observables=value)

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
        self._incidents = Incidents(value)
    
    def add_incident(self, incident):
        self.incidents.append(incident)

    @property
    def threat_actors(self):
        return self._threat_actors
    
    @threat_actors.setter
    def threat_actors(self, value):
        self._threat_actors = ThreatActors(value)

    def add_threat_actor(self, threat_actor):
        self._threat_actors.append(threat_actor)

    @property
    def courses_of_action(self):
        return self._courses_of_action
    
    @courses_of_action.setter
    def courses_of_action(self, value):
        self._courses_of_action = CoursesOfAction(value)

    def add_course_of_action(self, course_of_action):
        self._courses_of_action.append(course_of_action)

    @property
    def exploit_targets(self):
        return self._exploit_targets
    
    @exploit_targets.setter
    def exploit_targets(self, value):
        self._exploit_targets = ExploitTargets(value)

    def add_exploit_target(self, exploit_target):
        self._exploit_targets.append(exploit_target)

    @property
    def ttps(self):
        return self._ttps
    
    @ttps.setter
    def ttps(self, value):
        if isinstance(value, TTPs):
            self._ttps = value
        else:
            self._ttps = TTPs(value)
    
    def add_ttp(self, ttp):
        self.ttps.append(ttp)

    @property
    def reports(self):
        return self._reports

    @reports.setter
    def reports(self, value):
        self._reports = Reports(value)

    def add_report(self, report):
        self.reports.append(report)

    @property
    def related_packages(self):
        return self._related_packages

    @related_packages.setter
    def related_packages(self, value):
        if isinstance(value, RelatedPackages):
            self._related_packages = value
        else:
            self._related_packages = RelatedPackages(value)

    def add_related_package(self, related_package):
        self.related_packages.append(related_package)

    def add(self, entity):
        """Adds `entity` to a top-level collection. For example, if `entity` is
        an Indicator object, the `entity` will be added to the ``indicators``
        top-level collection.

        """
        if utils.is_cybox(entity):
            self.add_observable(entity)
            return

        tlo_adds = {
            Campaign: self.add_campaign,
            CourseOfAction: self.add_course_of_action,
            ExploitTarget: self.add_exploit_target,
            Incident: self.add_incident,
            Indicator: self.add_indicator,
            ThreatActor: self.add_threat_actor,
            TTP: self.add_threat_actor,
            Report: self.add_report,
            Observable: self.add_observable,
        }

        try:
            add = tlo_adds[entity.__class__]
            add(entity)
        except KeyError:
            error = "Cannot add type '{0}' to a top-level collection"
            error = error.format(type(entity))
            raise TypeError(error)

    def to_obj(self, return_obj=None, ns_info=None):
        super(STIXPackage, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.idref = self.idref
        return_obj.version = self.version
        return_obj.timestamp = utils.dates.serialize_value(self.timestamp)

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
        if self.reports:
            return_obj.Reports = self.reports.to_obj(ns_info=ns_info)
             
        return return_obj

    def to_dict(self):
        return super(STIXPackage, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.id
        return_obj.idref = obj.idref
        return_obj.timestamp = obj.timestamp
        return_obj.stix_header = STIXHeader.from_obj(obj.STIX_Header)
        return_obj.campaigns = Campaigns.from_obj(obj.Campaigns)
        return_obj.courses_of_action = CoursesOfAction.from_obj(obj.Courses_Of_Action)
        return_obj.exploit_targets = ExploitTargets.from_obj(obj.Exploit_Targets)
        return_obj.indicators = Indicators.from_obj(obj.Indicators)
        return_obj.observables = Observables.from_obj(obj.Observables)
        return_obj.incidents = Incidents.from_obj(obj.Incidents)
        return_obj.threat_actors = ThreatActors.from_obj(obj.Threat_Actors)
        return_obj.ttps = TTPs.from_obj(obj.TTPs)
        return_obj.related_packages = RelatedPackages.from_obj(obj.Related_Packages)
        return_obj.reports = Reports.from_obj(obj.Reports)

        # Don't overwrite unless a version is passed in
        if obj.version:
            return_obj.version = obj.version

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not return_obj:
            return_obj = cls()

        get = dict_repr.get

        return_obj.id_ = get('id')
        return_obj.idref = get('idref')
        return_obj.timestamp = get('timestamp')
        return_obj.version = get('version', cls._version)
        return_obj.stix_header = STIXHeader.from_dict(get('stix_header'))
        return_obj.campaigns = Campaigns.from_dict(get('campaigns'))
        return_obj.courses_of_action = CoursesOfAction.from_dict(get('courses_of_action'))
        return_obj.exploit_targets = ExploitTargets.from_dict(get('exploit_targets'))
        return_obj.indicators = Indicators.from_dict(get('indicators'))
        return_obj.observables = Observables.from_dict(get('observables'))
        return_obj.incidents = Incidents.from_dict(get('incidents'))
        return_obj.threat_actors = ThreatActors.from_dict(get('threat_actors'))
        return_obj.ttps = TTPs.from_dict(get('ttps'))
        return_obj.related_packages = RelatedPackages.from_dict(get('related_packages'))
        return_obj.reports = Reports.from_dict(get('reports'))
        
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
