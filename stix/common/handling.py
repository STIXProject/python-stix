
import stix

from stix.bindings.data_marking import MarkingSpecificationType, MarkingStructureType, MarkingType
from stix.bindings.extensions.marking.tlp import TLPMarkingStructureType
from stix.bindings.extensions.marking.simple_marking import SimpleMarkingStructureType
from stix.common.structured_text import StructuredText

import stix.bindings.data_marking as stix_data_marking_binding


class Handling(stix.Entity):
    _binding = stix_data_marking_binding
    _namespace = 'http://data-marking.mitre.org/Marking-1'
    
    def __init__(self, marking=None):
        self.marking = marking

    @property
    def marking(self):
        return self._marking

    @marking.setter
    def marking(self, value):
        #if value and not isinstance(value, MarkingType):
        #    raise ValueError('value must be instance of MarkingType')

        self._marking = value

    def to_obj(self, return_obj=None):
        if return_obj == None:
            return_obj = stix_data_marking_binding.MarkingType()

        if self.marking:
            return_obj.set_Marking(self.marking)
        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj=cls()

        if obj.get_Marking():
            marking_obj = obj.get_Marking()
            return_obj.marking = MarkingType.from_obj(obj.get_Marking())
        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        marking_list = dict_repr.get('marking')

        if marking_list:
            return_obj.marking = MarkingType.from_list(marking_list)

        return return_obj

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}

        if self.marking:
            return_dict['marking'] = self.marking.to_list()

        return return_dict
