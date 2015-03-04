# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.indicator import Indicator
from stix.test import EntityTestCase


class IndicatorTest(EntityTestCase, unittest.TestCase):
    klass = Indicator
    _full_dict = {
        'alternative_id': [
            "test 1",
            "not a test 2"
        ],
        'negate': True,
        'valid_time_positions': [
            {
                'start_time': {'value': '2013-08-22T01:23:45', 'precision':'minute'},
                'end_time': {'value': '2013-09-22T01:34:56', 'precision':'minute'}
            },
            {
                'start_time': {'value': '2014-08-22T01:23:45', 'precision':'minute'},
                'end_time': {'value': '2014-09-22T01:34:56', 'precision':'minute'}
            }
        ],
        'description': 'An indicator containing a File observable with an associated hash',
        'id': 'example:indicator-1ae45e9c-9b0b-11e3-ada0-28cfe912ced6',
        'observable': {
            'id': 'example:Observable-fdaa7cec-f8be-494d-b83f-575f6f018666',
            'object': {
                'id': 'example:File-ec52e6bc-2d7e-44e2-911b-468bb775a5c6',
                'properties': {
                    'hashes': [
                    {
                        'simple_hash_value': u'4EC0027BEF4D7E1786A04D021FA8A67F',
                        'type': u'MD5'
                    }
                    ],
                    'xsi:type': 'FileObjectType'
                }
            }
        },
        'producer': {
            'description': 'A sample description',
            'identity': {
                'id': 'example:Identity-1ae603ab-9b0b-11e3-980e-28cfe912ced8',
                'specification': {
                    'party_name': {
                        'name_lines': [
                        {'value': 'Foo'},
                        {'value': 'Bar'}
                        ],
                        'person_names': [
                        {'name_elements': [{'value': 'John Smith'}]},
                        {'name_elements': [{'value': 'Jill Smith'}]}
                        ]
                    }
                },
                'xsi:type': 'ciqIdentity:CIQIdentity3.0InstanceType'
            },
            'time': {'produced_time': '2014-02-21T10:16:14.947201'}
        },
        'related_campaigns': {
            'scope': 'inclusive',
            'related_campaigns': [
                {
                    'campaign': {
                        'idref': 'example:Campaign-2f193992-d1c9-45a4-9db6-edbe9f7109cb',
                        'names': ['foo', 'bar']
                    }
                },
                {
                    'campaign': {
                        'idref': 'example:Campaign-2f193992-d1c9-45a4-9db6-edbe9f7109cb',
                        'names': ['foo', 'bar']
                    }
                }
            ]
        },
        'title': 'File Hash Example',
        'version': '2.1.1'
    }

if __name__ == "__main__":
    unittest.main()
