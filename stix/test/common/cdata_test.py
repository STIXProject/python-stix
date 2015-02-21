# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
from lxml import etree
import stix.utils as utils

class CdataTests(unittest.TestCase):
    def test_strip_cdata(self):
        initial = "TESTTESTTEST"
        wrapped = "<![CDATA[%s]]>" % (initial)
        stripped = utils.strip_cdata(wrapped)

        self.assertEqual(stripped, initial)

    def test_wrap_cdata(self):
        initial = "TESTTESTTEST"
        wrapped = "<![CDATA[%s]]>" % (initial)
        cdata = utils.cdata(initial)

        self.assertEqual(wrapped, cdata)

    def test_round_trip(self):
        initial = "TESTTESTTEST"
        round_trip = utils.strip_cdata(utils.cdata(initial))

        self.assertEqual(initial, round_trip)

    def test_multi_cdata_strip(self):
        initial = "TESTTESTTEST"
        multi = "<![CDATA[{0}]]><![CDATA[{0}]]>".format(initial)
        stripped = utils.strip_cdata(multi)
        self.assertEqual(stripped, initial*2)

if __name__ == '__main__':
    unittest.main()
