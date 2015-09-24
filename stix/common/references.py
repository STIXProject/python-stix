import stix
from stix.bindings import stix_common as stix_common_binding


class References(stix.Entity):
    _binding = stix_common_binding
    _binding_class = stix_common_binding.ReferencesType
    _namespace = 'http://stix.mitre.org/common-1'

    # Fields
    reference = stix.ElementField("Reference", multiple=True)

    def __init__(self, references=None):
        super(References, self).__init__()
        self.reference = references

    def __iter__(self):
       for r in self.reference:
           yield r

    def __getitem__(self, item):
        return self.reference[item]

    def __setitem__(self, key, value):
        self.reference[key] = value

    def __delitem__(self, key):
        del self.reference[key]

    def to_dict(self):
        return [x for x in self.reference]

    @classmethod
    def from_dict(cls, cls_dict=None, return_obj=None):
        if not cls_dict:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.reference = [x for x in cls_dict]

        return return_obj
