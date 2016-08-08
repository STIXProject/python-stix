# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
from mixbox import entities

# internal
import stix
from stix.common import InformationSource

# bindings
import stix.bindings.data_marking as stix_data_marking_binding


class MarkingStructureFactory(entities.EntityFactory):
    @classmethod
    def entity_class(cls, key):
        import stix.extensions.marking.tlp  # noqa
        import stix.extensions.marking.simple_marking  # noqa
        import stix.extensions.marking.terms_of_use_marking  # noqa
        return stix.lookup_extension(key, default=MarkingStructure)


class MarkingStructure(stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingStructureType
    _namespace = 'http://data-marking.mitre.org/Marking-1'
    _XSI_TYPE = None  # overridden by subclasses

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    marking_model_name = fields.TypedField("marking_model_name")
    marking_model_ref = fields.TypedField("marking_model_ref")

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
        return stix.lookup_extension(xsi_type, default=MarkingStructure)


class MarkingSpecification(stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingSpecificationType
    _namespace = 'http://data-marking.mitre.org/Marking-1'

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    version = fields.TypedField("version")
    controlled_structure = fields.TypedField("Controlled_Structure")
    marking_structures = fields.TypedField("Marking_Structure", MarkingStructure, factory=MarkingStructureFactory, multiple=True, key_name="marking_structures")
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
    marking = fields.TypedField("Marking", MarkingSpecification, multiple=True)

    def __init__(self, markings=None):
        super(Marking, self).__init__(markings)

    def add_marking(self, value):
        self.marking.append(value)


# Backwards compatibility
add_extension = stix.add_extension
