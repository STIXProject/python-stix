# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.bindings.incident as incident_binding

# relative
from .loss_estimation import LossEstimation

from mixbox import entities, fields

class TotalLossEstimation(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.TotalLossEstimationType

    initial_reported_total_loss_estimation = fields.TypedField("Initial_Reported_Total_Loss_Estimation", LossEstimation)
    actual_total_loss_estimation = fields.TypedField("Actual_Total_Loss_Estimation", LossEstimation)

    def __init__(self):
        super(TotalLossEstimation, self).__init__()
