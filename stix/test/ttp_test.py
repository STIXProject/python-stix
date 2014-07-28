import unittest
from cybox.test import EntityTestCase
from stix.ttp import TTP

class TTPTests(EntityTestCase, unittest.TestCase):
    klass = TTP
    _full_dict = {
        'id': 'example:ttp-1',
        'version': '1.1',
        'title': "TTP1",
        'description': "This is a long description about a ttp",
        'short_description': "a TTP",
        'resources': {
            'tools': [
                {'title': "Tool"}
            ],
            'infrastructure': {'title': "Infrastructure"},
        },
        'handling': [
            {
                'marking_structures': [
                    {
                        'marking_model_name': 'TLP',
                        'color': "RED",
                        'xsi:type': "tlpMarking:TLPMarkingStructureType",
                    }
                ]
            }
        ],
        'exploit_targets': {
            'scope': "exclusive",
            'exploit_targets': [
                {
                    'exploit_target': {'id': 'example:ExploitTarget-1',
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
                        'marking_structures': [{
                            'marking_model_name': 'TLP',
                            'color': "RED",
                            'xsi:type': "tlpMarking:TLPMarkingStructureType",
                        }]
                    }
                    ]}
                },
            ]
        }
    }

if __name__ == "__main__":
    unittest.main()
