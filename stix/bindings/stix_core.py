# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:06:27 2013 by generateDS.py version 2.9a.
#

import sys
import getopt
import re as re_

import stix.bindings.stix_common as stix_common_binding
import stix.bindings.data_marking as data_marking_binding
import cybox.bindings.cybox_core as cybox_core_binding

import base64
from datetime import datetime, tzinfo, timedelta

XML_NS = "http://stix.mitre.org/stix-1"

DEFAULT_XML_NS_MAP = {  'http://capec.mitre.org/capec-2': 'capec',
                         'http://cpe.mitre.org/language/2.0': 'cpe',
                         'http://cybox.mitre.org/common-2': 'cyboxCommon',
                         'http://cybox.mitre.org/cybox-2': 'cybox',
                         'http://cybox.mitre.org/default_vocabularies-2': 'cyboxVocabs',
                         'http://cybox.mitre.org/objects#APIObject-2': 'APIObj',
                         'http://cybox.mitre.org/objects#AccountObject-2': 'AccountObj',
                         'http://cybox.mitre.org/objects#AddressObject-2': 'AddressObj',
                         'http://cybox.mitre.org/objects#ArtifactObject-2': 'ArtifactObj',
                         'http://cybox.mitre.org/objects#CodeObject-2': 'CodeObj',
                         'http://cybox.mitre.org/objects#CustomObject-1': 'CustomObj',
                         'http://cybox.mitre.org/objects#DNSCacheObject-2': 'DNSCacheObj',
                         'http://cybox.mitre.org/objects#DNSQueryObject-2': 'DNSQueryObj',
                         'http://cybox.mitre.org/objects#DNSRecordObject-2': 'DNSRecordObj',
                         'http://cybox.mitre.org/objects#DeviceObject-2': 'DeviceObj',
                         'http://cybox.mitre.org/objects#DiskObject-2': 'DiskObj',
                         'http://cybox.mitre.org/objects#DiskPartitionObject-2': 'DiskPartitionObj',
                         'http://cybox.mitre.org/objects#EmailMessageObject-2': 'EmailMessageObj',
                         'http://cybox.mitre.org/objects#FileObject-2': 'FileObj',
                         'http://cybox.mitre.org/objects#GUIDialogboxObject-2': 'GUIDialogBoxObj',
                         'http://cybox.mitre.org/objects#GUIObject-2': 'GUIObj',
                         'http://cybox.mitre.org/objects#GUIWindowObject-2': 'GUIWindowObj',
                         'http://cybox.mitre.org/objects#HTTPSessionObject-2': 'HTTPSessionObj',
                         'http://cybox.mitre.org/objects#LibraryObject-2': 'LibraryObj',
                         'http://cybox.mitre.org/objects#LinkObject-1': 'LinkObj',
                         'http://cybox.mitre.org/objects#LinuxPackageObject-2': 'LinuxPackageObj',
                         'http://cybox.mitre.org/objects#MemoryObject-2': 'MemoryObj',
                         'http://cybox.mitre.org/objects#MutexObject-2': 'MutexObj',
                         'http://cybox.mitre.org/objects#NetworkConnectionObject-2': 'NetworkConnectionObj',
                         'http://cybox.mitre.org/objects#NetworkFlowObject-2': 'NetFlowObj',
                         'http://cybox.mitre.org/objects#NetworkRouteEntryObject-2': 'NetworkRouteEntryObj',
                         'http://cybox.mitre.org/objects#NetworkRouteObject-2': 'NetworkRouteObj',
                         'http://cybox.mitre.org/objects#NetworkSocketObject-2': 'NetworkSocketObj',
                         'http://cybox.mitre.org/objects#NetworkSubnetObject-2': 'NetworkSubnetObj',
                         'http://cybox.mitre.org/objects#PDFFileObject-1': 'PDFFileObj',
                         'http://cybox.mitre.org/objects#PacketObject-2': 'PacketObj',
                         'http://cybox.mitre.org/objects#PipeObject-2': 'PipeObj',
                         'http://cybox.mitre.org/objects#PortObject-2': 'PortObj',
                         'http://cybox.mitre.org/objects#ProcessObject-2': 'ProcessObj',
                         'http://cybox.mitre.org/objects#ProductObject-2': 'ProductObj',
                         'http://cybox.mitre.org/objects#SemaphoreObject-2': 'SemaphoreObj',
                         'http://cybox.mitre.org/objects#SocketAddressObject-1': 'SocketAddressObj',
                         'http://cybox.mitre.org/objects#SystemObject-2': 'SystemObj',
                         'http://cybox.mitre.org/objects#URIObject-2': 'URIObj',
                         'http://cybox.mitre.org/objects#UnixFileObject-2': 'UnixFileObj',
                         'http://cybox.mitre.org/objects#UnixNetworkRouteEntryObject-2': 'UnixNetworkRouteEntryObj',
                         'http://cybox.mitre.org/objects#UnixPipeObject-2': 'UnixPipeObj',
                         'http://cybox.mitre.org/objects#UnixProcessObject-2': 'UnixProcessObj',
                         'http://cybox.mitre.org/objects#UnixUserAccountObject-2': 'UnixUserAccountObj',
                         'http://cybox.mitre.org/objects#UnixVolumeObject-2': 'UnixVolumeObj',
                         'http://cybox.mitre.org/objects#UserAccountObject-2': 'UserAccountObj',
                         'http://cybox.mitre.org/objects#UserSessionObject-2': 'UserSessionObj',
                         'http://cybox.mitre.org/objects#VolumeObject-2': 'VolumeObj',
                         'http://cybox.mitre.org/objects#WhoisObject-2': 'WhoisObj',
                         'http://cybox.mitre.org/objects#WinComputerAccountObject-2': 'WinComputerAccountObj',
                         'http://cybox.mitre.org/objects#WinCriticalSectionObject-2': 'WinCriticalSectionObj',
                         'http://cybox.mitre.org/objects#WinDriverObject-2': 'WinDriverObj',
                         'http://cybox.mitre.org/objects#WinEventLogObject-2': 'WinEventLogObj',
                         'http://cybox.mitre.org/objects#WinEventObject-2': 'WinEventObj',
                         'http://cybox.mitre.org/objects#WinExecutableFileObject-2': 'WinExecutableFileObj',
                         'http://cybox.mitre.org/objects#WinFileObject-2': 'WinFileObj',
                         'http://cybox.mitre.org/objects#WinHandleObject-2': 'WinHandleObj',
                         'http://cybox.mitre.org/objects#WinKernelHookObject-2': 'WinKernelHookObj',
                         'http://cybox.mitre.org/objects#WinKernelObject-2': 'WinKernelObj',
                         'http://cybox.mitre.org/objects#WinMailslotObject-2': 'WinMailslotObj',
                         'http://cybox.mitre.org/objects#WinMemoryPageRegionObject-2': 'WinMemoryPageRegionObj',
                         'http://cybox.mitre.org/objects#WinMutexObject-2': 'WinMutexObj',
                         'http://cybox.mitre.org/objects#WinNetworkRouteEntryObject-2': 'WinNetworkRouteEntryObj',
                         'http://cybox.mitre.org/objects#WinNetworkShareObject-2': 'WinNetworkShareObj',
                         'http://cybox.mitre.org/objects#WinPipeObject-2': 'WinPipeObj',
                         'http://cybox.mitre.org/objects#WinPrefetchObject-2': 'WinPrefetchObj',
                         'http://cybox.mitre.org/objects#WinProcessObject-2': 'WinProcessObj',
                         'http://cybox.mitre.org/objects#WinRegistryKeyObject-2': 'WinRegistryKeyObj',
                         'http://cybox.mitre.org/objects#WinSemaphoreObject-2': 'WinSemaphoreObj',
                         'http://cybox.mitre.org/objects#WinServiceObject-2': 'WinServiceObj',
                         'http://cybox.mitre.org/objects#WinSystemObject-2': 'WinSystemObj',
                         'http://cybox.mitre.org/objects#WinSystemRestoreObject-2': 'WinSystemRestoreObj',
                         'http://cybox.mitre.org/objects#WinTaskObject-2': 'WinTaskObj',
                         'http://cybox.mitre.org/objects#WinThreadObject-2': 'WinThreadObj',
                         'http://cybox.mitre.org/objects#WinUserAccountObject-2': 'WinUserAccountObj',
                         'http://cybox.mitre.org/objects#WinVolumeObject-2': 'WinVolumeObj',
                         'http://cybox.mitre.org/objects#WinWaitableTimerObject-2': 'WinWaitableTimerObj',
                         'http://cybox.mitre.org/objects#X509CertificateObject-2': 'X509CertificateObj',
                         'http://data-marking.mitre.org/Marking-1': 'marking',
                         'http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1': 'simpleMarking',
                         'http://data-marking.mitre.org/extensions/MarkingStructure#TLP-1': 'tlpMarking',
                         'http://maec.mitre.org/XMLSchema/maec-package-2': 'maec',
                         'http://oval.mitre.org/XMLSchema/oval-common-5': 'oval',
                         'http://oval.mitre.org/XMLSchema/oval-definitions-5': 'oval-def',
                         'http://oval.mitre.org/XMLSchema/oval-variables-5': 'oval-var',
                         'http://purl.oclc.org/dsdl/schematron': 'sch',
                         'http://purl.org/dc/elements/1.1/': 'dc',
                         'http://scap.nist.gov/schema/cvss-v2/1.0': 'cvssv2',
                         'http://scap.nist.gov/schema/scap-core/1.0': 'scap-core',
                         'http://schemas.mandiant.com/2010/ioc': 'ioc',
                         'http://schemas.mandiant.com/2010/ioc/TR/': 'ioc-tr',
                         'http://stix.mitre.org/Campaign-1': 'campaign',
                         'http://stix.mitre.org/CourseOfAction-1': 'coa',
                         'http://stix.mitre.org/ExploitTarget-1': 'et',
                         'http://stix.mitre.org/Incident-1': 'incident',
                         'http://stix.mitre.org/Indicator-2': 'indicator',
                         'http://stix.mitre.org/TTP-1': 'ttp',
                         'http://stix.mitre.org/ThreatActor-1': 'ta',
                         'http://stix.mitre.org/common-1': 'stixCommon',
                         'http://stix.mitre.org/default_vocabularies-1': 'stixVocabs',
                         'http://stix.mitre.org/extensions/AP#CAPEC2.6-1': 'capecInstance',
                         'http://stix.mitre.org/extensions/Address#CIQAddress3.0-1': 'ciqAddress',
                         'http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1': 'ciqIdentity',
                         'http://stix.mitre.org/extensions/Malware#MAEC4.0-1': 'maecInstance',
                         'http://stix.mitre.org/extensions/StructuredCOA#Generic-1': 'genericStructuredCOA',
                         'http://stix.mitre.org/extensions/TestMechanism#Generic-1': 'genericTM',
                         'http://stix.mitre.org/extensions/TestMechanism#OVAL5.10-1': 'ovalTM',
                         'http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1': 'openiocTM',
                         'http://stix.mitre.org/extensions/TestMechanism#Snort-1': 'snortTM',
                         'http://stix.mitre.org/extensions/TestMechanism#YARA-1': 'yaraTM',
                         'http://stix.mitre.org/extensions/Vulnerability#CVRF-1': 'cvrfVuln',
                         'http://stix.mitre.org/stix-1': 'stix',
                         'http://www.icasi.org/CVRF/schema/common/1.1': 'cvrf-common',
                         'http://www.icasi.org/CVRF/schema/cvrf/1.1': 'cvrf',
                         'http://www.icasi.org/CVRF/schema/prod/1.1': 'prod',
                         'http://www.icasi.org/CVRF/schema/vuln/1.1': 'vuln',
                         'http://www.w3.org/1999/xlink': 'xlink',
                         'http://www.w3.org/2000/09/xmldsig#': 'ds',
                         'http://www.w3.org/2001/XMLSchema': 'xs',
                         'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
                         'urn:oasis:names:tc:ciq:ct:3': 'ct',
                         'urn:oasis:names:tc:ciq:xal:3': 'a',
                         'urn:oasis:names:tc:ciq:xnl:3': 'xnl',
                         'urn:oasis:names:tc:ciq:xpil:3': 'ciq'}

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

