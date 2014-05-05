# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.campaign import Campaign
from cybox.test import EntityTestCase


class CampaignTest(EntityTestCase, unittest.TestCase):
    klass = Campaign
    _full_dict = {
        'id': "example:Campaign-341",
        'timestamp': "2014-01-31T06:14:46",
        'version': '1.1',
        'title': 'Purple Elephant',
        'description': 'A pretty novice set of actors.',
        'short_description': 'novices',
        'names': {
            'names': ["Dancing Hippos", "Crazy Squirrels"],
        },
        'intended_effects': [
            {
                'timestamp': "2014-03-11T06:24:26",
                'value': "Doing bad stuff",
            },
            {
                'timestamp': "2014-03-21T06:24:26",
                'value': "Doing really bad stuff",
            }
        ],
        'status': "Ongoing",
        'related_ttps': {
            'scope': "exclusive",
            'ttps': [
                {
                    'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                    'ttp': {'title': "Stealth", 'version': "1.1"},
                }
            ]
        },
        'related_incidents': {
            'scope': "inclusive",
            'incidents': [
                {
                    'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                    'incident': {'idref': "example:Incident-2",
                                 'version': "1.1"},
                }
            ]
        },
        'related_indicators': {
            'scope': "inclusive",
            'indicators': [
                {
                    'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                    'indicator': {'idref': "example:Indicator-77",
                                  'version': "2.1"},
                }
            ]
        },
        'attribution': [{
            'scope': "inclusive",
            'threat_actors': [
                {
                    'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                    'threat_actor': {'title': "Campaign Actor #1",
                                     'version': "1.1"},
                },
                {
                    'threat_actor': {'idref': "example:ThreatActor-111",
                                     'version': "1.1"},
                },
            ],
        }],
        'associated_campaigns': {
            'scope': "inclusive",
            'campaigns': [
                {
                    'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                    'information_source': {'description': "Threat Feed"},
                    'campaign': {'title': "Baby Elephant", 'version': "1.1"},
                }
            ],
        },
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'activity': [
                {
                    'date_time': "2012-01-01T08:45:31",
                    'description': "The first bad thing"
                },
                {
                    'date_time': "2012-01-02T08:45:31",
                    'description': "Another bad thing"
                },
        ],
        'information_source': {
            'description': "A former member of the campaign.",
            'identity': {
                'name': "Mr. D. Fector",
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
        ],
        'related_packages': {
            'packages': [
                {'idref': "example:Package-AB", 'relationship': "Parent"},
                {'idref': "example:Package-CD", 'relationship': "Child"}
            ]
        }
    }


if __name__ == "__main__":
    unittest.main()
