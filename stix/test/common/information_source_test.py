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
        'roles': [
            {
                'value': 'Initial Author',
                'xsi:type': 'stixVocabs:InformationSourceRoleVocab-1.0'
            },
            {
                'value': 'Transformer/Translator',
                'xsi:type': 'stixVocabs:InformationSourceRoleVocab-1.0'
            }
        ],
        'contributing_sources': {
            'sources': [
                {
                    'identity': {
                        'name': "Batman",
                    },
                    'description': 'Source #1'
                },
                {
                    'identity': {
                        'name': "Superman",
                    },
                    'description': 'Source #2'
               }
            ]
        },
        'references' : ['http://example.com'],
        'time': {
            'start_time': "2010-11-12T01:02:03",
            'end_time': "2013-12-11T03:02:01",
            'produced_time': "2013-12-11T03:02:01",
            'received_time': "2013-12-11T03:02:01",
        },
        'tools': [
            {
                'name': "Web",
                'description': "Superwebs",
            },
            {
                'name': "Tubes",
                'description': "Supertubes",
            },
        ],
        'references': [
            'http://example.com',
            'http://example.com'
        ]
    }


if __name__ == "__main__":
    unittest.main()
