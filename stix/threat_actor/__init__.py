# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.


from datetime import datetime

import dateutil

import stix
import stix.bindings.threat_actor as threat_actor_binding
from stix.common import Confidence, Identity, InformationSource, Statement, StructuredText, VocabString
from stix.data_marking import Marking
import stix.utils


class ThreatActor(stix.Entity):
    _binding = threat_actor_binding
    _binding_class = threat_actor_binding.ThreatActorType
    _namespace = 'http://stix.mitre.org/ThreatActor-1'
    _version = "1.1"

    def __init__(self):
        self.id_ = stix.utils.create_id("threatactor")
        self.idref = None
        self.timestamp = None
        self.version = self._version
        self.title = None
        self.description = None
        self.short_description = None
        self.identity = None
        self.type_ = []
        self.motivation = []
        self.sophistication = []
        self.intended_effect = []
        self.planning_and_operational_support = []
        self.handling = None
        self.confidence = None
        self.information_source = None
        # TODO: implement
        # - Observed_TTPs
        # - Associated_Campaigns
        # - Associated_Actors
        # - Related_Packages

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if not value:
            self._timestamp = None
        elif isinstance(value, datetime):
            self._timestamp =  value
        else:
            self._timestamp = dateutil.parser.parse(value)

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref)
        if self.timestamp:
           return_obj.set_timestamp(self.timestamp.isoformat())
        return_obj.set_version(self.version)
        return_obj.set_Title(self.title)
        if self.description:
            return_obj.set_Description(self.description.to_obj())
        if self.short_description:
            return_obj.set_Short_Description(self.short_description.to_obj())
        if self.identity:
            return_obj.set_Identity(self.identity.to_obj())
        if self.type_:
            return_obj.set_Type([x.to_obj() for x in self.type_])
        if self.motivation:
            return_obj.set_Motivation([x.to_obj() for x in self.motivation])
        if self.sophistication:
            return_obj.set_Sophistication([x.to_obj() for x in self.sophistication])
        if self.intended_effect:
            return_obj.set_Intended_Effect([x.to_obj() for x in self.intended_effect])
        if self.planning_and_operational_support:
            return_obj.set_Planning_And_Operational_Support([x.to_obj()
                    for x in self.planning_and_operational_support])
        if self.handling:
            return_obj.set_Handling(self.handling.to_obj())
        if self.confidence:
            return_obj.set_Confidence(self.confidence.to_obj())
        if self.information_source:
            return_obj.set_Information_Source(self.information_source.to_obj())

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
        return_obj.version = obj.get_version() if obj.get_version() else cls._version
        return_obj.title = obj.get_Title()
        return_obj.description = StructuredText.from_obj(obj.get_Description())
        return_obj.short_description = StructuredText.from_obj(obj.get_Short_Description())
        return_obj.identity = Identity.from_obj(obj.get_Identity())
        return_obj.type_ = [Statement.from_obj(x) for x in obj.get_Type()]
        return_obj.motivation = [Statement.from_obj(x) for x in obj.get_Motivation()]
        return_obj.sophistication = [Statement.from_obj(x) for x in obj.get_Sophistication()]
        return_obj.intended_effect = [Statement.from_obj(x) for x in obj.get_Intended_Effect()]
        return_obj.planning_and_operational_support = [Statement.from_obj(x)
                for x in obj.get_Planning_And_Operational_Support()]
        return_obj.handling = Marking.from_obj(obj.get_Handling())
        return_obj.confidence = Confidence.from_obj(obj.get_Confidence())
        return_obj.information_source = InformationSource.from_obj(obj.get_Information_Source())

        return return_obj

    def to_dict(self):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.idref:
            d['idref'] = self.idref
        if self.timestamp:
            d['timestamp'] = self.timestamp.isoformat()
        if self.version:
            d['version'] = self.version
        if self.title:
            d['title'] = self.title
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
        if self.identity:
            d['identity'] = self.identity.to_dict()
        if self.type_:
            d['type'] = [x.to_dict() for x in self.type_]
        if self.motivation:
            d['motivation'] = [x.to_dict() for x in self.motivation]
        if self.sophistication:
            d['sophistication'] = [x.to_dict() for x in self.sophistication]
        if self.intended_effect:
            d['intended_effect'] = [x.to_dict() for x in self.intended_effect]
        if self.planning_and_operational_support:
            d['planning_and_operational_support'] = [x.to_dict()
                    for x in self.planning_and_operational_support]
        if self.handling:
            d['handling'] = self.handling.to_dict()
        if self.confidence:
            d['confidence'] = self.confidence.to_dict()
        if self.information_source:
            d['information_source'] = self.information_source.to_dict()

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
        return_obj.identity = Identity.from_dict(dict_repr.get('identity'))
        return_obj.type_ = [Statement.from_dict(x) for x in dict_repr.get('type', [])]
        return_obj.motivation = [Statement.from_dict(x) for x in dict_repr.get('motivation', [])]
        return_obj.sophistication = [Statement.from_dict(x) for x in dict_repr.get('sophistication', [])]
        return_obj.intended_effect = [Statement.from_dict(x) for x in dict_repr.get('intended_effect', [])]
        return_obj.planning_and_operational_support = [Statement.from_dict(x)
                for x in dict_repr.get('planning_and_operational_support', [])]
        return_obj.handling = Marking.from_dict(dict_repr.get('handling'))
        return_obj.confidence = Confidence.from_dict(dict_repr.get('confidence'))
        return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))

        return return_obj
