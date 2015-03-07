__author__ = 'bworrell'

import unittest
from stix.test import EntityTestCase
from stix import common


class ToolInformationTests(EntityTestCase, unittest.TestCase):
    klass = common.ToolInformation

    _full_dict = {
        'id': 'example:test-1',   # from python-cybox
        'name': 'Test Tool Name',  # from python-cybox
        'title': 'Test Title',
        'short_description': 'Test Short Description'
    }


if __name__ == "__main__":
    unittest.main()
