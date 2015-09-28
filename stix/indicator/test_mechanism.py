# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields
from mixbox.cache import Cached

# internal
import stix
from stix.common import InformationSource, Statement

# bindings
import stix.bindings.indicator as indicator_binding
from stix.base import AttributeField, ElementField


class _BaseTestMechanism(Cached, stix.Entity):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = indicator_binding.TestMechanismType()
    
    id_ = fields.IdField("id")
    idref = fields.IdField("idref")
    efficacy = ElementField("Efficacy", Statement)
    producer = ElementField("Producer", InformationSource)
    
    def __init__(self, id_=None, idref=None):
        self._fields = {}
        self.id_ = id_
        self.idref = idref
        self.efficacy = None
        self.producer = None

    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        import stix.extensions.test_mechanism.snort_test_mechanism  # noqa
        import stix.extensions.test_mechanism.open_ioc_2010_test_mechanism  # noqa
        import stix.extensions.test_mechanism.yara_test_mechanism  # noqa
        import stix.extensions.test_mechanism.generic_test_mechanism  # noqa
        
        if not return_obj:
            klass = stix.lookup_extension(obj)
            return_obj = klass.from_obj(obj)
        else:
            return_obj.id_ = obj.id
            return_obj.idref = obj.idref
            return_obj.efficacy = Statement.from_obj(obj.Efficacy)
            return_obj.producer = InformationSource.from_obj(obj.Producer)
        
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        super(_BaseTestMechanism, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()
        
        return_obj.id = self.id_
        return_obj.idref = self.idref
        # return_obj.xsi_type = self._XSI_TYPE

        if self.efficacy:
            return_obj.Efficacy = self.efficacy.to_obj(ns_info=ns_info)
        if self.producer:
            return_obj.Producer = self.producer.to_obj(ns_info=ns_info)
        
        return return_obj
    
    @staticmethod
    def lookup_class(xsi_type):
        if not xsi_type:
            raise ValueError("xsi:type is required")

        return stix.lookup_extension(xsi_type)
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        
        import stix.extensions.test_mechanism.snort_test_mechanism  # noqa
        import stix.extensions.test_mechanism.open_ioc_2010_test_mechanism  # noqa
        import stix.extensions.test_mechanism.yara_test_mechanism  # noqa
        import stix.extensions.test_mechanism.generic_test_mechanism  # noqa
        
        if not return_obj:
            klass = stix.lookup_extension(d.get('xsi:type'))
            return_obj = klass.from_dict(d)
        else:
            return_obj.id_ = d.get('id')
            return_obj.idref = d.get('idref')
            return_obj.efficacy = Statement.from_dict(d.get('efficacy'))
            return_obj.producer = InformationSource.from_dict(d.get('producer'))
            
        return return_obj
    
    def to_dict(self):
        d = super(_BaseTestMechanism, self).to_dict()
        d['xsi:type'] = self._XSI_TYPE  # added by subclass
        return d
    

class TestMechanisms(stix.EntityList):
    _binding = indicator_binding
    _namespace = 'http://stix.mitre.org/Indicator-2'
    _binding_class = _binding.TestMechanismsType
    _contained_type = _BaseTestMechanism
    _binding_var = "Test_Mechanism"
    _inner_name = "test_mechanisms"
    _dict_as_list = True


# Backwards compatibility
add_extension = stix.add_extension
