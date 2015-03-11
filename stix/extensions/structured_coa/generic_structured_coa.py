# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.coa.structured_coa
from stix.common import EncodedCDATA, StructuredText, VocabString
from stix.coa.structured_coa import _BaseStructuredCOA
import stix.bindings.extensions.structured_coa.generic as generic_structured_coa_binding


class GenericStructuredCOA(_BaseStructuredCOA):
    _namespace = "http://stix.mitre.org/extensions/StructuredCOA#Generic-1"
    _binding = generic_structured_coa_binding
    _binding_class = _binding.GenericStructuredCOAType
    _XSI_TYPE = "genericStructuredCOA:GenericStructuredCOAType"

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
        return self._description

    @description.setter
    def description(self, value):
        self._set_var(StructuredText, description=value)

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
        return_obj.description = StructuredText.from_obj(obj.Description)
        return_obj.type_ = VocabString.from_obj(obj.Type)
        return_obj.specification = EncodedCDATA.from_obj(obj.Specification)

        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(GenericStructuredCOA, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        if self.reference_location:
            return_obj.reference_location = self.reference_location
        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
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
        return_obj.description = StructuredText.from_dict(d.get('description'))
        return_obj.type_ = VocabString.from_dict(d.get('type'))
        return_obj.specification = EncodedCDATA.from_dict(d.get('specification'))

        return return_obj

    def to_dict(self):
        return super(GenericStructuredCOA, self).to_dict()


# Register the extension
stix.coa.structured_coa.add_extension(GenericStructuredCOA)
