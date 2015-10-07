# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import assert_warnings
from stix.test import EntityTestCase, data_marking_test
from stix.test.common import information_source_test, structured_text_tests

from stix import core
from stix.utils import silence_warnings
from stix.common.vocabs import PackageIntent


class STIXHeaderTests(EntityTestCase, unittest.TestCase):
    klass = core.STIXHeader
    _full_dict = {
        'title': "A Title",
        'description': "A really, really long description",
        'short_description': 'A really, really short description',
        # 'handling': data_marking_test.MarkingTests._full_dict,
        'information_source': information_source_test.InformationSourceTests._full_dict,
        # 'profiles': ['foo', 'bar']
    }

    @silence_warnings
    def test_duplicate_package_intent(self):
        # Recreate https://github.com/STIXProject/python-stix/issues/63
        hdr = core.STIXHeader(package_intents=["Indicators - Watchlist"])
        self.assertEqual(1, len(hdr.package_intents))

    @assert_warnings
    def test_deprecated_title(self):
        h = core.STIXHeader()
        t = "title"
        h.title = t
        self.assertEqual(h.title, t)

    @assert_warnings
    def test_deprecated_description(self):
        h = core.STIXHeader()
        d = "description"
        h.description = d
        self.assertEqual(str(h.description), d)

    @assert_warnings
    def test_deprecated_short_description(self):
        h = core.STIXHeader()
        sd = "short_description"
        h.short_description = sd
        self.assertEqual(str(h.short_description), sd)

    @assert_warnings
    def test_deprecated_package_intents(self):
        h = core.STIXHeader()
        h.package_intents = PackageIntent.TERM_INCIDENT
        self.assertEqual(str(h.package_intents[0]), PackageIntent.TERM_INCIDENT)


class STIXHeaderMultiDescTests(EntityTestCase, unittest.TestCase):
    klass = core.STIXHeader
    _full_dict = {
        'description': structured_text_tests.StructuredTextListTests._full_dict,
        'short_description': structured_text_tests.StructuredTextListTests._full_dict
    }


if __name__ == "__main__":
    unittest.main()
