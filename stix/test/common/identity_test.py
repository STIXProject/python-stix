import unittest

from stix.test import EntityTestCase

from stix.common import Identity


class IdentityTests(EntityTestCase, unittest.TestCase):
    klass = Identity
    _full_dict = {
        'id': "foo",       
        'name': "Me",
        'related_identities': {
            #'scope': 'inclusive',
            'identities': [
                {
                    'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                    'identity': {'id': "foo2"}
                }
            ]
        }
    }


if __name__ == "__main__":
    unittest.main()
