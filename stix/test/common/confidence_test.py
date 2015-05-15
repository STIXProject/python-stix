# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase
from stix.test.common import structured_text_tests

from stix.common import Confidence


class ConfidenceTests(EntityTestCase, unittest.TestCase):
    klass = Confidence
    _full_dict = {
        'timestamp': "2014-01-31T06:14:46",
        'timestamp_precision': 'day',
        'value': {'value': "High", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'},
        'description': "An amazing source",
        'source': {
            'description': "An amazing source",
            'identity': {'name': "Spiderman",}
        }
    }

class ConfidenceMultiDescTests(EntityTestCase, unittest.TestCase):
    klass = Confidence
    _full_dict = {
        'description': structured_text_tests.StructuredTextListTests._full_dict
    }



if __name__ == "__main__":
    unittest.main()
