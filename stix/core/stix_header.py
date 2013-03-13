import stix
import stix.bindings.stix_common_0_2 as stix_common_binding
import stix.bindings.stix_core_1_0 as stix_core_binding
from stix.common import InformationSource
from cybox.common import StructuredText


class STIXHeader(stix.Entity):
    def __init__(self, package_intent=None, description=None, handling=None, information_source=None):
        self.package_intent = package_intent
        self.description = description
        #self.handling = handling # not implemented
        self.information_source = information_source
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        '''Sets the value of the description property. If the value is an instance of basestring, 
        it will be coerced into an instance of StructuredText, with its 'text' property set to 
        the input value'''
        
        if isinstance(value, basestring):
            st = StructuredText()
            st.add_text(value)
        elif isinstance(value, StructuredText):
            self._description = value
        elif not value:
            self._description = None
        else:
            raise ValueError('value must be instance of StructuredText or basestring')
    
    @property
    def information_source(self):
        return self._information_source
    
    @information_source.setter
    def information_source(self, value):
        if value and not isinstance(value, InformationSource):
            raise ValueError('value must instance of InformationSource')
        
        self._information_source = value
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        return_obj.package_intent = obj.get_PackageIntent()
        return_obj.description = StructuredText.from_obj(obj.get_Description())
        return_obj.information_source = InformationSource.from_obj(obj.get_InformationSource())
        
        return return_obj
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = stix_core_binding.STIXHeaderType()
        
        return_obj.set_PackageIntent(self.package_intent)
        
        if self.description:
            return_obj.set_Description(self.description.to_obj())
            
        if self.information_source:
            return_obj.set_InformationSource(self.information_source.to_obj())
        
        return return_obj
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        return_obj.package_intent = dict_repr.get('package_intent', None)
            
        desc_dict = dict_repr.get('description', None)
        return_obj.description = StructuredText.from_dict(desc_dict)
        
        info_dict = dict_repr.get('information_source', None)
        return_obj.information_source = InformationSource.from_dict(info_dict)
        
        return return_obj
    
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        if self.package_intent:
            return_dict['package_intent'] = self.package_intent
        
        if self.description:
            return_dict['description'] = self.description.to_dict()
            
        if self.information_source:
            return_dict['information_source'] = self.information_source.to_dict()
            
        return return_dict
        
        
        
        