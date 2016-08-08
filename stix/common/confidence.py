# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

from mixbox import fields

import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding

from .vocabs import VocabField
from .structured_text import StructuredTextList
from .datetimewithprecision import validate_precision


class Confidence(stix.Entity):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.ConfidenceType

    value = VocabField("Value")
    descriptions = fields.TypedField("Description", StructuredTextList)
    timestamp = fields.DateTimeField("timestamp")
    timestamp_precision = fields.TypedField("timestamp_precision", preset_hook=validate_precision)
    source = fields.TypedField("Source", type_="stix.common.InformationSource")
    
    def __init__(self, value=None, timestamp=None, description=None, source=None):
        super(Confidence, self).__init__()

        self.timestamp = timestamp or utils.dates.now()
        self.timestamp_precision = "second"
        self.value = value
        self.description = StructuredTextList(description)
        self.source = source

        # TODO: support confidence_assertion_chain
        # self.confidence_assertion_chain = None

    @property
    def description(self):
        """A single description about the contents or purpose of this object.

        Default Value: ``None``

        Note:
            If this object has more than one description set, this will return
            the description with the lowest ordinality value.

        Returns:
            An instance of :class:`.StructuredText`

        """
        return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        from stix.common.structured_text import StructuredTextList
        if value is None:
            self.descriptions = StructuredTextList()
        else:
            self.descriptions = StructuredTextList(value)

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        self.descriptions.add(description)


# class ConfidenceAssertionChain(stix.Entity):
#     _namespace = 'http://stix.mitre.org/common-2'
#     _binding = common_binding
#
#     def __init__(self):
#         self.confidence_assertions = []
#
#     def add_confidence_assertion(self, confidence_assertion):
#         if isinstance(confidence_assertion, Confidence):
#             self.confidence_assertions.append(confidence_assertion)
#         else:
#             tmp_confidence = Confidence(value=confidence_assertion)
#             self.confidence_assertions.append(tmp_confidence)
#
#     def to_obj(self, return_obj=None, ns_info=None):
#         super(ConfidenceAssertionChain, self).to_obj(return_obj=return_obj, ns_info=ns_info)
#
#         if not return_obj:
#             return_obj = self._binding.ConfidenceAssertionChainType()
#
#         return None
#
#     @classmethod
#     def from_obj(cls, obj, return_obj=None):
#         return None
#
#     def to_dict(self):
#         return {}
#
#     @classmethod
#     def from_dict(cls, dict_repr, return_obj=None):
#         return None
