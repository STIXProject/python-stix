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


if __name__ == "__main__":
    unittest.main()
