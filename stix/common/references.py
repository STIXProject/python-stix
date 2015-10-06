# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
import collections

from mixbox import fields

import stix
from stix.bindings import stix_common as stix_common_binding


class References(collections.MutableSequence, stix.Entity):
    _binding = stix_common_binding
    _binding_class = stix_common_binding.ReferencesType
    _namespace = 'http://stix.mitre.org/common-1'

    # Fields
    reference = fields.TypedField("Reference", multiple=True)

    def __init__(self, references=None):
        super(References, self).__init__()
        self.reference = references

    def __len__(self):
        return self.reference.__len__()

    def __getitem__(self, item):
        return self.reference.__getitem__(item)

    def __setitem__(self, key, value):
        self.reference.__setitem__(key, value)

    def __delitem__(self, key):
        self.reference.__delitem__(key)

    def insert(self, index, value):
        self.reference.insert(index, value)

    def to_dict(self):
        return [x for x in self]

    @classmethod
    def from_dict(cls, cls_dict=None):
        if not cls_dict:
            return None

        obj = cls()
        obj.reference = [x for x in cls_dict]
        return obj