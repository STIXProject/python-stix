# -*- coding: utf-8 -*-
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Tests for various encoding issues throughout the library"""

import unittest
from mixbox.vendor.six import BytesIO, text_type
from mixbox import binding_utils

from stix.core import STIXHeader, STIXPackage
from stix.campaign import Campaign
from stix.indicator import Indicator
from stix.incident import Incident
from stix.exploit_target import ExploitTarget
from stix.threat_actor import ThreatActor
from stix.ttp import TTP
from stix.common import StructuredText
from stix.incident import affected_asset
from stix.utils import silence_warnings

from stix.test import round_trip

UNICODE_STR = u"❤ ♎ ☀ ★ ☂ ♞ ☯ ☭ ☢ €☎⚑ ❄♫✂"

XML = \
u"""
<stix:STIX_Package
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:stix="http://stix.mitre.org/stix-1"
    xmlns:example="http://example.com/"
    id="example:Indicator-ba1d406e-937c-414f-9231-6e1dbe64fe8b" version="1.2" timestamp="2014-05-08T09:00:00.000000Z">
    <stix:STIX_Header>
        <stix:Title>{0}</stix:Title>
    </stix:STIX_Header>
</stix:STIX_Package>
""".format(UNICODE_STR)


class EncodingTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.orig_encoding = binding_utils.ExternalEncoding
        binding_utils.ExternalEncoding = 'utf-16'

    @classmethod
    def tearDownClass(cls):
        binding_utils.ExternalEncoding = cls.orig_encoding

    def _test_equal(self, obj1, obj2):
        self.assertEqual(obj1.title, obj2.title)
        self.assertEqual(obj1.description.value, obj2.description.value)
        self.assertEqual(obj1.short_description.value, obj2.short_description.value)

    def test_structured_text(self):
        s = StructuredText(UNICODE_STR)
        s2 = round_trip(s)
        self.assertEqual(s.value, s2.value)

    def test_asset_type(self):
        a = affected_asset.AssetType()
        a.count_affected = 1
        a2 = round_trip(a)
        self.assertEqual(a.count_affected, a2.count_affected)

    @silence_warnings
    def test_stix_header(self):
        header = STIXHeader()
        header.title = UNICODE_STR
        header.description = UNICODE_STR
        header.short_description = UNICODE_STR
        header2 = round_trip(header)
        self._test_equal(header, header2)

    def test_indicator(self):
        i = Indicator()
        i.title = UNICODE_STR
        i.description = UNICODE_STR
        i.short_description = UNICODE_STR
        i2 = round_trip(i)
        self._test_equal(i, i2)

    def test_incident(self):
        i = Incident()
        i.title = UNICODE_STR
        i.description = UNICODE_STR
        i.short_description = UNICODE_STR
        i2 = round_trip(i)
        self._test_equal(i, i2)

    def test_ttp(self):
        t = TTP()
        t.title = UNICODE_STR
        t.description = UNICODE_STR
        t.short_description = UNICODE_STR
        t2 = round_trip(t)
        self._test_equal(t, t2)

    def test_ta(self):
        t = ThreatActor()
        t.title = UNICODE_STR
        t.description = UNICODE_STR
        t.short_description = UNICODE_STR
        t2 = round_trip(t)
        self._test_equal(t, t2)

    def test_et(self):
        e = ExploitTarget()
        e.title = UNICODE_STR
        e.description = UNICODE_STR
        e.short_description = UNICODE_STR
        e2 = round_trip(e)
        self._test_equal(e, e2)

    def test_campaign(self):
        c = Campaign()
        c.title = UNICODE_STR
        c.description = UNICODE_STR
        c.short_description = UNICODE_STR
        c2 = round_trip(c)
        self._test_equal(c, c2)

    @silence_warnings
    def test_to_xml_utf16_encoded(self):
        encoding = 'utf-16'
        s = STIXHeader()
        s.title = UNICODE_STR
        xml = s.to_xml(encoding=encoding)
        print(xml)
        self.assertTrue(UNICODE_STR in xml.decode(encoding))

    @silence_warnings
    def test_to_xml_default_encoded(self):
        s = STIXHeader()
        s.title = UNICODE_STR
        xml = s.to_xml()
        self.assertTrue(UNICODE_STR in xml.decode('utf-8'))

    @silence_warnings
    def test_to_xml_no_encoding(self):
        s = STIXHeader()
        s.title = UNICODE_STR
        xml = s.to_xml(encoding=None)
        self.assertTrue(isinstance(xml, text_type))
        self.assertTrue(UNICODE_STR in xml)

    @silence_warnings
    def test_from_xml_utf16_encoded(self):
        utf16_xml = XML.encode('utf-16')
        sio = BytesIO(utf16_xml)
        sp = STIXPackage.from_xml(sio, encoding='utf-16')
        header = sp.stix_header
        self.assertEqual(header.title, UNICODE_STR)

    @silence_warnings
    def test_from_xml_default_encoded(self):
        utf8_xml = XML.encode('utf-8')
        sio = BytesIO(utf8_xml)
        sp = STIXPackage.from_xml(sio)
        header = sp.stix_header
        self.assertEqual(header.title, UNICODE_STR)

    @silence_warnings
    def test_utf16_roundtrip(self):
        sh = STIXHeader()
        sh.title = UNICODE_STR
        sp = STIXPackage()
        sp.stix_header = sh

        # serialize as utf-16
        xml16 = sp.to_xml(encoding='utf-16')

        # deserialize as utf-16
        sp2 = STIXPackage.from_xml(BytesIO(xml16), encoding='utf-16')
        sh2 = sp2.stix_header

        # check that the titles align
        self.assertEqual(sh.title, sh2.title)


if __name__ == "__main__":
    unittest.main()
