# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from stix.common.generic_relationship import GenericRelationshipList
from stix.common.related import RelatedIndicator
from cybox.core import Observable, Object

class RelatedIndicators(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedIndicatorsType

    def __init__(self, indicators=None, scope=None):
        super(RelatedIndicators, self).__init__(scope=scope)
        self.indicators = indicators

    @property
    def indicators(self):
        return self._indicators

    @indicators.setter
    def indicators(self, value):
        self._indicators = []

        if isinstance(value, list):
            for v in value:
                self.add_indicator(v)
        else:
            self.add_indicator(value)

    def add_indicator(self, indicator):
        if not indicator:
            return
        if isinstance(indicator, RelatedIndicator):
            self.indicators.append(indicator)
        else:
            raise ValueError("Cannot add %s to indicators list" % type(indicator))

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(RelatedIndicators, self).to_obj(return_obj)
        return_obj.set_Related_Indicator([x.to_obj() for x in self.indicators])
        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(RelatedIndicators, cls).from_obj(obj, return_obj)

        if obj.get_Related_Indicator():
            return_obj.indicators = [RelatedIndicator.from_obj(x) for x in obj.get_Related_Indicator()]

        return return_obj

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}

        super(RelatedIndicators, self).to_dict(return_dict)

        if self.indicators:
            return_dict['indicators'] = [x.to_dict() for x in self.indicators]

        return return_dict

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(RelatedIndicators, cls).from_dict(dict_repr, return_obj)
        return_obj.indicators = [RelatedIndicator.from_dict(x) for x in dict_repr.get('indicators', [])]
        return return_obj
