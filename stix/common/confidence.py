# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from . import VocabString, StructuredText, HighMediumLow
import stix.bindings.stix_common as common_binding


class Confidence(stix.Entity):
    _namespace = 'http://stix.mitre.org/common-2'
    _binding = common_binding
    
    def __init__(self, value=None, description=None, source=None):
        self.value = value
        self.description = description
        self.source = source
        self.confidence_assertion_chain = None
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, HighMediumLow):
            self._value = value
        else:
            self._value = HighMediumLow(value=value)
    
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        if isinstance(value, VocabString):
            self._source = value
        else:
            self._source = VocabString(value=value)
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._description = value
            else:
                self._description = StructuredText(value=value)
        else:
            self._description = None

    @property
    def confidence_assertion_chain(self):
        return self._confidence_assertion_chain
    
    @confidence_assertion_chain.setter
    def confidence_assertion_chain(self, value):
        if value:
            raise NotImplementedError()
        
class ConfidenceAssertionChain(stix.Entity):
    _namespace = 'http://stix.mitre.org/common-2'
    _binding = common_binding

    def __init__(self):
        self.confidence_assertions = []
        
    def add_confidence_assertion(self, confidence_assertion):
        if isinstance(confidence_assertion, Confidence):
            self.confidence_assertion.append(confidence_assertion)
        else:
            tmp_confidence = Confidence(value=confidence_assertion)
            self.confidence_assertions.append(tmp_confidence)
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding.ConfidenceAssertionChainType()
        
        pass
        
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        pass
    
    def to_dict(self, return_dict=None):
        pass
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        pass
