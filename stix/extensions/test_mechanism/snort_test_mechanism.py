# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.indicator.test_mechanism
from stix.common import EncodedCDATA
from stix.indicator.test_mechanism import _BaseTestMechanism
import stix.bindings.extensions.test_mechanism.snort as snort_tm_binding

class SnortTestMechanism(_BaseTestMechanism):
    _namespace = "http://stix.mitre.org/extensions/TestMechanism#Snort-1"
    _binding = snort_tm_binding
    _binding_class = _binding.SnortTestMechanismType
    _XSI_TYPE = "snortTM:SnortTestMechanismType"
    
    def __init__(self, id_=None, idref=None):
        super(SnortTestMechanism, self).__init__(id_=id_, idref=idref)
        self.product_name = None
        self.version = None
        self.rules = None
        self.event_filters = None
        self.rate_filters = None
        self.event_suppressions = None
    
    @property
    def rules(self):
        return self._rules
    
    @rules.setter
    def rules(self, value):
        self._rules = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_rule(v)
        else:
            self.add_rule(v)
    
    def add_rule(self, rule):
        if not rule:
            return
        elif isinstance(rule, EncodedCDATA):
            self.rules.append(rule)
        else:
            self.rules.append(EncodedCDATA(value=rule))
    
    @property
    def event_filters(self):
        return self._event_filters
    
    @event_filters.setter
    def event_filters(self, value):
        self._event_filters = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_event_filter(v)
        else:
            self.add_event_filter(v)
    
    def add_event_filter(self, item):
        if not item:
            return
        elif isinstance(item, EncodedCDATA):
            self.event_filters.append(item)
        else:
            self.rules.append(EncodedCDATA(value=item))  
    
    @property
    def rate_filters(self):
        return self._rate_filters
    
    @rate_filters.setter
    def rate_filters(self, value):
        self._rate_filters = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_rate_filter(v)
        else:
            self.add_rate_filter(v)
    
    def add_rate_filter(self, item):
        if not item:
            return
        elif isinstance(item, EncodedCDATA):
            self.rate_filters.append(item)
        else:
            self.rules.append(EncodedCDATA(value=item))  
    
    @property
    def event_suppressions(self):
        return self._event_suppressions
    
    @event_suppressions.setter
    def event_suppressions(self, value):
        self._event_suppressions = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_event_suppression(v)
        else:
            self.add_event_suppression(v)
    
    def add_event_suppression(self, item):
        if not item:
            return
        elif isinstance(item, EncodedCDATA):
            self.event_suppressions.append(item)
        else:
            self.rules.append(EncodedCDATA(value=item))  
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        super(SnortTestMechanism, cls).from_obj(obj, return_obj)
        return_obj.product_name = obj.get_Product_Name()
        return_obj.version = obj.get_Version()
        
        if obj.get_Rule():
            return_obj.rules = [EncodedCDATA.from_obj(x) for x in obj.get_Rule()]
        if obj.get_Event_Filter():
            return_obj.event_filters = [EncodedCDATA.from_obj(x) for x in obj.get_Event_Filter()]
        if obj.get_Rate_Filter():
            return_obj.rate_filters = [EncodedCDATA.from_obj(x) for x in obj.get_Rate_Filter()]
        if obj.get_Event_Suppression():
            return_obj.event_suppressions = [EncodedCDATA.from_obj(x) for x in obj.get_Event_Suppression()]
        
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if not return_obj:
            return_obj = self._binding_class()
            
        super(SnortTestMechanism, self).to_obj(return_obj)
        
        return_obj.set_Product_Name(self.product_name)
        return_obj.set_Version(self.version)
        
        if self.rules:
            return_obj.set_Rule([x.to_obj(ns_info=ns_info) for x in self.rules])
        if self.event_filters:
            return_obj.set_Event_Filter([x.to_obj(ns_info=ns_info) for x in self.event_filters])
        if self.rate_filters:
            return_obj.set_Rate_Filter([x.to_obj(ns_info=ns_info) for x in self.rate_filters])
        if self.event_suppressions:
            return_obj.set_Event_Suppression([x.to_obj(ns_info=ns_info) for x in self.event_suppressions])
        
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        super(SnortTestMechanism, cls).from_dict(d, return_obj)
        
        return_obj.product_name = d.get('product_name')
        return_obj.version = d.get('version')
        return_obj.rules = [EncodedCDATA.from_dict(x) for x in d.get('rules', [])]
        return_obj.event_filters = [EncodedCDATA.from_dict(x) for x in d.get('event_filters', [])]
        return_obj.rate_filters = [EncodedCDATA.from_dict(x) for x in d.get('rate_filters', [])]
        return_obj.event_suppressions = [EncodedCDATA.from_dict(x) for x in d.get('event_suppressions', [])]
        
        return return_obj
    
stix.indicator.test_mechanism.add_extension(SnortTestMechanism)
