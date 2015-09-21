# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
from stix.common import EncodedCDATA, StructuredTextList, VocabString
from stix.coa.structured_coa import _BaseStructuredCOA

# bindings
import stix.bindings.extensions.structured_coa.generic as generic_structured_coa_binding
from stix.base import ElementField

@stix.register_extension
class GenericStructuredCOA(_BaseStructuredCOA):
    _namespace = "http://stix.mitre.org/extensions/StructuredCOA#Generic-1"
    _binding = generic_structured_coa_binding
    _binding_class = _binding.GenericStructuredCOAType
    _XSI_TYPE = "genericStructuredCOA:GenericStructuredCOAType"

    specification = ElementField("Specification", EncodedCDATA)

    def __init__(self, id_=None, idref=None):
        super(GenericStructuredCOA, self).__init__(id_=id_, idref=idref)
        self.reference_location = None
        self.description = None
        self.type_ = None
        self.specification = None

    @property
    def specification(self):
        return self._specification

    @specification.setter
    def specification(self, value):
        self._set_var(EncodedCDATA, specification=value)

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
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, value):
        self._set_vocab(type=value)

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(GenericStructuredCOA, cls).from_obj(obj, return_obj)
        return_obj.reference_location = obj.reference_location
        return_obj.descriptions = StructuredTextList.from_obj(obj.Description)
        return_obj.type_ = VocabString.from_obj(obj.Type)
        return_obj.specification = EncodedCDATA.from_obj(obj.Specification)

        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(GenericStructuredCOA, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        if self.reference_location:
            return_obj.reference_location = self.reference_location
        if self.descriptions:
            return_obj.Description = self.descriptions.to_obj(ns_info=ns_info)
        if self.type_:
            return_obj.Type = self.type_.to_obj(ns_info=ns_info)
        if self.specification:
            return_obj.Specification = self.specification.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()

        super(GenericStructuredCOA, cls).from_dict(d, return_obj)
        return_obj.reference_location = d.get('reference_location')
        return_obj.descriptions = StructuredTextList.from_dict(d.get('description'))
        return_obj.type_ = VocabString.from_dict(d.get('type'))
        return_obj.specification = EncodedCDATA.from_dict(d.get('specification'))

        return return_obj

    def to_dict(self):
        return super(GenericStructuredCOA, self).to_dict()

