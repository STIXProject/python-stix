import unittest

from cybox.test import EntityTestCase

from stix.common import Identity


class IdentityTests(EntityTestCase, unittest.TestCase):
    klass = Identity
    _full_dict = {
        'id': "foo",
        'idref': "foo_ref",
        'name': "Me",
        'related_identities': {
            #'scope': 'inclusive',
            'identities': [
                {
                    'confidence': {'value': "Medium"},
                    'identity': {'id': "foo2"}
                }
            ]
        }
    }


if __name__ == "__main__":
    unittest.main()
