import unittest

from cybox.test import EntityTestCase

from stix.common import InformationSource


class InformationSourceTests(EntityTestCase, unittest.TestCase):
    klass = InformationSource
    _full_dict = {
        'identity': {
            'name': "Spiderman",
        },
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
    }


if __name__ == "__main__":
    unittest.main()
