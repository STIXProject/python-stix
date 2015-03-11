# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase, data_marking_test
from stix.test.common import (
    confidence_test, information_source_test, statement_test, related_test,
)
from stix.test.extensions.structured_coa import generic_test
import stix.coa as coa
import stix.coa.objective as objective


class RelatedCOAsTests(EntityTestCase, unittest.TestCase):
    klass = coa.RelatedCOAs

    _full_dict = {
        'coas': [
            related_test.RelatedCOATests._full_dict
        ]
    }

class ObjectiveTests(EntityTestCase, unittest.TestCase):
    klass = objective.Objective

    _full_dict = {
        'description': 'Test',
        'short_description': 'Short Description Test',
        'applicability_confidence': confidence_test.ConfidenceTests._full_dict
    }


class COATests(EntityTestCase, unittest.TestCase):
    klass = coa.CourseOfAction
    _full_dict = {
        'id': 'example:test-1',
        'timestamp': "2014-03-20T04:35:12",
        'version': '1.1',
        'title': "COA1",
        'description': "This is a long description about a course of action",
        'short_description': "a COA",
        'stage':  {
            'value': 'Remedy',
            'xsi:type': 'stixVocabs:COAStageVocab-1.0'
        },
        'type': {
            'value': 'Redirection',
            'xsi:type': 'stixVocabs:CourseOfActionTypeVocab-1.0'
        },
        'objective': ObjectiveTests._full_dict,
        'parameter_observables': {
            'major_version': 2,
            'minor_version': 1,
            'update_version': 0,
            'observables': [
                {
                    'idref': "example:Observable-1"
                }
            ]
        },
        'impact': statement_test.StatementTests._full_dict,
        'cost': statement_test.StatementTests._full_dict,
        'efficacy': statement_test.StatementTests._full_dict,
        'information_source': information_source_test.InformationSourceTests._full_dict,
        'handling': data_marking_test.MarkingTests._full_dict,
        'related_coas': RelatedCOAsTests._full_dict,
        'related_packages': related_test.RelatedPackageRefsTests._full_dict,
        'structured_coa': generic_test.GenericStructuredCOATests._full_dict
    }



    def test_structured_coa(self):
        coa_ = coa.CourseOfAction()

        def should_fail():
            coa_.structured_coa = "ERROR"

        self.assertRaises(
            TypeError,
            should_fail
        )

        from stix.extensions.structured_coa.generic_structured_coa import GenericStructuredCOA

        struct_coa = GenericStructuredCOA()
        struct_coa.description = "SUCCESS"
        coa_.structured_coa = struct_coa

        self.assertTrue(str(coa_.structured_coa.description) == "SUCCESS")


if __name__ == "__main__":
    unittest.main()
