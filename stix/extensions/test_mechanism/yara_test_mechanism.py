# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.indicator.test_mechanism
from stix.common import EncodedCDATA
from stix.indicator.test_mechanism import _BaseTestMechanism
import stix.bindings.extensions.test_mechanism.yara as yara_tm_binding


@stix.register_extension
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
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        obj = super(YaraTestMechanism, cls).from_obj(cls_obj)

        obj.version = cls_obj.Version
        obj.rule = EncodedCDATA.from_obj(cls_obj.Rule)

        return obj
    
    def to_obj(self, ns_info=None):
        obj = super(YaraTestMechanism, self).to_obj(ns_info=ns_info)

        if self.version:
            obj.Version = self.version
        if self.rule:
            obj.Rule = self.rule.to_obj(ns_info=ns_info)
        
        return obj
    
    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None

        obj = super(YaraTestMechanism, cls).from_dict(cls_dict)

        obj.version = cls_dict.get('version')
        obj.rule = EncodedCDATA.from_dict(cls_dict.get('rule'))
        
        return obj
    
    def to_dict(self):
        d = super(YaraTestMechanism, self).to_dict()
        
        if self.version:
            d['version'] = self.version

        if self.rule:
            d['rule'] = self.rule.to_dict()
        
        return d

