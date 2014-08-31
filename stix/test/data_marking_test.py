import unittest

from stix.test import EntityTestCase

from stix.data_marking import Marking, MarkingSpecification, MarkingStructure
import stix.extensions.marking.tlp


class MarkingTests(EntityTestCase, unittest.TestCase):
    klass = Marking
    _full_dict = [
        {
            'id': "foo",
        },
        {
            'id': "bar",
        },
    ]


class MarkingSpecificationTests(EntityTestCase, unittest.TestCase):
    klass = MarkingSpecification
    _full_dict = {
        'id': "foo",
        'idref': "foo_ref",
        'version': "1234",
        'controlled_structure': "some xpath",
        'marking_structures': [
            {
                'marking_model_name': 'TLP',
                'xsi:type': "tlpMarking:TLPMarkingStructureType",
            }
        ]
    }


class MarkingStructureTests(unittest.TestCase):

    def test_xsi_type_required(self):
        d = {
            'marking_model_name': 'TLP',
        }

        # If there's not an xsi:type in the dict, this will raise an error.
        self.assertRaises(ValueError, MarkingStructure.from_dict, d)

    def test_xsi_type_required(self):
        d = {
            'marking_model_name': 'TLP',
            'xsi:type': "UNKNOWN_XSI_TYPE",
        }

        self.assertRaises(ValueError, MarkingStructure.from_dict, d)



if __name__ == "__main__":
    unittest.main()
