# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase

from stix.common import InformationSource


class InformationSourceTests(EntityTestCase, unittest.TestCase):
    klass = InformationSource
    _full_dict = {
        'description': "An amazing source",
        'identity': {
            'name': "Spiderman",
        },
        'references' : ['http://example.com'],
        'time': {
            'start_time': "2010-11-12T01:02:03",
            'end_time': "2013-12-11T03:02:01",
        },
        'tools': [
            {
                'name': "Web",
                'description': "Superwebs",
            },
        ],
        'roles': [
            {
                'value': 'Initial Author',
                'xsi:type': 'stixVocabs:InformationSourceRoleVocab-1.0'
            },
            {
                'value': 'Transformer/Translator',
                'xsi:type': 'stixVocabs:InformationSourceRoleVocab-1.0'
            }
        ]
    }


if __name__ == "__main__":
    unittest.main()
