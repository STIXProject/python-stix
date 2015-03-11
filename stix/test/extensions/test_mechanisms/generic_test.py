# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
from stix.extensions.test_mechanism.generic_test_mechanism import GenericTestMechanism
from stix.test import EntityTestCase


class GenericTestMechanismTests(EntityTestCase, unittest.TestCase):
    klass = GenericTestMechanism
    _full_dict = {
        'id': 'example:testmechanism-a1475567-50f7-4dae-b0d0-47c7ea8e79e1',
        'efficacy': {
            'timestamp': '2014-06-20T15:16:56.987966+00:00',
            'value': {
                'value': 'Low',
                'xsi:type': 'stixVocabs:HighMediumLowVocab-1.0'
            }
        },
        'producer': {
            'identity': {
              'id': 'example:Identity-a0740d84-9fcd-44af-9033-94e76a53201e',
              'name': 'FOX IT'
            },
            'references': [
              'http://blog.fox-it.com/2014/04/08/openssl-heartbleed-bug-live-blog/'
            ]
        },
        'description': {
            'value': 'Foo',
            'structuring_format': 'Bar'
        },
        'type': "Test",
        'specification': {
            'value': "Test",
            'encoded': False
        },
        'xsi:type': 'genericTM:GenericTestMechanismType'
    }

if __name__ == "__main__":
    unittest.main()

