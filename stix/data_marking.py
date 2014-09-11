
import stix

from stix.bindings.data_marking import MarkingSpecificationType, MarkingStructureType, MarkingType
from stix.common import StructuredText
import stix.bindings.data_marking as stix_data_marking_binding

class Marking(stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingType
    _namespace = 'http://data-marking.mitre.org/Marking-1'

    def __init__(self, markings=None):
        self.markings = markings

    @property
    def markings(self):
        return self._markings

    @markings.setter
    def markings(self, value):
        self._markings = []

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
        self._markings.append(value)

    def to_obj(self):
        obj = self._binding_class()

        obj.set_Marking([x.to_obj() for x in self.markings])
        return obj

    def to_list(self):
        return [x.to_dict() for x in self.markings]

    @staticmethod
    def from_obj(obj):
        if not obj:
            return None

        mlist = [MarkingSpecification.from_obj(x) for x in obj.get_Marking()]
        return Marking(mlist)

    @staticmethod
    def from_list(markings_list):
        if not markings_list:
            return None

        mlist = [MarkingSpecification.from_dict(x) for x in markings_list]
        return Marking(mlist)

    to_dict = to_list
    from_dict = from_list


class MarkingSpecification(stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingSpecificationType
    _namespace = 'http://data-marking.mitre.org/Marking-1'

    def __init__(self,controlled_structure=None,marking_structures=[]):
        self.id_ = None
        self.idref = None
        self.version = None
        self.controlled_structure = controlled_structure
        self.marking_structures = marking_structures
        # TODO: add Information_Source

    def to_obj(self):
        obj = self._binding_class()

        obj.set_id(self.id_)
        obj.set_idref(self.idref)
        obj.set_version(self.version)
        obj.set_Controlled_Structure(self.controlled_structure)
        obj.set_Marking_Structure([x.to_obj() for x in self.marking_structures])

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
        if self.marking_structures:
            d['marking_structures'] = [x.to_dict() for x in self.marking_structures]

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
        m.marking_structures = [MarkingStructure.from_obj(x) for x in obj.get_Marking_Structure()]

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
        m.marking_structures = [MarkingStructure.from_dict(x) for x in
                marking_dict.get('marking_structures', [])]

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
        from stix.extensions.marking.tlp import TLPMarkingStructure
        from stix.extensions.marking.simple_marking import SimpleMarkingStructure
        from stix.extensions.marking.terms_of_use_marking import TermsOfUseMarkingStructure
        
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
        from stix.extensions.marking.tlp import TLPMarkingStructure
        from stix.extensions.marking.simple_marking import SimpleMarkingStructure
        from stix.extensions.marking.terms_of_use_marking import TermsOfUseMarkingStructure
        
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

