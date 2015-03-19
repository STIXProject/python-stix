# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import EncodedCDATA
from stix.indicator import test_mechanism
import stix.bindings.extensions.test_mechanism.snort as snort_tm_binding


class SnortTestMechanism(test_mechanism._BaseTestMechanism):
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
        self._rules = _EncodedCDATAs(value)
    
    def add_rule(self, rule):
        self.rules.append(rule)
    
    @property
    def event_filters(self):
        return self._event_filters
    
    @event_filters.setter
    def event_filters(self, value):
        self._event_filters = _EncodedCDATAs(value)
    
    def add_event_filter(self, item):
        self.event_filters.append(item)
    
    @property
    def rate_filters(self):
        return self._rate_filters
    
    @rate_filters.setter
    def rate_filters(self, value):
        self._rate_filters = _EncodedCDATAs(value)
    
    def add_rate_filter(self, item):
        self.rate_filters.append(item)
    
    @property
    def event_suppressions(self):
        return self._event_suppressions
    
    @event_suppressions.setter
    def event_suppressions(self, value):
        self._event_suppressions = _EncodedCDATAs(value)
    
    def add_event_suppression(self, item):
        self.event_suppressions.append(item)
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()
        
        super(SnortTestMechanism, cls).from_obj(obj, return_obj)
        return_obj.product_name = obj.Product_Name
        return_obj.version = obj.Version
        return_obj.rules = _EncodedCDATAs.from_obj(obj.Rule)
        return_obj.event_filters = _EncodedCDATAs.from_obj(obj.Event_Filter)
        return_obj.rate_filters = _EncodedCDATAs.from_obj(obj.Rate_Filter)
        return_obj.event_suppressions = _EncodedCDATAs.from_obj(obj.Event_Suppression)
        
        return return_obj
    
    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()
            
        super(SnortTestMechanism, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        return_obj.Product_Name = self.product_name
        return_obj.Version = self.version
        
        if self.rules:
            return_obj.Rule = self.rules.to_obj(ns_info=ns_info)
        if self.event_filters:
            return_obj.Event_Filter = self.event_filters.to_obj(ns_info=ns_info)
        if self.rate_filters:
            return_obj.Rate_Filter = self.rate_filters.to_obj(ns_info=ns_info)
        if self.event_suppressions:
            return_obj.Event_Suppression = self.event_suppressions.to_obj(ns_info=ns_info)
        
        return return_obj
    
    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if not return_obj:
            return_obj = cls()
            
        super(SnortTestMechanism, cls).from_dict(d, return_obj)

        get = d.get
        return_obj.product_name = get('product_name')
        return_obj.version = get('version')
        return_obj.rules = _EncodedCDATAs.from_dict(get('rules'))
        return_obj.event_filters = _EncodedCDATAs.from_dict(get('event_filters'))
        return_obj.rate_filters = _EncodedCDATAs.from_dict(get('rate_filters'))
        return_obj.event_suppressions = _EncodedCDATAs.from_dict(get('event_suppressions'))
        
        return return_obj

    def to_dict(self):
        return super(SnortTestMechanism, self).to_dict()


# Not an actual STIX data type!
class _EncodedCDATAs(stix.TypedList):
    _contained_type = EncodedCDATA


# Register this extension
test_mechanism.add_extension(SnortTestMechanism)
