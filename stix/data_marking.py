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
        self.markings = MarkingSpecifications(markings)

    @property
    def markings(self):
        return self._markings

    @markings.setter
    def markings(self, value):
        if isinstance(value, MarkingSpecifications):
            self._markings = value
        else:
            self._markings = MarkingSpecifications(value)

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

        return_obj.markings = MarkingSpecifications.from_obj(obj.Marking)

        return return_obj

    @classmethod
    def from_list(cls, markings_list, return_obj=None):
        if not markings_list:
            return None

        if not return_obj:
            return_obj = cls()

        mlist = MarkingSpecifications.from_list(markings_list)
        return_obj.markings = mlist

        return return_obj

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
        self.marking_structures = MarkingStructures(marking_structures)
        # TODO: add Information_Source


    @property
    def marking_structures(self):
        return self._marking_structures

    @marking_structures.setter
    def marking_structures(self, value):
        if isinstance(value, MarkingStructures):
            self._marking_structures = value
        else:
            self._marking_structures = MarkingStructures(value)


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
            d['marking_structures'] = self.marking_structures.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        m = return_obj if return_obj else cls()
        m.id_ = obj.id
        m.idref = obj.idref
        m.version = obj.version
        m.controlled_structure = obj.Controlled_Structure
        m.marking_structures = MarkingStructures.from_obj(obj.Marking_Structure)

        return m

    @classmethod
    def from_dict(cls, marking_dict, return_obj=None):
        if not marking_dict:
            return None

        get = marking_dict.get  # PEP8 line length fix
        m = return_obj if return_obj else cls()
        m.id_ = get('id')
        m.idref = get('idref')
        m.version = get('version')
        m.controlled_structure = get('controlled_structure')
        m.marking_structures = MarkingStructures.from_dict(
            get('marking_structures')
        )

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
        import stix.extensions.marking.tlp
        import stix.extensions.marking.simple_marking
        import stix.extensions.marking.terms_of_use_marking
        
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
        import stix.extensions.marking.tlp
        import stix.extensions.marking.simple_marking
        import stix.extensions.marking.terms_of_use_marking
        
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



class MarkingSpecifications(stix.TypedList):
    _contained_type = MarkingSpecification


class MarkingStructures(stix.TypedList):
    _contained_type = MarkingStructure


#: Mapping of marking extension types to classes
_EXTENSION_MAP = {}
def add_extension(cls):
    _EXTENSION_MAP[cls._XSI_TYPE] = cls


