# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from . import GenericRelationship
import stix.bindings.stix_common as common_binding

class RelatedThreatActor(GenericRelationship):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.RelatedThreatActorType

    def __init__(self, threat_actor=None, confidence=None, information_source=None, relationship=None):
        super(RelatedThreatActor, self).__init__(confidence=confidence, information_source=information_source, relationship=relationship)
        self.threat_actor = threat_actor

    @property
    def threat_actor(self):
        return self._threat_actor

    @threat_actor.setter
    def threat_actor(self, value):
        if value and not isinstance(value, ThreatActor):
            raise ValueError("value must be instance of ThreatActor")

        self._threat_actor = value

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(RelatedThreatActor, cls).from_obj(obj, return_obj)
        return_obj.threat_actor = ThreatActor.from_obj(obj=obj.get_Threat_Actor())
        return return_obj

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(RelatedThreatActor, self).to_obj(return_obj=return_obj)

        if self.threat_actor:
            return_obj.set_Threat_Actor(self.threat_actor.to_obj())

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(RelatedThreatActor, cls).from_dict(dict_repr, return_obj=return_obj)
        return_obj.threat_actor = ThreatActor.from_dict(dict_repr.get('threat_actor'))

        return return_obj

    def to_dict(self):
        d = super(RelatedThreatActor, self).to_dict()
        if self.threat_actor:
            d['threat_actor'] = self.threat_actor.to_dict()
            
        return d

class RelatedIndicator(GenericRelationship):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.RelatedIndicatorType

    def __init__(self, indicator=None, confidence=None, information_source=None, relationship=None):
        super(RelatedIndicator, self).__init__(confidence=confidence, information_source=information_source, relationship=relationship)
        self.indicator = indicator

    @property
    def indicator(self):
        return self._indicator

    @indicator.setter
    def indicator(self, value):
        if value and not isinstance(value, Indicator):
            raise ValueError("value must be instance of Indicator")

        self._indicator = value

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(RelatedIndicator, cls).from_obj(obj, return_obj)
        return_obj.indicator = Indicator.from_obj(obj=obj.get_Indicator())
        return return_obj

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(RelatedIndicator, self).to_obj(return_obj=return_obj)

        if self.indicator:
            return_obj.set_Indicator(self.indicator.to_obj())

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(RelatedIndicator, cls).from_dict(dict_repr, return_obj=return_obj)
        return_obj.indicator = Indicator.from_dict(dict_repr.get('indicator'))

        return return_obj

    def to_dict(self):
        d = super(RelatedIndicator, self).to_dict()
        if self.indicator:
            d['indicator'] = self.indicator.to_dict()

        return d

class RelatedTTP(GenericRelationship):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.RelatedTTPType

    def __init__(self, ttp=None, confidence=None, information_source=None, relationship=None):
        super(RelatedTTP, self).__init__(confidence=confidence, information_source=information_source, relationship=relationship)
        self.ttp = ttp

    @property
    def ttp(self):
        return self._ttp

    @ttp.setter
    def ttp(self, value):
        if value and not isinstance(value, TTP):
            raise ValueError("value must be instance of TTP")

        self._ttp = value

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(RelatedTTP, cls).from_obj(obj, return_obj)
        return_obj.ttp = TTP.from_obj(obj=obj.get_TTP())
        return return_obj

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(RelatedTTP, self).to_obj(return_obj=return_obj)

        if self.ttp:
            return_obj.set_TTP(self.ttp.to_obj())

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(RelatedTTP, cls).from_dict(dict_repr, return_obj=return_obj)
        return_obj.ttp = TTP.from_dict(dict_repr.get('ttp'))

        return return_obj

    def to_dict(self):
        d = super(RelatedTTP, self).to_dict()
        if self.ttp:
            d['ttp'] = self.ttp.to_dict()

        return d

from stix.threat_actor import ThreatActor
from stix.indicator import Indicator
from stix.ttp import TTP
