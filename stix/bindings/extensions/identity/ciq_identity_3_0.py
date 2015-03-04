# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:07:45 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import stix.bindings.stix_common as stix_common_binding

XML_NS = "http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1"

#
# Data representation classes.
#

class CIQIdentity3_0InstanceType(stix_common_binding.IdentityType):
    """The CIQIdentity3.0InstanceType provides an extension to the
    IdentityStructureAbstractType which imports and leverages
    version 3.0 of the OASIS CIQ-PIL schema for structured
    characterization of Identities."""
    subclass = None
    superclass = stix_common_binding.IdentityType
    def __init__(self, idref=None, id=None, Name=None, Related_Identities=None, Specification=None, Role=None):
        super(CIQIdentity3_0InstanceType, self).__init__(idref=idref, id=id, Name=Name, Related_Identities=Related_Identities)
        self.xmlns          = XML_NS
        self.xmlns_prefix   = "stix-ciqidentity"
        self.xml_type       = "CIQIdentity3.0InstanceType"
        self.xsi_type       = None
        self.Specification = Specification
        if Role is None:
            self.Role = []
        else:
            self.Role = Role
    def factory(*args_, **kwargs_):
        if CIQIdentity3_0InstanceType.subclass:
            return CIQIdentity3_0InstanceType.subclass(*args_, **kwargs_)
        else:
            return CIQIdentity3_0InstanceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Specification(self): return self.Specification
    def set_Specification(self, Specification): self.Specification = Specification
    def get_Role(self): return self.Role
    def set_Role(self, Role): self.Role = Role
    def add_Role(self, value): self.Role.append(value)
    def insert_Role(self, index, value): self.Role[index] = value
    def hasContent_(self):
        if (
            self.Specification is not None or
            self.Role or
            super(CIQIdentity3_0InstanceType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CIQIdentity3.0InstanceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CIQIdentity3.0InstanceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='', name_='CIQIdentity3.0InstanceType'):
        super(CIQIdentity3_0InstanceType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='CIQIdentity3.0InstanceType')
#         if 'xmlns' not in already_processed:
#             already_processed.add('xmlns')
#             xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
#             lwrite(xmlns)
#         if 'xsi:type' not in already_processed:
#             already_processed.add('xsi:type')
#             xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
#             lwrite(xsi_type)
        if self.xsi_type is not None:
            lwrite(' xsi:type=%s' % quote_attrib(self.xsi_type))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CIQIdentity3.0InstanceType', fromsubclass_=False, pretty_print=True):
        super(CIQIdentity3_0InstanceType, self).exportChildren(lwrite, level, nsmap, stix_common_binding.XML_NS, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Specification is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite(etree_.tostring(self.Specification, pretty_print=pretty_print))
            #self.Specification.export(lwrite, level, nsmap, namespace_, name_='Specification', pretty_print=pretty_print)
        for Role_ in self.Role:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Role>%s</%s:Role>%s' % (nsmap[namespace_], quote_xml(Role_), nsmap[namespace_], eol_))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(CIQIdentity3_0InstanceType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Specification':
            self.set_Specification(child_)
        elif nodeName_ == 'Role':
            Role_ = child_.text
            Role_ = self.gds_validate_string(Role_, node, 'Role')
            self.Role.append(Role_)
        super(CIQIdentity3_0InstanceType, self).buildChildren(child_, node, nodeName_, True)
# end class CIQIdentity3_0InstanceType

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
        rootTag = 'CIQIdentity3.0InstanceType'
        rootClass = CIQIdentity3_0InstanceType
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
        rootTag = 'CIQIdentity3.0InstanceType'
        rootClass = CIQIdentity3_0InstanceType
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
        rootTag = 'CIQIdentity3.0InstanceType'
        rootClass = CIQIdentity3_0InstanceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
#     sys.stdout.write('<?xml version="1.0" ?>\n')
#     rootObj.export(sys.stdout, 0, name_="CIQIdentity3.0InstanceType",
#         namespacedef_='')
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
    "STIXCIQIdentity3_0Type",
    "CIQIdentity3_0InstanceType"
    ]
