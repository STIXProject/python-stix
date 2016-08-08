# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import entities
from mixbox import fields

# internal
import stix
from stix.bindings import course_of_action as coa_binding


class StructuredCOAFactory(entities.EntityFactory):
    @classmethod
    def entity_class(cls, key):
        import stix.extensions.structured_coa.generic_structured_coa  # noqa
        return stix.lookup_extension(key)


class _BaseStructuredCOA(stix.Entity):
    _namespace = "http://stix.mitre.org/CourseOfAction-1"
    _binding = coa_binding
    _binding_class = coa_binding.StructuredCOAType

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")

    def __init__(self, id_=None, idref=None):
        super(_BaseStructuredCOA, self).__init__()
        self.id_ = id_
        self.idref = idref

    def to_dict(self):
        d = super(_BaseStructuredCOA, self).to_dict()
        d['xsi:type'] = self._XSI_TYPE
        return d

    def to_obj(self, ns_info=None):
        obj = super(_BaseStructuredCOA, self).to_obj(ns_info=ns_info)
        obj.xsi_type = self._XSI_TYPE
        return obj

# Backwards compatibility
add_extension = stix.add_extension
