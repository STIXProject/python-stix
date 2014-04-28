import unittest

from cybox.test import EntityTestCase

from stix.common import Statement


class StatementTests(EntityTestCase, unittest.TestCase):
    klass = Statement
    _full_dict = {
        'timestamp': "2014-01-31T06:14:46",
        'timestamp_precision': 'day',
        'value': "Something strange is going on",
        'description': "An amazing source",
        'source': "a source",
        'confidence': {
            'value': {'value': "Low", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'},
        },
    }


if __name__ == "__main__":
    unittest.main()
