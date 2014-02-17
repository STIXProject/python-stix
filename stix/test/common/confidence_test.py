import unittest

from cybox.test import EntityTestCase

from stix.common import Confidence


class ConfidenceTests(EntityTestCase, unittest.TestCase):
    klass = Confidence
    _full_dict = {
        'timestamp': "2014-01-31T06:14:46",
        'timestamp_precision': 'day',
        'value': "High",
        'description': "An amazing source",
        'source': "a source",
    }


if __name__ == "__main__":
    unittest.main()
