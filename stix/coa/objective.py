# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import StructuredTextList, Confidence
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
        """A single description about the contents or purpose of this object.

        Default Value: ``None``

        Note:
            If this object has more than one description set, this will return
            the description with the lowest ordinality value.

        Returns:
            An instance of
            :class:`.StructuredText`

        """
        return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        self.descriptions = value

    @property
    def descriptions(self):
        """A :class:`.StructuredTextList` object, containing descriptions about
        the purpose or intent of this object.

        This is typically used for the purpose of providing multiple
        descriptions with different classificaton markings.

        Iterating over this object will yield its contents sorted by their
        ``ordinality`` value.

        Default Value: Empty :class:`.StructuredTextList` object.

        Note:
            IF this is set to a value that is not an instance of
            :class:`.StructuredText`, an effort will ne made to convert it.
            If this is set to an iterable, any values contained that are not
            an instance of :class:`.StructuredText` will be be converted.

        Returns:
            An instance of
            :class:`.StructuredTextList`

        """
        return self._description

    @descriptions.setter
    def descriptions(self, value):
        self._description = StructuredTextList(value)

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        self.descriptions.add(description)

    @property
    def short_description(self):
        """A single short description about the contents or purpose of this
        object.

        Default Value: ``None``

        Note:
            If this object has more than one short description set, this will
            return the description with the lowest ordinality value.

        Returns:
            An instance of :class:`.StructuredText`

        """
        return next(iter(self.short_descriptions), None)

    @short_description.setter
    def short_description(self, value):
        self.short_descriptions = value

    @property
    def short_descriptions(self):
        """A :class:`.StructuredTextList` object, containing short descriptions
        about the purpose or intent of this object.

        This is typically used for the purpose of providing multiple
        short descriptions with different classificaton markings.

        Iterating over this object will yield its contents sorted by their
        ``ordinality`` value.

        Default Value: Empty :class:`.StructuredTextList` object.

        Note:
            IF this is set to a value that is not an instance of
            :class:`.StructuredText`, an effort will ne made to convert it.
            If this is set to an iterable, any values contained that are not
            an instance of :class:`.StructuredText` will be be converted.

        Returns:
            An instance of :class:`.StructuredTextList`

        """
        return self._short_description

    @short_descriptions.setter
    def short_descriptions(self, value):
        self._short_description = StructuredTextList(value)

    def add_short_description(self, description):
        """Adds a description to the ``short_descriptions`` collection.

        This is the same as calling "foo.short_descriptions.add(bar)".

        """
        self.short_descriptions.add(description)

    @property
    def applicability_confidence(self):
        return self._applicability_confidence
    
    @applicability_confidence.setter
    def applicability_confidence(self, value):
        self._set_var(Confidence, try_cast=False, applicability_confidence=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(Objective, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.descriptions:
            return_obj.Description = self.descriptions.to_obj(ns_info=ns_info)
        if self.short_descriptions:
            return_obj.Short_Description = self.short_descriptions.to_obj(ns_info=ns_info)
        if self.applicability_confidence:
            return_obj.Applicability_Confidence = self.applicability_confidence.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.descriptions = StructuredTextList.from_obj(obj.Description)
        return_obj.short_descriptions = StructuredTextList.from_obj(obj.Short_Description)
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

        get = dict_repr.get
        return_obj.description = StructuredTextList.from_dict(get('description'))
        return_obj.short_description = StructuredTextList.from_dict(get('short_description'))
        return_obj.applicability_confidence = Confidence.from_dict(get('applicability_confidence'))
        
        return return_obj
