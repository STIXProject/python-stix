# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
import stix.indicator.test_mechanism
from stix.common.vocabs import VocabField
from stix.common import EncodedCDATA, StructuredText, VocabString
from stix.indicator.test_mechanism import _BaseTestMechanism
import stix.bindings.extensions.test_mechanism.generic as generic_tm_binding


@stix.register_extension
class GenericTestMechanism(_BaseTestMechanism):
    _namespace = "http://stix.mitre.org/extensions/TestMechanism#Generic-1"
    _binding = generic_tm_binding
    _binding_class = _binding.GenericTestMechanismType
    _XSI_TYPE = "genericTM:GenericTestMechanismType"
    
    reference_location = fields.TypedField("reference_location")
    description = fields.TypedField("Description", StructuredText)
    specification = fields.TypedField("Specification", EncodedCDATA)
    type_ = VocabField("Type")

    def __init__(self, id_=None, idref=None):
        super(GenericTestMechanism, self).__init__(id_=id_, idref=idref)
