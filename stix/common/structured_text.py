# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.stix_common as stix_common_binding


class StructuredText(stix.Entity):
    _binding = stix_common_binding
    _binding_class = _binding.StructuredTextType
    _namespace = 'http://stix.mitre.org/common-1'

    def __init__(self, value=None):
        self.id_ = None
        self.value = value
        self.structuring_format = None
        self.ordinality = None

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(StructuredText, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        return_obj.id = self.id_
        return_obj.valueOf_ = self.value
        return_obj.ordinality = self.ordinality
        return_obj.structuring_format = self.structuring_format

        return return_obj

    def is_plain(self):
        plain = (
            (not self.id_) and
            (not self.structuring_format) and
            (self.ordinality in (1, None))
        )

        return plain

    def to_dict(self):
        # Return a plain string if there is no format specified.
        if self.is_plain():
            return self.value
        else:
            return super(StructuredText, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.id
        return_obj.value = obj.valueOf_
        return_obj.ordinality = obj.ordinality
        return_obj.structuring_format = obj.structuring_format

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        if not isinstance(d, dict):
            return_obj.value = d
        else:
            return_obj.id_ = d.get('id')
            return_obj.value = d.get('value')
            return_obj.ordinality = d.get('ordinality')
            return_obj.structuring_format = d.get('structuring_format')

        return return_obj
    
    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        return unicode(self.value)


class StructuredTextList(stix.TypedList):
    _contained_type = StructuredText

    def __iter__(self):
        return sorted(self._inner, key=lambda x: x.ordinality)

    def __getitem__(self, item):
        pass

    def __setitem__(self, key, value):
        pass
