# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix import utils
from stix.test import EntityTestCase
from stix.common import EncodedCDATA


class CDATATests(unittest.TestCase):
    def test_strip_cdata(self):
        initial = "TESTTESTTEST"
        wrapped = "<![CDATA[%s]]>" % initial
        stripped = utils.strip_cdata(wrapped)

        self.assertEqual(stripped, initial)

    def test_wrap_cdata(self):
        initial = "TESTTESTTEST"
        wrapped = "<![CDATA[%s]]>" % initial
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


class EncodedCDATATests(EntityTestCase, unittest.TestCase):
    klass = EncodedCDATA
    _full_dict = {
        'value': 'alert tcp any any -> any any (msg:"FOX-SRT - Flowbit - TLS-SSL Client Hello"; flow:established; dsize:< 500; content:"|16 03|"; depth:2; byte_test:1, <=, 2, 3; byte_test:1, !=, 2, 1; content:"|01|"; offset:5; depth:1; content:"|03|"; offset:9; byte_test:1, <=, 3, 10; byte_test:1, !=, 2, 9; content:"|00 0f 00|"; flowbits:set,foxsslsession; flowbits:noalert; threshold:type limit, track by_src, count 1, seconds 60; reference:cve,2014-0160; classtype:bad-unknown; sid: 21001130; rev:9;)',
        'encoded': False
    }

    def test_strip_cdata(self):
        stripped = "TESTTEST"
        wrapped = '<![CDATA[%s]]>' % stripped

        d = {
            'value': wrapped,
            'encoded': False
        }

        ecdata = EncodedCDATA.from_dict(d)
        self.assertEqual(ecdata.value, stripped)

    def test_set_value(self):
        stripped = "TESTTEST"
        wrapped = '<![CDATA[%s]]>' % stripped

        ecdata = EncodedCDATA()
        ecdata.value = wrapped

        self.assertEqual(ecdata.value, stripped)
        self.assertEqual(ecdata.cdata, wrapped)

    def test_set_none(self):
        ecdata = EncodedCDATA()
        ecdata.value = None

        self.assertTrue(ecdata.value is None)
        self.assertTrue(ecdata.cdata is None)


if __name__ == '__main__':
    unittest.main()
