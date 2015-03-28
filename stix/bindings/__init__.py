# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import re
import base64
import collections
import contextlib
from xml.sax import saxutils
from datetime import datetime, tzinfo, timedelta

from lxml import etree as etree_
import cybox.bindings as cybox_bindings

from stix import xmlconst

try:
    import maec.bindings as maec_bindings
    _MAEC_INSTALLED = True
except ImportError:
    _MAEC_INSTALLED = False


CDATA_START = "<![CDATA["
CDATA_END = "]]>"

ExternalEncoding = 'utf-8'
Tag_pattern_ = re.compile(r'({.*})?(.*)')

# These are only used internally
_tzoff_pattern = re.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
_Tag_strip_pattern_ = re.compile(r'\{.*\}')


@contextlib.contextmanager
def save_encoding(encoding='utf-8'):
    global ExternalEncoding

    try:
        # Save original binding encoding attribute value
        orig_stix_encoding = ExternalEncoding
        orig_cybox_encoding = cybox_bindings.ExternalEncoding

        # Set binding encoding attribute value to `encoding`
        ExternalEncoding = encoding
        cybox_bindings.ExternalEncoding = encoding

        # Set MAEC binding encoding attribute to `encoding` if python-maec
        # is installed.
        if _MAEC_INSTALLED:
            orig_maec_encoding = maec_bindings.ExternalEncoding
            maec_bindings.ExternalEncoding = encoding

        # Return to caller
        yield

    finally:
        # Reset the binding encoding attribute values to original values
        ExternalEncoding = orig_stix_encoding
        cybox_bindings.ExternalEncoding = orig_cybox_encoding

        if _MAEC_INSTALLED:
            maec_bindings.ExternalEncoding = orig_maec_encoding


def parsexml_(*args, **kwargs):
    from stix.utils.parser import get_xml_parser

    if 'parser' not in kwargs:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        # we ignore comments.
        kwargs['parser'] = get_xml_parser()
    return etree_.parse(*args, **kwargs)


class _FixedOffsetTZ(tzinfo):

    def __init__(self, offset, name):
        self.__offset = timedelta(minutes=offset)
        self.__name = name

    def utcoffset(self, dt):
        return self.__offset

    def tzname(self, dt):
        return self.__name

    def dst(self, dt):
        return None

    __reduce__ = object.__reduce__


