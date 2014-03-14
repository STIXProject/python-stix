# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.campaign import Campaign
from cybox.test import EntityTestCase


class CampaignTest(EntityTestCase, unittest.TestCase):
    klass = Campaign
    _full_dict = {
        'id': "example:Campaign-341",
        'title': 'Purple Elephant',
        'description': 'A pretty novice set of actors.',
        'short_description': 'novices',
        'version': '1.1',
    }


if __name__ == "__main__":
    unittest.main()
