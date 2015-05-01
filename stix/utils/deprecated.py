# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import functools
import warnings


def idref_deprecated(func):
    """Raises a deprecation warning if the input value has an idref attribute
    set.

    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        val = args[1]

        if val and val.idref:
            msg = "The use of idrefs has been deprecated for this field."
            warnings.warn(msg, category=DeprecationWarning)

        return func(*args, **kwargs)

    return inner