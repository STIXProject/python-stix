# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:07:51 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
from stix.bindings.course_of_action import StructuredCOAType
import stix.bindings.stix_common as stix_common_binding

XML_NS = "http://stix.mitre.org/extensions/StructuredCOA#Generic-1"

#
# Data representation classes.
#

class GenericStructuredCOAType(StructuredCOAType):
    """The GenericStructuredCOAType specifies an instantial extension from
    the abstract course_of_action_binding.StructuredCOAType intended to support the generic
    inclusion of any COA content.Specifies a reference URL for the
    location of the Generic Structured COA."""
    subclass = None
    superclass = StructuredCOAType
    def __init__(self, idref=None, id=None, reference_location=None, Description=None, Type=None, Specification=None):
        super(GenericStructuredCOAType, self).__init__(idref=idref, id=id)
        self.xmlns          = XML_NS
        self.xmlns_prefix   = "genericStructuredCOA"
        self.xml_type       = "GenericStructuredCOAType"
        self.reference_location = _cast(None, reference_location)
        self.Description = Description
        self.Type = Type
        self.Specification = Specification
    def factory(*args_, **kwargs_):
        if GenericStructuredCOAType.subclass:
            return GenericStructuredCOAType.subclass(*args_, **kwargs_)
        else:
            return GenericStructuredCOAType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def get_Specification(self): return self.Specification
    def set_Specification(self, Specification): self.Specification = Specification
    def get_reference_location(self): return self.reference_location
    def set_reference_location(self, reference_location): self.reference_location = reference_location
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Type is not None or
            self.Specification is not None or
            super(GenericStructuredCOAType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='GenericStructuredCOAType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='GenericStructuredCOAType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='genericStructuredCOA:', name_='GenericStructuredCOAType'):
        super(GenericStructuredCOAType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='GenericStructuredCOAType')
        # if 'xmlns' not in already_processed:
        #     already_processed.add('xmlns')
        #     xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
        #     lwrite(xmlns)
        # if 'xsi:type' not in already_processed:
        #     already_processed.add('xsi:type')
        #     xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
        #     lwrite(xsi_type)
        if self.reference_location is not None and 'reference_location' not in already_processed:
            already_processed.add('reference_location')
            lwrite(' reference_location=%s' % (quote_attrib(self.reference_location), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='GenericStructuredCOAType', fromsubclass_=False, pretty_print=True):
        super(GenericStructuredCOAType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, nsmap, namespace_, name_='Type', pretty_print=pretty_print)
        if self.Specification is not None:
            self.Specification.export(lwrite, level, nsmap, namespace_, name_='Specification', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('reference_location', node)
        if value is not None and 'reference_location' not in already_processed:
            already_processed.add('reference_location')
            self.reference_location = value
        super(GenericStructuredCOAType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Type':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Specification':
            obj_ = stix_common_binding.EncodedCDATAType.factory()
            obj_.build(child_)
            self.set_Specification(obj_)
        super(GenericStructuredCOAType, self).buildChildren(child_, node, nodeName_, True)
# end class GenericStructuredCOAType

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
        rootTag = 'GenericStructuredCOAType'
        rootClass = GenericStructuredCOAType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    sys.stdout.write('<?xml version="1.0" ?>\n')
    rootObj.export(sys.stdout, 0, name_=rootTag,
        namespacedef_='',
        pretty_print=True)
    return rootObj


def parseString(inString):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'GenericStructuredCOAType'
        rootClass = GenericStructuredCOAType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    # doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="GenericStructuredCOAType",
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
    "GenericStructuredCOAType"
    ]
