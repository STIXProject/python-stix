# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.campaign import Campaign
from cybox.test import EntityTestCase


class CampaignTest(EntityTestCase, unittest.TestCase):
    klass = Campaign
    _full_dict = {
        'id': "example:Campaign-341",
        'idref': 'example:Campaign-344',
        'timestamp': "2014-01-31T06:14:46",
        'version': '1.1',
        'title': 'Purple Elephant',
        'description': 'A pretty novice set of actors.',
        'short_description': 'novices',
        'related_ttps': {
            'scope': "exclusive",
            'ttps': [
                {
                    'confidence': {'value': "High"},
                    'ttp': {'title': "Stealth", 'version': "1.1"},
                }
            ]
        },
        'related_incidents': {
            'scope': "inclusive",
            'incidents': [
                {
                    'confidence': {'value': "Low"},
                    'incident': {'idref': "example:Incident-2",
                                 'version': "1.1"},
                }
            ]
        },
        'related_indicators': {
            'scope': "inclusive",
            'indicators': [
                {
                    'confidence': {'value': "Low"},
                    'indicator': {'idref': "example:Indicator-77",
                                  'version': "2.1"},
                }
            ]
        },
        'associated_campaigns': {
            'scope': "inclusive",
            'campaigns': [
                {
                    'confidence': {'value': "High"},
                    'information_source': {'description': "Threat Feed"},
                    'campaign': {'title': "Baby Elephant", 'version': "1.1"},
                }
            ],
        },
        'confidence': {"value": "Low"},
        'information_source': {
            'description': "A former member of the campaign.",
            'identity': {
                'name': "Mr. D. Fector",
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
