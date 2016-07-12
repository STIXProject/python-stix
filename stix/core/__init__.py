# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# base import
import stix

# deprecations
from stix.utils.deprecated import idref_deprecated

# component imports
from stix.campaign import Campaign
from stix.coa import CourseOfAction
from stix.exploit_target import ExploitTarget
from stix.indicator import Indicator
from stix.incident import Incident
from stix.report import Report
from stix.threat_actor import ThreatActor

# binding imports
from stix.bindings import stix_core as stix_core_binding
from stix.bindings import stix_common as stix_common_binding


class Campaigns(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.CampaignsType
    _contained_type = Campaign
    _binding_var = "Campaign"
    _inner_name = "campaigns"
    _dict_as_list = True

    def _is_valid(self, value):
        idref_deprecated(value)
        return stix.EntityList._is_valid(self, value)


class CoursesOfAction(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.CoursesOfActionType
    _contained_type = CourseOfAction
    _binding_var = "Course_Of_Action"
    _inner_name = "courses_of_action"
    _dict_as_list = True

    def _is_valid(self, value):
        idref_deprecated(value)
        return stix.EntityList._is_valid(self, value)


class ExploitTargets(stix.EntityList):
    _binding = stix_common_binding
    _namespace = 'http://stix.mitre.org/common-1'
    _binding_class = _binding.ExploitTargetsType
    _contained_type = ExploitTarget
    _binding_var = "Exploit_Target"
    _inner_name = "exploit_targets"
    _dict_as_list = True

    def _is_valid(self, value):
        idref_deprecated(value)
        return stix.EntityList._is_valid(self, value)


class Incidents(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.IncidentsType
    _contained_type = Incident
    _binding_var = "Incident"
    _inner_name = "incidents"
    _dict_as_list = True

    def _is_valid(self, value):
        idref_deprecated(value)
        return stix.EntityList._is_valid(self, value)


class Indicators(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.IndicatorsType
    _contained_type = Indicator
    _binding_var = "Indicator"
    _inner_name = "indicators"
    _dict_as_list = True

    def _is_valid(self, value):
        idref_deprecated(value)
        return stix.EntityList._is_valid(self, value)


class ThreatActors(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.ThreatActorsType
    _contained_type = ThreatActor
    _binding_var = "Threat_Actor"
    _inner_name = "threat_actors"
    _dict_as_list = True

    def _is_valid(self, value):
        idref_deprecated(value)
        return stix.EntityList._is_valid(self, value)


class Reports(stix.EntityList):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding_class = _binding.ReportsType
    _contained_type = Report
    _binding_var = "Report"
    _inner_name = "reports"
    _dict_as_list = True

    def _is_valid(self, value):
        idref_deprecated(value)
        return stix.EntityList._is_valid(self, value)


# Namespace flattening
from .stix_package import STIXPackage  # noqa
from .stix_header import STIXHeader  # noqa