# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

from mixbox.fields import TypedField, CDATAField

from .structured_text import StructuredText, StructuredTextList  # noqa
from .vocabs import VocabString   # noqa
from .datetimewithprecision import DateTimeWithPrecision  # noqa
from .activity import Activity  # noqa
from .confidence import Confidence  # noqa
from .identity import Identity  # noqa
from .information_source import InformationSource  # noqa
from .statement import Statement  # noqa
from .tools import ToolInformation  # noqa
from .names import Names  # noqa
from .campaign_reference import CampaignRef  # noqa
from .related import (   # noqa
    GenericRelationshipList, RelatedCampaign, RelatedCOA,
    RelatedExploitTarget, RelatedIdentity, RelatedIncident,
    RelatedIndicator, RelatedObservable, RelatedThreatActor, RelatedTTP,
    RelatedPackage, RelatedPackages, RelatedCampaignRef, RelatedReports,
    RelatedReport
)

# Patch in base types of Related* types
from stix.core import STIXPackage
from cybox.core import Observable
from stix.campaign import Campaign
from stix.coa import CourseOfAction
from stix.exploit_target import ExploitTarget
from stix.incident import Incident
from stix.indicator import Indicator
from stix.report import Report
from stix.threat_actor import ThreatActor
from stix.ttp import TTP


RelatedCampaign._base_type = Campaign  # noqa
RelatedCOA._base_type = CourseOfAction  # noqa
RelatedExploitTarget._base_type = ExploitTarget  # noqa
RelatedIdentity._base_type = Identity  # noqa
RelatedIncident._base_type = Incident  # noqa
RelatedIndicator._base_type = Indicator  # noqa
RelatedThreatActor._base_type = ThreatActor  # noqa
RelatedTTP._base_type = TTP  # noqa
RelatedObservable._base_type = Observable  # noqa
RelatedPackage._base_type = STIXPackage  # noqa
RelatedReport._base_type = Report  # noqa
RelatedCampaignRef._base_type = CampaignRef  # noqa

# Patch contained types
RelatedPackages._contained_type = RelatedPackage  # noqa
RelatedReports._contained_type = RelatedReport  # noqa

import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding


class EncodedCDATA(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.EncodedCDATAType

    value = CDATAField("valueOf_", key_name="value")
    encoded = TypedField("encoded")

    def __init__(self, value=None, encoded=None):
        super(EncodedCDATA, self).__init__()
        self.value = value
        self.encoded = encoded

    @property
    def cdata(self):
        return utils.cdata(self.value)

    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        return unicode(self.value)


# Initialize typed fields which could not be done in the class definition
Statement._init_typed_fields()
Identity._init_typed_fields()
Confidence._init_typed_fields()
