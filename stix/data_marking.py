# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
from mixbox.cache import Cached

# internal
import stix
from stix.common import InformationSource

# bindings
import stix.bindings.data_marking as stix_data_marking_binding


class MarkingStructure(Cached, stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingStructureType
    _namespace = 'http://data-marking.mitre.org/Marking-1'
    _XSI_TYPE = None  # overridden by subclasses

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    marking_model_name = fields.TypedField("marking_model_name")
    marking_mode_ref = fields.TypedField("marking_model_ref")

    def __init__(self):
        super(MarkingStructure, self).__init__()

        self.id_ = None
        self.idref = None
        self.marking_model_name = None
        self.marking_model_ref = None

    def to_dict(self):
        d = super(MarkingStructure, self).to_dict()

        if self._XSI_TYPE:
            d['xsi:type'] = self._XSI_TYPE

        return d

    @staticmethod
    def lookup_class(xsi_type):
        if not xsi_type:
            return MarkingStructure

        return stix.lookup_extension(xsi_type)

    @classmethod
    def from_obj(cls, cls_obj, partial=None):
        import stix.extensions.marking.tlp  # noqa
        import stix.extensions.marking.simple_marking  # noqa
        import stix.extensions.marking.terms_of_use_marking  # noqa

        if not cls_obj:
            return None

        if partial:
            m = partial
            m.id_ = cls_obj.id
            m.idref = cls_obj.idref
            m.marking_model_name = cls_obj.marking_model_name
            m.marking_model_ref = cls_obj.marking_model_ref

        else:
            klass = stix.lookup_extension(cls_obj, default=cls)
            m = klass.from_obj(cls_obj, klass())

        return m

    @classmethod
    def from_dict(cls, cls_dict, partial=None):
        import stix.extensions.marking.tlp  # noqa
        import stix.extensions.marking.simple_marking  # noqa
        import stix.extensions.marking.terms_of_use_marking  # noqa

        if not cls_dict:
            return None

        get = cls_dict.get

        if partial is not None:
            m = partial
            m.id_ = get('id')
            m.idref = get('idref')
            m.marking_model_name = get('marking_model_name')
            m.marking_model_ref = get('marking_model_ref')
        else:
            klass = stix.lookup_extension(get('xsi:type'), default=cls)
            m = klass.from_dict(cls_dict, klass())

        return m


class MarkingSpecification(Cached, stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingSpecificationType
    _namespace = 'http://data-marking.mitre.org/Marking-1'

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    version = fields.TypedField("version")
    controlled_structure = fields.TypedField("Controlled_Structure")
    marking_structures = fields.TypedField("Marking_Structure", MarkingStructure, multiple=True, key_name="marking_structures")
    information_source = fields.TypedField("Information_Source", InformationSource)

    def __init__(self, controlled_structure=None, marking_structures=None):
        super(MarkingSpecification, self).__init__()

        self.id_ = None
        self.idref = None
        self.version = None
        self.controlled_structure = controlled_structure
        self.marking_structures = marking_structures
        self.information_source = None


class Marking(stix.EntityList):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingType
    _namespace = 'http://data-marking.mitre.org/Marking-1'
    _contained_type = MarkingSpecification
    _binding_var = "Marking"

    def __init__(self, markings=None):
        super(Marking, self).__init__(markings)

    @property
    def markings(self):
        return self._inner

    @markings.setter
    def markings(self, value):
        self._inner = []
        self.extend(value)

    def add_marking(self, value):
        self.markings.append(value)


# Backwards compatibility
add_extension = stix.add_extension
