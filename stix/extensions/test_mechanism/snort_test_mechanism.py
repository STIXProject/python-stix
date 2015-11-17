# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import EncodedCDATA
from stix.indicator import test_mechanism
import stix.bindings.extensions.test_mechanism.snort as snort_tm_binding
from mixbox import fields

@stix.register_extension
class SnortTestMechanism(test_mechanism._BaseTestMechanism):
    _namespace = "http://stix.mitre.org/extensions/TestMechanism#Snort-1"
    _binding = snort_tm_binding
    _binding_class = _binding.SnortTestMechanismType
    _XSI_TYPE = "snortTM:SnortTestMechanismType"
    
    product_name = fields.TypedField("Product_Name", EncodedCDATA)
    version = fields.TypedField("Version", EncodedCDATA)
    rules = fields.TypedField("Rule", EncodedCDATA, multiple=True, key_name="rules")
    event_filters = fields.TypedField("Event_Filter", EncodedCDATA, multiple=True, key_name="event_filters")
    rate_filters = fields.TypedField("Rate_Filter", EncodedCDATA, multiple=True, key_name="rate_filters")
    event_suppressions = fields.TypedField("Event_Suppression", EncodedCDATA, multiple=True, key_name="event_suppressions")
    
    def __init__(self, id_=None, idref=None):
        super(SnortTestMechanism, self).__init__(id_=id_, idref=idref)
    