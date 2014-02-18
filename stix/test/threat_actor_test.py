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
