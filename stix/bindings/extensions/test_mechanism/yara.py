# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:07:58 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import stix.bindings.indicator as indicator_binding
import stix.bindings.stix_common as stix_common_binding

XML_NS = "http://stix.mitre.org/extensions/TestMechanism#YARA-1"

#
# Data representation classes.
#

class YaraTestMechanismType(indicator_binding.TestMechanismType):
    """The YaraTestMechanismType specifies an instantial extension from the
    abstract indicator_binding.TestMechanismType intended to support the inclusion of
    a YARA rule as a test mechanism content."""
    subclass = None
    superclass = indicator_binding.TestMechanismType
    def __init__(self, idref=None, id=None, Efficacy=None, Producer=None, Version=None, Rule=None):
        super(YaraTestMechanismType, self).__init__(idref=idref, id=id, Efficacy=Efficacy, Producer=Producer)
        self.xmlns          = XML_NS
        self.xmlns_prefix   = "yaraTM"
        self.xml_type       = "YaraTestMechanismType"
        self.Version = Version
        self.Rule = Rule
    def factory(*args_, **kwargs_):
        if YaraTestMechanismType.subclass:
            return YaraTestMechanismType.subclass(*args_, **kwargs_)
        else:
            return YaraTestMechanismType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def get_Rule(self): return self.Rule
    def set_Rule(self, Rule): self.Rule = Rule
    def hasContent_(self):
        if (
            self.Version is not None or
            self.Rule is not None or
            super(YaraTestMechanismType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='YaraTestMechanismType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='YaraTestMechanismType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='yaraTM:', name_='YaraTestMechanismType'):
        super(YaraTestMechanismType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='YaraTestMechanismType')
        # if 'xmlns' not in already_processed:
        #     already_processed.add('xmlns')
        #     xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
        #     lwrite(xmlns)
        # if 'xsi:type' not in already_processed:
        #     already_processed.add('xsi:type')
        #     xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
        #     lwrite(xsi_type)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='YaraTestMechanismType', fromsubclass_=False, pretty_print=True):
        super(YaraTestMechanismType, self).exportChildren(lwrite, level, nsmap, indicator_binding.XML_NS, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Version is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Version>%s</%s:Version>%s' % (nsmap[namespace_], quote_xml(self.Version), nsmap[namespace_], eol_))
        if self.Rule is not None:
            self.Rule.export(lwrite, level, nsmap, namespace_, name_='Rule', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(YaraTestMechanismType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Version':
            Version_ = child_.text
            Version_ = self.gds_validate_string(Version_, node, 'Version')
            self.Version = Version_
        elif nodeName_ == 'Rule':
            obj_ = stix_common_binding.EncodedCDATAType.factory()
            obj_.build(child_)
            self.set_Rule(obj_)
        super(YaraTestMechanismType, self).buildChildren(child_, node, nodeName_, True)
# end class YaraTestMechanismType

GDSClassesMapping = {}

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

def parse(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'YaraTestMechanismType'
        rootClass = YaraTestMechanismType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'YaraTestMechanismType'
        rootClass = YaraTestMechanismType
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
        rootTag = 'YaraTestMechanismType'
        rootClass = YaraTestMechanismType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    # doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="YaraTestMechanismType",
    #     namespacedef_='')
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
    "YaraTestMechanismType"
    ]
