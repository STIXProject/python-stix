# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import functools
import keyword

import lxml.etree

from mixbox import datautils
from mixbox.entities import Entity, EntityList
import mixbox.xml

from cybox.common import ObjectProperties
from cybox.core import Object, Observable

import stix

# relative
from . import dates

CDATA_START = "<![CDATA["
CDATA_END = "]]>"
CONFLICTING_NAMES = keyword.kwlist + ['id', 'type', 'range']


def raise_warnings(func):
    """Function decorator that causes all Python warnings to be raised as
    exceptions in the wrapped function.

    Example:
        >>> @raise_warnings
        >>> def foo():
        >>>     warnings.warn("this will raise an exception")

    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter('error')
            return func(*args, **kwargs)
    return inner


def silence_warnings(func):
    """Function decorator that silences/ignores all Python warnings in the
    wrapped function.

    Example:
        >>> @silence_warnings
        >>> def foo():
        >>>     warnings.warn("this will not appear")

    """
    @functools.wraps(func)
    def inner(*args, **kwargs):
        with warnings.catch_warnings(record=True):
            warnings.simplefilter('always')
            return func(*args, **kwargs)
    return inner


def is_cdata(text):
    """Returns ``True`` if `text` contains a CDATA block.

    Example:
        >>> is_cdata("<![CDATA[Foo]]>")
        True
        >>> is_cdata("NOPE")
        False

    """
    if not text:
        return False

    return CDATA_START in text


def strip_cdata(text):
    """Removes all CDATA blocks from `text` if it contains them.

    Note:
        If the function contains escaped XML characters outside of a
        CDATA block, they will be unescaped.

    Args:
        A string containing one or more CDATA blocks.

    Returns:
        An XML unescaped string with CDATA block qualifiers removed.

    """
    if not is_cdata(text):
        return text

    xml = "<e>{0}</e>".format(text)
    node = lxml.etree.fromstring(xml)
    return node.text


def cdata(text):
    """Wraps the input `text` in a ``<![CDATA[ ]]>`` block.

    If the text contains CDATA sections already, they are stripped and replaced
    by the application of an outer-most CDATA block.

    Args:
        text: A string to wrap in a CDATA block.

    Returns:
        The `text` value wrapped in ``<![CDATA[]]>``

    """
    if not text:
        return text

    if is_cdata(text):
        text = strip_cdata(text)

    escaped = "{0}{1}{2}".format(CDATA_START, text, CDATA_END)
    return escaped


def is_stix(entity):
    """Returns true if `entity` is an instance of :class:`stix.Entity`."""
    return isinstance(entity, stix.Entity)


def is_cybox(entity):
    """Returns true if `entity` is a CybOX Object, Observable, or
    ObjectProperties subclass.
    """
    return isinstance(entity, (Object, Observable, ObjectProperties))


def is_entity(entity):
    """Returns true if `entity` is :class:`mixbox.entities.Entity`."""
    return isinstance(entity, Entity)


def is_entitylist(entity):
    """Returns true if `entity` is an instance of :class:`.EntityList`
    or :class:`mixbox.entities.EntityList`.

    """
    return isinstance(entity, (EntityList, stix.EntityList))


def is_typedlist(entity):
    """Returns true if `entity` is an instance of :class:`.TypedList`

    """
    return isinstance(entity, stix.TypedList)


def private_name(name):
    """Returns the internal, private name used when setting Entity property
    values. Basically, it appends a "_" to `name` if there isn't already
    one there.

    """
    if name.startswith("_"):
        return name

    return "_" + name


def attr_name(name):
    """Converts `name` into the form expected for python-stix and
    python-cybox properties.

    This is used when attempting to access the property getter/setter via
    the __dict__ instance var entries.

    Example:
        >>> attr_name("id")
        'id_'
        >>> attr_name("Title")
        'title

    """
    name = name.lower()

    if name.startswith("_"):
        name = name[1:]

    if name in CONFLICTING_NAMES:
        name += "_"

    return name


def key_name(name):
    """Converts the input attribute name `name` into a key to be
    used in `to_dict()` return dictionaries.

    """
    name = attr_name(name)

    if name.endswith("_"):
        return name[:-1]

    return name


def check_version(expected, found):
    """Raises ValueError if `found` is not equal to or found within
    `expected`.

    """
    if datautils.is_sequence(expected):
        is_good = found in expected
    else:
        is_good = (found == expected)

    if not is_good:
        error = "Version '{0}' is invalid. Expected {1}."
        error = error.format(found, expected)
        raise ValueError(error)


def iter_vars(obj):
    """Returns a generator which yields a ``(property name, property value)``
    tuple with each iteration.

    Note:
        This will not yield vars that are attached during parse, such as
        ``__input_schemalocations__`` and ``__input_namespaces__``.

    """
    def check(name):
        return name not in ('__input_namespaces__', '__input_schemalocations__')

    instance_vars = vars(obj).iteritems()
    return ((attr_name(name), val) for name, val in instance_vars if check(name))


def is_dictable(obj):
    """Returns ``True`` if `obj` has a ``to_dict()`` method."""
    return hasattr(obj, "to_dict")


def is_timestamp(obj):
    """Returns ``True`` if `obj` is an instance of ``datetime.datetime``."""
    return isinstance(obj, datetime.datetime)


def is_date(obj):
    """Returns ``True`` if `obj` is an instance of ``datetime.date``."""
    return isinstance(obj, datetime.date)


def is_bool(obj):
    """Returns ``True`` if `obj` is a ``bool``."""
    return isinstance(obj, bool)


def has_value(var):
    """Returns ``True`` if `var` is not ``None`` and not empty."""
    if var is None:
        return

    return bool(var) or (var in (False, 0))


@silence_warnings
def to_dict(entity, skip=()):
    """Returns a dictionary representation of `entity`. This will iterate over
    the instance vars of `entity` and construct keys and values from those
    variable names and values.

    Args:
        entity: A ``Entity`` object.
        skip: An iterable containing keys to exclude from the dictionary. These
            should be the dictionary key names, and not the instance variable
            name (e.g., 'id' and NOT 'id_').

    Returns:
        A dictionary representation of the input `entity`.

    """
    def dict_iter(items):
        return [x.to_dict() if is_dictable(x) else x for x in items]


    d = {}
    for name, field in iter_vars(entity):
        key = key_name(name)

        if key in skip or not has_value(field):
            continue

        if is_dictable(field):
            d[key] = field.to_dict()
        elif is_timestamp(field):
            d[key] = dates.serialize_value(field)
        elif is_date(field):
            d[key] = dates.serialize_date(field)
        elif mixbox.xml.is_element(field) or mixbox.xml.is_etree(field):
            d[key] = lxml.etree.tostring(field)
        elif datautils.is_sequence(field):
            d[key] = dict_iter(field)
        else:
            d[key] = field

    return d


def xml_bool(value):
    """Returns ``True`` if `value` is an acceptable xs:boolean ``True`` value.
    Returns ``False`` if `value` is an acceptable xs:boolean ``False`` value.
    If `value` is ``None``, this function will return ``None``.

    """
    if value is None:
        return None

    if value in mixbox.xml.FALSE:
        return False

    if value in mixbox.xml.TRUE:
        return True

    error = "Unable to determine the xml boolean value of '{0}'".format(value)
    raise ValueError(error)


def cast_var(item, klass, arg=None):
    """Attempt to cast `item` to an instance of `klass`.

    Args:
        item: The object to cast.
        klass: The class to cast to.
        arg: The kwarg name to use for the `klass` ``__init__()`` parameter. If
            ``None``, a positional argument will be used.

    """
    if not arg:
        return klass(item)

    kwarg = {arg: item}     # kwarg dict
    return klass(**kwarg)   # klass(value='foobar')


def remove_entries(d, keys):
    """Removes all the `keys` from the dictionary `d`.

    Args:
        d: A dictionary.
        keys: An iterable collection of dictionary keys to remove.

    """
    for key in keys:
        d.pop(key, None)


# Namespace flattening
from .parser import *  # noqa
from .dates import *  # noqa
from .nsparser import *  # noqa
from .walk import *  # noqa
