# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import warnings
import functools


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
    if value is None:
        return

    fmt = "The use of this field has been deprecated. Received '{0}' object."

    msg = fmt.format(type(value).__name__)
    warnings.warn(msg)

