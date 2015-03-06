# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase

from stix.common import Names

class NamesTests(EntityTestCase, unittest.TestCase):
    klass = Names
    _full_dict = [
        "foo",
        "bar",
        {'value': 'User Data Loss', 'xsi:type': 'stixVocabs:IncidentEffectVocab-1.0'},
    ]


if __name__ == '__main__':
    unittest.main()
