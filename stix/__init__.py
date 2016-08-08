# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# Make sure base gets imported before common.
from .base import (Entity, EntityList, TypedCollection, TypedList,  # noqa
                   BaseCoreComponent)

from mixbox.vendor.six import string_types, iteritems

#: Mapping of xsi:types to implementation/extension classes
_EXTENSION_MAP = {}


def _lookup_unprefixed(typename):
    """Attempts to resolve a class for the input XML type `typename`.

    Args:
        typename: The name of an STIX XML type (e.g., TLPMarkingStructureType)
            without a namespace prefix.

    Returns:
        A stix.Entity implementation class for the `typename`.


    Raises:
        ValueError: If no class has been registered for the input `typename`.

    """
    for xsi_type, klass in iteritems(_EXTENSION_MAP):
        if typename in xsi_type:
            return klass

    error = "Unregistered extension type: %s" % typename
    raise ValueError(error)


def _lookup_extension(xsi_type):
    """Returns a Python class for the `xsi_type` value.

    Args:
        xsi_type: An xsi:type value string.

    Returns:
        A stix.Entity implementation class for the `xsi_type`.

    Raises:
        ValueError: If no class has been registered for the `xsi_type`.

    """
    import stix.extensions.malware.maec_4_1_malware
    
    if xsi_type in _EXTENSION_MAP:
        return _EXTENSION_MAP[xsi_type]

    raise ValueError("Unregistered xsi:type %s" % xsi_type)


def lookup_extension(typeinfo, default=None):
    """Returns a stix.Entity class for that has been registered for the
    `typeinfo` value.

    Note:
        This is for internal use only.

    Args:
        typeinfo: An object or string containing type information. This can be
            either an xsi:type attribute value or a stix.bindings object.
        default: Return class if typeinfo is None or contains no xml type
            information.

    Returns:
        A stix.Entity implementation class for the `xsi_type`.

    Raises:
        ValueError: If no class has been registered for the `xsi_type`.

    """
    if typeinfo is None and default:
        return default

    # If the `typeinfo` was a string, consider it a  full xsi:type value.
    if isinstance(typeinfo, string_types):
        return _lookup_extension(typeinfo)

    # Most extension bindings include this attribute.
    if not hasattr(typeinfo, 'xml_type'):
        if default:
            return default

        error = "Input %s is missing xml_type attribute. Cannot lookup class."
        raise ValueError(error % type(typeinfo))
    
    # Extension binding classes usually (always?) have an `xmlns_prefix`
    # class attribute.
    if hasattr(typeinfo, 'xmlns_prefix'):
        xsi_type = "%s:%s" % (typeinfo.xmlns_prefix, typeinfo.xml_type)
        return _lookup_extension(xsi_type)

    # no xmlns_prefix found, try to resolve the class by just the `xml_type`
    return _lookup_unprefixed(typeinfo.xml_type)


def add_extension(cls):
    """Registers a stix.Entity class as an implementation of an xml type.

    Classes must have an ``_XSI_TYPE`` class attributes to be registered. The
    value of this attribute must be a valid xsi:type.

    Note:
        This was designed for internal use.

    """
    _EXTENSION_MAP[cls._XSI_TYPE] = cls  # noqa


def register_extension(cls):
    """Class decorator for registering a stix.Entity class as an implementation
    of an xml type.

    Classes must have an ``_XSI_TYPE`` class attributes to be registered.

    Note:
        This was designed for internal use.

    """
    add_extension(cls)
    return cls

from . import common  # noqa
from .version import __version__  # noqa

def supported_stix_version():
    """Returns a tuple of STIX version strings that this version of python-stix
    supports (i.e., can parse).

    """
    return ('1.1.1', '1.2')

