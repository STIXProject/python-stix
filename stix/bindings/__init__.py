# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import collections

from lxml import etree as etree_
import mixbox.xml


TypeInfo = collections.namedtuple("TypeInfo", ('ns', 'typename'))


def get_type_info(node):
    """Returns a ``TypeInfo`` object for `node`.

    This is accomplished by parsing the ``xsi:type`` attribute found on
    `node`.

    Args:
        node: An lxml.etree element object.

    Raises:
        KeyError: If `node` does not have an ``xsi:type`` attribute.

    """
    xsi_type = node.attrib[mixbox.xml.TAG_XSI_TYPE]
    typeinfo = xsi_type.split(":")

    if len(typeinfo) == 2:
        prefix, typename = typeinfo
    else:
        typename = typeinfo
        prefix = None

    ns = node.nsmap[prefix]
    return TypeInfo(ns=ns, typename=typename)


#: A mapping of namespace/type information to binding classes.
_BINDING_EXTENSION_MAP = {}


def add_extension(cls):
    """Adds the binding class `cls` to the ``_EXTENSION_MAP``.

    This enables the lookup and instantiation of classes during parse when
    ``xsi:type`` attributes are encountered.

    """
    typeinfo = TypeInfo(ns=cls.xmlns, typename=cls.xml_type)
    _BINDING_EXTENSION_MAP[typeinfo] = cls


def register_extension(cls):
    """Class decorator for registering a binding class as an implementation of
    an xml type.

    Classes must have ``xmlns`` and ``xml_type`` class attributes to be
    registered.

    """
    add_extension(cls)
    return cls


def lookup_extension(typeinfo, default=None):
    """Looks up the binding class for `typeinfo`, which is a namespace/typename
    pairing.

    Args:
        typeinfo: An lxml Element node or a stix.bindings.TypeInfo namedtuple.
        default: A binding class that will be returned if typeinfo is an
            Element without an xsi:type attribute.

    Returns:
        A binding class that has been registered for the namespace and typename
        found on `typeinfo`.

    """
    if not isinstance(typeinfo, TypeInfo):
        if has_xsi_type(typeinfo):
            typeinfo = get_type_info(typeinfo)
        elif default:
            return default

    if typeinfo in _BINDING_EXTENSION_MAP:
        return _BINDING_EXTENSION_MAP[typeinfo]

    fmt = "No class implemented or registered for XML type '{%s}%s'"
    error = fmt % (typeinfo.ns, typeinfo.typename)
    raise NotImplementedError(error)


def has_xsi_type(node):
    """Returns ``True`` if `node` does not have an xsi:type attribute.

    """
    return mixbox.xml.TAG_XSI_TYPE in node.attrib


__all__ = [
    'TypeInfo',
    'add_extension',
    'etree_',
    'get_type_info',
    'has_xsi_type',
    'lookup_extension',
    'register_extension',
]
