# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

from mixbox import fields

import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding

from .datetimewithprecision import validate_precision
from .confidence import Confidence
from .structured_text import StructuredText
from .vocabs import VocabField, HighMediumLow
import mixbox
from stix.common.vocabs import VocabString


class Statement(stix.Entity):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.StatementType

    # Fields
    timestamp = fields.DateTimeField("timestamp")
    timestamp_precision = fields.TypedField("timestamp_precision", preset_hook=validate_precision)
    value = VocabField("Value", VocabString)
    description = fields.TypedField("Description", StructuredText)
    confidence = fields.TypedField("Confidence", Confidence)
    source = fields.TypedField("Source", type_="stix.common.InformationSource")

    def __init__(self, value=None, timestamp=None, description=None,
                 source=None):
        super(Statement, self).__init__()

        self.timestamp = timestamp or utils.dates.now()
        self.timestamp_precision = "second"
        self.value = value
        self.description = description
        self.source = source
        self.confidence = None


class StatementField(mixbox.fields.TypedField):
    def __init__(self, *args, **kwargs):
        self._vocab_type = kwargs.pop("vocab_type")
        super(StatementField, self).__init__(*args, **kwargs)
        self.type_ = Statement

    def _clean(self, value):
        if value is None:
            return None
        elif isinstance(value, Statement):
            return value
        elif isinstance(value, stix.common.VocabString):
            return Statement(value)
        else:
            vocabklass = self._vocab_type
            return Statement(vocabklass(value))
