# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
import random

from stix.test import EntityTestCase, TypedListTestCase

from stix import common

from mixbox.vendor.six.moves import range


class StructuredTextTests(unittest.TestCase, EntityTestCase):
    klass = common.StructuredText
    _full_dict = {
        'ordinality': 1,
        'value': 'TEST',
        'id': 'example:test-1',
        'structuring_format': 'text/plain'
    }


class StructuredTextListTests(unittest.TestCase, TypedListTestCase):
    klass = common.StructuredTextList

    _full_dict = [
        StructuredTextTests._full_dict,
        {
            'ordinality': 2,
            'value': 'TEST 2',
            'id': 'example:test-2',
            'structuring_format': 'text/plain'
        }
    ]

    @classmethod
    def _get_text_list(cls):
        slist = []

        for ordinality in range(1, 10):
            text = common.StructuredText("Ordinality %s" % ordinality)
            text.ordinality = ordinality
            slist.append(text)

        random.shuffle(slist)
        return slist

    @classmethod
    def setUpClass(cls):
        slist = cls._get_text_list()
        cls.slist = common.StructuredTextList(slist)

    def test_iter(self):
        for idx, text in enumerate(self.slist, 1):
            self.assertEqual(text.ordinality, idx)

    def test_reset(self):
        ords = (5,33,167)
        slist = common.StructuredTextList()

        for o in ords:
            text =  common.StructuredText("orig: %s" % o, o)
            slist.add(text)

        # test that original assignment worked correctly
        for o in ords:
            self.assertEqual(o, slist[o].ordinality)

        # reset ordinalities
        slist.reset()

        for o in range(1, len(ords) + 1):
            self.assertEqual(o, slist[o].ordinality)

    def test_ordinalities(self):
        all_ords = range(1,10)
        self.assertTrue(all(x in self.slist.ordinalities for x in all_ords))

    def test_add(self):
        slist = common.StructuredTextList()
        st1 = common.StructuredText("foo", ordinality=1)
        st2 = common.StructuredText("bar", ordinality=2)

        slist.add(st1)
        slist.add(st2)

        self.assertTrue(st1 in slist)
        self.assertTrue(st2 in slist)

    def test_insert(self):
        st1 = common.StructuredText("foo", ordinality=1)
        st2 = common.StructuredText("bar", ordinality=2)
        slist = common.StructuredTextList(st1, st2)

        new_st1 = common.StructuredText("foobar", ordinality=1)
        slist.insert(new_st1)

        # test that the ordinality shift worked
        self.assertEqual(new_st1.ordinality, 1)
        self.assertEqual(st1.ordinality, 2)
        self.assertEqual(st2.ordinality, 3)

    def test_insert_str(self):
        slist = common.StructuredTextList("foo", "bar")
        slist.insert("test")
        self.assertEqual(str(slist[3]), "test")

    def test_delitem(self):
        slist = common.StructuredTextList()
        st1 = common.StructuredText("foo", ordinality=1)
        st2 = common.StructuredText("bar", ordinality=2)

        slist.add(st1)
        slist.add(st2)

        del slist[1]

        self.assertTrue(st1 not in slist)
        self.assertTrue(st2 in slist)
        self.assertRaises(
            KeyError,
            slist.__getitem__,
            1
        )

    def test_remove(self):
        slist = common.StructuredTextList()
        st1 = common.StructuredText("foo", ordinality=1)
        st2 = common.StructuredText("bar", ordinality=2)

        slist.add(st1)
        slist.add(st2)
        slist.remove(st1)

        self.assertTrue(st1 not in slist)
        self.assertTrue(st2 in slist)
        self.assertRaises(
            KeyError,
            slist.__getitem__,
            1
        )

    def test_update(self):
        slist = common.StructuredTextList()
        st1 = common.StructuredText("foo", ordinality=1)
        st2 = common.StructuredText("bar", ordinality=2)

        slist.add(st1)
        slist.add(st2)

        new_st1 = common.StructuredText("FOO", ordinality=1)
        new_st2 = common.StructuredText("BAR", ordinality=2)

        newlist = [new_st1, new_st2]
        slist.update(newlist)

        self.assertEqual(slist[1], new_st1)
        self.assertEqual(slist[2], new_st2)
        self.assertTrue(st1 not in slist)
        self.assertTrue(st2 not in slist)

    def test_len(self):
        slist = common.StructuredTextList()
        st1 = common.StructuredText("foo", ordinality=1)
        st2 = common.StructuredText("bar", ordinality=2)

        slist.add(st1)
        slist.add(st2)

        self.assertEqual(len(slist), 2)

        del slist[1]

        self.assertEqual(len(slist), 1)


if __name__ == "__main__":
    unittest.main()
