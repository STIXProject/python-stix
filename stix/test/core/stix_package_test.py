import unittest

from cybox.test import EntityTestCase

from stix.core import STIXPackage


class STIXPackageTests(EntityTestCase, unittest.TestCase):
    klass = STIXPackage
    _full_dict = {
        'stix_header': {
            'title': "A Title",
            'description': "A really, really long description",
        },
        'ttps': {
            'ttps': [
            {
                'title': "Foo",
                'version': "1.1"
            },
            ]
        },
        'exploit_targets': [
        {
            'id': 'example:ExploitTarget-1',
            'version': '1.1',
            'title': "ExploitTarget1",
            'description': "This is a long description about an ExploitTarget",
            'short_description': "an ExploitTarget",
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
                    'color': "RED",
                    'xsi:type': "tlpMarking:TLPMarkingStructureType",
                }]
            }
            ]
        }
        ],
        'courses_of_action': [
        {
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
        ],
        'version': "1.1"
    }


if __name__ == "__main__":
    unittest.main()