class GeneratedsSuper(object):

    def gds_format_string(self, input_data, input_name=''):
        return input_data

    def gds_validate_string(self, input_data, node, input_name=''):
        return input_data

    def gds_format_base64(self, input_data, input_name=''):
        return base64.b64encode(input_data)

    def gds_validate_base64(self, input_data, node, input_name=''):
        return input_data

    def gds_format_integer(self, input_data, input_name=''):
        return '%d' % input_data

    def gds_validate_integer(self, input_data, node, input_name=''):
        return input_data

    def gds_format_integer_list(self, input_data, input_name=''):
        return '%s' % input_data

    def gds_validate_integer_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                fvalue = float(value)
            except (TypeError, ValueError), exp:
                raise_parse_error(node, 'Requires sequence of integers')
        return input_data

    def gds_format_float(self, input_data, input_name=''):
        return '%f' % input_data

    def gds_validate_float(self, input_data, node, input_name=''):
        return input_data

    def gds_format_float_list(self, input_data, input_name=''):
        return '%s' % input_data

    def gds_validate_float_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                fvalue = float(value)
            except (TypeError, ValueError), exp:
                raise_parse_error(node, 'Requires sequence of floats')
        return input_data

    def gds_format_double(self, input_data, input_name=''):
        return '%e' % input_data

    def gds_validate_double(self, input_data, node, input_name=''):
        return input_data

    def gds_format_double_list(self, input_data, input_name=''):
        return '%s' % input_data

    def gds_validate_double_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                fvalue = float(value)
            except (TypeError, ValueError), exp:
                raise_parse_error(node, 'Requires sequence of doubles')
        return input_data

    def gds_format_boolean(self, input_data, input_name=''):
        return ('%s' % input_data).lower()

    def gds_validate_boolean(self, input_data, node, input_name=''):
        return input_data

    def gds_format_boolean_list(self, input_data, input_name=''):
        return '%s' % input_data

    def gds_validate_boolean_list(self, input_data, node, input_name=''):
        values = input_data.split()
        for value in values:
            if value not in ('true', '1', 'false', '0'):
                msg = ('Requires sequence of booleans '
                       '("true", "1", "false", "0")')
                raise_parse_error(node, msg)
        return input_data

    def gds_validate_datetime(self, input_data, node, input_name=''):
        return input_data

    def gds_format_datetime(self, input_data, input_name=''):
        if isinstance(input_data, basestring):
            return input_data
        if input_data.microsecond == 0:
            _svalue = input_data.strftime('%Y-%m-%dT%H:%M:%S')
        else:
            _svalue = input_data.strftime('%Y-%m-%dT%H:%M:%S.%f')
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue

    def gds_parse_datetime(self, input_data, node, input_name=''):
        tz = None
        if input_data[-1] == 'Z':
            tz = _FixedOffsetTZ(0, 'GMT')
            input_data = input_data[:-1]
        else:
            results = _tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = _FixedOffsetTZ(tzoff, results.group(0))
                input_data = input_data[:-6]
        if len(input_data.split('.')) > 1:
            dt = datetime.strptime(input_data, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            dt = datetime.strptime(input_data, '%Y-%m-%dT%H:%M:%S')
        return dt.replace(tzinfo=tz)

    def gds_validate_date(self, input_data, node, input_name=''):
        return input_data

    def gds_format_date(self, input_data, input_name=''):
        if isinstance(input_data, basestring):
            return input_data
        _svalue = input_data.strftime('%Y-%m-%d')
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{0:02d}:{1:02d}'.format(hours, minutes)
        return _svalue

    def gds_parse_date(self, input_data, node, input_name=''):
        tz = None
        if input_data[-1] == 'Z':
            tz = _FixedOffsetTZ(0, 'GMT')
            input_data = input_data[:-1]
        else:
            results = _tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = _FixedOffsetTZ(tzoff, results.group(0))
                input_data = input_data[:-6]
        return datetime.strptime(input_data, '%Y-%m-%d').replace(tzinfo=tz)

    def gds_str_lower(self, instring):
        return instring.lower()

    def get_path_(self, node):
        path_list = []
        self.get_path_list_(node, path_list)
        path_list.reverse()
        path = '/'.join(path_list)
        return path

    def get_path_list_(self, node, path_list):
        if node is None:
            return
        tag = _Tag_strip_pattern_.sub('', node.tag)
        if tag:
            path_list.append(tag)
        self.get_path_list_(node.getparent(), path_list)

    def get_class_obj_(self, node, default_class=None):
        class_obj1 = default_class
        if 'xsi' in node.nsmap:
            classname = node.get('{%s}type' % node.nsmap['xsi'])
            if classname is not None:
                names = classname.split(':')
                if len(names) == 2:
                    classname = names[1]
                class_obj2 = globals().get(classname)
                if class_obj2 is not None:
                    class_obj1 = class_obj2
        return class_obj1

    def gds_build_any(self, node, type_name=None):
        return None


def showIndent(lwrite, level, pretty_print=True):
    if pretty_print:
        lwrite('    ' * level)


def quote_xml(text):
    if text is None:
        return u''

    # Convert `text` to unicode string. This is mainly a catch-all for non
    # string/unicode types like bool and int.
    try:
        text = unicode(text)
    except UnicodeDecodeError:
        text = text.decode(ExternalEncoding)

    # If it's a CDATA block, return the text as is.
    if text.startswith(CDATA_START):
        return text

    # If it's not a CDATA block, escape the XML and return the character
    # encoded string.
    return saxutils.escape(text)


def quote_attrib(text):
    if text is None:
        return u'""'

    # Convert `text` to unicode string. This is mainly a catch-all for non
    # string/unicode types like bool and int.
    try:
        text = unicode(text)
    except UnicodeDecodeError:
        text = text.decode(ExternalEncoding)

    # Return the escaped the value of text.
    # Note: This wraps the escaped text in quotation marks.
    return saxutils.quoteattr(text)


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\"')
        if s1.find('\n') == -1:
            return '"%s"' % s1
        else:
            return '"""%s"""' % s1


def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text


def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{%s}%s' % (namespace, name, ))
    return value


class GDSParseError(Exception):
    pass

def raise_parse_error(node, msg):
    msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline)
    raise GDSParseError(msg)


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)


TypeInfo = collections.namedtuple("TypeInfo", ('ns', 'typename'))


def get_type_info(node):
    xsi_type = node.attrib[xmlconst.TAG_XSI_TYPE]
    typeinfo = xsi_type.split(":")

    if len(typeinfo) == 2:
        prefix, typename = typeinfo
    else:
        typename = typeinfo
        prefix = None

    ns = node.nsmap[prefix]
    return TypeInfo(ns=ns, typename=typename)


__all__ = [
    '_cast',
    'etree_',
    'ExternalEncoding',
    'find_attr_value_',
    'get_all_text_',
    'get_type_info',
    'parsexml_',
    'quote_xml',
    'quote_attrib',
    'quote_python',
    'raise_parse_error',
    'showIndent',
    'Tag_pattern_',
    'GeneratedsSuper',
    'CDATA_START',
    'CDATA_END',
    'TypeInfo'
]
