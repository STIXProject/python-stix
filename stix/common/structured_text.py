# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
import itertools
import contextlib
import collections
from sys import version_info

from mixbox import fields

import stix
import stix.utils as utils
import stix.bindings.stix_common as stix_common_binding
from mixbox.vendor.six import text_type


#: Default ordinality value for StructuredText.
DEFAULT_ORDINALITY = 1


class StructuredText(stix.Entity):
    """Used for storing descriptive text elements.

    Attributes:
        id_: An id for the text element, typically used for controlled
            structure xpath selectors.
        value: The text value of this object.
        structuring_format: The format of the text. For example, ``html5``.
    """

    _binding = stix_common_binding
    _binding_class = _binding.StructuredTextType
    _namespace = 'http://stix.mitre.org/common-1'

    id_ = fields.IdField("id")
    ordinality = fields.TypedField("ordinality")
    value = fields.TypedField("valueOf_", key_name="value")
    structuring_format = fields.TypedField("structuring_format")


    def __init__(self, value=None, ordinality=None):
        super(StructuredText, self).__init__()

        self.id_ = None
        self.value = value
        self.structuring_format = None
        self.ordinality = ordinality

    def is_plain(self):
        plain = (
            (not self.id_) and
            (not self.structuring_format) and
            (self.ordinality is None)
        )

        return plain

    def to_dict(self):
        """Converts this object into a dictionary representation.

        Note:
            If no properies or attributes are set other than ``value``,
            this will return a string.

        """
        # Return a plain string if there is no format specified.
        if self.is_plain():
            return self.value
        else:
            return super(StructuredText, self).to_dict()

    def __str__(self):
        """Returns a UTF-8 encoded string representation of the ``value``.

        """
        if version_info < (3,):
            return self.__unicode__().encode("utf-8")
        else:
            return self.__unicode__()

    def __unicode__(self):
        """Returns a ``unicode`` string representation of the ``value``.

        """
        return text_type(self.value)


@contextlib.contextmanager
def _unset_default(text):
    """Unsets the ordinality of the StructuredText object `text` if the
    ordinality is equal to the DEFAULT_ORDINALITY.

    The ordinaity will be returned to its original state after exiting the
    context manager.

    """
    ordinality = text.ordinality

    try:
        if ordinality == DEFAULT_ORDINALITY:
            text.ordinality = None  # Unset

        yield #  Return to caller
    finally:
        # Reset
        text.ordinality = ordinality


