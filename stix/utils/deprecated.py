# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import warnings

from . import is_sequence


def idref_deprecated(entity):
    """Raises a Python UserWarning if `entity` arguments contains an idref
    value.

    """
    if not getattr(entity, 'idref', None):
        return

    fmt = ("The use of idrefs has been deprecated for this field. "
           "Received '{0}' object with idref: '{1}'.")

    msg = fmt.format(type(entity).__name__, entity.idref)
    warnings.warn(msg)


def deprecated(value):
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

