# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import idgen
from mixbox import fields

from cybox.core import Observable, Observables

# internal
import stix
import stix.utils as utils

# components
from stix.campaign import Campaign
from stix.coa import CourseOfAction
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


class Report(stix.Entity):
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

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    timestamp = fields.TypedField("timestamp")
    version = fields.TypedField("version")
    header = fields.TypedField("Header", Header)
    campaigns = fields.TypedField("Campaigns", type_="stix.report.Campaigns")
    courses_of_action = fields.TypedField("Courses_Of_Action", type_="stix.report.CoursesOfAction")
    exploit_targets = fields.TypedField("Exploit_Targets", type_="stix.report.ExploitTargets")
    observables = fields.TypedField("Observables", Observables)
    indicators = fields.TypedField("Indicators", type_="stix.report.Indicators")
    incidents = fields.TypedField("Incidents", type_="stix.report.Incidents")
    threat_actors = fields.TypedField("Threat_Actors", type_="stix.report.ThreatActors")
    ttps = fields.TypedField("TTPs", type_="stix.core.ttps.TTPs")
    related_reports = fields.TypedField("Related_Reports", type_="stix.report.RelatedReports")

    def __init__(self, id_=None, idref=None, timestamp=None, header=None,
                 courses_of_action=None, exploit_targets=None, indicators=None,
                 observables=None, incidents=None, threat_actors=None,
                 ttps=None, campaigns=None, related_reports=None):
        super(Report, self).__init__()
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

    def add_indicator(self, indicator):
        """Adds an :class:`.Indicator` object to the :attr:`indicators`
        collection.

        """
        if self.indicators is None:
            self.indicators = Indicators()
        self.indicators.append(indicator)

    def add_campaign(self, campaign):
        """Adds a :class:`Campaign` object to the :attr:`campaigns` collection.

        """
        if self.campaigns is None:
            self.campaigns = Campaigns()
        self.campaigns.append(campaign)

    def add_observable(self, observable):
        """Adds an ``Observable`` object to the :attr:`observables` collection.

        If `observable` is not an ``Observable`` instance, an effort will be
        made to convert it to one.

        """
        if not self.observables:
            self.observables = Observables(observables=observable)
        else:
            self.observables.add(observable)

    def add_incident(self, incident):
        """Adds an :class:`.Incident` object to the :attr:`incidents`
        collection.

        """
        if self.incidents is None:
            self.incidents = Incidents()
        self.incidents.append(incident)

    def add_threat_actor(self, threat_actor):
        """Adds an :class:`.ThreatActor` object to the :attr:`threat_actors`
        collection.

        """
        if self.threat_actors is None:
            self.threat_actors = ThreatActors()
        self.threat_actors.append(threat_actor)

    def add_course_of_action(self, course_of_action):
        """Adds an :class:`.CourseOfAction` object to the
        :attr:`courses_of_action` collection.

        """
        if self.courses_of_action is None:
            self.courses_of_action = CoursesOfAction()
        self.courses_of_action.append(course_of_action)

    def add_exploit_target(self, exploit_target):
        """Adds an :class:`.ExploitTarget` object to the
        :attr:`exploit_targets` collection.

        """
        if self.exploit_targets is None:
            self.exploit_targets = ExploitTargets()
        self.exploit_targets.append(exploit_target)

    def add_ttp(self, ttp):
        """Adds an :class:`.TTP` object to the :attr:`ttps` collection.

        """
        if self.ttps is None:
            self.ttps = TTPs()
        self.ttps.append(ttp)

    def add_related_report(self, related_report):
        """Adds an :class:`.RelatedReport` object to the
        :attr:`related_reports` collection.

        """
        if self.related_reports is None:
            self.related_reports = RelatedReports()
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
            TTP: self.add_ttp,
            Observable: self.add_observable,
        }

        try:
            add = tlo_adds[entity.__class__]
            add(entity)
        except KeyError:
            error = "Cannot add type '{0}' to a top-level collection"
            error = error.format(type(entity))
            raise TypeError(error)

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

from stix.core.ttps import TTPs
