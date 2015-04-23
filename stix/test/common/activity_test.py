# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase
from stix.test.common import structured_text_tests

from stix.common import Activity


class ActivityTests(EntityTestCase, unittest.TestCase):
    klass = Activity
    _full_dict = {
        'date_time': "2014-01-31T06:14:46",
        'description': "And then something happened...",
    }


class ActivityMultiDescTests(EntityTestCase, unittest.TestCase):
    klass = Activity
    _full_dict = {
        'date_time': "2014-01-31T06:14:46",
        'description': structured_text_tests.StructuredTextListTests._full_dict
    }


if __name__ == "__main__":
    unittest.main()
