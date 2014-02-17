# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

from .identity import *
from .information_source import InformationSource
from .generic_relationship import GenericRelationship
from .structured_text import StructuredText
from .vocabs import VocabString


class HighMediumLow(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:HighMediumLowVocab-1.0'

