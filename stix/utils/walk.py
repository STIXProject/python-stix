# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import itertools

from mixbox.datautils import is_sequence

# external
from cybox.common import ObjectProperties

# internal
from . import is_entity, is_entitylist, attr_name


def _is_skippable(owner, varname, varobj):
    if varname == "_fields" and isinstance(varobj, dict):
        return True

    if varname == "_parent" and isinstance(owner, ObjectProperties):
        return True

    if varname in ("__input_namespaces__", "__input_schemalocations__"):
        return True

    return False


def _iter_vars(obj):
    attrs = []

    if hasattr(obj, "__dict__"):
        attrs.append(vars(obj).iteritems())

    if hasattr(obj, "_fields"):
        attrs.append(obj._fields.iteritems())

    return itertools.chain.from_iterable(attrs)


def iterwalk(obj):
    """Returns an generator which 'walks` the input `obj` model. Each
    iteration yields a stix.Entity or cybox.Entity instance.

    This is performed depth-first.

    """
    def yield_and_walk(item):
        if not is_entity(item):
            return

        yield item
        for descendant in iterwalk(item):
            yield descendant

    for varname, varobj in _iter_vars(obj):
        if _is_skippable(obj, varname, varobj):
            continue

        if is_sequence(varobj) and not is_entitylist(varobj):
            for item in varobj:
                for descendant in yield_and_walk(item):
                    yield descendant

            continue

        for descendant in yield_and_walk(varobj):
            yield descendant


def iterpath(obj, path=None):
    """Returns a generator which `walks` the input `obj` model. Each
    iteration yields a triple containing a list of ancestor nodes, the name
    of the field, and the field value.

    Example:
        An Indicator Title with a value of "Test" could be yielded as follows:
        ([STIXPackage, Indicators, Indicator], "title", "Test")

    This is performed depth-first.

    """
    def yield_and_descend(name, item):
        yield (path, attr_name(name), item)

        if item is None:
            return

        for path_info in iterpath(item, path):
            yield path_info

    if path is None:
        path = []

    path.append(obj)

    for varname, varobj in _iter_vars(obj):
        if _is_skippable(obj, varname, varobj):
            continue

        if varname == "_inner" and is_entitylist(obj):
            for item in varobj:
                for path_info in iterpath(item, path):
                    yield path_info
        elif is_sequence(varobj) and not is_entitylist(varobj):
            for item in varobj:
                for path_info in yield_and_descend(varname, item):
                    yield path_info

        else:
            for path_info in yield_and_descend(varname, varobj):
                yield path_info

    path.pop()
