# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import collections

from mixbox import fields

import stix
from stix.bindings import stix_common as stix_common_binding


class Profiles(collections.MutableSequence, stix.Entity):
    _binding = stix_common_binding
    _binding_class = stix_common_binding.ProfilesType
    _namespace = 'http://stix.mitre.org/common-1'

    # Fields
    profile = fields.TypedField("Profile", multiple=True)

    def __init__(self, profiles=None):
        super(Profiles, self).__init__()
        self.profile = profiles

    def __len__(self):
        return self.profile.__len__()

    def __getitem__(self, item):
        return self.profile.__getitem__(item)

    def __setitem__(self, key, value):
        self.profile.__setitem__(key, value)

    def __delitem__(self, key):
        self.profile.__delitem__(key)

    def insert(self, index, value):
        self.profile.insert(index, value)

    def to_dict(self):
        return [x for x in self]

    @classmethod
    def from_dict(cls, cls_dict=None):
        if not cls_dict:
            return None

        obj = cls()
        obj.profile = [x for x in cls_dict]
        return obj
