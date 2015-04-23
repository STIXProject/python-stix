# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding

from .confidence import Confidence
from .structured_text import StructuredTextList
from .vocabs import VocabString, HighMediumLow


class Statement(stix.Entity):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.StatementType

    def __init__(self, value=None, timestamp=None, description=None,
                 source=None):
        self.timestamp = timestamp or utils.dates.now()
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
        self._timestamp = utils.dates.parse_value(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._set_vocab(HighMediumLow, value=value)

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        from .information_source import InformationSource
        self._set_var(InformationSource, try_cast=False, source=value)
          
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
        self.descriptions = value

    @property
    def descriptions(self):
        """A :class:`.StructuredTextList` object, containing descriptions about
        the purpose or intent of this object.

        Iterating over this object will yield its contents sorted by their
        ``ordinality`` value.

        Default Value: Empty :class:`StructuredTextList` object.

        Note:
            IF this is set to a value that is not an instance of
            :class:`.StructuredText`, an effort will ne made to convert it.
            If this is set to an iterable, any values contained that are not
            an instance of :class:`StructuredText` will be be converted.

        Returns:
            An instance of
            :class:`.StructuredTextList`

        """
        return self._descriptions

    @descriptions.setter
    def descriptions(self, value):
        self._descriptions = StructuredTextList(value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(Statement, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        obj = self._binding_class()
        obj.timestamp_precision = self.timestamp_precision

        if self.timestamp:
            obj.timestamp = self.timestamp.isoformat()
        if self.value:
            obj.Value = self.value.to_obj(ns_info=ns_info)
        if self.descriptions:
            obj.Description = self.descriptions.to_obj(ns_info=ns_info)
        if self.source:
            obj.Source = self.source.to_obj(ns_info=ns_info)
        if self.confidence:
            obj.Confidence = self.confidence.to_obj(ns_info=ns_info)

        return obj

    def to_dict(self):
        skip = ('timestamp_precision', 'description', 'descriptions')
        d = utils.to_dict(self, skip=skip)

        if self.timestamp_precision != 'second':
            d['timestamp_precision'] = self.timestamp_precision

        if self.descriptions:
            d['description'] = self.descriptions.to_dict()

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
        return_obj.descriptions = StructuredTextList.from_obj(obj.Description)
        return_obj.source = InformationSource.from_obj(obj.Source)
        return_obj.confidence = Confidence.from_obj(obj.Confidence)

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
        return_obj.descriptions = StructuredTextList.from_dict(d.get('description'))
        return_obj.source = InformationSource.from_dict(d.get('source'))
        return_obj.confidence = Confidence.from_dict(d.get('confidence'))

        return return_obj
