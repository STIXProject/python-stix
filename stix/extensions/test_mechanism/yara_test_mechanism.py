# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

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

    version = fields.TypedField("Version")
    rule = fields.TypedField("Rule", EncodedCDATA)

    def __init__(self, id_=None, idref=None):
        super(YaraTestMechanism, self).__init__(id_=id_, idref=idref)
