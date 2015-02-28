# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import itertools

# external
from cybox.common import ObjectProperties

# internal
from . import is_entity


def _is_skippable(varname, owner):
    return varname in ("_parent", "_fields") and isinstance(owner, ObjectProperties)


def _iter_vars(obj):
    instance_vars = getattr(obj, "__dict__", {}).iteritems()
    typed_fields  = getattr(obj, "_fields", {}).iteritems()
    return itertools.chain(instance_vars, typed_fields)


def _iterwalk(obj):
    def iterdescend(item):
        if not is_entity(item):
            return

        yield item
        for descendant in _iterwalk(item):
            yield descendant

    for varname, varobj in _iter_vars(obj):
        if _is_skippable(varname, obj):
            continue

        if isinstance(varobj, (list, tuple)):
            for item in varobj:
                for descendant in iterdescend(item):
                    yield descendant

            continue

        for descendant in iterdescend(varobj):
            yield descendant


def iterwalk(obj):
    return _iterwalk(obj)
