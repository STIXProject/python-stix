# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

from .structured_text import StructuredText  # noqa
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
    RelatedPackage, RelatedPackages, RelatedCampaignRef
)

# Patch in base types of Related* types
from stix.core import STIXPackage
from cybox.core import Observable
from stix.campaign import Campaign
from stix.coa import CourseOfAction
from stix.exploit_target import ExploitTarget
from stix.incident import Incident
from stix.indicator import Indicator
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
RelatedCampaignRef._base_type = CampaignRef  # noqa

# Path the RelatedPackages _contained_type
RelatedPackages._contained_type = RelatedPackage  # noqa


import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding


class EncodedCDATA(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.EncodedCDATAType
    
    def __init__(self, value=None, encoded=None):
        self.value = value
        self.encoded = encoded

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = utils.strip_cdata(value)

    @property
    def cdata(self):
        return utils.cdata(self.value)

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()
        
        return_obj.value = obj.valueOf_
        return_obj.encoded = obj.encoded

        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        super(EncodedCDATA, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.encoded = self.encoded
        return_obj.valueOf_ = utils.cdata(self.value)

        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()
            
        return_obj.value = utils.strip_cdata(d.get('value'))
        return_obj.encoded = bool(d.get('encoded'))

        return return_obj

    def to_dict(self):
        d = {}

        if not self.value:
            return d

        d['value'] = utils.strip_cdata(self.value)
        d['encoded'] = bool(self.encoded)

        return d

    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        return unicode(self.value)
