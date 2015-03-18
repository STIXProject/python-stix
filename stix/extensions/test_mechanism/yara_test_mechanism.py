# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.indicator.test_mechanism
from stix.common import EncodedCDATA
from stix.indicator.test_mechanism import _BaseTestMechanism
import stix.bindings.extensions.test_mechanism.yara as yara_tm_binding


class YaraTestMechanism(_BaseTestMechanism):
    _namespace = "http://stix.mitre.org/extensions/TestMechanism#YARA-1"
    _binding = yara_tm_binding
    _binding_class = _binding.YaraTestMechanismType
    _XSI_TYPE = "yaraTM:YaraTestMechanismType"
    
    def __init__(self, id_=None, idref=None):
        super(YaraTestMechanism, self).__init__(id_=id_, idref=idref)
        self.version = None
        self.rule = None
    
    @property
    def rule(self):
        return self._rule
    
    @rule.setter
    def rule(self, value):
        if not value:
            self._rule = None
        if isinstance(value, EncodedCDATA):
            self._rule = value
        else:
            self._rule = EncodedCDATA(value=value)
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        super(YaraTestMechanism, cls).from_obj(obj, return_obj)
        return_obj.version = obj.Version 
        return_obj.rule = EncodedCDATA.from_obj(obj.Rule)
        
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()
            
        super(YaraTestMechanism, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if self.version:
            return_obj.Version = self.version
        if self.rule:
            return_obj.Rule = self.rule.to_obj(ns_info=ns_info)
        
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        super(YaraTestMechanism, cls).from_dict(d, return_obj)
        return_obj.version = d.get('version')
        return_obj.rule = EncodedCDATA.from_dict(d.get('rule'))
        
        return return_obj
    
    def to_dict(self):
        d = super(YaraTestMechanism, self).to_dict()
        
        if self.version:
            d['version'] = self.version
        if self.rule:
            d['rule'] = self.rule.to_dict()
        
        return d
    
stix.indicator.test_mechanism.add_extension(YaraTestMechanism)
