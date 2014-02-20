import stix
import stix.bindings.stix_common as common_binding

from .confidence import Confidence
from .information_source import InformationSource
from .vocabs import VocabString
from stix.bindings import stix_common


class Relationship(VocabString):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding

class GenericRelationship(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    
    def __init__(self, confidence=None, information_source=None, relationship=None):
        self.confidence = confidence
        self.information_source = information_source
        self.relationship = relationship
        
    @property
    def confidence(self):
        return self._confidence
    
    @confidence.setter
    def confidence(self, value):
        if value:
            if isinstance(value, Confidence):
                self._confidence = value
            else:
                self._confidence = Confidence(value=value)
        else:
            self._confidence = None
    
    @property
    def information_source(self):
        return self._information_source
    
    @information_source.setter
    def information_source(self, value):
        if value and not isinstance(value, InformationSource):
            raise ValueError('value must be instance of InformationSource')
        
        self._information_source = value
    
    @property
    def relationship(self):
        return self._relationship
    
    @relationship.setter
    def relationship(self, value):
        if value:
            if isinstance(value, Relationship):
                self._relationship = value
            else:
                self._relationship = Relationship(value=value)
        else:
            self._relationship = None
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
            
        return_obj.confidence = Confidence.from_obj(obj.get_Confidence())
        return_obj.information_source = InformationSource.from_obj(obj.get_Information_Source())
        return_obj.relationship = Relationship.from_obj(obj.get_Relationship())
        
        return return_obj
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding.GenericRelationshipType()
        
        if self.confidence:    
            return_obj.set_Confidence(self.confidence.to_obj())
        
        if self.information_source:
            return_obj.set_Information_Source(self.information_source.to_obj())
        
        if self.relationship:
            return_obj.set_Relationship(self.relationship.to_obj())
            
        return return_obj
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()
            
        return_obj.confidence = Confidence.from_dict(dict_repr.get('confidence'))
        return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))
        return_obj.relationship = Relationship.from_dict(dict_repr.get('relationship'))
        
        return return_obj
        
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
            
        if self.confidence:
            return_dict['confidence'] = self.confidence.to_dict()
        
        if self.information_source:
            return_dict['information_source'] = self.information_source.to_dict()
            
        if self.relationship:
            return_dict['relationship'] = self.relationship.to_dict()
            
        return return_dict
    
    
    
class GenericRelationshipList(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.GenericRelationshipListType
    
    def __init__(self, scope):
        self.scope = scope
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()
            
        return_obj.scope = self.scope
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
            
        return_obj.scope = obj.get_scope()
        return return_obj
    
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
            
        if self.scope:
            return_dict['scope'] = self.scope
        
        return return_dict
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()
            
        return_obj.scope = dict_repr.get('scope')
        return return_obj
    
    
