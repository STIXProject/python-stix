import stix
from stix.bindings import stix_common as stix_common_binding


class Profiles(stix.Entity):
    _binding = stix_common_binding
    _binding_class = stix_common_binding.ProfilesType
    _namespace = 'http://stix.mitre.org/common-1'

    # Fields
    profile = stix.ElementField("Profile", multiple=True)

    def __init__(self, profiles=None):
        super(Profiles, self).__init__()
        self.profile = profiles

    def __iter__(self):
       for x in self.profile:
           yield x

    def __getitem__(self, item):
        return self.profile[item]

    def __setitem__(self, key, value):
        self.profile[key] = value

    def __delitem__(self, key):
        del self.profile[key]

    def to_dict(self):
        return [x for x in self.profile]

    @classmethod
    def from_dict(cls, cls_dict=None, return_obj=None):
        if not cls_dict:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.profile = [x for x in cls_dict]

        return return_obj
