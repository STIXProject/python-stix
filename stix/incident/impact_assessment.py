# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from stix.common import VocabString
from stix.common.vocabs import ImpactQualification, IncidentEffect
from .direct_impact_summary import DirectImpactSummary
from .indirect_impact_summary import IndirectImpactSummary
from .total_loss_estimation import TotalLossEstimation
from .effects import Effects

class ImpactAssessment(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.ImpactAssessmentType

    def __init__(self):
        super(ImpactAssessment, self).__init__()
        self.direct_impact_summary = None
        self.indirect_impact_summary = None
        self.total_loss_estimation = None
        self.impact_qualification = None
        self.effects = None
        #self.external_impact_assessment_model = None

    @property
    def direct_impact_summary(self):
        return self._direct_impact_summary

    @direct_impact_summary.setter
    def direct_impact_summary(self, value):
        if not value:
            self._direct_impact_summary = None
        elif isinstance(value, DirectImpactSummary):
            self._direct_impact_summary = value
        else:
            raise ValueError('Value must be a DirectImpactSummary instance')

    @property
    def indirect_impact_summary(self):
        return self._indirect_impact_summary

    @indirect_impact_summary.setter
    def indirect_impact_summary(self, value):
        if not value:
            self._indirect_impact_summary = None
        elif isinstance(value, IndirectImpactSummary):
            self._indirect_impact_summary = value
        else:
            raise ValueError('Value must be a IndirectImpactSummary instance')

    @property
    def total_loss_estimation(self):
        return self._total_loss_estimation

    @total_loss_estimation.setter
    def total_loss_estimation(self, value):
        if not value:
            self._total_loss_estimation = None
        elif isinstance(value, TotalLossEstimation):
            self._total_loss_estimation = value
        else:
            raise ValueError('Value must be a TotalLossEstimation instance')

    @property
    def impact_qualification(self):
        return self._impact_qualification

    @impact_qualification.setter
    def impact_qualification(self, value):
        if value:
            if isinstance(value, ImpactQualification):
                self._impact_qualification = value
            else:
                self._impact_qualification = ImpactQualification(value=value)
        else:
            self._impact_qualification = None

    def to_obj(self):
        obj = self._binding_class()
        if self.direct_impact_summary:
            obj.set_Direct_Impact_Summary(self.direct_impact_summary.to_obj())
        if self.indirect_impact_summary:
            obj.set_Indirect_Impact_Summary(self.indirect_impact_summary.to_obj())
        if self.total_loss_estimation:
            obj.set_Total_Loss_Estimation(self.total_loss_estimation.to_obj())
        if self.impact_qualification:
            obj.set_Impact_Qualification(self.impact_qualification.to_obj())
        if self.effects:
            obj.set_Effects(self.effects.to_obj())
        return obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.direct_impact_summary = DirectImpactSummary.from_obj(obj.get_Direct_Impact_Summary())
        return_obj.indirect_impact_summary = IndirectImpactSummary.from_obj(obj.get_Indirect_Impact_Summary())
        return_obj.total_loss_estimation = TotalLossEstimation.from_obj(obj.get_Total_Loss_Estimation())
        return_obj.impact_qualification = ImpactQualification.from_obj(obj.get_Impact_Qualification())
        
        if obj.get_Effects():
            return_obj.effects = Effects.from_obj(obj.get_Effects())
        return return_obj

    def to_dict(self):    
        d  = {}
        if self.direct_impact_summary:
            d['direct_impact_summary'] = self.direct_impact_summary.to_dict()
        if self.indirect_impact_summary:
            d['indirect_impact_summary'] = self.indirect_impact_summary.to_dict()
        if self.total_loss_estimation:
            d['total_loss_estimation'] = self.total_loss_estimation.to_dict()
        if self.impact_qualification:
            d['impact_qualification'] = self.impact_qualification.to_dict()
        if self.effects:
            d['effects'] = self.effects.to_dict()
        return d

    @classmethod
    def from_dict(cls, dict_, return_obj=None):
        if not dict_:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.direct_impact_summary = DirectImpactSummary.from_dict(dict_.get('direct_impact_summary'))
        return_obj.indirect_impact_summary = IndirectImpactSummary.from_dict(dict_.get('indirect_impact_summary'))
        return_obj.total_loss_estimation = TotalLossEstimation.from_dict(dict_.get('total_loss_estimation'))
        return_obj.impact_qualification = ImpactQualification.from_dict(dict_.get('impact_qualification'))
        return_obj.effects = Effects.from_dict(dict_.get('effects'))

        return return_obj
