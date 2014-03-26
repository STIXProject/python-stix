# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

from .structured_text import StructuredText
from .vocabs import VocabString, HighMediumLow
from .datetimewithprecision import DateTimeWithPrecision
from .activity import Activity
from .confidence import Confidence
from .identity import Identity
from .information_source import InformationSource
from .statement import Statement
from .tools import ToolInformation

from .related import (GenericRelationshipList, RelatedCampaign, RelatedCOA,
        RelatedExploitTarget, RelatedIdentity, RelatedIncident, 
        RelatedIndicator, RelatedObservable, RelatedThreatActor, RelatedTTP)

# Patch in base types of Related* types
from cybox.core import Observable
from stix.campaign import Campaign
from stix.coa import CourseOfAction
from stix.exploit_target import ExploitTarget
from stix.incident import Incident
from stix.indicator import Indicator
from stix.threat_actor import ThreatActor
from stix.ttp import TTP

RelatedCampaign._base_type = Campaign
RelatedCOA._base_type = CourseOfAction
RelatedExploitTarget._base_type = ExploitTarget
RelatedIdentity._base_type = Identity
RelatedIncident._base_type = Incident
RelatedIndicator._base_type = Indicator
RelatedThreatActor._base_type = ThreatActor
RelatedTTP._base_type = TTP
RelatedObservable._base_type = Observable

import stix
import stix.bindings.stix_common as common_binding
class EncodedCDATA(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.EncodedCDATAType
    
    def __init__(self, value=None, encoded=None):
        self.value = value
        self.encoded = encoded
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        return_obj.value =  obj.get_valueOf_()
        return_obj.encoded = obj.get_encoded()
        return return_obj
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()
            
        return_obj.set_valueOf_(self.value)
        return_obj.set_encoded(self.encoded)
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        return_obj.value = d.get('value')
        return_obj.encoded = bool(d.get('encoded') )
        return return_obj
    
    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        return unicode(self.value)

