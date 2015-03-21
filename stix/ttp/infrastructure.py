# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from cybox.core import Observables

# internal
import stix
from stix.common import StructuredText, VocabString
from stix.common.vocabs import AttackerInfrastructureType
import stix.bindings.ttp as ttp_binding


class Infrastructure(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.InfrastructureType
    _namespace = "http://stix.mitre.org/TTP-1"

    def __init__(self, id_=None, title=None, description=None, short_description=None):
        self.id_ = id_
        self.title = title
        self.description = description
        self.short_description = short_description
        self.types = None
        self.observable_characterization = None

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
        self._set_var(StructuredText, description=value)

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, value):
        self._set_var(StructuredText, short_description=value)

    @property
    def types(self):
        return self._types

    @types.setter
    def types(self, value):
        self._types = InfraStructureTypes(value)

    def add_type(self, type_):
        self.types.append(type_)

    @property
    def observable_characterization(self):
        return self._observable_characterization

    @observable_characterization.setter
    def observable_characterization(self, value):
        self._set_var(Observables, observable_characterization=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(Infrastructure, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.Title = self.title

        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.short_description:
            return_obj.Short_Description = self.short_description.to_obj(ns_info=ns_info)
        if self.types:
            return_obj.Type = [x.to_obj(ns_info=ns_info) for x in self.types]
        if self.observable_characterization:
            return_obj.Observable_Characterization = self.observable_characterization.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.id
        return_obj.title = obj.Title
        return_obj.description = StructuredText.from_obj(obj.Description)
        return_obj.short_description = StructuredText.from_obj(obj.Short_Description)
        return_obj.observable_characterization = Observables.from_obj(obj.Observable_Characterization)

        if obj.Type:
            return_obj.types = [VocabString.from_obj(x) for x in obj.Type]

        return return_obj

    def to_dict(self):
        return super(Infrastructure, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = dict_repr.get('id')
        return_obj.title = dict_repr.get('title')
        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))
        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))
        return_obj.types = [VocabString.from_dict(x) for x in dict_repr.get('types', [])]
        return_obj.observable_characterization = Observables.from_dict(dict_repr.get('observable_characterization'))

        return return_obj


class InfraStructureTypes(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _contained_type = VocabString
    _dict_as_list = True

    def _fix_value(self, value):
        return AttackerInfrastructureType(value)
