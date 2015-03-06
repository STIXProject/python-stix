# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase
from stix.common import CampaignRef


class CampaignRefTests(EntityTestCase, unittest.TestCase):
    klass = CampaignRef
    _full_dict = {
        'idref': "example:foo-1",
        'timestamp': "2014-01-31T06:14:46",
        'names': ["foo", "bar"]
    }


if __name__ == '__main__':
    unittest.main()


