
import stix

from stix.bindings.data_marking import MarkingSpecificationType, MarkingStructureType, MarkingType
from stix.bindings.extensions.marking.tlp import TLPMarkingStructureType
from stix.bindings.extensions.marking.simple_marking import SimpleMarkingStructureType
from stix.common.structured_text import StructuredText

import stix.bindings.data_marking as stix_data_marking_binding


class Marking(stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingType
    _namespace = 'http://data-marking.mitre.org/Marking-1'

    def __init__(self, marking=None):
        self.marking = marking

    @property
    def marking(self):
        return self._marking

    @marking.setter
    def marking(self, value):
        self._marking = []

        if value is None:
            return
        elif isinstance(value, list):
            for m in value:
                self.add_marking(m)
        else:
            self.add_marking(value)

    def add_marking(self, value):
        if not isinstance(value, MarkingSpecification):
            raise ValueError('value must be instance of MarkingSpecification')
        self._marking.append(value)

    def to_obj(self):
        obj = self._binding_class()

        obj.set_Marking([x.to_obj() for x in self.marking])
        return obj

    def to_list(self):
        return [x.to_dict() for x in self.marking]

    @staticmethod
    def from_obj(obj):
        if not obj:
            return None

        mlist = [MarkingSpecification.from_obj(x) for x in obj.get_Marking()]
        return Marking(mlist)

    @staticmethod
    def from_list(marking_list):
        if not marking_list:
            return None

        mlist = [MarkingSpecification.from_dict(x) for x in marking_list]
        return Marking(mlist)

    to_dict = to_list
    from_dict = from_list


class MarkingSpecification(stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingSpecificationType
    _namespace = 'http://data-marking.mitre.org/Marking-1'

    def __init__(self):
        self.id_ = None
        self.idref = None
        self.version = None
        self.controlled_structure = None
        self.marking_structure = []
        # TODO: add Information_Source

    def to_obj(self):
        obj = self._binding_class()

        obj.set_id(self.id_)
        obj.set_idref(self.idref)
        obj.set_version(self.version)
        obj.set_Controlled_Structure(self.controlled_structure)
        obj.set_Marking_Structure([x.to_obj() for x in self.marking_structure])

        return obj

    def to_dict(self):
        d = {}

        if self.id_:
            d['id'] = self.id_
        if self.idref:
            d['idref'] = self.idref
        if self.version:
            d['version'] = self.version
        if self.controlled_structure:
            d['controlled_structure'] = self.controlled_structure
        if self.marking_structure:
            d['marking_structure'] = [x.to_dict() for x in
                    self.marking_structure]

        return d

    @staticmethod
    def from_obj(obj):
        if not obj:
            return None

        m = MarkingSpecification()

        m.id_ = obj.get_id()
        m.idref = obj.get_idref()
        m.version = obj.get_version()
        m.controlled_structure = obj.get_Controlled_Structure()
        m.marking_structure = [MarkingStructure.from_obj(x) for x in obj.get_Marking_Structure()]

        return m

    @staticmethod
    def from_dict(marking_dict):
        if not marking_dict:
            return None

        m = MarkingSpecification()

        m.id_ = marking_dict.get('id')
        m.idref = marking_dict.get('idref')
        m.version = marking_dict.get('version')
        m.controlled_structure = marking_dict.get('controlled_structure')
        m.marking_structure = [MarkingStructure.from_dict(x) for x in
                marking_dict.get('marking_structure', [])]

        return m


class MarkingStructure(stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingStructureType
    _namespace = 'http://data-marking.mitre.org/Marking-1'

    def __init__(self):
        self.marking_model_name = None
        self.marking_model_ref = None

    def to_obj(self, obj=None):
        if not obj:
            obj = self._binding_class()

        obj.set_marking_model_name(self.marking_model_name)
        obj.set_marking_model_ref(self.marking_model_ref)

        return obj

    def to_dict(self):
        d = {}

        d['xsi:type'] = self._XSI_TYPE
        if self.marking_model_name:
            d['marking_model_name'] = self.marking_model_name
        if self.marking_model_ref:
            d['marking_model_ref'] = self.marking_model_ref

        return d

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

    @staticmethod
    def from_obj(obj, partial=None):
        if not obj:
            return None

        if partial:
            m = partial
            m.marking_model_name = obj.get_marking_model_name()
            m.marking_model_ref = obj.get_marking_model_ref()

        else:
            cls = MarkingStructure.lookup_class(obj.xml_type)
            m = cls.from_obj(obj)

        return m

    @staticmethod
    def from_dict(marking_dict, partial=None):
        if not marking_dict:
            return None

        if partial is not None:
            m = partial
            m.marking_model_name = marking_dict.get('marking_model_name')
            m.marking_model_ref = marking_dict.get('marking_model_ref')

        else:
            cls = MarkingStructure.lookup_class(marking_dict.get('xsi:type'))
            m = cls.from_dict(marking_dict)

        return m


_EXTENSION_MAP = {}
def add_extension(cls):
    _EXTENSION_MAP[cls._XSI_TYPE] = cls

