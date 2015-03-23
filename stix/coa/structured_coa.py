# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.bindings import course_of_action as coa_binding


class _BaseStructuredCOA(stix.Entity):
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

        from stix.extensions.structured_coa.generic_structured_coa import GenericStructuredCOA   # noqa

        if not return_obj:
            klass = _BaseStructuredCOA.lookup_class(obj.xml_type)
            return_obj = klass.from_obj(obj)
        else:
            return_obj.id_ = obj.id
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
        for (k, v) in _EXTENSION_MAP.iteritems():
            # TODO: for now we ignore the prefix and just check for
            # a partial match
            if xsi_type in k:
                return v

        raise ValueError("Unregistered xsi:type %s" % xsi_type)

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        from stix.extensions.structured_coa.generic_structured_coa import GenericStructuredCOA   # noqa

        if not return_obj:
            klass = _BaseStructuredCOA.lookup_class(d.get('xsi:type'))
            return_obj = klass.from_dict(d)
        else:
            return_obj.id_ = d.get('id')
            return_obj.idref = d.get('idref')

        return return_obj

    def to_dict(self):
        d = super(_BaseStructuredCOA, self).to_dict()
        d['xsi:type'] = self._XSI_TYPE  # added by subclass
        return d


#: Mapping of structured coa extension types to classes
_EXTENSION_MAP = {}


def add_extension(cls):
    _EXTENSION_MAP[cls._XSI_TYPE] = cls  # noqa
