# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import StringIO
import unittest
import warnings

# external
import lxml.etree

# internal
import stix
from stix.core import STIXPackage
from stix.utils import nsparser


NSMAP = {
    "test:a": "a",
    "test:b": "b",
    "test:c": "c"
}


SCHEMALOCS = {
    "test:a": "/dev/null",
    "test:b": "/dev/null",
    "test:c": "/dev/null"
}


class A(stix.Entity):
    _namespace = "test:a"
    _XSI_TYPE = "a:AType"


class B(A):
    _namespace = "test:b"
    _XSI_TYPE = "b:BType"


class C(B):
    _namespace = "test:c"
    _XSI_TYPE = "c:CType"


class NamespaceInfoTests(unittest.TestCase):
    def test_nsinfo_collect(self):
        """Tests that the NamespaceInfo.collect() method correctly ascends the MRO
        of input objects.

        """
        nsinfo = nsparser.NamespaceInfo()

        # Collect classes
        nsinfo.collect(C())

        # Parse collected classes
        nsinfo._parse_collected_classes()

        self.assertEqual(len(nsinfo._collected_namespaces), 4)  # noqa

    def test_namespace_collect(self):
        """Test that NamespaceInfo correctly pulls namespaces from all classes
        in an objects MRO.

        """
        nsinfo = nsparser.NamespaceInfo()

        # Collect classes
        nsinfo.collect(C())

        # finalize the namespace dictionary
        nsinfo.finalize(ns_dict=NSMAP, schemaloc_dict=SCHEMALOCS)
        namespaces = nsinfo.finalized_namespaces.values()

        self.assertTrue(all(ns in namespaces for ns in NSMAP.iterkeys()))

    def test_user_provided_ns(self):
        """Test that user-provided namespaces are serialized.

        """
        p = STIXPackage()
        nsinfo = nsparser.NamespaceInfo()

        # Collect classes
        nsinfo.collect(p)

        TEST_PREFIX = 'test'
        TEST_NS = 'a:unit:test'
        NEW_STIX_PREFIX = 'newstix'
        NEW_STIX_NS = "http://stix.mitre.org/stix-1"

        test_dict = {
            TEST_NS: TEST_PREFIX,
            NEW_STIX_NS: NEW_STIX_PREFIX
        }

        finalized = nsinfo._finalize_namespaces(ns_dict=test_dict)
        nsinfo.finalized_namespaces

        self.assertEqual(finalized.get(TEST_PREFIX), TEST_NS)
        self.assertEqual(finalized.get(NEW_STIX_PREFIX), NEW_STIX_NS)

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            xml = p.to_xml(ns_dict=test_dict)

        # Parse the exported document and make sure that the namespaces
        # made it through the serialization process.
        e = lxml.etree.XML(xml)
        self.assertEqual(e.nsmap.get(TEST_PREFIX), TEST_NS)
        self.assertEqual(e.nsmap.get(NEW_STIX_PREFIX), NEW_STIX_NS)

    def test_duplicate_ns_prefix(self):
        """Test that duplicate namespace prefix mappings raise errors.

        """
        p = STIXPackage()
        bad = {'bad:ns': 'stix'}  # 'stix' is already default ns prefix

        self.assertRaises(
            nsparser.DuplicatePrefixError,
            p.to_xml,
            ns_dict=bad
        )

        # Build a valid stix document that has a default namespace remapped
        # to another namespace. We remap 'cybox' to a bogus ns here.
        xml = (
            """<stix:STIX_Package
                    xmlns:cybox="THISISGONNABEPROBLEM"
                    xmlns:stix="http://stix.mitre.org/stix-1"
                    version="1.1.1"
                    timestamp="2015-04-09T14:22:25.620831+00:00"/>"""
        )

        sio = StringIO.StringIO(xml)
        p = STIXPackage.from_xml(sio)

        # Exporting should raise an error.
        self.assertRaises(
            nsparser.DuplicatePrefixError,
            p.to_xml
        )

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
                    version="1.1.1"
                    timestamp="2015-04-09T14:22:25.620831+00:00"/>"""
        )

        sio = StringIO.StringIO(xml)
        p = STIXPackage.from_xml(sio)

        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            serialized = p.to_xml()

        e = lxml.etree.XML(serialized)
        self.assertEqual(e.nsmap.get('TEST'), 'a:test')
        self.assertEqual(e.nsmap.get('FOO'), 'a:foo')
        self.assertEqual(e.nsmap.get('BAR'), 'a:bar')


if __name__ == "__main__":
    unittest.main()