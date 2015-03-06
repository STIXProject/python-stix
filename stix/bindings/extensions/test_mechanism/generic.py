# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:07:52 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import stix.bindings.indicator as indicator_binding
import stix.bindings.stix_common as stix_common_binding

XML_NS = "http://stix.mitre.org/extensions/TestMechanism#Generic-1"

#
# Data representation classes.
#

class GenericTestMechanismType(indicator_binding.TestMechanismType):
    """The GenericTestMechanismType specifies an instantial extension from
    the abstract indicator_binding.TestMechanismType intended to support the generic
    inclusion of any test mechanism content.Specifies a reference
    URL for the location of the Generic Test Mechanism."""
    subclass = None
    superclass = indicator_binding.TestMechanismType
    def __init__(self, idref=None, id=None, Efficacy=None, Producer=None, reference_location=None, Description=None, Type=None, Specification=None):
        super(GenericTestMechanismType, self).__init__(idref=idref, id=id, Efficacy=Efficacy, Producer=Producer)
        self.xmlns          = XML_NS
        self.xmlns_prefix   = "genericTM"
        self.xml_type       = "GenericTestMechanismType"
        self.reference_location = _cast(None, reference_location)
        self.Description = Description
        self.Type = Type
        self.Specification = Specification
    def factory(*args_, **kwargs_):
        if GenericTestMechanismType.subclass:
            return GenericTestMechanismType.subclass(*args_, **kwargs_)
        else:
            return GenericTestMechanismType(*args_, **kwargs_)
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
            super(GenericTestMechanismType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='GenericTestMechanismType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='GenericTestMechanismType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='genericTM:', name_='GenericTestMechanismType'):
        super(GenericTestMechanismType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='GenericTestMechanismType')
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
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='GenericTestMechanismType', fromsubclass_=False, pretty_print=True):
        super(GenericTestMechanismType, self).exportChildren(lwrite, level, nsmap, indicator_binding.XML_NS, name_, True, pretty_print=pretty_print)
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
        super(GenericTestMechanismType, self).buildAttributes(node, attrs, already_processed)
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
        super(GenericTestMechanismType, self).buildChildren(child_, node, nodeName_, True)
# end class GenericTestMechanismType

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
        rootTag = 'GenericTestMechanismType'
        rootClass = GenericTestMechanismType
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
        rootTag = 'GenericTestMechanismType'
        rootClass = GenericTestMechanismType
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
        rootTag = 'GenericTestMechanismType'
        rootClass = GenericTestMechanismType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="GenericTestMechanismType",
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
    "GenericTestMechanismType"
    ]
