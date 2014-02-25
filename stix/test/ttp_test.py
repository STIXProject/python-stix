import unittest
from cybox.test import EntityTestCase
from stix.ttp import TTP

class TTPTests(EntityTestCase, unittest.TestCase):
    klass = TTP
    _full_dict = {
        'id': 'example:ttp-1',
        'version': '1.1',
        'title': "TTP1",
        'description': "This is a long description about a ttp",
        'short_description': "a TTP",
    }

if __name__ == "__main__":
    unittest.main()
