# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
from stix.test import EntityTestCase
from stix.coa import CourseOfAction

class COATests(EntityTestCase, unittest.TestCase):
    klass = CourseOfAction
    _full_dict = {
        'id': 'example:coa-1',
        'timestamp': "2014-03-20T04:35:12",
        'version': '1.1',
        'title': "COA1",
        'stage':  {'value': 'Remedy', 'xsi:type': 'stixVocabs:COAStageVocab-1.0'},
        'type': {'value': 'Redirection', 'xsi:type': 'stixVocabs:CourseOfActionTypeVocab-1.0'},
        'description': "This is a long description about a course of action",
        'short_description': "a COA",
        'objective': {
            'description': "This is why we're taking this action",
            'short_description': "Stop the bad stuff",
            'applicability_confidence': {'value': {'value': 'Medium', 
                                                   'xsi:type': 'stixVocabs:HighMediumLowVocab-1.0'}},
        },
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
        'impact': {'value': {'value': 'Medium', 
                             'xsi:type': 'stixVocabs:HighMediumLowVocab-1.0'}},
        'cost': {'value': {'value': 'Medium', 
                           'xsi:type': 'stixVocabs:HighMediumLowVocab-1.0'}},
        'efficacy': {'value': {'value': 'Medium', 
                               'xsi:type': 'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Mr. Evil's enemy",
            'identity': {
                'name': "Ms. Good",
            },
        },
        'handling': [
            {
                'marking_structures': [{
                    'marking_model_name': 'TLP',
                    'color': "GREEN",
                    'xsi:type': "tlpMarking:TLPMarkingStructureType",
                }]
            }
        ],
        'related_coas': {
            'scope': "exclusive",
            'coas': [
                {
                    'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                    'course_of_action': {'idref': "example:COA-52",
                                         'version': '1.1.1'},
                }
            ]
        },
        'related_packages': {
            'packages': [
                {'idref': "example:Package-AB", 'relationship': "Parent"},
                {'idref': "example:Package-CD", 'relationship': "Child"}
            ]
        },
    }

if __name__ == "__main__":
    unittest.main()
