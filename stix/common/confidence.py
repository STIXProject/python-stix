# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding

from . import vocabs, VocabString
from .structured_text import StructuredTextList, StructuredTextListField
from stix.base import ElementField, AttributeField

class Confidence(stix.Entity):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.ConfidenceType

    value = ElementField("Value", VocabString)
    descriptions = StructuredTextListField("Description", StructuredTextList, key_name="description")
    timestamp = AttributeField("timestamp")
    timestamp_precision = AttributeField("timestamp_precision")
    source = ElementField("Source")
    
    def __init__(self, value=None, timestamp=None, description=None, source=None):
        import random
        self._fields = { 'a': random.random() }
        self.timestamp = timestamp or utils.dates.now()
        self.timestamp_precision = "second"
        self.value = value
        self.description = description
        self.source = source
        print "#######################################################"
        print "#######################################################"
        print "#######################################################"
        print "#######################################################"
        print "#######################################################"
        print "#######################################################"
        print "#######################################################"
        print "#######################################################"
        print "#######################################################"
        print self, self.descriptions, self._fields
        pass
        # TODO: support confidence_assertion_chain
        # self.confidence_assertion_chain = None
    
    # called in stix.common.related
    @classmethod
    def initClassFields(cls):
        from .information_source import InformationSource
        cls.source.type_ = InformationSource
        
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = utils.dates.parse_value(value)

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
        return next(iter(self.descriptions), "None")

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

    # @property
    # def confidence_assertion_chain(self):
    #     return self._confidence_assertion_chain

    # @confidence_assertion_chain.setter
    # def confidence_assertion_chain(self, value):
    #     if value:
    #         raise NotImplementedError()


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
