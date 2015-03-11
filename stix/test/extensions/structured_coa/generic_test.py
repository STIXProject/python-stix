# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
from stix.extensions.structured_coa.generic_structured_coa import GenericStructuredCOA
from stix.test import EntityTestCase

class GenericStructuredCOATests(EntityTestCase, unittest.TestCase):
    klass = GenericStructuredCOA
    _full_dict = {
        'id': 'example:test-1',
        'description': {
            'value': 'Foo',
            'structuring_format': 'Bar'
        },
        'type': "Test",
        'specification': {
            'value': "Test",
            'encoded': False
        },
        'xsi:type': 'genericStructuredCOA:GenericStructuredCOAType'
    }

if __name__ == "__main__":
    unittest.main()

