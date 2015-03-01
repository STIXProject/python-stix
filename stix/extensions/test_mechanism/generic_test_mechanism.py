# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.indicator.test_mechanism
from stix.common import EncodedCDATA, StructuredText, VocabString
from stix.indicator.test_mechanism import _BaseTestMechanism
import stix.bindings.extensions.test_mechanism.generic as generic_tm_binding


class GenericTestMechanism(_BaseTestMechanism):
    _namespace = "http://stix.mitre.org/extensions/TestMechanism#Generic-1"
    _binding = generic_tm_binding
    _binding_class = _binding.GenericTestMechanismType
    _XSI_TYPE = "genericTM:GenericTestMechanismType"
    
    def __init__(self, id_=None, idref=None):
        super(GenericTestMechanism, self).__init__(id_=id_, idref=idref)
        self.reference_location = None
        self.description = None
        self.type_ = None
        self.specification = None
        
    @property
    def specification(self):
        return self._specification
    
    @specification.setter
    def specification(self, value):
        if not value:
            self._specification = None
        if isinstance(value, EncodedCDATA):
            self._specification = value
        else:
            self._specification = EncodedCDATA(value=value)
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not value:
            self._description = None
        elif isinstance(value, StructuredText):
            self._description = value
        else:
            self._description = StructuredText(value)
    
    @property
    def type_(self):
        return self._type
    
    @type_.setter
    def type_(self, value):
        if not value:
            self._type = None
        elif isinstance(value, VocabString):
            self._type = value
        else:
            self._type = VocabString(value)
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        super(GenericTestMechanism, cls).from_obj(obj, return_obj)
        return_obj.reference_location = obj.reference_location
        return_obj.description = StructuredText.from_obj(obj.Description)
        return_obj.type_ = VocabString.from_obj(obj.Type)
        return_obj.specification = EncodedCDATA.from_obj(obj.Specification)
        
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()
            
        super(GenericTestMechanism, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        if self.reference_location:
            return_obj.reference_location = self.reference_location
        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.type_:
            return_obj.Type = self.type_.to_obj(ns_info=ns_info)
        if self.specification:
            return_obj.Specification = self.specification.to_obj(ns_info=ns_info)
        
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        super(GenericTestMechanism, cls).from_dict(d, return_obj)
        return_obj.reference_location = d.get('reference_location')
        return_obj.description = StructuredText.from_dict(d.get('description'))
        return_obj.type_ = VocabString.from_dict(d.get('type'))
        return_obj.specification = EncodedCDATA.from_dict(d.get('specification'))
        
        return return_obj
    
    def to_dict(self):
        d = super(GenericTestMechanism, self).to_dict()
        
        if self.reference_location:
            d['reference_location'] = self.reference_location
        if self.description:
            d['description'] = self.description.to_dict()
        if self.type_:
            d['type'] = self.type_.to_dict()
        if self.specification:
            d['specification'] = self.specification.to_dict()
        
        return d

    
stix.indicator.test_mechanism.add_extension(GenericTestMechanism)
