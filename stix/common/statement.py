# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

from datetime import datetime
import dateutil
from dateutil.tz import tzutc

import stix
import stix.bindings.stix_common as common_binding

from .confidence import Confidence
from .structured_text import StructuredText
from .vocabs import VocabString, HighMediumLow


class Statement(stix.Entity):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.StatementType

    def __init__(self, value=None, timestamp=None, description=None, source=None):
        self.timestamp = timestamp or datetime.now(tzutc())
        self.timestamp_precision = "second"
        self.value = value
        self.description = description
        self.source = source
        self.confidence = None

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
            # HighMediumLow is the default vocab to use for the Value
            # field.
            self._value = HighMediumLow(value=value)

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        from .information_source import InformationSource
        
        if value is None:
            self._source = None
        elif isinstance(value, InformationSource):
            self._source = value
        else:
            raise ValueError("source must be of type InformationSource")
          
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
        if self.confidence:
            obj.set_Confidence(self.confidence.to_obj())

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
        if self.source:
            d['source'] = self.source.to_dict()
        if self.confidence:
            d['confidence'] = self.confidence.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj):
        from .information_source import InformationSource
        
        if not obj:
            return None
        s = cls()

        s.timestamp = obj.get_timestamp()
        s.timestamp_precision = obj.get_timestamp_precision()
        s.value = VocabString.from_obj(obj.get_Value())
        s.description = StructuredText.from_obj(obj.get_Description())
        s.source = InformationSource.from_obj(obj.get_Source())
        s.confidence = Confidence.from_obj(obj.get_Confidence())

        return s

    @classmethod
    def from_dict(cls, dict_):
        from .information_source import InformationSource
        
        if dict_ is None:
            return None
        s = cls()

        s.timestamp = dict_.get('timestamp')
        s.timestamp_precision = dict_.get('timestamp_precision', 'second')
        s.value = VocabString.from_dict(dict_.get('value'))
        s.description = StructuredText.from_dict(dict_.get('description'))
        s.source = InformationSource.from_dict(dict_.get('source'))
        s.confidence = Confidence.from_dict(dict_.get('confidence'))

        return s
