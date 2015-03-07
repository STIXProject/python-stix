# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import json
import itertools

import cybox.utils

import stix.bindings as bindings
from stix.utils import NamespaceInfo


def round_trip_dict(cls, dict_):
    obj = cls.object_from_dict(dict_)
    dict2 = cls.dict_from_object(obj)

    return dict2

def round_trip(o, output=False, list_=False):
    """ Performs all eight conversions to verify import/export functionality.

    1. cybox.Entity -> dict/list
    2. dict/list -> JSON string
    3. JSON string -> dict/list
    4. dict/list -> cybox.Entity
    5. cybox.Entity -> Bindings Object
    6. Bindings Object -> XML String
    7. XML String -> Bindings Object
    8. Bindings object -> cybox.Entity

    It returns the final object, so tests which call this function can check to
    ensure it was not modified during any of the transforms.
    """

    klass = o.__class__
    if output:
        print "Class: ", klass
        print "-" * 40

    # 1. cybox.Entity -> dict/list
    if list_:
        d = o.to_list()
    else:
        d = o.to_dict()

    # 2. dict/list -> JSON string
    json_string = json.dumps(d)

    if output:
        print(json_string)
        print "-" * 40

    # Before parsing the JSON, make sure the cache is clear
    cybox.utils.cache_clear()

    # 3. JSON string -> dict/list
    d2 = json.loads(json_string)

    # 4. dict/list -> cybox.Entity
    if list_:
        o2 = klass.from_list(d2)
    else:
        o2 = klass.from_dict(d2)

    # 5. Entity -> Bindings Object
    ns_info = NamespaceInfo()
    xobj = o2.to_obj(ns_info=ns_info)

    try:
        # 6. Bindings Object -> XML String
        xml_string = o2.to_xml(encoding=bindings.ExternalEncoding)

        if not isinstance(xml_string, unicode):
            xml_string = xml_string.decode(bindings.ExternalEncoding)

    except KeyError as ex:
        print str(ex)
        ns_info.finalize()
        print ns_info.finalized_namespaces
        raise ex

    if output:
        print(xml_string)
        print "-" * 40

    # Before parsing the XML, make sure the cache is clear
    cybox.utils.cache_clear()

    #7. XML String -> Bindings Object
    xobj2 = klass._binding.parseString(xml_string)

    # 8. Bindings object -> cybox.Entity
    o3 = klass.from_obj(xobj2)

    return o3

class EntityTestCase(object):
    """A base class for testing STIX Entities"""

    def setUp(self):
        self.assertNotEqual(self.klass, None)
        self.assertNotEqual(self._full_dict, None)

    def test_round_trip_full_dict(self):
        # Don't run this test on the base class
        if type(self) == type(EntityTestCase):
            return

        dict2 = round_trip_dict(self.klass, self._full_dict)
        self.maxDiff = None
        self.assertEqual(self._full_dict, dict2)

    def _combine(self, d):
        items = itertools.chain(
            self._full_dict.iteritems(),
            d.iteritems()
        )

        return dict(items)

    def test_round_trip_full(self):
        # Don't run this test on the base class
        if type(self) == type(EntityTestCase):
            return

        ent = self.klass.from_dict(self._full_dict)
        ent2 = round_trip(ent, output=True)

        #TODO: eventually we want to test the objects are the same, but for
        # now, just make sure there aren't any errors.

    def _test_round_trip_dict(self, input):
        dict2 = round_trip_dict(self.klass, input)

        self.maxDiff = None
        self.assertEqual(input, dict2)

    def _test_partial_dict(self, partial):
        d = self._combine(partial)
        self._test_round_trip_dict(d)


class TypedListTestCase(object):
    def test_round_trip_rt(self):
        if type(self) == type(TypedListTestCase):
            return

        obj = self.klass.from_dict(self._full_dict)
        dict2 = obj.to_dict()
        self.assertEqual(self._full_dict, dict2)