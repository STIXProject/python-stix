# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
import stix.indicator.test_mechanism
from stix.common.vocabs import VocabField
from stix.common import EncodedCDATA, StructuredTextList, VocabString
from stix.indicator.test_mechanism import _BaseTestMechanism
import stix.bindings.extensions.test_mechanism.generic as generic_tm_binding


@stix.register_extension
class GenericTestMechanism(_BaseTestMechanism):
    _namespace = "http://stix.mitre.org/extensions/TestMechanism#Generic-1"
    _binding = generic_tm_binding
    _binding_class = _binding.GenericTestMechanismType
    _XSI_TYPE = "genericTM:GenericTestMechanismType"
    
    reference_location = fields.TypedField("reference_location")
    descriptions = fields.TypedField("Description", StructuredTextList)
    specification = fields.TypedField("Specification", EncodedCDATA)
    type_ = VocabField("Type")
    
    def __init__(self, id_=None, idref=None):
        super(GenericTestMechanism, self).__init__(id_=id_, idref=idref)
        self.descriptions = StructuredTextList()

    @property
    def description(self):
        """A single description about the contents or purpose of this object.

        Default Value: ``None``

        Note:
            If this object has more than one description set, this will return
            the description with the lowest ordinality value.

        Returns:
            An instance of
            :class:`.StructuredText`

        """
        return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        self.descriptions = StructuredTextList(value)

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        if self.descriptions is None:
            self.descriptions = StructuredTextList()
        self.descriptions.add(description)
