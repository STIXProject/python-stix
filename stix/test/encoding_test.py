# -*- coding: utf-8 -*-
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Tests for various encoding issues throughout the library"""

import unittest

import stix.bindings as bindings
from stix.core import STIXHeader
from stix.campaign import Campaign
from stix.indicator import Indicator
from stix.incident import Incident
from stix.exploit_target import ExploitTarget
from stix.threat_actor import ThreatActor
from stix.ttp import TTP
from stix.common import StructuredText
import stix.incident.affected_asset as affected_asset

from stix.test import round_trip

UNICODE_STR = u"❤ ♎ ☀ ★ ☂ ♞ ☯ ☭ ☢ €☎⚑ ❄♫✂"

class EncodingTests(unittest.TestCase):

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

    def test_quote_xml(self):
        s = bindings.quote_xml(UNICODE_STR)
        s = s.decode(bindings.ExternalEncoding)
        self.assertEqual(s, UNICODE_STR)

    def test_quote_attrib(self):
        """Tests that the stix.bindings.quote_attrib method works properly
        on unicode inputs.

        Note:
            The quote_attrib method (more specifically, saxutils.quoteattr())
            adds quotation marks around the input data, so we need to strip
            the leading and trailing chars to test effectively
        """
        s = bindings.quote_attrib(UNICODE_STR)
        s = s[1:-1]
        s = s.decode(bindings.ExternalEncoding)
        self.assertEqual(s, UNICODE_STR)

    def test_quote_attrib_int(self):
        i = 65536
        s = bindings.quote_attrib(i)
        s = s[1:-1]
        self.assertEqual(str(i), s)

    def test_quote_attrib_bool(self):
        b = True
        s = bindings.quote_attrib(b)
        s = s[1:-1]
        self.assertEqual(str(b), s)

    def test_quote_xml_int(self):
        i = 65536
        s = bindings.quote_xml(i)
        self.assertEqual(str(i), s)

    def test_quote_xml_bool(self):
        b = True
        s = bindings.quote_xml(b)
        self.assertEqual(str(b), s)

    def test_quote_xml_encoded(self):
        encoding = bindings.ExternalEncoding
        encoded = UNICODE_STR.encode(encoding)
        quoted = bindings.quote_xml(encoded)
        decoded = quoted.decode(encoding)
        self.assertEqual(UNICODE_STR, decoded)

    def test_quote_attrib_encoded(self):
        encoding = bindings.ExternalEncoding
        encoded = UNICODE_STR.encode(encoding)
        quoted = bindings.quote_attrib(encoded)[1:-1]
        decoded = quoted.decode(encoding)
        self.assertEqual(UNICODE_STR, decoded)

    def test_quote_xml_zero(self):
        i = 0
        s = bindings.quote_xml(i)
        self.assertEqual(str(i), s)

    def test_quote_attrib_zero(self):
        i = 0
        s = bindings.quote_attrib(i)
        s = s[1:-1]
        self.assertEqual(str(i), s)

    def test_quote_xml_none(self):
        i = None
        s = bindings.quote_xml(i)
        self.assertEqual('', s)

    def test_quote_attrib_none(self):
        i = None
        s = bindings.quote_attrib(i)
        s = s[1:-1]
        self.assertEqual('', s)

    def test_quote_attrib_empty(self):
        i = ''
        s = bindings.quote_attrib(i)
        s = s[1:-1]
        self.assertEqual('', s)

    def test_quote_xml_empty(self):
        i = ''
        s = bindings.quote_xml(i)
        self.assertEqual('', s)


if __name__ == "__main__":
    unittest.main()
