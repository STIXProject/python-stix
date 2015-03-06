# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:07:54 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import stix.bindings.indicator as indicator_binding

XML_NS = "http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1"

#
# Data representation classes.
#

class OpenIOC2010TestMechanismType(indicator_binding.TestMechanismType):
    """The OpenIOC2010TestMechanismType provides an extension to the
    indicator_binding.TestMechanismType which imports and leverages the 2010 Open IOC
    schema in order to include OpenIOC elements as the test
    mechanism."""
    subclass = None
    superclass = indicator_binding.TestMechanismType
    def __init__(self, idref=None, id=None, Efficacy=None, Producer=None, ioc=None):
        super(OpenIOC2010TestMechanismType, self).__init__(idref=idref, id=id, Efficacy=Efficacy, Producer=Producer)
        self.xmlns          = XML_NS
        self.xmlns_prefix   = "stix-openioc"
        self.xml_type       = "OpenIOC2010TestMechanismType"
        self.ioc = ioc
    def factory(*args_, **kwargs_):
        if OpenIOC2010TestMechanismType.subclass:
            return OpenIOC2010TestMechanismType.subclass(*args_, **kwargs_)
        else:
            return OpenIOC2010TestMechanismType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ioc(self): return self.ioc
    def set_ioc(self, ioc): self.ioc = ioc
    def hasContent_(self):
        if (
            self.ioc is not None or
            super(OpenIOC2010TestMechanismType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='OpenIOC2010TestMechanismType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='OpenIOC2010TestMechanismType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='OpenIOC2010TestMechanismType'):
        super(OpenIOC2010TestMechanismType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='OpenIOC2010TestMechanismType')
        # if 'xmlns' not in already_processed:
        #     already_processed.add('xmlns')
        #     xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
        #     lwrite(xmlns)
        # if 'xsi:type' not in already_processed:
        #     already_processed.add('xsi:type')
        #     xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
        #     lwrite(xsi_type)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='OpenIOC2010TestMechanismType', fromsubclass_=False, pretty_print=True):
        super(OpenIOC2010TestMechanismType, self).exportChildren(lwrite, level, nsmap, indicator_binding.XML_NS, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.ioc is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite(etree_.tostring(self.ioc, pretty_print=pretty_print))
            #self.ioc.export(lwrite, level, nsmap, namespace_, name_='ioc', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(OpenIOC2010TestMechanismType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'ioc':
            self.set_ioc(child_)
        super(OpenIOC2010TestMechanismType, self).buildChildren(child_, node, nodeName_, True)
# end class OpenIOC2010TestMechanismType

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
        rootTag = 'OpenIOC2010TestMechanismType'
        rootClass = OpenIOC2010TestMechanismType
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
        rootTag = 'OpenIOC2010TestMechanismType'
        rootClass = OpenIOC2010TestMechanismType
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
        rootTag = 'OpenIOC2010TestMechanismType'
        rootClass = OpenIOC2010TestMechanismType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    # doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="OpenIOC2010TestMechanismType",
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
    "OpenIOC2010TestMechanismType"
    ]
