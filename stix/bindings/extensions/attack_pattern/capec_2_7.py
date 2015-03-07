# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:07:43 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import stix.bindings.ttp as ttp_binding

XML_NS = "http://stix.mitre.org/extensions/AP#CAPEC2.7-1"

#
# Data representation classes.
#

class CAPEC2_7InstanceType(ttp_binding.AttackPatternType):
    """The CAPECInstanceType provides an extension to the
    APStructureAbstractType which imports and leverages the CAPEC
    schema for structured characterization of Attack Patterns."""
    subclass = None
    superclass = ttp_binding.AttackPatternType
    def __init__(self, capec_id=None, Description=None, CAPEC=None):
        super(CAPEC2_7InstanceType, self).__init__(capec_id=capec_id, Description=Description)
        self.CAPEC = CAPEC
        self.xmlns          = XML_NS
        self.xmlns_prefix   = "capecInstance"
        self.xml_type       = "CAPEC2.7InstanceType"

    def factory(*args_, **kwargs_):
        if CAPEC2_7InstanceType.subclass:
            return CAPEC2_7InstanceType.subclass(*args_, **kwargs_)
        else:
            return CAPEC2_7InstanceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_CAPEC(self): return self.CAPEC
    def set_CAPEC(self, CAPEC): self.CAPEC = CAPEC
    def hasContent_(self):
        if (
            self.CAPEC is not None or
            super(CAPEC2_7InstanceType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CAPEC2.7InstanceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CAPEC2.7InstanceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='CAPEC2.7InstanceType'):
        super(CAPEC2_7InstanceType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='CAPEC2.7InstanceType')
        if 'xmlns' not in already_processed:
            already_processed.add('xmlns')
            xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
            lwrite(xmlns)
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            xsi_type = "  xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
            lwrite(xsi_type)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CAPEC2.7InstanceType', fromsubclass_=False, pretty_print=True):
        super(CAPEC2_7InstanceType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.CAPEC is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite(etree_.tostring(self.CAPEC, pretty_print=pretty_print))
            #self.CAPEC.export(lwrite, level, nsmap, namespace_, name_='CAPEC', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(CAPEC2_7InstanceType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'CAPEC':
            self.set_CAPEC(child_)
        super(CAPEC2_7InstanceType, self).buildChildren(child_, node, nodeName_, True)
# end class CAPEC2_6InstanceType

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
        rootTag = 'CAPEC2.7InstanceType'
        rootClass = CAPEC2_7InstanceType
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
        rootTag = 'CAPEC2.7InstanceType'
        rootClass = CAPEC2_7InstanceType
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
        rootTag = 'CAPEC2.7InstanceType'
        rootClass = CAPEC2_7InstanceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="CAPEC2.7InstanceType",
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
    "CAPEC2_6InstanceType"
    ]
