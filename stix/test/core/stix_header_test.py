# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase

from stix.core import STIXHeader


class IdentityTests(EntityTestCase, unittest.TestCase):
    klass = STIXHeader
    _full_dict = {
        'title': "A Title",
        'description': "A really, really long description",
        'short_description': 'A really, really short description',
        'handling': [
            {
                'marking_structures': [{
                    'marking_model_name': 'TLP',
                    'color': "WHITE",
                    'xsi:type': "tlpMarking:TLPMarkingStructureType",
                }]
            }
        ]
    }

    def test_duplicate_package_intent(self):
        # Recreate https://github.com/STIXProject/python-stix/issues/63
        hdr = STIXHeader(package_intents=["Indicators - Watchlist"])
        self.assertEqual(1, len(hdr.package_intents))


if __name__ == "__main__":
    unittest.main()
