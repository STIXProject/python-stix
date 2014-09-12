# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix.utils import dates
import stix.bindings.ttp as ttp_binding
from stix.common import StructuredText, VocabString, InformationSource, Statement
from stix.common.vocabs import IntendedEffect
from stix.data_marking import Marking
from .behavior import Behavior
from .resource import Resource
from .victim_targeting import VictimTargeting
from datetime import datetime
from dateutil.tz import tzutc

class TTP(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.TTPType
    _namespace = "http://stix.mitre.org/TTP-1"
    _version = "1.1.1"

    def __init__(self, id_=None, idref=None, timestamp=None, title=None, description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("ttp")
        self.idref = idref
        self.version = self._version
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
            self.timestamp = datetime.now(tzutc()) if not idref else None

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
        self._timestamp = dates.parse_value(value)

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
        self._intended_effects = []

        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_intended_effect(v)
        else:
            self.add_intended_effect(value)

    def add_intended_effect(self, value):
        if not value:
            return
        elif isinstance(value, Statement):
            self.intended_effects.append(value)
        else:
            intended_effect = IntendedEffect(value)
            self.intended_effects.append(Statement(value=intended_effect))

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

        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref)
        return_obj.set_timestamp(dates.serialize_value(self.timestamp))
        return_obj.set_version(self.version)
        return_obj.set_Title(self.title)

        if self.description:
            return_obj.set_Description(self.description.to_obj(ns_info=ns_info))
        if self.short_description:
            return_obj.set_Short_Description(self.short_description.to_obj(ns_info=ns_info))
        if self.behavior:
            return_obj.set_Behavior(self.behavior.to_obj(ns_info=ns_info))
        if self.related_ttps:
            return_obj.set_Related_TTPs(self.related_ttps.to_obj(ns_info=ns_info))
        if self.exploit_targets:
            return_obj.set_Exploit_Targets(self.exploit_targets.to_obj(ns_info=ns_info))
        if self.information_source:
            return_obj.set_Information_Source(self.information_source.to_obj(ns_info=ns_info))
        if self.intended_effects:
            return_obj.set_Intended_Effect([x.to_obj(ns_info=ns_info) for x in self.intended_effects])
        if self.resources:
            return_obj.set_Resources(self.resources.to_obj(ns_info=ns_info))
        if self.victim_targeting:
            return_obj.set_Victim_Targeting(self.victim_targeting.to_obj(ns_info=ns_info))
        if self.handling:
            return_obj.set_Handling(self.handling.to_obj(ns_info=ns_info))

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.get_id()
        return_obj.idref = obj.get_idref()
        return_obj.timestamp = obj.get_timestamp()

        if isinstance(obj, cls._binding_class): # TTPType properties
            return_obj.version = obj.get_version() or cls._version
            return_obj.title = obj.get_Title()
            return_obj.description = StructuredText.from_obj(obj.get_Description())
            return_obj.short_description = StructuredText.from_obj(obj.get_Short_Description())
            return_obj.behavior = Behavior.from_obj(obj.get_Behavior())
            return_obj.related_ttps = RelatedTTPs.from_obj(obj.get_Related_TTPs())
            return_obj.exploit_targets = ExploitTargets.from_obj(obj.get_Exploit_Targets())
            return_obj.information_source = InformationSource.from_obj(obj.get_Information_Source())
            return_obj.resources = Resource.from_obj(obj.get_Resources())
            return_obj.victim_targeting = VictimTargeting.from_obj(obj.get_Victim_Targeting())
            return_obj.handling = Marking.from_obj(obj.get_Handling())

            if obj.get_Intended_Effect():
                return_obj.intended_effects = [Statement.from_obj(x) for x in obj.get_Intended_Effect()]

        return return_obj

    def to_dict(self):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.idref:
            d['idref'] = self.idref
        if self.timestamp:
            d['timestamp'] = dates.serialize_value(self.timestamp)
        if self.version:
            d['version'] = self.version or self._version
        if self.title:
            d['title'] = self.title
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
        if self.behavior:
            d['behavior'] = self.behavior.to_dict()
        if self.related_ttps:
            d['related_ttps'] = self.related_ttps.to_dict()
        if self.exploit_targets:
            d['exploit_targets'] = self.exploit_targets.to_dict()
        if self.information_source:
            d['information_source'] = self.information_source.to_dict()
        if self.intended_effects:
            d['intended_effects'] = [x.to_dict() for x in self.intended_effects]
        if self.resources:
            d['resources'] = self.resources.to_dict()
        if self.victim_targeting:
            d['victim_targeting'] = self.victim_targeting.to_dict()
        if self.handling:
            d['handling'] = self.handling.to_dict()

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = dict_repr.get('id')
        return_obj.idref = dict_repr.get('idref')
        return_obj.timestamp = dict_repr.get('timestamp')
        return_obj.version = dict_repr.get('version', cls._version)
        return_obj.title = dict_repr.get('title')
        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))
        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))
        return_obj.behavior = Behavior.from_dict(dict_repr.get('behavior'))
        return_obj.related_ttps = RelatedTTPs.from_dict(dict_repr.get('related_ttps'))
        return_obj.exploit_targets = ExploitTargets.from_dict(dict_repr.get('exploit_targets'))
        return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))
        return_obj.intended_effects = [Statement.from_dict(x) for x in dict_repr.get('intended_effects', [])]
        return_obj.resources = Resource.from_dict(dict_repr.get('resources'))
        return_obj.victim_targeting = VictimTargeting.from_dict(dict_repr.get('victim_targeting'))
        return_obj.handling = Marking.from_dict(dict_repr.get('handling'))

        return return_obj

# Avoid circular imports
from .related_ttps import RelatedTTPs
from .exploit_targets import ExploitTargets
