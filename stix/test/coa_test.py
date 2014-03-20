import unittest
from cybox.test import EntityTestCase
from stix.coa import CourseOfAction

class COATests(EntityTestCase, unittest.TestCase):
    klass = CourseOfAction
    _full_dict = {
        'id': 'example:coa-1',
        'idref': 'example:coa-2',
        'version': '1.1',
        'timestamp': "2014-03-20T04:35:12",
        'title': "COA1",
        'description': "This is a long description about a course of action",
        'short_description': "a COA",
        'stage': "Remedy",
        'type': "Redirection",
        'cost': {
            'value': "100"
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

if __name__ == "__main__":
    unittest.main()
