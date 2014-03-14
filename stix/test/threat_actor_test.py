import unittest

from cybox.test import EntityTestCase

from stix.threat_actor import ThreatActor


class ThreatActorTests(EntityTestCase, unittest.TestCase):
    klass = ThreatActor
    _full_dict = {
        'id': 'example:ThreatActor-1',
        'idref': 'example:ThreatActor-2',
        'timestamp': "2014-01-31T06:14:46",
        'version': '1.1',
        'title': "BadGuy1",
        'description': "This is a long description about a threat actor.",
        'short_description': "A bad guy",
        'identity': {
            'name': "Mr. Evil",
        },
        'type': [
            {'value': "Hacker"},
        ],
        'motivation': [
            {'value': "Ego"},
            {'value': "Opportunistic"},
        ],
        'sophistication': [
            {'value': "Novice"},
        ],
        'intended_effect': [
            {'value': "Account Takeover"},
            {'value': "Extortion"},
        ],
        'planning_and_operational_support': [
            {'value': "Financial Resources"},
        ],
        'observed_ttps': {
            'scope': "exclusive",
            'ttps': [
                {
                    'confidence': {'value': "High"},
                    'ttp': {'title': "A TTP", 'version': "1.1"},
                }
            ],
        },
        'associated_campaigns': {
            'scope': "inclusive",
            'campaigns': [
                {
                    'information_source': {'description': "Mailing List"},
                    'campaign': {'title': "Campaign1", 'version': "1.1"},
                }
            ],
        },
        'associated_actors': {
            'scope': "inclusive",
            'threat_actors': [
                {
                    'confidence': {'value': "Low"},
                    'threat_actor': {'title': "Related Bad Guy!", 'version': "1.1"},
                }
            ],
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
        'confidence': {"value": "High"},
        'information_source': {
            'description': "Mr. Evil's enemy",
            'identity': {
                'name': "Ms. Good",
            },
        },
    }


if __name__ == "__main__":
    unittest.main()
