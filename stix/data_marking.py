# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import signals
from mixbox.cache import Cached

# internal
import stix
from stix.common import InformationSource

# bindings
import stix.bindings.data_marking as stix_data_marking_binding


class Marking(stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingType
    _namespace = 'http://data-marking.mitre.org/Marking-1'

    def __init__(self, markings=None):
        self.markings = _MarkingSpecifications(markings)

    @property
    def markings(self):
        return self._markings

    @markings.setter
    def markings(self, value):
        self._markings = _MarkingSpecifications(value)

    def add_marking(self, value):
        self._markings.append(value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(Marking, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        obj = self._binding_class()

        if self.markings:
            obj.Marking = self.markings.to_obj(ns_info=ns_info)

        return obj

    def to_list(self):
        return self.markings.to_list() if self.markings else []

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.markings = _MarkingSpecifications.from_obj(obj.Marking)
        signals.emit("Entity.created.from_obj", return_obj, obj)
        return return_obj

    @classmethod
    def from_list(cls, markings_list, return_obj=None):
        if not markings_list:
            return None

        if not return_obj:
            return_obj = cls()

        mlist = _MarkingSpecifications.from_list(markings_list)
        return_obj.markings = mlist

        return return_obj

    to_dict = to_list
    from_dict = from_list


class MarkingSpecification(Cached, stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingSpecificationType
    _namespace = 'http://data-marking.mitre.org/Marking-1'

    def __init__(self, controlled_structure=None, marking_structures=None):
        super(MarkingSpecification, self).__init__()

        self.id_ = None
        self.idref = None
        self.version = None
        self.controlled_structure = controlled_structure
        self.marking_structures = _MarkingStructures(marking_structures)
        self.information_source = None

    @property
    def information_source(self):
        return self._information_source

    @information_source.setter
    def information_source(self, value):
        self._set_var(InformationSource, try_cast=False, information_source=value)

    @property
    def marking_structures(self):
        return self._marking_structures

    @marking_structures.setter
    def marking_structures(self, value):
        self._marking_structures = _MarkingStructures(value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(MarkingSpecification, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        obj = self._binding_class()

        obj.id = self.id_
        obj.idref = self.idref
        obj.version = self.version
        obj.Controlled_Structure = self.controlled_structure
        obj.Marking_Structure = self.marking_structures.to_obj(ns_info=ns_info)

        if self.information_source:
            obj.Information_Source = self.information_source.to_obj(ns_info=ns_info)

        return obj

    def to_dict(self):
        return super(MarkingSpecification, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.id
        return_obj.idref = obj.idref
        return_obj.version = obj.version
        return_obj.controlled_structure = obj.Controlled_Structure
        return_obj.marking_structures = _MarkingStructures.from_obj(obj.Marking_Structure)
        return_obj.information_source = InformationSource.from_obj(obj.Information_Source)

        signals.emit("Entity.created.from_obj", return_obj, obj)
        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()

        get = d.get  # PEP8 line length fix
        return_obj.id_ = get('id')
        return_obj.idref = get('idref')
        return_obj.version = get('version')
        return_obj.controlled_structure = get('controlled_structure')
        return_obj.marking_structures = _MarkingStructures.from_dict(
            get('marking_structures')
        )
        return_obj.information_source = InformationSource.from_dict(
            get('information_source')
        )

        return return_obj


class MarkingStructure(Cached, stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingStructureType
    _namespace = 'http://data-marking.mitre.org/Marking-1'
    _XSI_TYPE = None  # overridden by subclasses

    def __init__(self):
        self.id_ = None
        self.idref = None
        self.marking_model_name = None
        self.marking_model_ref = None

    def to_obj(self, return_obj=None, ns_info=None):
        super(MarkingStructure, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.idref = self.idref
        return_obj.marking_model_name = self.marking_model_name
        return_obj.marking_model_ref = self.marking_model_ref

        return return_obj

    def to_dict(self):
        d = {}

        if self._XSI_TYPE:
            d['xsi:type'] = self._XSI_TYPE

        if self.id_:
            d['id'] = self.id_
        if self.idref:
            d['idref'] = self.idref
        if self.marking_model_name:
            d['marking_model_name'] = self.marking_model_name
        if self.marking_model_ref:
            d['marking_model_ref'] = self.marking_model_ref

        return d

    @staticmethod
    def lookup_class(xsi_type):
        if not xsi_type:
            return MarkingStructure

        return stix.lookup_extension(xsi_type)

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        import stix.extensions.marking.tlp  # noqa
        import stix.extensions.marking.simple_marking  # noqa
        import stix.extensions.marking.terms_of_use_marking  # noqa

        if not obj:
            return None

        if return_obj:
            m = return_obj
            m.id_ = obj.id
            m.idref = obj.idref
            m.marking_model_name = obj.marking_model_name
            m.marking_model_ref = obj.marking_model_ref

        else:
            klass = stix.lookup_extension(obj, default=cls)
            m = klass.from_obj(obj, return_obj=klass())

        signals.emit("Entity.created.from_obj", return_obj, obj)
        return m

    @classmethod
    def from_dict(cls, d, return_obj=None):
        import stix.extensions.marking.tlp  # noqa
        import stix.extensions.marking.simple_marking  # noqa
        import stix.extensions.marking.terms_of_use_marking  # noqa
        
        if not d:
            return None

        get = d.get
        
        if return_obj is not None:
            m = return_obj
            m.id_ = get('id')
            m.idref = get('idref')
            m.marking_model_name = get('marking_model_name')
            m.marking_model_ref = get('marking_model_ref')
        else:
            klass = stix.lookup_extension(get('xsi:type'), default=cls)
            m = klass.from_dict(d, return_obj=klass())

        return m


# Not Actual STIX Types!
class _MarkingSpecifications(stix.TypedList):
    _contained_type = MarkingSpecification


class _MarkingStructures(stix.TypedList):
    _contained_type = MarkingStructure


# Backwards compatibility
add_extension = stix.add_extension
