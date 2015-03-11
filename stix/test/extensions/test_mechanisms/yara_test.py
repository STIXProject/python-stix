# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
from stix.test import EntityTestCase
from stix.extensions.test_mechanism.yara_test_mechanism import YaraTestMechanism

class YaraTestMechanismTests(EntityTestCase, unittest.TestCase):
    klass = YaraTestMechanism
    _full_dict = {
        'id': 'example:testmechanism-a1475567-50f7-4dae-b0d0-47c7ea8e79e1',
        'efficacy': {
            'timestamp': '2014-06-20T15:16:56.987966+00:00',
            'value': {
                'value': 'Low',
                'xsi:type': 'stixVocabs:HighMediumLowVocab-1.0'
            }
        },
        'version': 'Test Version',
        'producer': {
            'identity': {
                  'id': 'example:Identity-a0740d84-9fcd-44af-9033-94e76a53201e',
                  'name': 'test'
            },
            'references': [
                'http://example.com/'
            ]
        },
        'rule': {
            'value': 'Test',
            'encoded': False
        },
        'xsi:type': 'yaraTM:YaraTestMechanismType'
    }


if __name__ == "__main__":
    unittest.main()

