# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import StructuredText
import stix.bindings.ttp as ttp_binding


class AttackPattern(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.AttackPatternType
    _namespace = "http://stix.mitre.org/TTP-1"

    def __init__(self, id_=None, title=None, description=None, short_description=None):
        self.id_ = id_
        self.capec_id = None
        self.title = title
        self.description = description
        self.short_description = short_description

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

    def to_obj(self, return_obj=None, ns_info=None):
        super(AttackPattern, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.capec_id = self.capec_id
        return_obj.Title = self.title

        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.short_description:
            return_obj.Short_Description = self.short_description.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.id
        return_obj.capec_id = obj.capec_id
        return_obj.title = obj.Title
        return_obj.description = StructuredText.from_obj(obj.Description)
        return_obj.short_description = StructuredText.from_obj(obj.Short_Description)

        return return_obj

    def to_dict(self):
        return super(AttackPattern, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = dict_repr.get('id')
        return_obj.capec_id = dict_repr.get('capec_id')
        return_obj.title = dict_repr.get('title')
        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))
        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))

        return return_obj
