# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
from stix.extensions.test_mechanism.snort_test_mechanism import SnortTestMechanism
from stix.test import EntityTestCase


class SnortTestMechanismTests(EntityTestCase, unittest.TestCase):
    klass = SnortTestMechanism
    _full_dict = {
        'efficacy': {
            'timestamp': '2014-06-20T15:16:56.987966+00:00',
            'value': {
                'value': 'Low',
                'xsi:type': 'stixVocabs:HighMediumLowVocab-1.0'
            }
        },
        'id': 'example:testmechanism-a1475567-50f7-4dae-b0d0-47c7ea8e79e1',
              'producer': {
                  'identity': {
                      'id': 'example:Identity-a0740d84-9fcd-44af-9033-94e76a53201e',
                      'name': 'FOX IT'
                  },
                  'references': [
                      'http://blog.fox-it.com/2014/04/08/openssl-heartbleed-bug-live-blog/'
                  ]
              },
        'rules': [
            {
                'value': 'alert tcp any any -> any any (msg:"FOX-SRT - Flowbit - TLS-SSL Client Hello"; flow:established; dsize:< 500; content:"|16 03|"; depth:2; byte_test:1, <=, 2, 3; byte_test:1, !=, 2, 1; content:"|01|"; offset:5; depth:1; content:"|03|"; offset:9; byte_test:1, <=, 3, 10; byte_test:1, !=, 2, 9; content:"|00 0f 00|"; flowbits:set,foxsslsession; flowbits:noalert; threshold:type limit, track by_src, count 1, seconds 60; reference:cve,2014-0160; classtype:bad-unknown; sid: 21001130; rev:9;)',
                'encoded': False
            },
            {
                'value': 'alert tcp any any -> any any (msg:"FOX-SRT - Suspicious - TLS-SSL Large Heartbeat Response"; flow:established; flowbits:isset,foxsslsession; content:"|18 03|"; depth: 2; byte_test:1, <=, 3, 2; byte_test:1, !=, 2, 1; byte_test:2, >, 200, 3; threshold:type limit, track by_src, count 1, seconds 600; reference:cve,2014-0160; classtype:bad-unknown; sid: 21001131; rev:5;)',
                'encoded': False
            }
        ],
        'event_filters': [
            {
                'value': "Foo",
                'encoded': False
            },
            {
                'value': 'Bar>',
                'encoded': False
            }
        ],
        'rate_filters': [
             {
                'value': "Foo",
                'encoded': False
            },
            {
                'value': 'Bar>',
                'encoded': False
            }
        ],
        'event_suppressions': [
             {
                'value': "Foo",
                'encoded': False
            },
            {
                'value': 'Bar>',
                'encoded': False
            }
        ],
        'xsi:type': 'snortTM:SnortTestMechanismType'
    }

if __name__ == "__main__":
    unittest.main()

