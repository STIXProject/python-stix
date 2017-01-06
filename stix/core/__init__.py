# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
from functools import partial

# mixbox
from mixbox import fields

# base import
import stix

# component imports
from stix.campaign import Campaign
from stix.coa import CourseOfAction
from stix.exploit_target import ExploitTarget
from stix.indicator import Indicator
from stix.incident import Incident
from stix.threat_actor import ThreatActor

# binding imports
from stix.bindings import stix_core as stix_core_binding
from stix.bindings import stix_common as stix_common_binding


class Campaigns(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.CampaignsType

    campaign = fields.TypedField(
        name="Campaign",
        type_=Campaign,
        multiple=True
    )


class CoursesOfAction(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.CoursesOfActionType

    course_of_action = fields.TypedField(
        name="Course_Of_Action",
        type_=CourseOfAction,
        multiple=True
    )


class ExploitTargets(stix.EntityList):
    _binding = stix_common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.ExploitTargetsType

    exploit_target = fields.TypedField(
        name="Exploit_Target",
        type_=ExploitTarget,
        multiple=True
    )


class Incidents(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.IncidentsType

    incident = fields.TypedField(
        name="Incident",
        type_=Incident,
        multiple=True
    )


class Indicators(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.IndicatorsType

    indicator = fields.TypedField(
        name="Indicator",
        type_=Indicator,
        multiple=True
    )


class ThreatActors(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.ThreatActorsType

    threat_actor = fields.TypedField(
        name="Threat_Actor",
        type_=ThreatActor,
        multiple=True
    )


# Namespace flattening
from .stix_package import STIXPackage  # noqa
from .stix_header import STIXHeader  # noqa
