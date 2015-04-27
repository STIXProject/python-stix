# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import collections
import contextlib
import keyword
import warnings

# external
import cybox
import lxml.etree

# internal
import stix
import stix.xmlconst as xmlconst

# relative
from . import dates


CDATA_START = "<![CDATA["
CDATA_END = "]]>"
CONFLICTING_NAMES = keyword.kwlist + ['id', 'type', 'range']


@contextlib.contextmanager
def ignored(*exceptions):
    """Allows you to ignore exceptions cleanly using context managers. This
    exists in Python 3.

    """
    try:
        yield
    except exceptions:
        pass


def is_cdata(text):
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
    """Wraps the input `text` in a <![CDATA[]]> block.

    If the text contains CDATA sections already, they are stripped and replaced
    by the application of an outer-most CDATA block.

    Args:
        text: A string to wrap in a CDATA block.

    Returns:
        The `text` value wrapped in <![CDATA[]]>

    """
    if not text:
        return text

    if is_cdata(text):
        text = strip_cdata(text)

    escaped = "{0}{1}{2}".format(CDATA_START, text, CDATA_END)
    return escaped


def is_stix(entity):
    """Returns true if `entity` is an instance of :class:`.Entity`."""
    return isinstance(entity, stix.Entity)


def is_cybox(entity):
    """Returns true if `entity` is an instance of :class:`cybox.Entity`."""
    return isinstance(entity, cybox.Entity)


def is_entity(entity):
    """Returns true if `entity` is an instance of :class:`.Entity` or
    :class:`cybox.Entity`.

    """
    return isinstance(entity, (cybox.Entity, stix.Entity))


def is_entitylist(entity):
    """Returns true if `entity` is an instance of :class:`.EntityList`
    or :class:`cybox.EntityList`.

    """
    return isinstance(entity, (cybox.EntityList, stix.EntityList))


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


def is_sequence(item):
    """Returns ``True`` if `value` is a sequence type (e.g., ``list``, or
    ``tuple``). String types will return ``False``.

    """
    return hasattr(item, "__iter__")


def check_version(expected, found):
    """Raises ValueError if `found` is not equal to or found within
    `expected`.

    """
    if is_sequence(expected):
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

    instance_vars = obj.__dict__.iteritems()
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


def is_element(obj):
    """Returns ``True`` if `obj` is an lxml ``Element``."""
    return isinstance(obj, lxml.etree._Element)  # noqa


def is_etree(obj):
    """Returns ``True`` if `obj` is an lxml ``ElementTree``."""
    return isinstance(obj, lxml.etree._ElementTree)  # noqa


def has_value(var):
    """Returns ``True`` if `var` is not ``None`` and not empty."""
    if var is None:
        return

    return bool(var) or (var in (False, 0))


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

    def dictify(entity):
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
            elif is_element(field) or is_etree(field):
                d[key] = lxml.etree.tostring(field)
            elif is_sequence(field):
                d[key] = dict_iter(field)
            else:
                d[key] = field

        return d

    d = {}
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        d.update(dictify(entity))

    return d


def xml_bool(value):
    """Returns ``True`` if `value` is an acceptable xs:boolean ``True`` value.
    Returns ``False`` if `value` is an acceptable xs:boolean ``False`` value.
    If `value` is ``None``, this function will return ``None``.

    """
    if value is None:
        return None

    if value in xmlconst.FALSE:
        return False

    if value in xmlconst.TRUE:
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


# Namespace flattening
from .nsparser import *  # noqa
from .dates import *  # noqa
from .idgen import *  # noqa
from .nsparser import *  # noqa
from .walk import *  # noqa
