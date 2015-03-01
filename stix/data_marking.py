# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils as utils
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
        elif utils.is_sequence(value):
            for m in value:
                self.add_marking(m)
        else:
            self.add_marking(value)

    def add_marking(self, value):
        if not isinstance(value, MarkingSpecification):
            raise ValueError('value must be instance of MarkingSpecification')
        self._markings.append(value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(Marking, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        obj = self._binding_class()
        obj.Marking = [x.to_obj(ns_info=ns_info) for x in self.markings]
        return obj

    def to_list(self):
        return [x.to_dict() for x in self.markings]

    @staticmethod
    def from_obj(obj):
        if not obj:
            return None

        mlist = [MarkingSpecification.from_obj(x) for x in obj.Marking]
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

    def __init__(self, controlled_structure=None, marking_structures=None):
        self.id_ = None
        self.idref = None
        self.version = None
        self.controlled_structure = controlled_structure

        if utils.is_sequence(marking_structures):
            self.marking_structures = marking_structures
        elif marking_structures is None:
            self.marking_structures = []
        else:
            raise TypeError('marking_structures must be a list, or None')

        # TODO: add Information_Source

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
        obj.Marking_Structure = [
            x.to_obj(ns_info=ns_info) for x in self.marking_structures
        ]

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
            d['marking_structures'] = [
                x.to_dict() for x in self.marking_structures
            ]

        return d

    @staticmethod
    def from_obj(obj):
        if not obj:
            return None

        m = MarkingSpecification()

        m.id_ = obj.id
        m.idref = obj.idref
        m.version = obj.version
        m.controlled_structure = obj.Controlled_Structure
        m.marking_structures = [
            MarkingStructure.from_obj(x) for x in obj.Marking_Structure
        ]

        return m

    @staticmethod
    def from_dict(marking_dict):
        if not marking_dict:
            return None



        get = marking_dict.get  # PEP8 line length fix
        m = MarkingSpecification()

        m.id_ = get('id')
        m.idref = get('idref')
        m.version = get('version')
        m.controlled_structure = get('controlled_structure')
        m.marking_structures = [
            MarkingStructure.from_dict(x) for x in get('marking_structures', [])
        ]

        return m


class MarkingStructure(stix.Entity):
    _binding = stix_data_marking_binding
    _binding_class = stix_data_marking_binding.MarkingStructureType
    _namespace = 'http://data-marking.mitre.org/Marking-1'

    def __init__(self):
        self.marking_model_name = None
        self.marking_model_ref = None

    def to_obj(self, return_obj=None, ns_info=None):
        super(MarkingStructure, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.marking_model_name = self.marking_model_name
        return_obj.marking_model_ref = self.marking_model_ref

        return return_obj

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
            m.marking_model_name = obj.marking_model_name
            m.marking_model_ref = obj.marking_model_ref

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


#: Mapping of marking extension types to classes
_EXTENSION_MAP = {}
def add_extension(cls):
    _EXTENSION_MAP[cls._XSI_TYPE] = cls

