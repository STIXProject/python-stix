# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.indicator.test_mechanism
from stix.indicator.test_mechanism import _BaseTestMechanism
import stix.bindings.extensions.test_mechanism.open_ioc_2010 as open_ioc_tm_binding
from lxml import etree
from itertools import izip
from StringIO import StringIO

class OpenIOCTestMechanism(_BaseTestMechanism):
    _namespace = "http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1"
    _binding = open_ioc_tm_binding
    _binding_class = _binding.OpenIOC2010TestMechanismType
    _xml_ns_prefix = "stix-openioc"
    _XSI_TYPE = "stix-openioc:OpenIOC2010TestMechanismType"
    
    
    def __init__(self, id_=None, idref=None):
        super(OpenIOCTestMechanism, self).__init__(id_=id_, idref=idref)
        self.ioc = None
    
    @property
    def ioc(self):
        return self._ioc
    
    @ioc.setter
    def ioc(self, value):
        if value is None:
            self._ioc = None
            return
        elif isinstance(value, etree._ElementTree):
            tree = value
        elif isinstance(value, etree._Element):
            tree = etree.ElementTree(value)
        else:
            raise ValueError('ioc must be instance of lxml.etree._Element '
                             'or lxml.etree._ElementTree')
        
        root = tree.getroot()
        expected_node_tag = "{%s}ioc" % (self._namespace)
        if root.tag != expected_node_tag:
            ns_ioc = "http://schemas.mandiant.com/2010/ioc"
            node_ns = root.tag[1:].split("}")[0] if root.tag.startswith("{") else None
            if node_ns == ns_ioc:
                # attempt to cast
                etree.register_namespace(self._xml_ns_prefix, self._namespace)
                root.tag = expected_node_tag
            else:
                raise ValueError("Cannot set ioc property. Expected tag %s found %s" 
                                 % (expected_node_tag, root.tag))
        
        self.__input_namespaces__ = {}
        for alias,ns in root.nsmap.iteritems():
            self.__input_namespaces__[ns] = alias
            
        self.__input_schemalocations__ = {}
        schemaloc_str = root.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}schemaLocation')
        if schemaloc_str:
            pairs = izip(*[iter(schemaloc_str.split())]*2)
            self.__input_schemalocations__ = dict(pairs)
        
        self._ioc = tree
        
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        super(OpenIOCTestMechanism, cls).from_obj(obj, return_obj)
        return_obj.ioc = obj.get_ioc()
        return return_obj
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()
            
        super(OpenIOCTestMechanism, self).to_obj(return_obj)
        return_obj.set_ioc(self.ioc) 
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        super(OpenIOCTestMechanism, cls).from_dict(d, return_obj)
        if 'ioc' in d:
            parser = etree.ETCompatXMLParser(huge_tree=True)
            return_obj.ioc = etree.parse(StringIO(d['ioc']), parser=parser)
        
        return return_obj
    
stix.indicator.test_mechanism.add_extension(OpenIOCTestMechanism)
