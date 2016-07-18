# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox.cache import Cached

# internal
import stix
from stix.bindings import course_of_action as coa_binding


class _BaseStructuredCOA(Cached, stix.Entity):
    _namespace = "http://stix.mitre.org/CourseOfAction-1"
    _binding = coa_binding
    _binding_class = coa_binding.StructuredCOAType

    def __init__(self, id_=None, idref=None):
        self.id_ = id_
        self.idref = idref

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        # Registers the class extension
        import stix.extensions.structured_coa.generic_structured_coa  # noqa

        if not return_obj:
            klass = stix.lookup_extension(obj)
            return_obj = klass.from_obj(obj)
        else:
            return_obj.id_ = obj.id_
            return_obj.idref = obj.idref

        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        super(_BaseStructuredCOA, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.idref = self.idref
        return_obj.xsi_type = self._XSI_TYPE

        return return_obj

    @staticmethod
    def lookup_class(xsi_type):
        if not xsi_type:
            raise ValueError("xsi:type is required")

        return stix.lookup_extension(xsi_type)

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        import stix.extensions.structured_coa.generic_structured_coa  # noqa

        if not return_obj:
            klass = stix.lookup_extension(d.get('xsi:type'))
            return_obj = klass.from_dict(d)
        else:
            return_obj.id_ = d.get('id')
            return_obj.idref = d.get('idref')

        return return_obj

    def to_dict(self):
        d = super(_BaseStructuredCOA, self).to_dict()
        d['xsi:type'] = self._XSI_TYPE  # added by subclass
        return d


# Backwards compatibility
add_extension = stix.add_extension
