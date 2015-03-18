# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix.bindings.extensions.marking.simple_marking as simple_marking_binding
import stix.data_marking
from stix.data_marking import MarkingStructure


class SimpleMarkingStructure(MarkingStructure):
    _binding = simple_marking_binding
    _binding_class = simple_marking_binding.SimpleMarkingStructureType
    _namespace = 'http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1'
    _XSI_TYPE = "simpleMarking:SimpleMarkingStructureType"

    def __init__(self, statement=None):
        super(SimpleMarkingStructure, self).__init__()
        self.statement = statement

    def to_obj(self, return_obj=None, ns_info=None):
        super(SimpleMarkingStructure, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        MarkingStructure.to_obj(self, return_obj=return_obj, ns_info=ns_info)
        return_obj.Statement = self.statement

        return return_obj

    def to_dict(self):
        d = MarkingStructure.to_dict(self)
        if self.statement:
            d['statement'] = self.statement

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        MarkingStructure.from_obj(obj, return_obj)
        return_obj.statement = obj.Statement

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        MarkingStructure.from_dict(d, return_obj=return_obj)
        return_obj.statement = d.get('statement')

        return return_obj


# Register extension
stix.data_marking.add_extension(SimpleMarkingStructure)
