# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import idgen
from mixbox import fields
from mixbox.cache import Cached

from cybox.core import Observable, Observables

# internal
import stix
import stix.utils as utils

# components
from stix.campaign import Campaign
from stix.coa import CourseOfAction
from stix.core.ttps import TTPs
from stix.exploit_target import ExploitTarget
from stix.indicator import Indicator
from stix.incident import Incident
from stix.threat_actor import ThreatActor
from stix.ttp import TTP

# relationships
from stix.common.related import RelatedReports

# relative imports
from .header import Header

# binding imports
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.report as report_binding


class Report(Cached, stix.Entity):
    """A STIX Report Object.

    Args:
        id_ (optional): An identifier. If ``None``, a value will be generated
            via ``mixbox.idgen.create_id()``. If set, this will unset the
            ``idref`` property.
        idref (optional): An identifier reference. If set this will unset the
            ``id_`` property.
        timestamp (optional): A timestamp value. Can be an instance of
            ``datetime.datetime`` or ``str``.
        header: A Report :class:`.Header` object.
        campaigns: A collection of :class:`.Campaign` objects.
        course_of_action: A collection of :class:`.CourseOfAction` objects.
        exploit_targets: A collection of :class:`.ExploitTarget` objects.
        incidents: A collection of :class:`.Incident` objects.
        indicators: A collection of :class:`.Indicator` objects.
        threat_actors: A collection of :class:`.ThreatActor` objects.
        ttps: A collection of :class:`.TTP` objects.
        related_reports: A collection of :class:`.RelatedReport` objects.

    """
    _binding = report_binding
    _binding_class = _binding.ReportType
    _namespace = 'http://stix.mitre.org/Report-1'
    _version = "1.0"

    def __init__(self, id_=None, idref=None, timestamp=None, header=None,
                 courses_of_action=None, exploit_targets=None, indicators=None,
                 observables=None, incidents=None, threat_actors=None,
                 ttps=None, campaigns=None, related_reports=None):
        
        self.id_ = id_ or idgen.create_id("Report")
        self.idref = idref
        self.version = self._version
        self.header = header
        self.campaigns = campaigns
        self.courses_of_action = courses_of_action
        self.exploit_targets = exploit_targets
        self.observables = observables
        self.indicators = indicators
        self.incidents = incidents
        self.threat_actors = threat_actors
        self.ttps = ttps
        self.related_reports = related_reports
        
        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = utils.dates.now() if not idref else None

    @property
    def id_(self):
        """A globally unique identifier for this Report. By default, one
        will be generated automatically.

        """
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
        """A reference to another Report identifier. Setting this will unset
        any previous ``id`` values.

        """
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
        """Specifies a timestamp for the definition of this specific Report
        object.

        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = utils.dates.parse_value(value)

    @property
    def header(self):
        """The :class:`.Header` section for the Report.

        """
        return self._header

    @header.setter
    def header(self, value):
        self._set_var(Header, try_cast=False, header=value)

    @property
    def indicators(self):
        """The top-level :class:`.Indicator` collection. This behaves like
        a ``MutableSequence`` type.

        """
        return self._indicators

    @indicators.setter
    def indicators(self, value):
        self._indicators = Indicators(value)

    def add_indicator(self, indicator):
        """Adds an :class:`.Indicator` object to the :attr:`indicators`
        collection.

        """
        self.indicators.append(indicator)

    @property
    def campaigns(self):
        """The top-level :class:`.Campaign` collection. This behaves like
        a ``MutableSequence`` type.

        """
        return self._campaigns

    @campaigns.setter
    def campaigns(self, value):
        self._campaigns = Campaigns(value)

    def add_campaign(self, campaign):
        """Adds a :class:`Campaign` object to the :attr:`campaigns` collection.

        """
        self.campaigns.append(campaign)

    @property
    def observables(self):
        """The top-level ``Observable`` collection. This behaves like
        a ``MutableSequence`` type.

        """
        return self._observables

    @observables.setter
    def observables(self, value):
        self._set_var(Observables, observables=value)

    def add_observable(self, observable):
        """Adds an ``Observable`` object to the :attr:`observables` collection.

        If `observable` is not an ``Observable`` instance, an effort will be
        made to convert it to one.

        """
        if not self.observables:
            self.observables = Observables(observables=observable)
        else:
            self.observables.add(observable)

    @property
    def incidents(self):
        """The top-level :class:`.Incident` collection. This behaves like
        a ``MutableSequence`` type.

        """
        return self._incidents
    
    @incidents.setter
    def incidents(self, value):
        self._incidents = Incidents(value)
    
    def add_incident(self, incident):
        """Adds an :class:`.Incident` object to the :attr:`incidents`
        collection.

        """
        self.incidents.append(incident)

    @property
    def threat_actors(self):
        """The top-level :class:`.ThreatActor` collection. This behaves like
        a ``MutableSequence`` type.

        """
        return self._threat_actors
    
    @threat_actors.setter
    def threat_actors(self, value):
        self._threat_actors = ThreatActors(value)

    def add_threat_actor(self, threat_actor):
        """Adds an :class:`.ThreatActor` object to the :attr:`threat_actors`
        collection.

        """
        self._threat_actors.append(threat_actor)

    @property
    def courses_of_action(self):
        """The top-level :class:`.CourseOfAction` collection. This behaves like
        a ``MutableSequence`` type.

        """
        return self._courses_of_action
    
    @courses_of_action.setter
    def courses_of_action(self, value):
        self._courses_of_action = CoursesOfAction(value)

    def add_course_of_action(self, course_of_action):
        """Adds an :class:`.CourseOfAction` object to the
        :attr:`courses_of_action` collection.

        """
        self._courses_of_action.append(course_of_action)

    @property
    def exploit_targets(self):
        """The top-level :class:`.ExploitTarget` collection. This behaves like
        a ``MutableSequence`` type.

        """
        return self._exploit_targets
    
    @exploit_targets.setter
    def exploit_targets(self, value):
        self._exploit_targets = ExploitTargets(value)

    def add_exploit_target(self, exploit_target):
        """Adds an :class:`.ExploitTarget` object to the
        :attr:`exploit_targets` collection.

        """
        self._exploit_targets.append(exploit_target)

    @property
    def ttps(self):
        """The top-level :class:`.TTP` collection. This behaves like
        a ``MutableSequence`` type.

        """
        return self._ttps
    
    @ttps.setter
    def ttps(self, value):
        if isinstance(value, TTPs):
            self._ttps = value
        else:
            self._ttps = TTPs(value)
    
    def add_ttp(self, ttp):
        """Adds an :class:`.TTP` object to the :attr:`ttps` collection.

        """
        self.ttps.append(ttp)

    @property
    def related_reports(self):
        """The top-level :class:`.RelatedReports` collection. This behaves like
        a ``MutableSequence`` type.

        """
        return self._related_reports

    @related_reports.setter
    def related_reports(self, value):
        if isinstance(value, RelatedReports):
            self._related_reports = value
        else:
            self._related_reports = RelatedReports(value)

    def add_related_report(self, related_report):
        """Adds an :class:`.RelatedReport` object to the
        :attr:`related_reports` collection.

        """
        self.related_reports.append(related_report)

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
        super(Report, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.idref = self.idref
        return_obj.version = self.version
        return_obj.timestamp = utils.dates.serialize_value(self.timestamp)

        if self.header:
            return_obj.Header = self.header.to_obj(ns_info=ns_info)
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
        if self.related_reports:
            return_obj.Related_Reports = self.related_reports.to_obj(ns_info=ns_info)
             
        return return_obj

    def to_dict(self):
        return super(Report, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not return_obj:
            return_obj = cls()

        # ReportBaseType fields
        return_obj.id_ = obj.id
        return_obj.idref = obj.idref
        return_obj.timestamp = obj.timestamp

        # ReportType fields
        if isinstance(obj, cls._binding_class):
            return_obj.header = Header.from_obj(obj.Header)
            return_obj.campaigns = Campaigns.from_obj(obj.Campaigns)
            return_obj.courses_of_action = CoursesOfAction.from_obj(obj.Courses_Of_Action)
            return_obj.exploit_targets = ExploitTargets.from_obj(obj.Exploit_Targets)
            return_obj.indicators = Indicators.from_obj(obj.Indicators)
            return_obj.observables = Observables.from_obj(obj.Observables)
            return_obj.incidents = Incidents.from_obj(obj.Incidents)
            return_obj.threat_actors = ThreatActors.from_obj(obj.Threat_Actors)
            return_obj.ttps = TTPs.from_obj(obj.TTPs)
            return_obj.related_reports = RelatedReports.from_obj(obj.Related_Reports)

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
        return_obj.header = Header.from_dict(get('header'))
        return_obj.campaigns = Campaigns.from_dict(get('campaigns'))
        return_obj.courses_of_action = CoursesOfAction.from_dict(get('courses_of_action'))
        return_obj.exploit_targets = ExploitTargets.from_dict(get('exploit_targets'))
        return_obj.indicators = Indicators.from_dict(get('indicators'))
        return_obj.observables = Observables.from_dict(get('observables'))
        return_obj.incidents = Incidents.from_dict(get('incidents'))
        return_obj.threat_actors = ThreatActors.from_dict(get('threat_actors'))
        return_obj.ttps = TTPs.from_dict(get('ttps'))
        return_obj.related_reports = RelatedReports.from_dict(get('related_reports'))
        
        return return_obj


class Campaigns(stix.EntityList):
    _binding = report_binding
    _namespace = 'http://stix.mitre.org/Report-1'
    _binding_class = _binding.CampaignsType

    campaign = fields.TypedField("Campaign", Campaign, multiple=True, key_name="campaigns")


class CoursesOfAction(stix.EntityList):
    _binding = report_binding
    _namespace = 'http://stix.mitre.org/Report-1'
    _binding_class = _binding.CoursesOfActionType

    course_of_action = fields.TypedField("Course_Of_Action", CourseOfAction, multiple=True, key_name="courses_of_action")


class ExploitTargets(stix.EntityList):
    _binding = stix_common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.ExploitTargetsType

    exploit_target = fields.TypedField("Exploit_Target", ExploitTarget, multiple=True, key_name="exploit_targets")


class Incidents(stix.EntityList):
    _binding = report_binding
    _namespace = 'http://stix.mitre.org/Report-1'
    _binding_class = _binding.IncidentsType

    incident = fields.TypedField("Incident", Incident, multiple=True, key_name="incidents")


class Indicators(stix.EntityList):
    _binding = report_binding
    _namespace = 'http://stix.mitre.org/Report-1'
    _binding_class = _binding.IndicatorsType
    _contained_type = Indicator

    indicator = fields.TypedField("Indicator", Indicator, multiple=True, key_name="indicators")


class ThreatActors(stix.EntityList):
    _binding = report_binding
    _namespace = 'http://stix.mitre.org/Report-1'
    _binding_class = _binding.ThreatActorsType

    threat_actor = fields.TypedField("Threat_Actor", ThreatActor, multiple=True, key_name="threat_actors")
