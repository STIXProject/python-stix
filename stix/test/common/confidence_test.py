# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase

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


if __name__ == "__main__":
    unittest.main()
