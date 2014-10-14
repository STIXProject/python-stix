# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from lxml import etree

from .idgen import *
from .nsparser import *

CDATA_START = "<![CDATA["
CDATA_END = "]]>"

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
