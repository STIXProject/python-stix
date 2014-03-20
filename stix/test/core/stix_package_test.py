import unittest

from cybox.test import EntityTestCase

from stix.core import STIXPackage


class STIXPackageTests(EntityTestCase, unittest.TestCase):
    klass = STIXPackage
    _full_dict = {
        'stix_header': {
            'title': "A Title",
            'description': "A really, really long description",
        },
        'ttps': {
            'ttps': [
                {
                    'title': "Foo",
                    'version': "1.1"
                },
            ]
        },
        'version': "1.1"
    }


if __name__ == "__main__":
    unittest.main()
