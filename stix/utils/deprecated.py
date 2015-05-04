# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import warnings


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



