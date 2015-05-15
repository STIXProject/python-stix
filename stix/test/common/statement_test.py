# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase
from stix.test.common import structured_text_tests

from stix.common import Statement


class StatementTests(EntityTestCase, unittest.TestCase):
    klass = Statement
    _full_dict = {
        'timestamp': "2014-01-31T06:14:46",
        'timestamp_precision': 'day',
        'value': "Something strange is going on",
        'description': "An amazing source",
        'source': { 'description': "An amazing source",
                    'identity': {'name': "Spiderman",}
                   },
        'confidence': {
            'value': {'value': "Low", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'},
        },
    }


class StatementMultiDescTests(EntityTestCase, unittest.TestCase):
    klass = Statement
    _full_dict = {
        'description': structured_text_tests.StructuredTextListTests._full_dict
    }


if __name__ == "__main__":
    unittest.main()
