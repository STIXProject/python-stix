# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix.common import StructuredText, Confidence
import stix.bindings.course_of_action as coa_binding

class Objective(stix.Entity):
    _binding = coa_binding
    _binding_class = coa_binding.ObjectiveType
    _namespace = "http://stix.mitre.org/CourseOfAction-1"
    
    def __init__(self, description=None, short_description=None):
        self.description = description
        self.short_description = short_description
        self.applicability_confidence = None

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

    def to_obj(self, return_obj=None, ns_info=None):
        super(Objective, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.short_description:
            return_obj.Short_Description = self.short_description.to_obj(ns_info=ns_info)
        if self.applicability_confidence:
            return_obj.Applicability_Confidence = self.applicability_confidence.to_obj(ns_info=ns_info)

        return return_obj

    @property
    def applicability_confidence(self):
        return self._applicability_confidence
    
    @applicability_confidence.setter
    def applicability_confidence(self, value):
        if not value:
            self._applicability_confidence = None
        elif isinstance(value, Confidence):
            self._applicability_confidence = value
        else:
            raise ValueError('Cannot set applicability_confidence to type %s' % type(value))

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.description = StructuredText.from_obj(obj.Description)
        return_obj.short_description = StructuredText.from_obj(obj.Short_Description)
        return_obj.applicability_confidence = Confidence.from_obj(obj.Applicability_Confidence)
        return return_obj

    def to_dict(self):
        return super(Objective, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))
        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))
        return_obj.applicability_confidence = Confidence.from_dict(dict_repr.get('applicability_confidence'))
        
        return return_obj
