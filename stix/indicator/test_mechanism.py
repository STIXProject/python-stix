# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix.common import InformationSource, Statement
import stix.bindings.indicator as indicator_binding

class _BaseTestMechanism(stix.Entity):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = indicator_binding.TestMechanismType()
    
    def __init__(self, id_=None, idref=None):
        self.id_ = id_ or stix.utils.create_id("testmechanism")
        self.idref = idref
        self.efficacy = None
        self.producer = None
    
    @property
    def efficacy(self):
        return self._efficacy
    
    @efficacy.setter
    def efficacy(self, value):
        if not value:
            self._efficacy = None
        elif isinstance(value, Statement):
            self._efficacy = value
        else:
            self._efficacy = Statement(value=value)
    
    @property
    def producer(self):
        return self._producer
    
    @producer.setter
    def producer(self, value):
        if not value:
            self._producer = None
        elif isinstance(value, InformationSource):
            self._producer = value
        else:
            raise ValueError('Cannot set producer to type %s' % type(value))
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        from stix.extensions.test_mechanism.snort_test_mechanism import SnortTestMechanism
        from stix.extensions.test_mechanism.open_ioc_2010_test_mechanism import OpenIOCTestMechanism
        from stix.extensions.test_mechanism.yara_test_mechanism import YaraTestMechanism
        
        if not return_obj:
            klass = _BaseTestMechanism.lookup_class(obj.xml_type)
            return_obj = klass.from_obj(obj)
        else:
            return_obj.id_ = obj.get_id()
            return_obj.idref = obj.get_idref()
            return_obj.efficacy = Statement.from_obj(obj.get_Efficacy())
            return_obj.producer = InformationSource.from_obj(obj.get_Producer())
        
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        super(_BaseTestMechanism, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()
        
        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref)
        
        if self.efficacy:
            return_obj.set_Efficacy(self.efficacy.to_obj(ns_info=ns_info))
        if self.producer:
            return_obj.set_Producer(self.producer.to_obj(ns_info=ns_info))
        
        return return_obj
    
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
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        
        from stix.extensions.test_mechanism.snort_test_mechanism import SnortTestMechanism
        from stix.extensions.test_mechanism.open_ioc_2010_test_mechanism import OpenIOCTestMechanism
        from stix.extensions.test_mechanism.yara_test_mechanism import YaraTestMechanism
        
        if not return_obj:
            klass = _BaseTestMechanism.lookup_class(d.get('xsi:type'))
            return_obj = klass.from_dict(d)
        else:
            return_obj.id_ = d.get('id')
            return_obj.idref = d.get('idref')
            return_obj.efficacy = Statement.from_dict(d.get('efficacy'))
            return_obj.producer = InformationSource.from_dict(d.get('producer'))
            
        return return_obj
    
    def to_dict(self):
        d = super(_BaseTestMechanism, self).to_dict()
        d['xsi:type'] = self._XSI_TYPE # added by subclass
        return d
    
_EXTENSION_MAP = {}
def add_extension(cls):
    _EXTENSION_MAP[cls._XSI_TYPE] = cls
