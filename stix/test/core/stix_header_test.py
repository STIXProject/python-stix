# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase, data_marking_test
from stix.test.common import information_source_test

from stix import core


class STIXHeaderTests(EntityTestCase, unittest.TestCase):
    klass = core.STIXHeader
    _full_dict = {
        'title': "A Title",
        'description': "A really, really long description",
        'short_description': 'A really, really short description',
        'handling': data_marking_test.MarkingTests._full_dict,
        'information_source': information_source_test.InformationSourceTests._full_dict,
        'profiles': ['foo', 'bar']
    }

    def test_duplicate_package_intent(self):
        # Recreate https://github.com/STIXProject/python-stix/issues/63
        hdr = core.STIXHeader(package_intents=["Indicators - Watchlist"])
        self.assertEqual(1, len(hdr.package_intents))


if __name__ == "__main__":
    unittest.main()
