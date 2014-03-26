import unittest
from cybox.test import EntityTestCase
from stix.coa import CourseOfAction

class COATests(EntityTestCase, unittest.TestCase):
    klass = CourseOfAction
    _full_dict = {
        'id': 'example:coa-1',
        'idref': 'example:coa-2',
        'timestamp': "2014-03-20T04:35:12",
        'version': '1.1',
        'title': "COA1",
        'stage': "Remedy",
        'type': "Redirection",
        'description': "This is a long description about a course of action",
        'short_description': "a COA",
        'objective': {
            'description': "This is why we're taking this action",
            'short_description': "Stop the bad stuff",
            'applicability_confidence': {
                'value': "Medium"
            },
        },
        'impact': {
            'value': "Large"
        },
        'cost': {
            'value': "100"
        },
        'efficacy': {
            'value': "Half"
        },
        'information_source': {
            'description': "Mr. Evil's enemy",
            'identity': {
                'name': "Ms. Good",
            },
        },
        'handling': [
            {
                'marking_structure': [{
                    'marking_model_name': 'TLP',
                    'color': "GREEN",
                    'xsi:type': "tlpMarking:TLPMarkingStructureType",
                }]
            }
        ],
        'related_packages': {
            'packages': [
                {'idref': "example:Package-AB", 'relationship': "Parent"},
                {'idref': "example:Package-CD", 'relationship': "Child"}
            ]
        },
        'related_coas': {
            'scope': 'inclusive',
            'coas': [
                { 'course_of_action': {
                    'id': 'example:coa-5',
                    'idref': 'example:coa-6',
                    'version': '1.1',
                    'timestamp': "2014-03-25T09:35:12",
                    'title': "COA Related",
                    'description': "This is a long description about a course of action that is related",
                    'short_description': "a COA",
                    'stage': "Remedy",
                    'type': "Redirection",
                    'cost': {
                        'value': "50"
                    },
                    'efficacy': {
                        'value': "Half"
                    },
                    'impact': {
                        'value': "Large"
                    },
                    'information_source': {
                        'description': "Mr. Evil's enemy",
                        'identity': {
                            'name': "Ms. Good",
                        },
                    },
                    'handling': [
                    {
                        'marking_structure': [{
                            'marking_model_name': 'TLP',
                            'color': "GREEN",
                            'xsi:type': "tlpMarking:TLPMarkingStructureType",
                        }]
                    }
                    ]
                }
            }
            ]
        }
    }

if __name__ == "__main__":
    unittest.main()
