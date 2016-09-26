import unittest

from stix.test import EntityTestCase

from stix.extensions.marking.ais import AISMarkingStructure


class AISMarkingStructureNotProprietaryTests(EntityTestCase, unittest.TestCase):
    klass = AISMarkingStructure
    _full_dict = {
        'not_proprietary':
            {
                'cisa_proprietary': 'false',
                'ais_consent': {'consent': 'NONE'},
                'tlp_marking': {'color': 'GREEN'}
            },
        'xsi:type': 'AIS:AISMarkingStructure'
    }


class AISMarkingStructureIsProprietaryTests(EntityTestCase, unittest.TestCase):
    klass = AISMarkingStructure
    _full_dict = {
        'is_proprietary':
            {
                'cisa_proprietary': 'true',
                'ais_consent': {'consent': 'EVERYONE'},
                'tlp_marking': {'color': 'AMBER'}
            },
        'xsi:type': 'AIS:AISMarkingStructure'
    }

if __name__ == "__main__":
    unittest.main()
