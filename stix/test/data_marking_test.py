# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

import stix.data_marking as dm
from stix.test import EntityTestCase
from stix.test.common import information_source_test


class MarkingSpecificationTests(EntityTestCase, unittest.TestCase):
    klass = dm.MarkingSpecification
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
        self.assertRaises(ValueError, dm.MarkingStructure.from_dict, d)

    def test_xsi_type_required(self):
        d = {
            'marking_model_name': 'TLP',
            'xsi:type': "UNKNOWN_XSI_TYPE",
        }

        self.assertRaises(ValueError, dm.MarkingStructure.from_dict, d)


class MarkingTests(EntityTestCase, unittest.TestCase):
    klass = dm.Marking
    _full_dict = [
        {
            'id': "foo",
            'information_source': information_source_test.InformationSourceTests._full_dict
        },
        {
            'id': "bar",
        },
    ]


if __name__ == "__main__":
    unittest.main()
