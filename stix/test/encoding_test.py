# -*- coding: utf-8 -*-
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""Tests for various encoding issues throughout the library"""

import unittest

import stix.bindings as bindings
from stix.core import STIXHeader
from stix.indicator import Indicator
from stix.common import StructuredText
from stix.test import round_trip

UNICODE_STR = u"❤ ♎ ☀ ★ ☂ ♞ ☯ ☭ ☢ €☎⚑ ❄♫✂"

def _test_unicode_values(val1, val2):
    encoding = bindings.ExternalEncoding

    if isinstance(val1, unicode):
        val1 = val1.encode(encoding)

    if isinstance(val2, unicode):
        val2 = val2.encode(encoding)

    return val1 == val2


class EncodingTests(unittest.TestCase):

    def test_double_encode(self):
        s = StructuredText(UNICODE_STR)
        s2 = round_trip(s)
        self.assertTrue(_test_unicode_values(s.value, s2.value))

    def test_stix_header(self):
        header = STIXHeader()
        header.title = UNICODE_STR
        header.description = UNICODE_STR
        header.short_description = UNICODE_STR
        header2 = round_trip(header)
        self.assertTrue(_test_unicode_values(header.title, header2.title))

    def test_indicator(self):
        i = Indicator()
        i.title = UNICODE_STR
        i.description = UNICODE_STR
        i.short_description = UNICODE_STR
        i2 = round_trip(i)
        self.assertTrue(_test_unicode_values(i.title, i2.title))

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


if __name__ == "__main__":
    unittest.main()
