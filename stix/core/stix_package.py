# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# mixbox
from mixbox import idgen
from mixbox import fields

# cybox
from cybox.core import Observable, Observables

# base
import stix

# utility imports
from .. import utils
from ..utils import parser
from ..utils import deprecated

# component imports
from ..campaign import Campaign
from ..coa import CourseOfAction
from ..exploit_target import ExploitTarget
from ..indicator import Indicator
from ..incident import Incident
from ..threat_actor import ThreatActor
from ..ttp import TTP
from ..report import Report

# relationship imports
from ..common.related import RelatedPackages

# relative imports
from .stix_header import STIXHeader
from .ttps import TTPs
from . import (Campaigns, CoursesOfAction, ExploitTargets, Incidents,
               Indicators, ThreatActors, Reports)

# binding imports
import stix.bindings.stix_core as stix_core_binding
import mixbox.entities

class STIXPackage(stix.Entity):
    """A STIX Package object.

    Args:
        id_ (optional): An identifier. If ``None``, a value will be generated
            via ``mixbox.idgen.create_id()``. If set, this will unset the
            ``idref`` property.
        idref: **DEPRECATED** An identifier reference. If set this will unset
            the ``id_`` property.
        timestamp: **DEPRECATED** A timestamp value. Can be an instance of
            ``datetime.datetime`` or ``str``.
        header: A Report :class:`.Header` object.
        campaigns: A collection of :class:`.Campaign` objects.
        course_of_action: A collection of :class:`.CourseOfAction` objects.
        exploit_targets: A collection of :class:`.ExploitTarget` objects.
        incidents: A collection of :class:`.Incident` objects.
        indicators: A collection of :class:`.Indicator` objects.
        threat_actors: A collection of :class:`.ThreatActor` objects.
        ttps: A collection of :class:`.TTP` objects.
        related_packages: **DEPRECATED**. A collection of
            :class:`.RelatedPackage` objects.
        reports: A collection of :class:`.Report` objects.

    """
    _binding = stix_core_binding
    _binding_class = _binding.STIXType
    _namespace = 'http://stix.mitre.org/stix-1'
    _version = "1.2"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1", "1.2")

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref", preset_hook=deprecated.field)
    version = fields.TypedField("version")
    timestamp = fields.DateTimeField("timestamp", preset_hook=deprecated.field)
    stix_header = fields.TypedField("STIX_Header", STIXHeader)
    campaigns = fields.TypedField("Campaigns", Campaigns)
    courses_of_action = fields.TypedField("Courses_Of_Action", CoursesOfAction)
    exploit_targets = fields.TypedField("Exploit_Targets", ExploitTargets)
    observables = fields.TypedField("Observables", Observables)
    indicators = fields.TypedField("Indicators", Indicators)
    incidents = fields.TypedField("Incidents", Incidents)
    threat_actors = fields.TypedField("Threat_Actors", ThreatActors)
    ttps = fields.TypedField("TTPs", TTPs)
    related_packages = fields.TypedField("Related_Packages", RelatedPackages)
    reports = fields.TypedField("Reports", Reports)

    def __init__(self, id_=None, idref=None, timestamp=None, stix_header=None,
                 courses_of_action=None, exploit_targets=None, indicators=None,
                 observables=None, incidents=None, threat_actors=None,
                 ttps=None, campaigns=None, related_packages=None,
                 reports=None):
        
        super(STIXPackage, self).__init__()
        
        self.id_ = id_ or idgen.create_id("Package")
        self.idref = idref
        self.version = STIXPackage._version
        self.stix_header = stix_header
        self.campaigns = campaigns or Campaigns()
        self.courses_of_action = courses_of_action or CoursesOfAction()
        self.exploit_targets = exploit_targets or ExploitTargets()
        self.observables = observables or Observables()
        self.indicators = indicators or Indicators()
        self.incidents = incidents or Incidents()
        self.threat_actors = threat_actors or ThreatActors()
        self.ttps = ttps or TTPs()
        self.related_packages = related_packages
        self.reports = reports or Reports()
        self.timestamp = timestamp

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

    def add_report(self, report):
        """Adds a :class:`.Report` object to the :attr:`reports` collection.

        """
        if self.reports is None:
            self.reports = Reports()
        self.reports.append(report)

    def add_related_package(self, related_package):
        """Adds a :class:`.RelatedPackage` object to the
        :attr:`related_packages` collection.

        """
        if self.related_packages is None:
            self.related_packages = RelatedPackages()
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
            TTP: self.add_ttp,
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
