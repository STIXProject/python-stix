# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.stix_common as stix_common_binding


class StructuredText(stix.Entity):
    _binding = stix_common_binding
    _namespace = 'http://stix.mitre.org/common-1'

    def __init__(self, value=None):
        self.value = value
        self.structuring_format = None

    def to_obj(self, return_obj=None, ns_info=None):
        super(StructuredText, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        text_obj = self._binding.StructuredTextType()

        text_obj.valueOf_ = self.value
        if self.structuring_format is not None:
            text_obj.structuring_format = self.structuring_format
        return text_obj

    def to_dict(self):
        # Return a plain string if there is no format specified.
        if self.structuring_format is None:
            return self.value
        else:
            return super(StructuredText, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.value = obj.valueOf_
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
            return_obj.value = d.get('value')
            return_obj.structuring_format = d.get('structuring_format')

        return return_obj
    
    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        return unicode(self.value)
