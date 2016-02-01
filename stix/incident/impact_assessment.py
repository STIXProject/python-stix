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

from mixbox import fields, entities
from stix.common.vocabs import VocabField

class ImpactAssessment(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.ImpactAssessmentType

    direct_impact_summary = fields.TypedField("Direct_Impact_Summary", DirectImpactSummary)
    indirect_impact_summary = fields.TypedField("Indirect_Impact_Summary", IndirectImpactSummary)
    total_loss_estimation = fields.TypedField("Total_Loss_Estimation", TotalLossEstimation)
    impact_qualification = vocabs.VocabField("Impact_Qualification", vocabs.ImpactQualification)
    effects = fields.TypedField("Effects", type_="stix.incident.impact_assessment.Effects")

    def __init__(self):
        super(ImpactAssessment, self).__init__()
        self.direct_impact_summary = None
        self.indirect_impact_summary = None
        self.total_loss_estimation = None
        self.impact_qualification = None
        self.effects = None
        # self.external_impact_assessment_model = None


class Effects(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.EffectsType

    effects = VocabField("Effect", VocabString, multiple=True, key_name="effects")
    
    @classmethod
    def _dict_as_list(cls):
        return True

    def _fix_value(self, value):
        return vocabs.IncidentEffect(value=value)
