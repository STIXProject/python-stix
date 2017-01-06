# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
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
    value = fields.TypedField("valueOf_", key_name="value")
    structuring_format = fields.TypedField("structuring_format")

    def __init__(self, value=None):
        super(StructuredText, self).__init__()

        self.id_ = None
        self.value = value
        self.structuring_format = None

    def is_plain(self):
        plain = (
            (not self.id_) and
            (not self.structuring_format)
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
