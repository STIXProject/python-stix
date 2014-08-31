# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import VocabString, Identity
from cybox.core import Observables
import stix.bindings.ttp as ttp_binding
from stix.common.vocabs import SystemType, InformationType

class VictimTargeting(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.VictimTargetingType
    _namespace = "http://stix.mitre.org/TTP-1"

    def __init__(self):
        self.identity = None
        self.targeted_systems = None
        self.targeted_information = None
        self.targeted_technical_details = None

    @property
    def targeted_systems(self):
        return self._targeted_systems

    @targeted_systems.setter
    def targeted_systems(self, value):
        self._targeted_systems = TargetedSystems()
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_targeted_system(v)
        else:
            self.add_targeted_system(value)

    def add_targeted_system(self, system):
        if not system:
            return
        elif isinstance(system, VocabString):
            self._targeted_systems.append(system)
        else:
            self._targeted_systems.append(SystemType(value=system))

    @property
    def targeted_information(self):
        return self._targeted_information

    @targeted_information.setter
    def targeted_information(self, value):
        self._targeted_information = TargetedInformation()
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_targeted_information(v)
        else:
            self.add_targeted_information(value)

    def add_targeted_information(self, targeted_information):
        if not targeted_information:
            return
        elif isinstance(targeted_information, VocabString):
            self._targeted_information.append(targeted_information)
        else:
            self._targeted_information.append(InformationType(value=targeted_information))

    @property
    def targeted_technical_details(self):
        return self._targeted_technical_details

    @targeted_technical_details.setter
    def targeted_technical_details(self, value):
        if not value:
            self._targeted_technical_details = None
        elif isinstance(value, Observables):
            self._targeted_technical_details = value
        else:
            self._targeted_technical_details = Observables(observables=[value])

    def _to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        if self.identity:
            return_obj.set_Identity(self.identity.to_obj(ns_info=ns_info))
        if self.targeted_information:
            return_obj.set_Targeted_Information([x.to_obj(ns_info=ns_info) for x in self.targeted_information])
        if self.targeted_systems:
            return_obj.set_Targeted_Systems([x.to_obj(ns_info=ns_info) for x in self.targeted_systems])
        if self.targeted_technical_details:
            return_obj.set_Targeted_Technical_Details(self.targeted_technical_details.to_obj(ns_info=ns_info))

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.identity = Identity.from_obj(obj.get_Identity())
        return_obj.targeted_technical_details = Observables.from_obj(obj.get_Targeted_Technical_Details())

        if obj.get_Targeted_Systems():
            return_obj.targeted_systems = [VocabString.from_obj(x) for x in obj.get_Targeted_Systems()]
        if obj.get_Targeted_Information():
            return_obj.targeted_information = [VocabString.from_obj(x) for x in obj.get_Targeted_Information()]

        return return_obj

    def to_dict(self):
        d = {}
        if self.identity:
            d['identity'] = self.identity.to_dict()
        if self.targeted_systems:
            d['targeted_systems']  = [x.to_dict() for x in self.targeted_systems]
        if self.targeted_information:
            d['targeted_information'] = [x.to_dict() for x in self.targeted_information]
        if self.targeted_technical_details:
            d['targeted_technical_details'] = self.targeted_technical_details.to_dict()

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.identity = Identity.from_dict(dict_repr.get('identity'))
        return_obj.targeted_systems = [VocabString.from_dict(x) for x in dict_repr.get('targeted_systems', [])]
        return_obj.targeted_information = [VocabString.from_dict(x) for x in dict_repr.get('targeted_information', [])]
        return_obj.targeted_technical_details = Observables.from_dict(dict_repr.get('targeted_technical_details'))

        return return_obj


class TargetedSystems(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _contained_type = VocabString

    def _fix_value(self, value):
        return SystemType(value)


class TargetedInformation(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _contained_type = VocabString

    def _fix_value(self, value):
        return InformationType(value)
