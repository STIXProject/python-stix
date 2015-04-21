# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import itertools

# internal
import stix
import stix.utils as utils
import stix.bindings.stix_common as stix_common_binding


class StructuredText(stix.Entity):
    _binding = stix_common_binding
    _binding_class = _binding.StructuredTextType
    _namespace = 'http://stix.mitre.org/common-1'

    def __init__(self, value=None, ordinality=None):
        self.id_ = None
        self.value = value
        self.structuring_format = None
        self.ordinality = ordinality

    @property
    def ordinality(self):
        return self._ordinality

    @ordinality.setter
    def ordinality(self, value):
        if value is None:
            self._ordinality = None
            return

        value = int(value)

        if value > 0:
            self._ordinality = value
            return

        error = "Value must be an integer > 0. Received {0}".format(value)
        raise ValueError(error)

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(StructuredText, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        return_obj.id = self.id_
        return_obj.valueOf_ = self.value
        return_obj.ordinality = self.ordinality
        return_obj.structuring_format = self.structuring_format

        return return_obj

    def is_plain(self):
        plain = (
            (not self.id_) and
            (not self.structuring_format) and
            (self.ordinality is None)
        )

        return plain

    def to_dict(self):
        # Return a plain string if there is no format specified.
        if self.is_plain():
            return self.value
        else:
            return super(StructuredText, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.id
        return_obj.value = obj.valueOf_
        return_obj.ordinality = obj.ordinality
        return_obj.structuring_format = obj.structuring_format

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        if not isinstance(d, dict):
            return_obj.value = d
        else:
            return_obj.id_ = d.get('id')
            return_obj.value = d.get('value')
            return_obj.ordinality = d.get('ordinality')
            return_obj.structuring_format = d.get('structuring_format')

        return return_obj
    
    def __str__(self):
        return self.__unicode__().encode("utf-8")

    def __unicode__(self):
        return unicode(self.value)


def _ordkey(text):
    o = text.ordinality
    o = int(o) if o is not None else None
    return (o is None, o)


class StructuredTextList(stix.TypedList):
    _contained_type = StructuredText

    def with_ordinality(self, ordinality):
        if not isinstance(ordinality, int):
            error = "ordinality must be an integer. Received {}"
            error = error.format(type(ordinality))
            raise ValueError(error)

        for item in self._inner:
            if item.ordinality == ordinality:
                return item

        return None

    def with_id(self, id):
        for text in self._inner:
            if text.id_ == id:
                return text

        return None

    def reset(self):
        for idx, item in enumerate(self.sorted, 1):
            item.ordinality = idx

    @property
    def sorted(self):
        return sorted(self._inner, key=_ordkey)

    @property
    def ordinalities(self):
        return tuple(x.ordinality for x in self.sorted)

    def __iter__(self):
        return iter(self.sorted)

    def __getitem__(self, key):
        o = int(key)
        text = self.with_ordinality(o)

        if text:
            return text

        error = "No item found with an ordinality of {0}".format(o)
        raise IndexError(error)

    def __setitem__(self, key, value):
        o = int(key)

        if o < 1:
            raise IndexError("ordinality must be > 0")

        if not self._is_valid(value):
            value = self._fix_value(value)

        if value.ordinality is None:
            value.ordinality = o
        elif value.ordinality != o:
            error = (
                "Ordinality mismatch. {0} found on input object but index "
                "was {1}"
            ).format(value.ordinality, o)
            raise ValueError(error)

        existing = self.with_ordinality(o)

        if existing is not None:
            self._inner.remove(existing)

        self._inner.append(value)

    def __delitem__(self, key):
        o = int(key)
        text = self.with_ordinality(o)

        if text:
            self._inner.remove(text)
            return

        error = "No item found with an ordinality of {0}".format(o)
        raise IndexError(error)

    def insert(self, idx, value):
        if value is None:
            return

        if not self._is_valid(value):
            value = self._fix_value(value)

        if value.ordinality is None:
            if self._inner:
                new_ord = self.ordinalities[-1] + 1
                value.ordinality = new_ord
            else:
                value.ordinality = 1

        exists = self.with_ordinality(value.ordinality)
        if not exists:
            self._inner.append(value)
            return

        error = "Value with ordinality {0} exists: '{1}'."
        error = error.format(value.ordinality, exists.value)
        raise ValueError(error)

    def to_list(self):
        l = super(StructuredTextList, self).to_list()

        if len(l) > 1:
            return l

        d = l[0]
        ordinality = int(d.get('ordinality', 1))

        if ordinality != 1:
            return l

        del d['ordinality']

        if len(d.keys()) == 1 and 'value' in d:
            return d['value']

        return d

    to_dict = to_list

