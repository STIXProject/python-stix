# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.bindings.incident as incident_binding
from stix.common import vocabs, VocabString

# relative
from .direct_impact_summary import DirectImpactSummary
from .indirect_impact_summary import IndirectImpactSummary
from .total_loss_estimation import TotalLossEstimation


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
        # self.external_impact_assessment_model = None

    @property
    def effects(self):
        return self._effects
    
    @effects.setter
    def effects(self, value):
        self._effects = Effects(value)
    
    def add_effect(self, value):
        self.effects.append(value)

    @property
    def direct_impact_summary(self):
        return self._direct_impact_summary

    @direct_impact_summary.setter
    def direct_impact_summary(self, value):
        self._set_var(DirectImpactSummary, try_cast=False, direct_impact_summary=value)

    @property
    def indirect_impact_summary(self):
        return self._indirect_impact_summary

    @indirect_impact_summary.setter
    def indirect_impact_summary(self, value):
        self._set_var(IndirectImpactSummary, try_cast=False, indirect_impact_summary=value)

    @property
    def total_loss_estimation(self):
        return self._total_loss_estimation

    @total_loss_estimation.setter
    def total_loss_estimation(self, value):
        self._set_var(TotalLossEstimation, try_cast=False, total_loss_estimation=value)

    @property
    def impact_qualification(self):
        return self._impact_qualification

    @impact_qualification.setter
    def impact_qualification(self, value):
        self._set_vocab(vocabs.ImpactQualification, impact_qualification=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(ImpactAssessment, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        obj = self._binding_class()

        if self.direct_impact_summary:
            obj.Direct_Impact_Summary = self.direct_impact_summary.to_obj(ns_info=ns_info)
        if self.indirect_impact_summary:
            obj.Indirect_Impact_Summary = self.indirect_impact_summary.to_obj(ns_info=ns_info)
        if self.total_loss_estimation:
            obj.Total_Loss_Estimation = self.total_loss_estimation.to_obj(ns_info=ns_info)
        if self.impact_qualification:
            obj.Impact_Qualification = self.impact_qualification.to_obj(ns_info=ns_info)
        if self.effects:
            obj.Effects = self.effects.to_obj(ns_info=ns_info)

        return obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.direct_impact_summary = DirectImpactSummary.from_obj(obj.Direct_Impact_Summary)
        return_obj.indirect_impact_summary = IndirectImpactSummary.from_obj(obj.Indirect_Impact_Summary)
        return_obj.total_loss_estimation = TotalLossEstimation.from_obj(obj.Total_Loss_Estimation)
        return_obj.impact_qualification = VocabString.from_obj(obj.Impact_Qualification)
        return_obj.effects = Effects.from_obj(obj.Effects)

        return return_obj

    def to_dict(self):    
        return super(ImpactAssessment, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()
        
        get = dict_repr.get
        return_obj.direct_impact_summary = DirectImpactSummary.from_dict(get('direct_impact_summary'))
        return_obj.indirect_impact_summary = IndirectImpactSummary.from_dict(get('indirect_impact_summary'))
        return_obj.total_loss_estimation = TotalLossEstimation.from_dict(get('total_loss_estimation'))
        return_obj.impact_qualification = VocabString.from_dict(get('impact_qualification'))
        return_obj.effects = Effects.from_dict(get('effects'))

        return return_obj


class Effects(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _contained_type = VocabString
    _binding = incident_binding
    _binding_class = _binding.EffectsType
    _inner_name = "effects"
    _binding_var = "Effect"
    _dict_as_list = True

    def _fix_value(self, value):
        return vocabs.IncidentEffect(value=value)
