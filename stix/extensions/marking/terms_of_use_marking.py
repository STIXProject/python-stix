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

    def to_obj(self):
        obj = self._binding_class()

        MarkingStructure.to_obj(self, obj)

        obj.set_Terms_Of_Use(self.terms_of_use)

        return obj

    def to_dict(self):
        d = MarkingStructure.to_dict(self)
        if self.terms_of_use:
            d['terms_of_use'] = self.terms_of_use

        return d

    @staticmethod
    def from_obj(obj):
        if not obj:
            return None

        m = TermsOfUseMarkingStructure()
        MarkingStructure.from_obj(obj, m)
        m.terms_of_use = obj.get_Terms_Of_Use()

        return m

    @staticmethod
    def from_dict(marking_dict):
        if not marking_dict:
            return None

        m = TermsOfUseMarkingStructure()
        MarkingStructure.from_dict(marking_dict, m)
        m.terms_of_use = marking_dict.get('terms_of_use')

        return m


stix.data_marking.add_extension(TermsOfUseMarkingStructure)

