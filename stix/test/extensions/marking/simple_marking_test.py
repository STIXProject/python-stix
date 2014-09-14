import unittest

from stix.test import EntityTestCase

from stix.extensions.marking.simple_marking import SimpleMarkingStructure


class SimpleMarkingStructureTests(EntityTestCase, unittest.TestCase):
    klass = SimpleMarkingStructure
    _full_dict = {
        'statement': "This is a marking statement",
        'xsi:type': "simpleMarking:SimpleMarkingStructureType",
    }


if __name__ == "__main__":
    unittest.main()

