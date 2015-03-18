# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding

from . import vocabs, VocabString
from .structured_text import StructuredText


class Confidence(stix.Entity):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.ConfidenceType

    def __init__(self, value=None, timestamp=None, description=None, source=None):
        self.timestamp = timestamp or utils.dates.now()
        self.timestamp_precision = "second"
        self.value = value
        self.description = description
        self.source = source
        # TODO: support confidence_assertion_chain
        # self.confidence_assertion_chain = None

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = utils.dates.parse_value(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._set_vocab(vocabs.HighMediumLow, value=value)

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        from .information_source import InformationSource
        self._set_var(InformationSource, try_cast=False, source=value)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._set_var(StructuredText, description=value)

    # @property
    # def confidence_assertion_chain(self):
    #     return self._confidence_assertion_chain

    # @confidence_assertion_chain.setter
    # def confidence_assertion_chain(self, value):
    #     if value:
    #         raise NotImplementedError()

    def to_obj(self, return_obj=None, ns_info=None):
        super(Confidence, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        obj = self._binding_class()
        obj.timestamp = utils.dates.serialize_value(self.timestamp)
        obj.timestamp_precision = self.timestamp_precision

        if self.value:
            obj.Value = self.value.to_obj(ns_info=ns_info)
        if self.description:
            obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.source:
            obj.Source = self.source.to_obj(ns_info=ns_info)

        return obj

    def to_dict(self):
        d = utils.to_dict(self, skip=('timestamp_precision',))

        if self.timestamp_precision != 'second':
            d['timestamp_precision'] = self.timestamp_precision

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        from .information_source import InformationSource
        
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.timestamp = obj.timestamp
        return_obj.timestamp_precision = obj.timestamp_precision
        return_obj.value = VocabString.from_obj(obj.Value)
        return_obj.description = StructuredText.from_obj(obj.Description)
        return_obj.source = InformationSource.from_obj(obj.Source)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        from .information_source import InformationSource
        
        if not d:
            return None
        
        if not return_obj:
            return_obj = cls()

        return_obj.timestamp = d.get('timestamp')
        return_obj.timestamp_precision = d.get('timestamp_precision', 'second')
        return_obj.value = VocabString.from_dict(d.get('value'))
        return_obj.description = StructuredText.from_dict(d.get('description'))
        return_obj.source = InformationSource.from_dict(d.get('source'))

        return return_obj


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
