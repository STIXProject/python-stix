# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix_header import STIXHeader
from stix.indicator import Indicator
from cybox.core import Observables

import stix.bindings.stix_core as stix_core_binding
import cybox.bindings.cybox_core as cybox_core_binding

from lxml import etree
from StringIO import StringIO

class STIXPackage(stix.Entity):
    '''
    classdocs
    '''

    def __init__(self, id_=None, idref_=None, stix_header=None, indicators=None, observables=None):
        '''
        Constructor
        '''
        self.id_ = id_ if id_ else stix.utils.create_id() 
        self.idref_ = idref_
        self.version = '1.0'
        self.indicators = indicators
        self.observables = observables
        self.stix_header = stix_header
    
    @property
    def stix_header(self):
        return self._stix_header
    
    @stix_header.setter
    def stix_header(self, value):
        if value and not isinstance(value, STIXHeader):
            raise ValueError('value must be instance of STIXHeader')
        
        self._stix_header = value
    
    @property
    def indicators(self):
        return self._indicators
    
    @indicators.setter
    def indicators(self, valuelist):
        self._indicators = [] # initialize
        
        if valuelist:   
            for value in valuelist:
                self.add_indicator(value)
    
    @property
    def observables(self):
        return self._observables
    
    @observables.setter
    def observables(self, value):
        if value and not isinstance(value, Observables):
            raise ValueError('value must be instance of cybox.core.Observables')
            
        self._observables = value
        
    def add_indicator(self, indicator):
        if indicator and not isinstance(indicator, Indicator):
            raise ValueError('indicator must be instance of stix.indicator.Indicator')
    
        self.indicators.append(indicator)
        
    def add_observable(self, observable):
        if not self.observables:
            self.observables = Observables(observable)
        else:
            self.observables.add(observable)
        
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = stix_core_binding.STIXType()
        
        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref_)
        return_obj.set_version(self.version)
        
        if self.stix_header:
            return_obj.set_STIX_Header(self.stix_header.to_obj())
        
        if self.indicators:
            indicators_obj = stix_core_binding.IndicatorsType()
            
            for indicator in self.indicators:
                indicators_obj.add_Indicator(indicator.to_obj())
            
            return_obj.set_Indicators(indicators_obj)
        
        if self.observables:
            observables_obj = self.observables.to_obj()
            return_obj.set_Observables(observables_obj)
        
        return return_obj
    
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        if self.id_:
            return_dict['id'] = self.id_
            
        return_dict['version'] = self.version
        
        if self.idref_:
            return_dict['idref'] = self.idref_
        
        if self.stix_header:
            return_dict['stix_header'] = self.stix_header.to_dict()
            
        if self.indicators:
            for indicator in self.indicators:
                return_dict.setdefault('indicators', []).append(indicator.to_dict())
                
        if self.observables:
            return_dict['observables'] = self.observables.to_dict()
        
        return return_dict
        
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not return_obj:
            return_obj = cls()
            
        return_obj.id_ = obj.get_id()
        return_obj.idref_ = obj.get_idref()
        return_obj.version = obj.get_version()
        return_obj.stix_header = STIXHeader.from_obj(obj.get_STIX_Header())
        
        if obj.get_Indicators():
            indicators_obj = obj.get_Indicators()
            if indicators_obj.get_Indicator():
                for indicator_obj in indicators_obj.get_Indicator():
                    return_obj.add_indicator(Indicator.from_obj(indicator_obj))
        
        if obj.get_Observables():
            observables_obj = obj.get_Observables()
            return_obj.observables = Observables.from_obj(observables_obj)
        
        return return_obj
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not return_obj:
            return_obj = cls()
        
        return_obj.id_ = dict_repr.get('id', None)
        return_obj.idref_ = dict_repr.get('idref', None)
        return_obj.version = dict_repr.get('version', None)
        
        header_dict = dict_repr.get('stix_header', None)
        return_obj.stix_header = STIXHeader.from_dict(header_dict)
        
        indicators = dict_repr.get('indicators', [])
        for indicator_dict in indicators:
            return_obj.add_indicator(Indicator.from_dict(indicator_dict))
        
        observables_dict = dict_repr.get('observables')
        return_obj.observables = Observables.from_dict(observables_dict)
        
        return return_obj
    
    @classmethod
    def from_xml(cls, xml_file):
        '''
        Returns a tuple of (api_object, binding_object).
        Parameters:
        xml_file - either a filename or a stream object
        '''
        
        if isinstance(xml_file, basestring):
            f = open(xml_file, "rb")
        else:
            f = xml_file
        
        doc = etree.parse(f)
        stix_package_obj = stix_core_binding.STIXType()
        stix_package_obj.build(doc.getroot())
        stix_package = STIXPackage().from_obj(stix_package_obj)
        
        return (stix_package, stix_package_obj)
            
    
    def to_xml(self, namespace_def_list = None):
        '''Overrides the stix.to_xml() method. Namespace definitions are hardcoded--this is only temporary'''
        s = StringIO()
        if namespace_def_list == None:
            self.to_obj().export(s, 0,  core_binding.DEFAULT_XML_NS_MAP)
        elif isinstance(namespace_def_list, list) and len(namespace_def_list) > 0:
            xml_ns_map = stix_core_binding.DEFAULT_XML_NS_MAP
            for namespace_def in namespace_def_list:
                split_namespace_def = namespace_def.split('=')
                xml_ns_map[split_namespace_def[1].strip('"')] = split_namespace_def[0].split('xmlns:')[1]
            self.to_obj().export(s, 0, xml_ns_map)
        return s.getvalue()
        
    
        
    