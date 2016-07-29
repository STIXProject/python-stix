# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox.vendor.six import StringIO
import unittest

from stix.utils import (EntityParser, UnknownVersionError,
                        UnsupportedRootElementError, UnsupportedVersionError)


class ParserTests(unittest.TestCase):

    def test_valid(self):
        valid = """
        <stix:STIX_Package xmlns:stix="http://stix.mitre.org/stix-1"
            version="1.2" id="example:Package-1">
        </stix:STIX_Package>
        """

        parser = EntityParser()
        package = parser.parse_xml(StringIO(valid))

        self.assertEqual("example:Package-1", package.id_)

    def test_wrong_root_element(self):
        wrong_root = """
        <stix:NotAPackage xmlns:stix="http://stix.mitre.org/stix-1"
            version="1.2" id="example:Package-1">
        </stix:NotAPackage>
        """

        parser = EntityParser()
        self.assertRaises(UnsupportedRootElementError,
                          parser.parse_xml, StringIO(wrong_root))

        package = parser.parse_xml(StringIO(wrong_root),
                                   check_root=False)

        self.assertEqual("example:Package-1", package.id_)
        self.assertEqual("1.2", package.version)

    def test_wrong_version(self):
        wrong_version = """
        <stix:STIX_Package xmlns:stix="http://stix.mitre.org/stix-1"
            version="17.8.9" id="example:Package-1">
        </stix:STIX_Package>
        """

        parser = EntityParser()
        self.assertRaises(UnsupportedVersionError,
                          parser.parse_xml, StringIO(wrong_version))

        package = parser.parse_xml(StringIO(wrong_version),
                                   check_version=False)

        self.assertEqual("example:Package-1", package.id_)
        self.assertEqual("17.8.9", package.version)

    def test_missing_version(self):
        missing_version = """
        <stix:STIX_Package xmlns:stix="http://stix.mitre.org/stix-1"
            id="example:Package-1">
        </stix:STIX_Package>
        """

        parser = EntityParser()
        self.assertRaises(UnknownVersionError,
                          parser.parse_xml, StringIO(missing_version))

        package = parser.parse_xml(StringIO(missing_version),
                                   check_version=False)

        self.assertEqual("example:Package-1", package.id_)


if __name__ == "__main__":
    unittest.main()
