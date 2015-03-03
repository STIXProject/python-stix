# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.utils as utils
import stix.bindings.ttp as ttp_binding
from stix.common import vocabs, StructuredText, InformationSource, Statement
from stix.data_marking import Marking

# relative
from .behavior import Behavior
from .resource import Resource
from .victim_targeting import VictimTargeting


class TTP(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.TTPType
    _namespace = "http://stix.mitre.org/TTP-1"
    _version = "1.1.1"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1")

    def __init__(self, id_=None, idref=None, timestamp=None, title=None, description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("ttp")
        self.idref = idref
        self.version = None # self._version
        self.title = title
        self.description = description
        self.short_description = short_description
        self.behavior = None
        self.related_ttps = None
        self.information_source = None
        self.intended_effects = None
        self.resources = None
        self.victim_targeting = None
        self.handling = None
        self.exploit_targets = ExploitTargets()

        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = utils.dates.now() if not idref else None

    @property
    def id_(self):
        return self._id
    
    @id_.setter
    def id_(self, value):
        if not value:
            self._id = None
        else:
            self._id = value
            self.idref = None
    
    @property
    def version(self):
        return self._version
    
    @version.setter
    def version(self, value):
        if not value:
            self._version = None
        else:
            utils.check_version(self._ALL_VERSIONS, value)
            self._version = value
    
    @property
    def idref(self):
        return self._idref
    
    @idref.setter
    def idref(self, value):
        if not value:
            self._idref = None
        else:
            self._idref = value
            self.id_ = None # unset id_ if idref is present
    
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = utils.dates.parse_value(value)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._description = value
            else:
                self._description = StructuredText(value=value)
        else:
            self._description = None

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._short_description = value
            else:
                self._short_description = StructuredText(value=value)
        else:
            self._short_description = None

    @property
    def behavior(self):
        return self._behavior

    @behavior.setter
    def behavior(self, value):
        if not value:
            self._behavior = None
        elif isinstance(value, Behavior):
            self._behavior = value
        else:
            raise ValueError('Value must be a Behavior instance')

    @property
    def related_ttps(self):
        return self._related_ttps

    @related_ttps.setter
    def related_ttps(self, value):

        if not value:
            self._related_ttps = RelatedTTPs()
        elif isinstance(value, RelatedTTPs):
            self._related_ttps = value
        else:
            raise ValueError("value must be RelatedTTPs instance")

    @property
    def exploit_targets(self):
        return self._exploit_targets

    @exploit_targets.setter
    def exploit_targets(self, value):
        if not value:
            self._exploit_targets = ExploitTargets()
        elif isinstance(value, ExploitTargets):
            self._exploit_targets = value
        else:
            raise ValueError("value must be ExploitTargets instance")

    @property
    def information_source(self):
        return self._information_source

    @information_source.setter
    def information_source(self, value):
        if not value:
            self._information_source = None
        elif isinstance(value, InformationSource):
            self._information_source = value
        else:
            raise ValueError('value must be instance of InformationSource')

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
        if not value:
            self._resources = None
        elif isinstance(value, Resource):
            self._resources = value
        else:
            raise ValueError('value must be instance of Resource')

    @property
    def victim_targeting(self):
        return self._victim_targeting

    @victim_targeting.setter
    def victim_targeting(self, value):
        if not value:
            self._victim_targeting = None
        elif isinstance(value, VictimTargeting):
            self._victim_targeting = value
        else:
            raise ValueError('value must be instance of VictimTargeting')

    @property
    def handling(self):
        return self._handling

    @handling.setter
    def handling(self, value):
        if value and not isinstance(value, Marking):
            raise ValueError('value must be instance of Marking')

        self._handling = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(TTP, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.idref = self.idref
        return_obj.timestamp = utils.dates.serialize_value(self.timestamp)
        return_obj.version = self.version
        return_obj.Title = self.title

        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.short_description:
            return_obj.Short_Description = self.short_description.to_obj(ns_info=ns_info)
        if self.behavior:
            return_obj.Behavior = self.behavior.to_obj(ns_info=ns_info)
        if self.related_ttps:
            return_obj.Related_TTPs = self.related_ttps.to_obj(ns_info=ns_info)
        if self.exploit_targets:
            return_obj.Exploit_Targets = self.exploit_targets.to_obj(ns_info=ns_info)
        if self.information_source:
            return_obj.Information_Source = self.information_source.to_obj(ns_info=ns_info)
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

        return_obj.id_ = obj.id
        return_obj.idref = obj.idref
        return_obj.timestamp = obj.timestamp

        if isinstance(obj, cls._binding_class): # TTPType properties
            return_obj.version = obj.version
            return_obj.title = obj.Title
            return_obj.description = StructuredText.from_obj(obj.Description)
            return_obj.short_description = StructuredText.from_obj(obj.Short_Description)
            return_obj.behavior = Behavior.from_obj(obj.Behavior)
            return_obj.related_ttps = RelatedTTPs.from_obj(obj.Related_TTPs)
            return_obj.exploit_targets = ExploitTargets.from_obj(obj.Exploit_Targets)
            return_obj.information_source = InformationSource.from_obj(obj.Information_Source)
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

        get = dict_repr.get
        
        return_obj.id_ = get('id')
        return_obj.idref = get('idref')
        return_obj.timestamp = get('timestamp')
        return_obj.version = get('version')
        return_obj.title = get('title')
        return_obj.description = StructuredText.from_dict(get('description'))
        return_obj.short_description = StructuredText.from_dict(get('short_description'))
        return_obj.behavior = Behavior.from_dict(get('behavior'))
        return_obj.related_ttps = RelatedTTPs.from_dict(get('related_ttps'))
        return_obj.exploit_targets = ExploitTargets.from_dict(get('exploit_targets'))
        return_obj.information_source = InformationSource.from_dict(get('information_source'))
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
