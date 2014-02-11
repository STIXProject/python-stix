import unittest

from cybox.test import EntityTestCase

from stix.common import Identity


class IdentityTests(EntityTestCase, unittest.TestCase):
    klass = Identity
    _full_dict = {
        'id': "foo",
        'idref': "foo_ref",
        'name': "Me",
    }


if __name__ == "__main__":
    unittest.main()
