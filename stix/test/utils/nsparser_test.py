# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import unittest

# internal
import stix
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
    def test_namespace_collect(self):
        nsinfo = nsparser.NamespaceInfo()

        # Collect classes
        nsinfo.collect(C())

        # Parse collected classes
        nsinfo._parse_collected_classes()

        self.assertEqual(len(nsinfo._collected_namespaces), 4)  # noqa


    def test_namespace_dict(self):
        nsinfo = nsparser.NamespaceInfo()

        # Collect classes
        nsinfo.collect(C())

        # finalize the namespace dictionary
        nsinfo.finalize(ns_dict=NSMAP, schemaloc_dict=SCHEMALOCS)
        namespaces = nsinfo.finalized_namespaces.values()

        self.assertTrue(all(ns in namespaces for ns in NSMAP.iterkeys()))
