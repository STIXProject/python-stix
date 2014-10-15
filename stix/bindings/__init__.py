# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import sys
import getopt
import re as re_
import base64
from datetime import datetime, tzinfo, timedelta
from xml.sax import saxutils

CDATA_START = "<![CDATA["
CDATA_END = "]]>"

etree_ = None
Verbose_import_ = False
(   XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
    ) = range(3)
XMLParser_import_library = None
# lxml
from lxml import etree as etree_
XMLParser_import_library = XMLParser_import_lxml
if Verbose_import_:
    print("running with lxml.etree")

def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
        'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser(huge_tree=True)
    doc = etree_.parse(*args, **kwargs)
    return doc


class GeneratedsSuper(object):
    tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
    class _FixedOffsetTZ(tzinfo):
        def __init__(self, offset, name):
            self.__offset = timedelta(minutes = offset)
            self.__name = name
        def utcoffset(self, dt):
            return self.__offset
        def tzname(self, dt):
            return self.__name
        def dst(self, dt):
            return None
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
            if value not in ('true', '1', 'false', '0', ):
                raise_parse_error(node,
                    'Requires sequence of booleans '
                    '("true", "1", "false", "0")')
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
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'GMT')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        if len(input_data.split('.')) > 1:
            dt = datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            dt = datetime.strptime(
                    input_data, '%Y-%m-%dT%H:%M:%S')
        return dt.replace(tzinfo = tz)

    def gds_validate_date(self, input_data, node, input_name=''):
        return input_data
    def gds_format_date(self, input_data, input_name=''):
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
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'GMT')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        return datetime.strptime(input_data,
            '%Y-%m-%d').replace(tzinfo = tz)
    def gds_str_lower(self, instring):
        return instring.lower()
    def get_path_(self, node):
        path_list = []
        self.get_path_list_(node, path_list)
        path_list.reverse()
        path = '/'.join(path_list)
        return path
    Tag_strip_pattern_ = re_.compile(r'\{.*\}')
    def get_path_list_(self, node, path_list):
        if node is None:
            return
        tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
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


#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = 'utf-8'
Tag_pattern_ = re_.compile(r'({.*})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\n\r\s]+")
Namespace_extract_pat_ = re_.compile(r'{(.*)}(.*)')

#
# Support/utility functions.
#

def showIndent(lwrite, level, pretty_print=True):
    if pretty_print:

            lwrite('    ' * level)

def quote_xml(text):
    if not text:
        return ''

    if text.startswith(CDATA_START):
        return text

    return saxutils.escape(text)


def quote_attrib(text):
    if not text:
        return ''

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
    if XMLParser_import_library == XMLParser_import_lxml:
        msg = '%s (element %s/line %d)' % (
            msg, node.tag, node.sourceline, )
    else:
        msg = '%s (element %s)' % (msg, node.tag, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    def export(self, lwrite, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                lwrite(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(lwrite, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(lwrite, level, namespace, name, pretty_print)
    def exportSimple(self, lwrite, level, name):
        if self.content_type == MixedContainer.TypeString:
            lwrite('<%s>%s</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            lwrite('<%s>%d</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            lwrite('<%s>%f</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            lwrite('<%s>%g</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            lwrite('<%s>%s</%s>' %
                (self.name, base64.b64encode(self.value), self.name))
    def to_etree(self, element):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                if len(element) > 0:
                    if element[-1].tail is None:
                        element[-1].tail = self.value
                    else:
                        element[-1].tail += self.value
                else:
                    if element.text is None:
                        element.text = self.value
                    else:
                        element.text += self.value
        elif self.category == MixedContainer.CategorySimple:
            subelement = etree_.SubElement(element, '%s' % self.name)
            subelement.text = self.to_etree_simple()
        else:    # category == MixedContainer.CategoryComplex
            self.value.to_etree(element)
    def to_etree_simple(self):
        if self.content_type == MixedContainer.TypeString:
            text = self.value
        elif (self.content_type == MixedContainer.TypeInteger or
                self.content_type == MixedContainer.TypeBoolean):
            text = '%d' % self.value
        elif (self.content_type == MixedContainer.TypeFloat or
                self.content_type == MixedContainer.TypeDecimal):
            text = '%f' % self.value
        elif self.content_type == MixedContainer.TypeDouble:
            text = '%g' % self.value
        elif self.content_type == MixedContainer.TypeBase64:
            text = '%s' % base64.b64encode(self.value)
        return text
    def exportLiteral(self, lwrite, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(lwrite, level)
            lwrite('model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(lwrite, level)
            lwrite('model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(lwrite, level)
            lwrite('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(lwrite, level + 1)
            showIndent(lwrite, level)
            lwrite(')\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0):
        self.name = name
        self.data_type = data_type
        self.container = container
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

__all__ = [
    '_cast',
    'etree_',
    'ExternalEncoding',
    'find_attr_value_',
    'get_all_text_',
    'parsexml_',
    'quote_xml',
    'quote_attrib',
    'quote_python',
    'raise_parse_error',
    'showIndent',
    'String_cleanup_pat_',
    'Tag_pattern_',
    'Verbose_import_',
    'XMLParser_import_library',
    'MemberSpec_',
    'GDSParseError',
    'GeneratedsSuper',
    'MixedContainer',
    'CDATA_START',
    'CDATA_END'
]
