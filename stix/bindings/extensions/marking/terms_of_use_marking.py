# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:07:49 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import stix.bindings.data_marking as data_marking_binding

XML_NS = "http://data-marking.mitre.org/extensions/MarkingStructure#Terms_Of_Use-1"

#
# Data representation classes.
#

class TermsOfUseMarkingStructureType(data_marking_binding.MarkingStructureType):
    """The TermsOfUseMarkingStructureType is a basic implementation of the
    data marking schema that allows for a string statement
    describing the Terms Of Use to be associated with the data being
    marked.Nodes may be marked by multiple Terms Of Use Marking
    statements. When this occurs, all of the multiple Terms of Use
    Marking statements apply. Its up to the organization adding an
    additional Term Of User Marking statement to ensure that it's
    Terms Of Use does not conflict with any previously applied Terms
    Of Use Marking Statement.

    """
    subclass = None
    superclass = data_marking_binding.MarkingStructureType

    xmlns          = XML_NS
    xmlns_prefix   = "TOUMarking"
    xml_type       = "TermsOfUseMarkingStructureType"

    def __init__(self, idref=None, marking_model_ref=None, marking_model_name=None, id=None, Terms_Of_Use=None):
        super(TermsOfUseMarkingStructureType, self).__init__(idref=idref, marking_model_ref=marking_model_ref, marking_model_name=marking_model_name, id=id)

        self.Terms_Of_Use = Terms_Of_Use
    def factory(*args_, **kwargs_):
        if TermsOfUseMarkingStructureType.subclass:
            return TermsOfUseMarkingStructureType.subclass(*args_, **kwargs_)
        else:
            return TermsOfUseMarkingStructureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Terms_Of_Use(self): return self.Terms_Of_Use
    def set_Terms_Of_Use(self, Terms_Of_Use): self.Terms_Of_Use = Terms_Of_Use
    def hasContent_(self):
        if (
            self.Terms_Of_Use is not None or
            super(TermsOfUseMarkingStructureType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TermsOfUseMarkingStructureType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TermsOfUseMarkingStructureType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='TOUMarking:', name_='TermsOfUseMarkingStructureType'):
        super(TermsOfUseMarkingStructureType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='TermsOfUseMarkingStructureType')
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
            lwrite(xsi_type)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TermsOfUseMarkingStructureType', fromsubclass_=False, pretty_print=True):
        super(TermsOfUseMarkingStructureType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Terms_Of_Use is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Terms_Of_Use>%s</%s:Terms_Of_Use>%s' % (nsmap[namespace_], quote_xml(self.Terms_Of_Use), nsmap[namespace_], eol_))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(TermsOfUseMarkingStructureType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Terms_Of_Use':
            Terms_Of_Use_ = child_.text
            Terms_Of_Use_ = self.gds_validate_string(Terms_Of_Use_, node, 'Terms_Of_Use')
            self.Terms_Of_Use = Terms_Of_Use_
        super(TermsOfUseMarkingStructureType, self).buildChildren(child_, node, nodeName_, True)
# end class TermsOfUseMarkingStructureType

data_marking_binding.add_extension(TermsOfUseMarkingStructureType)

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
        rootTag = 'TermsOfUseMarkingStructureType'
        rootClass = TermsOfUseMarkingStructureType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_=rootTag,
    #     namespacedef_='',
    #     pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'TermsOfUseMarkingStructureType'
        rootClass = TermsOfUseMarkingStructureType
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
        rootTag = 'TermsOfUseMarkingStructureType'
        rootClass = TermsOfUseMarkingStructureType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="TermsOfUseMarkingStructureType",
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
    "TermsOfUseMarkingStructureType"
    ]
