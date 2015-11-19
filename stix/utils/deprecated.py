# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import warnings

from mixbox.datautils import is_sequence
from mixbox.typedlist import TypedList


def idref(entity):
    """Raises a Python UserWarning if `entity` arguments contains an idref
    value.

    """
    if not getattr(entity, 'idref', None):
        return

    fmt = ("The use of idrefs has been deprecated for this field. "
           "Received '{0}' object with idref: '{1}'.")

    msg = fmt.format(type(entity).__name__, entity.idref)
    warnings.warn(msg)


def field(instance, value):
    """Raise a Python UserWarning if the `value` is not None. This is to be
    used with a TypedField preset or postset hook.
    """
    warn(value)


def warn(value):
    """Raises a Python UserWarning if `value` is not None.

    This is typically going to be used inside setter functions for deprecated
    fields. The deprecation warning shouldn't be raised when the field is being
    initialized to ``None``.

    """
    if value is None:
        return

    if is_sequence(value) and not value:
        return

    fmt = "The use of this field has been deprecated. Received '{0}' object."
    msg = fmt.format(type(value).__name__)
    warnings.warn(msg)


class IdrefDeprecatedList(TypedList):
    """TypedList specialization that raises a UserWarning if an inserted value
    contains an idref.
    """

    def insert(self, idx, value):
        idref(value)
        super(IdrefDeprecatedList, self).insert(idx, value)


class DeprecatedList(TypedList):
    """TypedList specialization that raises a UserWarning if a non-None
    value is inserted.
    """
    def insert(self, idx, value):
        warn(value)
        super(DeprecatedList, self).insert(idx, value)
