import stix.bindings.extensions.marking.tlp as tlp_binding
import stix.data_marking
from stix.data_marking import MarkingStructure


class TLPMarkingStructure(MarkingStructure):
    _binding = tlp_binding
    _binding_class = tlp_binding.TLPMarkingStructureType
    _namespace = 'http://data-marking.mitre.org/extensions/MarkingStructure#TLP-1'
    _XSI_TYPE = "tlpMarking:TLPMarkingStructureType"

    def __init__(self):
        super(TLPMarkingStructure, self).__init__()
        self.color = None

    def to_obj(self, return_obj=None, ns_info=None):
        super(TLPMarkingStructure, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        obj = self._binding_class()

        MarkingStructure.to_obj(self, return_obj=obj, ns_info=ns_info)

        obj.color = self.color

        return obj

    def to_dict(self):
        d = MarkingStructure.to_dict(self)
        if self.color:
            d['color'] = self.color

        return d

    @staticmethod
    def from_obj(obj):
        if not obj:
            return None

        m = TLPMarkingStructure()
        MarkingStructure.from_obj(obj, m)
        m.color = obj.color

        return m

    @staticmethod
    def from_dict(marking_dict):
        if not marking_dict:
            return None

        m = TLPMarkingStructure()
        MarkingStructure.from_dict(marking_dict, m)
        m.color = marking_dict.get('color')

        return m


stix.data_marking.add_extension(TLPMarkingStructure)

