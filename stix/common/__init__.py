# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import
from sys import version_info

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
from .references import References  # noqa
from .profiles import Profiles  # noqa
from .related import (   # noqa
    GenericRelationshipList, RelatedCampaign, RelatedCOA,
    RelatedExploitTarget, RelatedIdentity, RelatedIncident,
    RelatedIndicator, RelatedObservable, RelatedThreatActor, RelatedTTP,
    RelatedPackage, RelatedPackages, RelatedCampaignRef, RelatedReports,
    RelatedReport
)

import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding

from mixbox.vendor.six import text_type

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
        if version_info < (3,):
            return self.__unicode__().encode("utf-8")
        else:
            return self.__unicode__()

    def __unicode__(self):
        return text_type(self.value)
