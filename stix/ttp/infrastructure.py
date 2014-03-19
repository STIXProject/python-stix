# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix.common import StructuredText, VocabString
from cybox.core import Observables, Observable, Object
import stix.bindings.ttp as ttp_binding

class AttackerInfrastructureType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:AttackerInfrastructureTypeVocab-1.0'

class Infrastructure(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.InfrastructureType
    _namespace = "http://stix.mitre.org/TTP-1"

    def __init__(self, id_=None, title=None, description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("infrastructure")
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
    def types(self):
        return self._types

    @types.setter
    def types(self, value):
        self._types = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_type(v)
        else:
            self.add_type(value)

    def add_type(self, type_):
        if not type_:
            return
        elif isinstance(type_, AttackerInfrastructureType):
            self._types.append(type_)
        else:
            self._types.append(AttackerInfrastructureType(value=type_))

    @property
    def observable_characterization(self):
        return self._observable_characterization

    @observable_characterization.setter
    def observable_characterization(self, value):
        if not value:
            self._observable_characterization = None
        elif isinstance(value, Observables):
            self._observable_characterization = value
        else:
            self._observable_characterization = Observables(observables=[value])

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        return_obj.set_id(self.id_)
        return_obj.set_Title(self.title)

        if self.description:
            return_obj.set_Description(self.description.to_obj())
        if self.short_description:
            return_obj.set_Short_Description(self.short_description.to_obj())
        if self.types:
            return_obj.set_Type([x.to_obj() for x in self.types])
        if self.observable_characterization:
            return_obj.set_Observable_Characterization(self.observable_characterization.to_obj())

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.get_id()
        return_obj.title = obj.get_Title()
        return_obj.description = StructuredText.from_obj(obj.get_Description())
        return_obj.short_description = StructuredText.from_obj(obj.get_Short_Description())
        return_obj.observable_characterization = Observables.from_obj(obj.get_Observable_Characterization())

        if obj.get_Type():
            return_obj.types = [AttackerInfrastructureType.from_obj(x) for x in obj.get_Type()]

        return return_obj

    def to_dict(self):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.title:
            d['title'] = self.title
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
        if self.types:
            d['types'] = [x.to_dict() for x in self.types]
        if self.observable_characterization:
            d['observable_characterization'] = self.observable_characterization.to_dict()

        return d

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
        return_obj.types = [AttackerInfrastructureType.from_dict(x) for x in dict_repr.get('types', [])]
        return_obj.observable_characterization = Observables.from_dict(dict_repr.get('observable_characterization'))

        return return_obj
