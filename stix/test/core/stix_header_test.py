import unittest

from cybox.test import EntityTestCase

from stix.core import STIXHeader


class IdentityTests(EntityTestCase, unittest.TestCase):
    klass = STIXHeader
    _full_dict = {
        'title': "A Title",
        'description': "A really, really long description",
        'handling': [
            {
                'marking_structure': [{
                    'marking_model_name': 'TLP',
                    'color': "WHITE",
                    'xsi:type': "tlpMarking:TLPMarkingStructureType",
                }]
            }
        ]
    }

    def test_duplicate_package_intent(self):
        # Recreate https://github.com/STIXProject/python-stix/issues/63
        hdr = STIXHeader(package_intents=["Net Defense"])
        self.assertEqual(1, len(hdr.package_intent))


if __name__ == "__main__":
    unittest.main()
