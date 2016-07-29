# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import unittest

# external
import lxml.etree
from mixbox.vendor.six import StringIO

# internal
import mixbox.namespaces
from stix.core import STIXPackage
from stix.utils import silence_warnings


class NamespaceInfoTests(unittest.TestCase):

    @silence_warnings
    def test_user_provided_ns(self):
        """Test that user-provided namespaces are serialized.

        """
        p = STIXPackage()

        TEST_PREFIX = 'test'
        TEST_NS = 'a:unit:test'
        NEW_STIX_PREFIX = 'newstix'
        NEW_STIX_NS = "http://stix.mitre.org/stix-1"

        test_dict = {
            TEST_NS: TEST_PREFIX,
            NEW_STIX_NS: NEW_STIX_PREFIX
        }

        # Parse the exported document and make sure that the namespaces
        # made it through the serialization process.
        xml = p.to_xml(ns_dict=test_dict)
        e = lxml.etree.XML(xml)
        self.assertEqual(e.nsmap.get(TEST_PREFIX), TEST_NS)
        self.assertEqual(e.nsmap.get(NEW_STIX_PREFIX), NEW_STIX_NS)

    @silence_warnings
    def test_duplicate_ns_prefix(self):
        """Test that duplicate namespace prefix mappings raise errors.

        """
        p = STIXPackage()
        bad = {'bad:ns': 'stix'}  # 'stix' is already default ns prefix

        self.assertRaises(
            mixbox.namespaces.DuplicatePrefixError,
            p.to_xml,
            ns_dict=bad
        )

        # Build a valid stix document that has a default namespace remapped
        # to another namespace. We remap 'stixCommon' to a bogus ns here.
        xml = (
            """<stix:STIX_Package
                    xmlns:stixCommon="THISISGONNABEPROBLEM"
                    xmlns:stix="http://stix.mitre.org/stix-1"
                    xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
                    version="1.2"
                    timestamp="2015-04-09T14:22:25.620831+00:00">
                <stix:STIX_Header>
                    <stix:Description>A unit test</stix:Description>
                </stix:STIX_Header>
            </stix:STIX_Package>"""
        )

        sio = StringIO(xml)
        p = STIXPackage.from_xml(sio)

        # Exporting should raise an error.
        self.assertRaises(
            mixbox.namespaces.DuplicatePrefixError,
            p.to_xml
        )


    @silence_warnings
    def test_parsed_namespaces(self):
        """Test that non-default namespaces make it through the parse-serialize
        process.

        """
        xml = (
            """<stix:STIX_Package
                    xmlns:TEST="a:test"
                    xmlns:FOO="a:foo"
                    xmlns:BAR="a:bar"
                    xmlns:cybox="http://cybox.mitre.org/cybox-2"
                    xmlns:cyboxCommon="http://cybox.mitre.org/common-2"
                    xmlns:cyboxVocabs="http://cybox.mitre.org/default_vocabularies-2"
                    xmlns:example="http://example.com"
                    xmlns:stix="http://stix.mitre.org/stix-1"
                    xmlns:stixCommon="http://stix.mitre.org/common-1"
                    xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
                    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                    id="example:Package-e2454ee8-e59c-43ac-a085-46ae4516fd6e"
                    version="1.2"
                    timestamp="2015-04-09T14:22:25.620831+00:00"/>"""
        )

        sio = StringIO(xml)
        p = STIXPackage.from_xml(sio)

        serialized = p.to_xml()
        e = lxml.etree.XML(serialized)
        self.assertEqual(e.nsmap.get('TEST'), 'a:test')
        self.assertEqual(e.nsmap.get('FOO'), 'a:foo')
        self.assertEqual(e.nsmap.get('BAR'), 'a:bar')


if __name__ == "__main__":
    unittest.main()