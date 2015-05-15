# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import unittest

# internal
from stix import utils


class UtilsTests(unittest.TestCase):
    def test_is_sequence(self):
        self.assertTrue(utils.is_sequence([1,2,3]))
        self.assertTrue(utils.is_sequence((1,2,3)))
        self.assertTrue(utils.is_sequence(set([1,2,3])))
        self.assertTrue(utils.is_sequence({1:1}))

        # Make sure that strings are not sequences.
        self.assertEqual(False, utils.is_sequence("abc"))