#
# User methods
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

try:
    from generatedssuper import GeneratedsSuper
except ImportError, exp:

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

def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')

def quote_xml(inStr):
    if not inStr:
        return ''
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1

def quote_attrib(inStr):
    s1 = (isinstance(inStr, basestring) and inStr or
          '%s' % inStr)
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1

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
    def export(self, outfile, level, name, namespace, pretty_print=True):
        if self.category == MixedContainer.CategoryText:
            # Prevent exporting empty content as empty lines.
            if self.value.strip():
                outfile.write(self.value)
        elif self.category == MixedContainer.CategorySimple:
            self.exportSimple(outfile, level, name)
        else:    # category == MixedContainer.CategoryComplex
            self.value.export(outfile, level, namespace, name, pretty_print)
    def exportSimple(self, outfile, level, name):
        if self.content_type == MixedContainer.TypeString:
            outfile.write('<%s>%s</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeInteger or \
                self.content_type == MixedContainer.TypeBoolean:
            outfile.write('<%s>%d</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeFloat or \
                self.content_type == MixedContainer.TypeDecimal:
            outfile.write('<%s>%f</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeDouble:
            outfile.write('<%s>%g</%s>' %
                (self.name, self.value, self.name))
        elif self.content_type == MixedContainer.TypeBase64:
            outfile.write('<%s>%s</%s>' %
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
    def exportLiteral(self, outfile, level, name):
        if self.category == MixedContainer.CategoryText:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value))
        elif self.category == MixedContainer.CategorySimple:
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s", "%s"),\n'
                % (self.category, self.content_type, self.name, self.value))
        else:    # category == MixedContainer.CategoryComplex
            showIndent(outfile, level)
            outfile.write('model_.MixedContainer(%d, %d, "%s",\n' % \
                (self.category, self.content_type, self.name,))
            self.value.exportLiteral(outfile, level + 1)
            showIndent(outfile, level)
            outfile.write(')\n')


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

#
# Data representation classes.
#

class STIXType(GeneratedsSuper):
    """STIXType defines a bundle of information characterized in the
    Structured Threat Information eXpression (STIX)
    language.Specifies a globally unique identifier for this STIX
    Package. Specifies a globally unique identifier of a STIX
    Package specified elsewhere.Specifies the relevant STIX schema
    version for this content."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, version=None, STIX_Header=None, Observables=None, Indicators=None, TTPs=None, Exploit_Targets=None, Incidents=None, Courses_Of_Action=None, Campaigns=None, Threat_Actors=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.version = _cast(None, version)
        self.STIX_Header = STIX_Header
        self.Observables = Observables
        self.Indicators = Indicators
        self.TTPs = TTPs
        self.Exploit_Targets = Exploit_Targets
        self.Incidents = Incidents
        self.Courses_Of_Action = Courses_Of_Action
        self.Campaigns = Campaigns
        self.Threat_Actors = Threat_Actors
        self.nsmap = {}
    def factory(*args_, **kwargs_):
        if STIXType.subclass:
            return STIXType.subclass(*args_, **kwargs_)
        else:
            return STIXType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_STIX_Header(self): return self.STIX_Header
    def set_STIX_Header(self, STIX_Header): self.STIX_Header = STIX_Header
    def get_Observables(self): return self.Observables
    def set_Observables(self, Observables): self.Observables = Observables
    def get_Indicators(self): return self.Indicators
    def set_Indicators(self, Indicators): self.Indicators = Indicators
    def get_TTPs(self): return self.TTPs
    def set_TTPs(self, TTPs): self.TTPs = TTPs
    def get_Exploit_Targets(self): return self.Exploit_Targets
    def set_Exploit_Targets(self, Exploit_Targets): self.Exploit_Targets = Exploit_Targets
    def get_Incidents(self): return self.Incidents
    def set_Incidents(self, Incidents): self.Incidents = Incidents
    def get_Courses_Of_Action(self): return self.Courses_Of_Action
    def set_Courses_Of_Action(self, Courses_Of_Action): self.Courses_Of_Action = Courses_Of_Action
    def get_Campaigns(self): return self.Campaigns
    def set_Campaigns(self, Campaigns): self.Campaigns = Campaigns
    def get_Threat_Actors(self): return self.Threat_Actors
    def set_Threat_Actors(self, Threat_Actors): self.Threat_Actors = Threat_Actors
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def hasContent_(self):
        if (
            self.STIX_Header is not None or
            self.Observables is not None or
            self.Indicators is not None or
            self.TTPs is not None or
            self.Exploit_Targets is not None or
            self.Incidents is not None or
            self.Courses_Of_Action is not None or
            self.Campaigns is not None or
            self.Threat_Actors is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, nsmap, namespace_=XML_NS, name_='STIX_Package', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, nsmap, already_processed, namespace_, name_='STIXType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, nsmap, already_processed, namespace_=XML_NS, name_='STIXType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            outfile.write(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            outfile.write(' id=%s' % (quote_attrib(self.id), ))
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            outfile.write(' version=%s' % (quote_attrib(self.version), ))

        for ns, prefix in nsmap.iteritems():
            outfile.write(' xmlns:%s="%s"' % (prefix, ns))

    def exportChildren(self, outfile, level, nsmap, namespace_=XML_NS, name_='STIXType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.STIX_Header is not None:
            self.STIX_Header.export(outfile, level, nsmap, namespace_, name_='STIX_Header', pretty_print=pretty_print)
        if self.Observables is not None:
            self.Observables.export(outfile, level, "%s:" % (nsmap[namespace_]), name_='Observables', pretty_print=pretty_print) # no nsmap parameter, so we use this hack to pass the right namespace prefix
        if self.Indicators is not None:
            self.Indicators.export(outfile, level, nsmap, namespace_, name_='Indicators', pretty_print=pretty_print)
        if self.TTPs is not None:
            self.TTPs.export(outfile, level, nsmap, namespace_, name_='TTPs', pretty_print=pretty_print)
        if self.Exploit_Targets is not None:
            self.Exploit_Targets.export(outfile, level, nsmap, namespace_, name_='Exploit_Targets', pretty_print=pretty_print)
        if self.Incidents is not None:
            self.Incidents.export(outfile, level, nsmap, namespace_, name_='Incidents', pretty_print=pretty_print)
        if self.Courses_Of_Action is not None:
            self.Courses_Of_Action.export(outfile, level, nsmap, namespace_, name_='Courses_Of_Action', pretty_print=pretty_print)
        if self.Campaigns is not None:
            self.Campaigns.export(outfile, level, nsmap, namespace_, name_='Campaigns', pretty_print=pretty_print)
        if self.Threat_Actors is not None:
            self.Threat_Actors.export(outfile, level, nsmap, namespace_, name_='Threat_Actors', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='STIXType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            showIndent(outfile, level)
            outfile.write('idref = %s,\n' % (self.idref,))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            showIndent(outfile, level)
            outfile.write('id = %s,\n' % (self.id,))
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            showIndent(outfile, level)
            outfile.write('version = %s,\n' % (self.version,))
    def exportLiteralChildren(self, outfile, level, name_):
        if self.STIX_Header is not None:
            outfile.write('STIX_Header=model_.STIXHeaderType(\n')
            self.STIX_Header.exportLiteral(outfile, level, name_='STIX_Header')
            outfile.write('),\n')
        if self.Observables is not None:
            outfile.write('Observables=model_.cybox_core_binding.ObservablesType(\n')
            self.Observables.exportLiteral(outfile, level, name_='Observables')
            outfile.write('),\n')
        if self.Indicators is not None:
            outfile.write('Indicators=model_.IndicatorsType(\n')
            self.Indicators.exportLiteral(outfile, level, name_='Indicators')
            outfile.write('),\n')
        if self.TTPs is not None:
            outfile.write('TTPs=model_.TTPsType(\n')
            self.TTPs.exportLiteral(outfile, level, name_='TTPs')
            outfile.write('),\n')
        if self.Exploit_Targets is not None:
            outfile.write('Exploit_Targets=model_.stix_common_binding.ExploitTargetsType(\n')
            self.Exploit_Targets.exportLiteral(outfile, level, name_='Exploit_Targets')
            outfile.write('),\n')
        if self.Incidents is not None:
            outfile.write('Incidents=model_.IncidentsType(\n')
            self.Incidents.exportLiteral(outfile, level, name_='Incidents')
            outfile.write('),\n')
        if self.Courses_Of_Action is not None:
            outfile.write('Courses_Of_Action=model_.CoursesOfActionType(\n')
            self.Courses_Of_Action.exportLiteral(outfile, level, name_='Courses_Of_Action')
            outfile.write('),\n')
        if self.Campaigns is not None:
            outfile.write('Campaigns=model_.CampaignsType(\n')
            self.Campaigns.exportLiteral(outfile, level, name_='Campaigns')
            outfile.write('),\n')
        if self.Threat_Actors is not None:
            outfile.write('Threat_Actors=model_.ThreatActorsType(\n')
            self.Threat_Actors.exportLiteral(outfile, level, name_='Threat_Actors')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.nsmap = node.nsmap
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            self.idref = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'STIX_Header':
            obj_ = STIXHeaderType.factory()
            obj_.build(child_)
            self.set_STIX_Header(obj_)
        elif nodeName_ == 'Observables':
            obj_ = cybox_core_binding.ObservablesType.factory()
            obj_.build(child_)
            self.set_Observables(obj_)
        elif nodeName_ == 'Indicators':
            obj_ = IndicatorsType.factory()
            obj_.build(child_)
            self.set_Indicators(obj_)
        elif nodeName_ == 'TTPs':
            obj_ = TTPsType.factory()
            obj_.build(child_)
            self.set_TTPs(obj_)
        elif nodeName_ == 'Exploit_Targets':
            obj_ = stix_common_binding.ExploitTargetsType.factory()
            obj_.build(child_)
            self.set_Exploit_Targets(obj_)
        elif nodeName_ == 'Incidents':
            obj_ = IncidentsType.factory()
            obj_.build(child_)
            self.set_Incidents(obj_)
        elif nodeName_ == 'Courses_Of_Action':
            obj_ = CoursesOfActionType.factory()
            obj_.build(child_)
            self.set_Courses_Of_Action(obj_)
        elif nodeName_ == 'Campaigns':
            obj_ = CampaignsType.factory()
            obj_.build(child_)
            self.set_Campaigns(obj_)
        elif nodeName_ == 'Threat_Actors':
            obj_ = ThreatActorsType.factory()
            obj_.build(child_)
            self.set_Threat_Actors(obj_)
# end class STIXType

class STIXHeaderType(GeneratedsSuper):
    """The STIXHeaderType provides a structure for characterizing a package
    of STIX content."""
    subclass = None
    superclass = None
    def __init__(self, Title=None, Package_Intent=None, Description=None, Handling=None, Information_Source=None):
        self.Title = Title
        self.Package_Intent = Package_Intent
        self.Description = Description
        self.Handling = Handling
        self.Information_Source = Information_Source
    def factory(*args_, **kwargs_):
        if STIXHeaderType.subclass:
            return STIXHeaderType.subclass(*args_, **kwargs_)
        else:
            return STIXHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Package_Intent(self): return self.Package_Intent
    def set_Package_Intent(self, Package_Intent): self.Package_Intent = Package_Intent
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Handling(self): return self.Handling
    def set_Handling(self, Handling): self.Handling = Handling
    def get_Information_Source(self): return self.Information_Source
    def set_Information_Source(self, Information_Source): self.Information_Source = Information_Source
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Package_Intent is not None or
            self.Description is not None or
            self.Handling is not None or
            self.Information_Source is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, nsmap, namespace_=XML_NS, name_='STIXHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='STIXHeaderType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_=XML_NS, name_='STIXHeaderType'):
        pass
    def exportChildren(self, outfile, level, nsmap, namespace_=XML_NS, name_='STIXHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(outfile, level, pretty_print)
            outfile.write('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_], self.gds_format_string(quote_xml(self.Title).encode(ExternalEncoding), input_name='Title'), nsmap[namespace_], eol_))
        if self.Package_Intent is not None:
            self.Package_Intent.export(outfile, level, nsmap, namespace_, name_='Package_Intent', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(outfile, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Handling is not None:
            self.Handling.export(outfile, level, nsmap, namespace_, name_='Handling', pretty_print=pretty_print)
        if self.Information_Source is not None:
            self.Information_Source.export(outfile, level, nsmap, namespace_, name_='Information_Source', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='STIXHeaderType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        if self.Title is not None:
            showIndent(outfile, level)
            outfile.write('Title=%s,\n' % quote_python(self.Title).encode(ExternalEncoding))
        if self.Package_Intent is not None:
            outfile.write('Package_Intent=model_.stix_common_binding.ControlledVocabularyStringType(\n')
            self.Package_Intent.exportLiteral(outfile, level, name_='Package_Intent')
            outfile.write('),\n')
        if self.Description is not None:
            outfile.write('Description=model_.stix_common_binding.StructuredTextType(\n')
            self.Description.exportLiteral(outfile, level, name_='Description')
            outfile.write('),\n')
        if self.Handling is not None:
            outfile.write('Handling=model_.data_marking_binding.MarkingType(\n')
            self.Handling.exportLiteral(outfile, level, name_='Handling')
            outfile.write('),\n')
        if self.Information_Source is not None:
            outfile.write('Information_Source=model_.stix_common_binding.InformationSourceType(\n')
            self.Information_Source.exportLiteral(outfile, level, name_='Information_Source')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'Package_Intent':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Package_Intent(obj_)
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Handling':
            obj_ = data_marking_binding.MarkingType.factory()
            obj_.build(child_)
            self.set_Handling(obj_)
        elif nodeName_ == 'Information_Source':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Information_Source(obj_)
# end class STIXHeaderType

class IndicatorsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Indicator=None):
        if Indicator is None:
            self.Indicator = []
        else:
            self.Indicator = Indicator
    def factory(*args_, **kwargs_):
        if IndicatorsType.subclass:
            return IndicatorsType.subclass(*args_, **kwargs_)
        else:
            return IndicatorsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Indicator(self): return self.Indicator
    def set_Indicator(self, Indicator): self.Indicator = Indicator
    def add_Indicator(self, value): self.Indicator.append(value)
    def insert_Indicator(self, index, value): self.Indicator[index] = value
    def hasContent_(self):
        if (
            self.Indicator
            ):
            return True
        else:
            return False
    def export(self, outfile, level, nsmap, namespace_=XML_NS, name_='IndicatorsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IndicatorsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_=XML_NS, name_='IndicatorsType'):
        pass
    def exportChildren(self, outfile, level, nsmap, namespace_=XML_NS, name_='IndicatorsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Indicator_ in self.Indicator:
            Indicator_.export(outfile, level, nsmap, namespace_, name_='Indicator', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='IndicatorsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Indicator=[\n')
        level += 1
        for Indicator_ in self.Indicator:
            outfile.write('model_.stix_common_binding.IndicatorBaseType(\n')
            Indicator_.exportLiteral(outfile, level, name_='stix_common_binding.IndicatorBaseType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Indicator':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
            
                if type_name_ == "IndicatorType":
                    import stix.bindings.indicator as indicator_binding
                    obj_ = indicator_binding.IndicatorType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = stix_common_binding.IndicatorBaseType.factory() # not abstract
                
            obj_.build(child_)
            self.Indicator.append(obj_)
# end class IndicatorsType

class TTPsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, TTP=None, Kill_Chains=None):
        if TTP is None:
            self.TTP = []
        else:
            self.TTP = TTP
        self.Kill_Chains = Kill_Chains
    def factory(*args_, **kwargs_):
        if TTPsType.subclass:
            return TTPsType.subclass(*args_, **kwargs_)
        else:
            return TTPsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_TTP(self): return self.TTP
    def set_TTP(self, TTP): self.TTP = TTP
    def add_TTP(self, value): self.TTP.append(value)
    def insert_TTP(self, index, value): self.TTP[index] = value
    def get_Kill_Chains(self): return self.Kill_Chains
    def set_Kill_Chains(self, Kill_Chains): self.Kill_Chains = Kill_Chains
    def hasContent_(self):
        if (
            self.TTP or
            self.Kill_Chains is not None
            ):
            return True
        else:
            return False
    def export(self, outfile, level, nsmap, namespace_=XML_NS, name_='TTPsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='TTPsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_=XML_NS, name_='TTPsType'):
        pass
    def exportChildren(self, outfile, level, nsmap, namespace_=XML_NS, name_='TTPsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for TTP_ in self.TTP:
            TTP_.export(outfile, level, nsmap, namespace_, name_='TTP', pretty_print=pretty_print)
        if self.Kill_Chains is not None:
            self.Kill_Chains.export(outfile, level, nsmap, namespace_, name_='Kill_Chains', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='TTPsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('TTP=[\n')
        level += 1
        for TTP_ in self.TTP:
            outfile.write('model_.stix_common_binding.TTPBaseType(\n')
            TTP_.exportLiteral(outfile, level, name_='stix_common_binding.TTPBaseType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
        if self.Kill_Chains is not None:
            outfile.write('Kill_Chains=model_.stix_common_binding.KillChainsType(\n')
            self.Kill_Chains.exportLiteral(outfile, level, name_='Kill_Chains')
            outfile.write('),\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'TTP':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
            
                if type_name_ == "TTPType":
                    import stix.bindings.ttp as ttp_binding
                    obj_ = ttp_binding.TTPType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = stix_common_binding.TTPBaseType.factory() # not abstract
                
            obj_.build(child_)
            self.TTP.append(obj_)
        elif nodeName_ == 'Kill_Chains':
            obj_ = stix_common_binding.KillChainsType.factory()
            obj_.build(child_)
            self.set_Kill_Chains(obj_)
# end class TTPsType

class IncidentsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Incident=None):
        if Incident is None:
            self.Incident = []
        else:
            self.Incident = Incident
    def factory(*args_, **kwargs_):
        if IncidentsType.subclass:
            return IncidentsType.subclass(*args_, **kwargs_)
        else:
            return IncidentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Incident(self): return self.Incident
    def set_Incident(self, Incident): self.Incident = Incident
    def add_Incident(self, value): self.Incident.append(value)
    def insert_Incident(self, index, value): self.Incident[index] = value
    def hasContent_(self):
        if (
            self.Incident
            ):
            return True
        else:
            return False
    def export(self, outfile, level, nsmap, namespace_=XML_NS, name_='IncidentsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='IncidentsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_=XML_NS, name_='IncidentsType'):
        pass
    def exportChildren(self, outfile, level, nsmap, namespace_=XML_NS, name_='IncidentsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Incident_ in self.Incident:
            Incident_.export(outfile, level, nsmap, namespace_, name_='Incident', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='IncidentsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Incident=[\n')
        level += 1
        for Incident_ in self.Incident:
            outfile.write('model_.stix_common_binding.IncidentBaseType(\n')
            Incident_.exportLiteral(outfile, level, name_='stix_common_binding.IncidentBaseType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Incident':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
            
                if type_name_ == "IncidentType":
                    import stix.bindings.incident as incident_binding
                    obj_ = incident_binding.IncidentType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = stix_common_binding.IncidentBaseType.factory() # not abstract
                
            obj_.build(child_)
            self.Incident.append(obj_)
# end class IncidentsType

class CoursesOfActionType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Course_Of_Action=None):
        if Course_Of_Action is None:
            self.Course_Of_Action = []
        else:
            self.Course_Of_Action = Course_Of_Action
    def factory(*args_, **kwargs_):
        if CoursesOfActionType.subclass:
            return CoursesOfActionType.subclass(*args_, **kwargs_)
        else:
            return CoursesOfActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Course_Of_Action(self): return self.Course_Of_Action
    def set_Course_Of_Action(self, Course_Of_Action): self.Course_Of_Action = Course_Of_Action
    def add_Course_Of_Action(self, value): self.Course_Of_Action.append(value)
    def insert_Course_Of_Action(self, index, value): self.Course_Of_Action[index] = value
    def hasContent_(self):
        if (
            self.Course_Of_Action
            ):
            return True
        else:
            return False
    def export(self, outfile, level, nsmap, namespace_=XML_NS, name_='CoursesOfActionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CoursesOfActionType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_=XML_NS, name_='CoursesOfActionType'):
        pass
    def exportChildren(self, outfile, level, nsmap, namespace_=XML_NS, name_='CoursesOfActionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Course_Of_Action_ in self.Course_Of_Action:
            Course_Of_Action_.export(outfile, level, nsmap, namespace_, name_='Course_Of_Action', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='CoursesOfActionType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Course_Of_Action=[\n')
        level += 1
        for Course_Of_Action_ in self.Course_Of_Action:
            outfile.write('model_.stix_common_binding.CourseOfActionBaseType(\n')
            Course_Of_Action_.exportLiteral(outfile, level, name_='stix_common_binding.CourseOfActionBaseType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Course_Of_Action':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
            
                if type_name_ == "CourseOfActionType":
                    import stix.bindings.course_of_action as coa_binding
                    obj_ = coa_binding.CourseOfActionType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = stix_common_binding.CourseOfActionBaseType.factory() # not abstract
                
            obj_.build(child_)
            self.Course_Of_Action.append(obj_)
# end class CoursesOfActionType

class CampaignsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Campaign=None):
        if Campaign is None:
            self.Campaign = []
        else:
            self.Campaign = Campaign
    def factory(*args_, **kwargs_):
        if CampaignsType.subclass:
            return CampaignsType.subclass(*args_, **kwargs_)
        else:
            return CampaignsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Campaign(self): return self.Campaign
    def set_Campaign(self, Campaign): self.Campaign = Campaign
    def add_Campaign(self, value): self.Campaign.append(value)
    def insert_Campaign(self, index, value): self.Campaign[index] = value
    def hasContent_(self):
        if (
            self.Campaign
            ):
            return True
        else:
            return False
    def export(self, outfile, level, nsmap, namespace_=XML_NS, name_='CampaignsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='CampaignsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_=XML_NS, name_='CampaignsType'):
        pass
    def exportChildren(self, outfile, level, nsmap, namespace_=XML_NS, name_='CampaignsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Campaign_ in self.Campaign:
            Campaign_.export(outfile, level, nsmap, namespace_, name_='Campaign', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='CampaignsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Campaign=[\n')
        level += 1
        for Campaign_ in self.Campaign:
            outfile.write('model_.stix_common_binding.CampaignBaseType(\n')
            Campaign_.exportLiteral(outfile, level, name_='stix_common_binding.CampaignBaseType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Campaign':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
            
                if type_name_ == "CampaignType":
                    import stix.bindings.campaign as campaign_binding
                    obj_ = campaign_binding.CampaignType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = stix_common_binding.CampaignBaseType.factory() # not abstract
                
            obj_.build(child_)
            self.Campaign.append(obj_)
# end class CampaignsType

class ThreatActorsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Threat_Actor=None):
        if Threat_Actor is None:
            self.Threat_Actor = []
        else:
            self.Threat_Actor = Threat_Actor
    def factory(*args_, **kwargs_):
        if ThreatActorsType.subclass:
            return ThreatActorsType.subclass(*args_, **kwargs_)
        else:
            return ThreatActorsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Threat_Actor(self): return self.Threat_Actor
    def set_Threat_Actor(self, Threat_Actor): self.Threat_Actor = Threat_Actor
    def add_Threat_Actor(self, value): self.Threat_Actor.append(value)
    def insert_Threat_Actor(self, index, value): self.Threat_Actor[index] = value
    def hasContent_(self):
        if (
            self.Threat_Actor
            ):
            return True
        else:
            return False
    def export(self, outfile, level, nsmap, namespace_=XML_NS, name_='ThreatActorsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(outfile, level, pretty_print)
        outfile.write('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(outfile, level, already_processed, namespace_, name_='ThreatActorsType')
        if self.hasContent_():
            outfile.write('>%s' % (eol_, ))
            self.exportChildren(outfile, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(outfile, level, pretty_print)
            outfile.write('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            outfile.write('/>%s' % (eol_, ))
    def exportAttributes(self, outfile, level, already_processed, namespace_=XML_NS, name_='ThreatActorsType'):
        pass
    def exportChildren(self, outfile, level, nsmap, namespace_=XML_NS, name_='ThreatActorsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Threat_Actor_ in self.Threat_Actor:
            Threat_Actor_.export(outfile, level, nsmap, namespace_, name_='Threat_Actor', pretty_print=pretty_print)
    def exportLiteral(self, outfile, level, name_='ThreatActorsType'):
        level += 1
        already_processed = set()
        self.exportLiteralAttributes(outfile, level, already_processed, name_)
        if self.hasContent_():
            self.exportLiteralChildren(outfile, level, name_)
    def exportLiteralAttributes(self, outfile, level, already_processed, name_):
        pass
    def exportLiteralChildren(self, outfile, level, name_):
        showIndent(outfile, level)
        outfile.write('Threat_Actor=[\n')
        level += 1
        for Threat_Actor_ in self.Threat_Actor:
            outfile.write('model_.stix_common_binding.ThreatActorBaseType(\n')
            Threat_Actor_.exportLiteral(outfile, level, name_='stix_common_binding.ThreatActorBaseType')
            showIndent(outfile, level)
            outfile.write('),\n')
        level -= 1
        showIndent(outfile, level)
        outfile.write('],\n')
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Threat_Actor':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
            
                if type_name_ == "ThreatActorType":
                    import stix.bindings.threat_actor as ta_binding
                    obj_ = ta_binding.ThreatActorType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = stix_common_binding.ThreatActorBaseType.factory() # not abstract
                
            obj_.build(child_)
            self.Threat_Actor.append(obj_)
# end class ThreatActorsType

GDSClassesMapping = {
    'Information_Source': stix_common_binding.InformationSourceType,
    'Indicator': stix_common_binding.IndicatorBaseType,
    'Defined_Effect': cybox_core_binding.DefinedEffectType,
    'Exploit_Target': stix_common_binding.ExploitTargetBaseType,
    'Action': cybox_core_binding.ActionType,
    'Object': cybox_core_binding.ObjectType,
    'Incident': stix_common_binding.IncidentBaseType,
    'Information_Source_Type': stix_common_binding.ControlledVocabularyStringType,
    'Confidence_Assertion_Chain': stix_common_binding.ConfidenceAssertionChainType,
    'Observable': cybox_core_binding.ObservableType,
    'Confidence_Assertion': stix_common_binding.ConfidenceType,
    'Related_Object': cybox_core_binding.RelatedObjectType,
    'Argument_Name': stix_common_binding.ControlledVocabularyStringType,
    'Evasion_Techniques': cybox_core_binding.ObfuscationTechniquesType,
    'Old_Object': cybox_core_binding.ObjectType,
    'Campaign': stix_common_binding.CampaignBaseType,
    'Encoding': stix_common_binding.ControlledVocabularyStringType,
    'Associated_Objects': cybox_core_binding.AssociatedObjectsType,
    'Object_Pool': cybox_core_binding.ObjectPoolType,
    'Event': cybox_core_binding.EventType,
    'Source': stix_common_binding.ControlledVocabularyStringType,
    'State': stix_common_binding.ControlledVocabularyStringType,
    'Marking_Structure': data_marking_binding.MarkingStructureType,
    'Type': stix_common_binding.ControlledVocabularyStringType,
    'Tool_Type': stix_common_binding.ControlledVocabularyStringType,
    'Relationship': stix_common_binding.ControlledVocabularyStringType,
    'TTP': stix_common_binding.TTPBaseType,
    'Obfuscation_Technique': cybox_core_binding.ObfuscationTechniqueType,
    'Exploit_Targets': stix_common_binding.ExploitTargetsType,
    'Action_Pool': cybox_core_binding.ActionPoolType,
    'Properties': cybox_core_binding.PropertiesType,
    'Course_Of_Action': stix_common_binding.CourseOfActionBaseType,
    'Action_Argument': cybox_core_binding.ActionArgumentType,
    'Reference_Description': stix_common_binding.StructuredTextType,
    'Package_Intent': stix_common_binding.ControlledVocabularyStringType,
    'Association_Type': stix_common_binding.ControlledVocabularyStringType,
    'Marking': data_marking_binding.MarkingSpecificationType,
    'Associated_Object': cybox_core_binding.AssociatedObjectType,
    'Related_Objects': cybox_core_binding.RelatedObjectsType,
    'Related_Identities': stix_common_binding.RelatedIdentitiesType,
    'Observable_Composition': cybox_core_binding.ObservableCompositionType,
    'Property_Pool': cybox_core_binding.PropertyPoolType,
    'Domain_Specific_Object_Properties': cybox_core_binding.DomainSpecificObjectPropertiesType,
    'Kill_Chains': stix_common_binding.KillChainsType,
    'Identity': stix_common_binding.IdentityType,
    'Action_Reference': cybox_core_binding.ActionReferenceType,
    'Usage_Context_Assumption': stix_common_binding.StructuredTextType,
    'Pools': cybox_core_binding.PoolsType,
    'Threat_Actor': stix_common_binding.ThreatActorBaseType,
    'Event_Pool': cybox_core_binding.EventPoolType,
    'Action_Arguments': cybox_core_binding.ActionArgumentsType,
    'Frequency': cybox_core_binding.FrequencyType,
    'Keywords': cybox_core_binding.KeywordsType,
    'Pattern_Fidelity': cybox_core_binding.PatternFidelityType,
    'Confidence': stix_common_binding.ConfidenceType,
    'Kill_Chain': stix_common_binding.KillChainType,
    'Relationships': cybox_core_binding.RelationshipsType,
    'Description': stix_common_binding.StructuredTextType,
    'Action_Pertinent_Object_Properties': cybox_core_binding.ActionPertinentObjectPropertiesType,
    'Handling': data_marking_binding.MarkingType,
    'Name': stix_common_binding.ControlledVocabularyStringType,
    'Kill_Chain_Phase': stix_common_binding.KillChainPhaseReferenceType,
    'Related_Identity': stix_common_binding.RelatedIdentityType,
    'Values': cybox_core_binding.ValuesType,
    'Observables': cybox_core_binding.ObservablesType,
    'New_Object': cybox_core_binding.ObjectType,
    'Actions': cybox_core_binding.ActionsType,
    'Dependency_Description': stix_common_binding.StructuredTextType,
    'Action_Aliases': cybox_core_binding.ActionAliasesType,
}

USAGE_TEXT = """
Usage: python <Parser>.py [ -s ] <in_xml_file>
"""

def usage():
    print USAGE_TEXT
    sys.exit(1)

def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass

def parse(inFileName, nsmap=None):
    if not nsmap:
        nsmap = DEFAULT_XML_NS_MAP
        
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'STIX_Package'
        rootClass = STIXType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, nsmap, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'STIX_Package'
        rootClass = STIXType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    rootElement = rootObj.to_etree(None, name_=rootTag)
    content = etree_.tostring(rootElement, pretty_print=True,
        xml_declaration=True, encoding="utf-8")
    sys.stdout.write(content)
    sys.stdout.write('\n')
    return rootObj, rootElement

def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'STIX_Package'
        rootClass = STIXType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_="STIX_Package",
        namespacedef_='')
    return rootObj

def parseLiteral(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'STIX_Package'
        rootClass = STIXType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('#from stix_core import *\n\n')
    sys.stdout.write('from datetime import datetime as datetime_\n\n')
    sys.stdout.write('import stix_core as model_\n\n')
    sys.stdout.write('rootObj = model_.rootTag(\n')
    rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
    sys.stdout.write(')\n')
    return rootObj

def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()

if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

__all__ = [
    "STIXType",
    "STIXHeaderType",
    "IndicatorsType",
    "TTPsType",
    "IncidentsType",
    "CoursesOfActionType",
    "CampaignsType",
    "ThreatActorsType"
    ]
