# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import functools
import warnings


def idref_deprecated(func):
    """Raises a python warning if the input value has an idref attribute
    set.

    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        if kwargs:
            val = next(kwargs.itervalues())
        else:
            val = args[1]

        if getattr(val, 'idref', None):
            msg = ("The use of idrefs has been deprecated for this field. "
                   "'{0}' object with idref: '{1}'.")
            warnings.warn(msg.format(type(val).__name__, val.idref))

        return func(*args, **kwargs)

    return inner