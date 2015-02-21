# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase

from stix.common.related import RelatedPackageRef


class StatementTests(EntityTestCase, unittest.TestCase):
    klass = RelatedPackageRef
    _full_dict = {
        'idref': "example:Campaign-133",
        'timestamp': "2014-01-31T06:14:46",
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Source of the relationship",
        },
        'relationship': "Associated",
    }


if __name__ == "__main__":
    unittest.main()
