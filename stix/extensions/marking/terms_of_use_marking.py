# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix.bindings.extensions.marking.terms_of_use_marking as tou_marking_binding
import stix.data_marking
from stix.data_marking import MarkingStructure


class TermsOfUseMarkingStructure(MarkingStructure):
    _binding = tou_marking_binding
    _binding_class = tou_marking_binding.TermsOfUseMarkingStructureType
    _namespace = 'http://data-marking.mitre.org/extensions/MarkingStructure#Terms_Of_Use-1'
    _XSI_TYPE = "TOUMarking:TermsOfUseMarkingStructureType"

    def __init__(self, terms_of_use=None):
        super(TermsOfUseMarkingStructure, self).__init__()
        self.terms_of_use = terms_of_use

    def to_obj(self, return_obj=None, ns_info=None):
        super(TermsOfUseMarkingStructure, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        MarkingStructure.to_obj(self, return_obj=return_obj, ns_info=ns_info)
        return_obj.Terms_Of_Use = self.terms_of_use

        return return_obj

    def to_dict(self):
        d = MarkingStructure.to_dict(self)

        if self.terms_of_use:
            d['terms_of_use'] = self.terms_of_use

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        MarkingStructure.from_obj(obj, return_obj=return_obj)
        return_obj.terms_of_use = obj.Terms_Of_Use

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        MarkingStructure.from_dict(d, return_obj)
        return_obj.terms_of_use = d.get('terms_of_use')

        return return_obj


# Register extension
stix.data_marking.add_extension(TermsOfUseMarkingStructure)
