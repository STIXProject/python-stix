# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import contextlib

from lxml import etree

import stix
import cybox

CDATA_START = "<![CDATA["
CDATA_END = "]]>"

@contextlib.contextmanager
def ignored(*exceptions):
    """Allows you to ignore exceptions cleanly using context managers. This
    exists in Python 3.

    """
    try:
        yield
    except exceptions:
        pass


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
    xml = "<e>%s</e>" % text
    node = etree.fromstring(xml)
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
        return

    if CDATA_START in text:
        text = strip_cdata(text)

    escaped = "{0}{1}{2}".format(CDATA_START, text, CDATA_END)
    return escaped


def iter_vars(obj):
    d = getattr(obj, "__dict__", {})
    return d.iteritems()


def iter_typed_fields(obj):
    d = getattr(obj, "_fields", {})
    return d.itervalues()


def is_stix(entity):
    return isinstance(entity, stix.Entity)


def is_cybox(entity):
    return isinstance(entity, cybox.Entity)


def is_entity(entity):
    return isinstance(entity, (cybox.Entity, stix.Entity))


from .idgen import *
from .nsparser import *
