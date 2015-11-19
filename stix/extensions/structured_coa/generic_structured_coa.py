# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields

# internal
import stix
from stix.common import EncodedCDATA, StructuredTextList
from stix.common.vocabs import VocabField
from stix.coa.structured_coa import _BaseStructuredCOA

# bindings
import stix.bindings.extensions.structured_coa.generic as generic_structured_coa_binding


@stix.register_extension
class GenericStructuredCOA(_BaseStructuredCOA):
    _namespace = "http://stix.mitre.org/extensions/StructuredCOA#Generic-1"
    _binding = generic_structured_coa_binding
    _binding_class = _binding.GenericStructuredCOAType
    _XSI_TYPE = "genericStructuredCOA:GenericStructuredCOAType"

    specification = fields.TypedField("Specification", EncodedCDATA)
    descriptions = fields.TypedField("Description", type_=StructuredTextList)
    reference_location = fields.TypedField("reference_location")
    type_ = VocabField("Type")

    def __init__(self, id_=None, idref=None):
        super(GenericStructuredCOA, self).__init__(id_=id_, idref=idref)
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
        if self.descriptions is not None:
            return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        self.descriptions = StructuredTextList(value)

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        self.descriptions.add(description)
