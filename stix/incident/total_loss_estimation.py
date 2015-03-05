# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.bindings.incident as incident_binding

# relative
from .loss_estimation import LossEstimation


class TotalLossEstimation(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.TotalLossEstimationType

    def __init__(self):
        super(TotalLossEstimation, self).__init__()
        self.initial_reported_total_loss_estimation = None
        self.actual_total_loss_estimation = None

    @property
    def initial_reported_total_loss_estimation(self):
        return self._initial_reported_total_loss_estimation

    @initial_reported_total_loss_estimation.setter
    def initial_reported_total_loss_estimation(self, value):
        self._set_var(LossEstimation, initial_reported_total_loss_estimation=value)

    @property
    def actual_total_loss_estimation(self):
        return self._actual_total_loss_estimation

    @actual_total_loss_estimation.setter
    def actual_total_loss_estimation(self, value):
        self._set_var(LossEstimation, actual_total_loss_estimation=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(TotalLossEstimation, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        obj = self._binding_class()
        if self.initial_reported_total_loss_estimation:
            obj.Initial_Reported_Total_Loss_Estimation = self.initial_reported_total_loss_estimation.to_obj(ns_info=ns_info)
        if self.actual_total_loss_estimation:
            obj.Actual_Total_Loss_Estimation = self.actual_total_loss_estimation.to_obj(ns_info=ns_info)
        return obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.initial_reported_total_loss_estimation = LossEstimation.from_obj(obj.Initial_Reported_Total_Loss_Estimation)
        return_obj.actual_total_loss_estimation = LossEstimation.from_obj(obj.Actual_Total_Loss_Estimation)
        return return_obj

    def to_dict(self):    
        return super(TotalLossEstimation, self).to_dict()

    @classmethod
    def from_dict(cls, dict_, return_obj=None):
        if not dict_:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.initial_reported_total_loss_estimation = LossEstimation.from_dict(dict_.get('initial_reported_total_loss_estimation'))
        return_obj.actual_total_loss_estimation = LossEstimation.from_dict(dict_.get('actual_total_loss_estimation'))

        return return_obj
