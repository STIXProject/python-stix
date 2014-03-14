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

from .related import (GenericRelationshipList, RelatedIdentity, RelatedThreatActor,
        RelatedIndicator, RelatedTTP)


# Patch in related types here
from stix.threat_actor import ThreatActor
from stix.indicator import Indicator
from stix.ttp import TTP

RelatedIdentity._base_type = Identity
RelatedThreatActor._base_type = ThreatActor
RelatedIndicator._base_type = Indicator
RelatedTTP._base_type = TTP
