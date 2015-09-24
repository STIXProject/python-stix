# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding

from stix.base import AttributeField, ElementField

from .confidence import Confidence
from .structured_text import StructuredTextList
from .vocabs import VocabField, HighMediumLow


class Statement(stix.Entity):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.StatementType

    # Fields
    timestamp = AttributeField("timestamp")
    timestamp_precision = AttributeField("timestamp_precision")
    value = VocabField("Value", HighMediumLow)
    descriptions = ElementField("Description", StructuredTextList)
    confidence = ElementField("Confidence", Confidence)

    # Set by init_typed_fields() to avoid
    source = None

    def __init__(self, value=None, timestamp=None, description=None,
                 source=None):
        super(Statement, self).__init__()

        self.timestamp = timestamp or utils.dates.now()
        self.timestamp_precision = "second"
        self.value = value
        self.description = description
        self.source = source
        self.confidence = None

    @classmethod
    def _init_typed_fields(cls):
        from stix.common.information_source import InformationSource
        cls.source = ElementField("Source", InformationSource)

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

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        self.descriptions.add(description)
