# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.bindings.ttp as ttp_binding
from stix.common import vocabs, Statement
from stix.data_marking import Marking

# relative
from .behavior import Behavior
from .resource import Resource
from .victim_targeting import VictimTargeting


class TTP(stix.BaseCoreComponent):
    _binding = ttp_binding
    _binding_class = _binding.TTPType
    _namespace = "http://stix.mitre.org/TTP-1"
    _version = "1.1.1"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1")
    _ID_PREFIX = "ttp"

    def __init__(self, id_=None, idref=None, timestamp=None, title=None,
                 description=None, short_description=None):

        super(TTP, self).__init__(
            id_=id_,
            idref=idref,
            timestamp=timestamp,
            title=title,
            description=description,
            short_description=short_description
        )

        self.behavior = None
        self.related_ttps = None
        self.intended_effects = None
        self.resources = None
        self.victim_targeting = None
        self.handling = None
        self.exploit_targets = ExploitTargets()

    @property
    def behavior(self):
        return self._behavior

    @behavior.setter
    def behavior(self, value):
        self._set_var(Behavior, try_cast=False, behavior=value)

    @property
    def related_ttps(self):
        return self._related_ttps

    @related_ttps.setter
    def related_ttps(self, value):
        if isinstance(value, RelatedTTPs):
            self._related_ttps = value
        else:
            self._related_ttps = RelatedTTPs(value)

    @property
    def exploit_targets(self):
        return self._exploit_targets

    @exploit_targets.setter
    def exploit_targets(self, value):
        if isinstance(value, ExploitTargets):
            self._exploit_targets = value
        else:
            self._exploit_targets = ExploitTargets(value)

    @property
    def intended_effects(self):
        return self._intended_effects

    @intended_effects.setter
    def intended_effects(self, value):
        self._intended_effects = _IntendedEffects(value)

    def add_intended_effect(self, value):
        self.intended_effects.append(value)

    @property
    def resources(self):
        return self._resources

    @resources.setter
    def resources(self, value):
        self._set_var(Resource, resources=value)

    @property
    def victim_targeting(self):
        return self._victim_targeting

    @victim_targeting.setter
    def victim_targeting(self, value):
        self._set_var(VictimTargeting, try_cast=False, victim_targeting=value)

    @property
    def handling(self):
        return self._handling

    @handling.setter
    def handling(self, value):
        self._set_var(Marking, try_cast=False, handling=value)

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(TTP, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if self.behavior:
            return_obj.Behavior = self.behavior.to_obj(ns_info=ns_info)
        if self.related_ttps:
            return_obj.Related_TTPs = self.related_ttps.to_obj(ns_info=ns_info)
        if self.exploit_targets:
            return_obj.Exploit_Targets = self.exploit_targets.to_obj(ns_info=ns_info)
        if self.intended_effects:
            return_obj.Intended_Effect = self.intended_effects.to_obj(ns_info=ns_info)
        if self.resources:
            return_obj.Resources = self.resources.to_obj(ns_info=ns_info)
        if self.victim_targeting:
            return_obj.Victim_Targeting = self.victim_targeting.to_obj(ns_info=ns_info)
        if self.handling:
            return_obj.Handling = self.handling.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(TTP, cls).from_obj(obj, return_obj=return_obj)

        if isinstance(obj, cls._binding_class):
            return_obj.behavior = Behavior.from_obj(obj.Behavior)
            return_obj.related_ttps = RelatedTTPs.from_obj(obj.Related_TTPs)
            return_obj.exploit_targets = ExploitTargets.from_obj(obj.Exploit_Targets)
            return_obj.resources = Resource.from_obj(obj.Resources)
            return_obj.victim_targeting = VictimTargeting.from_obj(obj.Victim_Targeting)
            return_obj.handling = Marking.from_obj(obj.Handling)
            return_obj.intended_effects = _IntendedEffects.from_obj(obj.Intended_Effect)

        return return_obj

    def to_dict(self):
        return super(TTP, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(TTP, cls).from_dict(dict_repr, return_obj=return_obj)

        get = dict_repr.get
        return_obj.behavior = Behavior.from_dict(get('behavior'))
        return_obj.related_ttps = RelatedTTPs.from_dict(get('related_ttps'))
        return_obj.exploit_targets = ExploitTargets.from_dict(get('exploit_targets'))
        return_obj.intended_effects = _IntendedEffects.from_dict(get('intended_effects'))
        return_obj.resources = Resource.from_dict(get('resources'))
        return_obj.victim_targeting = VictimTargeting.from_dict(get('victim_targeting'))
        return_obj.handling = Marking.from_dict(get('handling'))

        return return_obj


# NOT ACTUAL STIX TYPE
class _IntendedEffects(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        intended_effect = vocabs.IntendedEffect(value)
        return Statement(value=intended_effect)


# Avoid circular imports
from .related_ttps import RelatedTTPs
from .exploit_targets import ExploitTargets
