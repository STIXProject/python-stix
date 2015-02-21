# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase

from stix.common import Activity


class ActivityTests(EntityTestCase, unittest.TestCase):
    klass = Activity
    _full_dict = {
        'date_time': "2014-01-31T06:14:46",
        'description': "And then something happened...",
    }


if __name__ == "__main__":
    unittest.main()