class StructuredTextList(stix.TypedCollection, collections.Sequence):
    """A sequence type used to store StructureText objects.

    Args:
        *args: A variable-length argument list which can contain single
            :class:`.StructuredText` objects or sequences of objects.

    """
    _treat_none_as_empty_list = True
    _contained_type = StructuredText
    _try_cast = True

    def __init__(self, *args):
        stix.TypedCollection.__init__(self, *args)

    def _initialize_inner(self, *args):
        # Check if it was initialized with args=None
        if not any(args):
            return

        for arg in args:
            if utils.is_sequence(arg):
                self.update(arg)
            else:
                self.add(arg)

    def with_id(self, id):
        """Returns a :class:`.StructuredText` object with a matching `id` or
        ``None`` if not found.

        """
        for text in self._inner:
            if text.id_ == id:
                return text

        # Not found. Return None.
        return None

    def reset(self):
        """Assigns sequential ordinality values to each of the sorted
        :class:`.StructuredText` objects, starting with ``1`` and ending
        at ``len(self)``.

        """
        for idx, item in enumerate(self.sorted, 1):
            item.ordinality = idx

    @property
    def sorted(self):
        """Returns a copy of the collection of internal
        :class:`.StructuredText` objects, sorted by their ``ordinality``.

        """
        return sorted(self._inner, key=lambda x: int(x.ordinality))

    @property
    def ordinalities(self):
        """Returns a sorted list of all the ``ordinality`` attribute
        values of the internal :class:`StructuredTex` objects.

        """
        return tuple(x.ordinality for x in self.sorted)

    @property
    def next_ordinality(self):
        """Returns the "+1" of the highest ordinality in the collection.

        """
        ords = self.ordinalities

        if not ords:
            return 1

        return ords[-1] + 1

    def __iter__(self):
        """Returns an iterator for the collection sorted by ordinality.

        """
        return iter(self.sorted)

    def __getitem__(self, key):
        """Returns the :class:`.StructuredText` object with a matching
        ordinality.

        Args:
            key: An ordinality value.

        Raises:
            KeyError: If `key` does not match the ordinality of any
                :class:`.StructuredText` object.

        """
        o = int(key)

        for item in self._inner:
            if item.ordinality == o:
                return item

        error = "No item found with an ordinality of {0}".format(o)
        raise KeyError(error)

    def __delitem__(self, key):
        """Removes the item with a given ordinality.

        Args:
            key: An ordinality value.

        Raises:
            KeyError: If the `key` does not match the ordinality for any object
                in the collection.

        """
        self._inner.remove(self[key])

    def __reversed__(self):
        """Yields the :class:`StructuredText` collection in descending order
        of their ordinalities.

        """
        for text in reversed(self.sorted):
            yield text

    def add(self, value):
        """Adds the :class:`.StructuredText` `value` to the collection.

        If `value` is not a :class:`.StructuredText` object, an attempt will
        be made to convert it to one.

        Note:
            If `value` does not have an ``ordinality`` set, one will be
            assigned. If `value` has an ordinality which matches one already
            in the collection, `value` will replace the existing item.

        Args:
            value: A :class:`.StructuredText` object.

        """
        if not self._is_valid(value):
            value = self._fix_value(value)

        if value.ordinality is None:
            value.ordinality = self.next_ordinality

        # Remove the existing item if there is one.
        with utils.ignored(KeyError):
            del self[value.ordinality]

        self._inner.append(value)

    def update(self, iterable):
        """Adds each item of `iterable` to the collection.

        Note:
            Any existing objects with conflicting ordinality values will be
            overwritten.

        Args:
            iterable: An iterable collection of :class:`.StructuredText` objects
                to add to this collection.

        """
        for item in iterable:
            self.add(item)

    def _shift(self, ordinality):
        """Increments the ordinality values on all objects in the collection
        that have an ordinality greater than or equal to `ordinality`.

        This is used in ``insert()`` operations.

        Note:
            This will only shift contiguous ordinalities, so if the collection
            contains the ordinaliities [1,2,6], then _shift(1) would result in
            [2,3,6] since 6 is not contiguous with [1,2].

        """
        to_shift = []

        for o in itertools.count(ordinality):
            try:
                to_shift.append(self[o])
            except KeyError:
                break

        for text in to_shift:
            text.ordinality += 1

    def insert(self, value):
        """Inserts `value` into the collection.

        If `value` has an ordinality which conflicts with an existing value,
        the existing value (and any contiguous values) will have their
        ordinality values incremented by one.

        """
        if not self._is_valid(value):
            value = self._fix_value(value)

        if value.ordinality is None:
            self.add(value)
        else:
            self._shift(value.ordinality)
            self._inner.append(value)

    def remove(self, value):
        """Removes the value from the collection.

        """
        self._inner.remove(value)

    def to_obj(self, ns_info=None):
        """Returns a binding object list for the StructuredTextList.

        If the list has a length of 1, and its member has an ordinality of 1,
        the ordinality will be unset.

        """
        #print "STList to_obj called"
        
        if not self:
            return []

        if len(self) > 1:
            return super(StructuredTextList, self).to_obj(ns_info=ns_info)

        # One item. Temporarily unset the ordinality if its the default value.
        text = self._inner[0]

        with _unset_default(text):
            l = [text.to_obj(ns_info=ns_info)]

        return l

    def to_list(self):
        """Returns a list of dictionary representations of the contained
        objects.

        An attempt is made to flatten out the returned list when there is only
        one item in the collection. This is to support backwards
        compatibility with previous versions of python-stix.

        * If the list repr has more than one item, return the list.
        * If there is only one item, inspect it.

          * If the item is not a dictionary, return it.
          * If its ``ordinality`` key has a corresponding value of ``1``, remove
            it from the dictionary since it's assumed if there is only one item.
          * After removing ``ordinality``, if the only key left is ``value``,
            just return the value of ``value`` (a string).

        """
        if not self:
            return []

        if len(self) > 1:
            return super(StructuredTextList, self).to_list()

        # One item. Temporarily unset the ordinality if its the default value.
        text = self._inner[0]

        # Temporarily unset the ordinality to create our dictionary
        with _unset_default(text):
            d = text.to_dict()

        return d

    to_dict = to_list

