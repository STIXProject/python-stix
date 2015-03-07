# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:07:55 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import stix.bindings.indicator as indicator_binding

XML_NS = "http://stix.mitre.org/extensions/TestMechanism#OVAL5.10-1"

#
# Data representation classes.
#

class OVAL5_10TestMechanismType(indicator_binding.TestMechanismType):
    """The OVALTestMechanismType provides an extension to the
    indicator_binding.TestMechanismType which imports and leverages the OVAL schema in
    order to include OVAL Definitions as the test mechanism."""
    subclass = None
    superclass = indicator_binding.TestMechanismType
    def __init__(self, idref=None, id=None, Efficacy=None, Producer=None, oval_definitions=None, oval_variables=None):
        super(OVAL5_10TestMechanismType, self).__init__(idref=idref, id=id, Efficacy=Efficacy, Producer=Producer)
        self.xmlns          = XML_NS
        self.xmlns_prefix   = "ovalTM"
        self.xml_type       = "OVAL5.10TestMechanismType"
        self.oval_definitions = oval_definitions
        self.oval_variables = oval_variables
    def factory(*args_, **kwargs_):
        if OVAL5_10TestMechanismType.subclass:
            return OVAL5_10TestMechanismType.subclass(*args_, **kwargs_)
        else:
            return OVAL5_10TestMechanismType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_oval_definitions(self): return self.oval_definitions
    def set_oval_definitions(self, oval_definitions): self.oval_definitions = oval_definitions
    def get_oval_variables(self): return self.oval_variables
    def set_oval_variables(self, oval_variables): self.oval_variables = oval_variables
    def hasContent_(self):
        if (
            self.oval_definitions is not None or
            self.oval_variables is not None or
            super(OVAL5_10TestMechanismType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='OVAL5.10TestMechanismType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='OVAL5.10TestMechanismType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='OVAL5.10TestMechanismType'):
        super(OVAL5_10TestMechanismType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='OVAL5.10TestMechanismType')
        # if 'xmlns' not in already_processed:
        #     already_processed.add('xmlns')
        #     xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
        #     lwrite(xmlns)
        # if 'xsi:type' not in already_processed:
        #     already_processed.add('xsi:type')
        #     xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
        #     lwrite(xsi_type)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='OVAL5.10TestMechanismType', fromsubclass_=False, pretty_print=True):
        super(OVAL5_10TestMechanismType, self).exportChildren(lwrite, level, nsmap, indicator_binding.XML_NS, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.oval_definitions is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite(etree_.tostring(self.oval_definitions, pretty_print=pretty_print))
            #self.oval_definitions.export(lwrite, level, nsmap, namespace_, name_='oval_definitions', pretty_print=pretty_print)
        if self.oval_variables is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite(etree_.tostring(self.oval_variables, pretty_print=pretty_print))
            #self.oval_variables.export(lwrite, level, nsmap, namespace_, name_='oval_variables', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(OVAL5_10TestMechanismType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'oval_definitions':
            self.set_oval_definitions(child_)
        elif nodeName_ == 'oval_variables':
            self.set_oval_variables(child_)
        super(OVAL5_10TestMechanismType, self).buildChildren(child_, node, nodeName_, True)
# end class OVAL5_10TestMechanismType

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
        rootTag = 'OVAL5.10TestMechanismType'
        rootClass = OVAL5_10TestMechanismType
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
        rootTag = 'OVAL5.10TestMechanismType'
        rootClass = OVAL5_10TestMechanismType
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
        rootTag = 'OVAL5.10TestMechanismType'
        rootClass = OVAL5_10TestMechanismType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    # doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="OVAL5.10TestMechanismType",
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
    "OVAL5_10TestMechanismType"
    ]
