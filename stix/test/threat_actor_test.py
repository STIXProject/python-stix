import unittest

from cybox.test import EntityTestCase

from stix.threat_actor import ThreatActor


class ThreatActorTests(EntityTestCase, unittest.TestCase):
    klass = ThreatActor
    _full_dict = {
        'id': 'example:ThreatActor-1',
        'timestamp': "2014-01-31T06:14:46",
        'version': '1.1',
        'title': "BadGuy1",
        'description': "This is a long description about a threat actor.",
        'short_description': "A bad guy",
        'identity': {
            'name': "Mr. Evil",
        },
        'types': [
            {'value': {"value" : "Hacker", 
                       "xsi:type" : "stixVocabs:ThreatActorTypeVocab-1.0"}},
        ],
        'motivations': [
            {'value': {"value" : "Ego", 
                       "xsi:type" : "stixVocabs:MotivationVocab-1.1"}},
            {'value': {"value" : "Opportunistic", 
                       "xsi:type" : "stixVocabs:MotivationVocab-1.1"}},
        ],
        'sophistications': [
            {'value': {"value" : "Novice", 
                       "xsi:type" : "stixVocabs:ThreatActorSophisticationVocab-1.0"}},
        ],
        'intended_effects': [
            {'value': {"value" : "Destruction", 
                       "xsi:type" : "stixVocabs:IntendedEffectVocab-1.0"}},
            {'value': {"value" : "Disruption", 
                       "xsi:type" : "stixVocabs:IntendedEffectVocab-1.0"}},
        ],
        'planning_and_operational_supports': [
            {'value': {"value" : "Data Exploitation", 
                       "xsi:type" : 'stixVocabs:PlanningAndOperationalSupportVocab-1.0.1'}},
        ],
        'observed_ttps': {
            'scope': "exclusive",
            'ttps': [
                {
                    'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
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
                    'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                    'threat_actor': {'title': "Related Bad Guy!", 'version': "1.1"},
                }
            ],
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
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Mr. Evil's enemy",
            'identity': {
                'name': "Ms. Good",
            },
        },
        'related_packages': {
            'packages': [
                {'idref': "example:Package-1234", 'relationship': "Parent"},
                {'idref': "example:Package-1235", 'relationship': "Child"}
            ]
        }
    }


if __name__ == "__main__":
    unittest.main()
