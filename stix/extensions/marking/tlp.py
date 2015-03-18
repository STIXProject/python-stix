# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix.bindings.extensions.marking.tlp as tlp_binding
import stix.data_marking
from stix.data_marking import MarkingStructure


class TLPMarkingStructure(MarkingStructure):
    _binding = tlp_binding
    _binding_class = tlp_binding.TLPMarkingStructureType
    _namespace = 'http://data-marking.mitre.org/extensions/MarkingStructure#TLP-1'
    _XSI_TYPE = "tlpMarking:TLPMarkingStructureType"

    def __init__(self, color=None):
        super(TLPMarkingStructure, self).__init__()
        self.color = color

    def to_obj(self, return_obj=None, ns_info=None):
        super(TLPMarkingStructure, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        MarkingStructure.to_obj(self, return_obj=return_obj, ns_info=ns_info)
        return_obj.color = self.color

        return return_obj

    def to_dict(self):
        d = MarkingStructure.to_dict(self)
        if self.color:
            d['color'] = self.color

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        MarkingStructure.from_obj(obj, return_obj=return_obj)
        return_obj.color = obj.color

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        MarkingStructure.from_dict(d, return_obj)
        return_obj.color = d.get('color')

        return return_obj


# Register extension
stix.data_marking.add_extension(TLPMarkingStructure)
