# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from cybox.core import Observables

# internal
import stix
from stix.common import vocabs, VocabString, Identity
import stix.bindings.ttp as ttp_binding


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
        self._targeted_systems = TargetedSystems(value)

    def add_targeted_system(self, system):
        self._targeted_systems.append(system)

    @property
    def targeted_information(self):
        return self._targeted_information

    @targeted_information.setter
    def targeted_information(self, value):
        self._targeted_information = TargetedInformation(value)

    def add_targeted_information(self, targeted_information):
        self._targeted_information.append(targeted_information)

    @property
    def targeted_technical_details(self):
        return self._targeted_technical_details

    @targeted_technical_details.setter
    def targeted_technical_details(self, value):
        self._set_var(Observables, targeted_technical_details=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(VictimTargeting, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.identity:
            return_obj.Identity = self.identity.to_obj(ns_info=ns_info)
        if self.targeted_information:
            return_obj.Targeted_Information = self.targeted_information.to_obj(ns_info=ns_info)
        if self.targeted_systems:
            return_obj.Targeted_Systems = self.targeted_systems.to_obj(ns_info=ns_info)
        if self.targeted_technical_details:
            return_obj.Targeted_Technical_Details = self.targeted_technical_details.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.identity = Identity.from_obj(obj.Identity)
        return_obj.targeted_technical_details = Observables.from_obj(obj.Targeted_Technical_Details)
        return_obj.targeted_systems = TargetedSystems.from_obj(obj.Targeted_Systems)
        return_obj.targeted_information = TargetedInformation.from_obj(obj.Targeted_Information)

        return return_obj

    def to_dict(self):
        return super(VictimTargeting, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        get = dict_repr.get
        return_obj.identity = Identity.from_dict(get('identity'))
        return_obj.targeted_systems = TargetedSystems.from_dict(get('targeted_systems'))
        return_obj.targeted_information = TargetedInformation.from_dict(get('targeted_information'))
        return_obj.targeted_technical_details = Observables.from_dict(get('targeted_technical_details'))

        return return_obj


class TargetedSystems(stix.TypedList):
    _contained_type = VocabString

    def _fix_value(self, value):
        return vocabs.SystemType(value)


class TargetedInformation(stix.TypedList):
    _contained_type = VocabString

    def _fix_value(self, value):
        return vocabs.InformationType(value)
