# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from datetime import datetime
import dateutil

import stix
import stix.bindings.stix_common as common_binding

from .structured_text import StructuredText
from .vocabs import VocabString, HighMediumLow


class Confidence(stix.Entity):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.ConfidenceType

    def __init__(self, value=None, description=None, source=None):
        self.timestamp = None
        self.timestamp_precision = "second"
        self.value = value
        self.description = description
        self.source = source
        #TODO: support confidence_assertion_chain
        #self.onfidence_assertion_chain = None

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if not value:
            self._timestamp = None
        elif isinstance(value, datetime):
            self._timestamp =  value
        else:
            self._timestamp = dateutil.parser.parse(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value is None:
            self._value = None
        if isinstance(value, VocabString):
            self._value = value
        else:
            self._value = HighMediumLow(value=value)

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        if value is None:
            self._source = None
        elif isinstance(value, VocabString):
            self._source = value
        else:
            self._source = VocabString(value=value)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if not value:
            self._description = None
        elif isinstance(value, StructuredText):
            self._description = value
        else:
            self._description = StructuredText(value=value)

    # @property
    # def confidence_assertion_chain(self):
    #     return self._confidence_assertion_chain

    # @confidence_assertion_chain.setter
    # def confidence_assertion_chain(self, value):
    #     if value:
    #         raise NotImplementedError()

    def to_obj(self):
        obj = self._binding_class()

        if self.timestamp:
            obj.set_timestamp(self.timestamp.isoformat())
        obj.set_timestamp_precision(self.timestamp_precision)
        if self.value:
            obj.set_Value(self.value.to_obj())
        if self.description:
            obj.set_Description(self.description.to_obj())
        if self.source:
            obj.set_Source(self.source.to_obj())

        return obj

    def to_dict(self):
        d = {}
        if self.timestamp:
            d['timestamp'] = self.timestamp.isoformat()
        if self.timestamp_precision != 'second':
            d['timestamp_precision'] = self.timestamp_precision
        if self.value:
            d['value'] = self.value.to_dict()
        if self.description:
            d['description'] = self.description.to_dict()
        if self.source:
            d['source'] = self.source.to_dict()
            
        return d

    @staticmethod
    def from_obj(obj):
        if not obj:
            return None
        c = Confidence()

        c.timestamp = obj.get_timestamp()
        c.timestamp_precision = obj.get_timestamp_precision()
        c.value = HighMediumLow.from_obj(obj.get_Value())
        c.description = StructuredText.from_obj(obj.get_Description())
        c.source = VocabString.from_obj(obj.get_Source())

        return c

    @staticmethod
    def from_dict(dict_):
        if dict_ is None:
            return None
        c = Confidence()

        c.timestamp = dict_.get('timestamp')
        c.timestamp_precision = dict_.get('timestamp_precision', 'second')
        c.value = HighMediumLow.from_dict(dict_.get('value'))
        c.description = StructuredText.from_dict(dict_.get('description'))
        c.source = VocabString.from_dict(dict_.get('source'))

        return c


class ConfidenceAssertionChain(stix.Entity):
    _namespace = 'http://stix.mitre.org/common-2'
    _binding = common_binding

    def __init__(self):
        self.confidence_assertions = []

    def add_confidence_assertion(self, confidence_assertion):
        if isinstance(confidence_assertion, Confidence):
            self.confidence_assertion.append(confidence_assertion)
        else:
            tmp_confidence = Confidence(value=confidence_assertion)
            self.confidence_assertions.append(tmp_confidence)

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding.ConfidenceAssertionChainType()

        return None

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        return None

    def to_dict(self):
        return {}

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        return None
