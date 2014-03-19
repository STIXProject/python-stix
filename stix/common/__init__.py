# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

from .structured_text import StructuredText
from .vocabs import VocabString, HighMediumLow
from .datetimewithprecision import DateTimeWithPrecision
from .confidence import Confidence
from .identity import Identity
from .information_source import InformationSource
from .statement import Statement
from .tools import ToolInformation

from .related import (GenericRelationshipList, RelatedCampaign, RelatedCOA,
        RelatedIdentity, RelatedIncident, RelatedIndicator, RelatedObservable,
        RelatedThreatActor, RelatedTTP)

# Patch in base types of Related* types
from cybox.core import Observable
from stix.campaign import Campaign
from stix.coa import CourseOfAction
from stix.incident import Incident
from stix.indicator import Indicator
from stix.threat_actor import ThreatActor
from stix.ttp import TTP

RelatedCampaign._base_type = Campaign
RelatedCOA._base_type = CourseOfAction
RelatedIdentity._base_type = Identity
RelatedIncident._base_type = Incident
RelatedIndicator._base_type = Indicator
RelatedThreatActor._base_type = ThreatActor
RelatedTTP._base_type = TTP
RelatedObservable._base_type = Observable
