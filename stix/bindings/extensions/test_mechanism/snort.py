# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:07:57 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import stix.bindings.indicator as indicator_binding
import stix.bindings.stix_common as stix_common_binding

XML_NS = "http://stix.mitre.org/extensions/TestMechanism#Snort-1"

#
# Data representation classes.
#

class SnortTestMechanismType(indicator_binding.TestMechanismType):
    """The SnortTestMechanismType specifies an instantial extension from
    the abstract TestMechanismType intended to support the inclusion
    of a Snort rule as a test mechanism content."""
    subclass = None
    superclass = indicator_binding.TestMechanismType
    def __init__(self, idref=None, id=None, Efficacy=None, Producer=None, Product_Name=None, Version=None, Rule=None, Event_Filter=None, Rate_Filter=None, Event_Suppression=None):
        super(SnortTestMechanismType, self).__init__(idref=idref, id=id, Efficacy=Efficacy, Producer=Producer)
        self.xmlns          = XML_NS
        self.xmlns_prefix   = "snortTM"
        self.xml_type       = "SnortTestMechanismType"
        self.Product_Name = Product_Name
        self.Version = Version
        if Rule is None:
            self.Rule = []
        else:
            self.Rule = Rule
        if Event_Filter is None:
            self.Event_Filter = []
        else:
            self.Event_Filter = Event_Filter
        if Rate_Filter is None:
            self.Rate_Filter = []
        else:
            self.Rate_Filter = Rate_Filter
        if Event_Suppression is None:
            self.Event_Suppression = []
        else:
            self.Event_Suppression = Event_Suppression
    def factory(*args_, **kwargs_):
        if SnortTestMechanismType.subclass:
            return SnortTestMechanismType.subclass(*args_, **kwargs_)
        else:
            return SnortTestMechanismType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Product_Name(self): return self.Product_Name
    def set_Product_Name(self, Product_Name): self.Product_Name = Product_Name
    def get_Version(self): return self.Version
    def set_Version(self, Version): self.Version = Version
    def get_Rule(self): return self.Rule
    def set_Rule(self, Rule): self.Rule = Rule
    def add_Rule(self, value): self.Rule.append(value)
    def insert_Rule(self, index, value): self.Rule[index] = value
    def get_Event_Filter(self): return self.Event_Filter
    def set_Event_Filter(self, Event_Filter): self.Event_Filter = Event_Filter
    def add_Event_Filter(self, value): self.Event_Filter.append(value)
    def insert_Event_Filter(self, index, value): self.Event_Filter[index] = value
    def get_Rate_Filter(self): return self.Rate_Filter
    def set_Rate_Filter(self, Rate_Filter): self.Rate_Filter = Rate_Filter
    def add_Rate_Filter(self, value): self.Rate_Filter.append(value)
    def insert_Rate_Filter(self, index, value): self.Rate_Filter[index] = value
    def get_Event_Suppression(self): return self.Event_Suppression
    def set_Event_Suppression(self, Event_Suppression): self.Event_Suppression = Event_Suppression
    def add_Event_Suppression(self, value): self.Event_Suppression.append(value)
    def insert_Event_Suppression(self, index, value): self.Event_Suppression[index] = value
    def hasContent_(self):
        if (
            self.Product_Name is not None or
            self.Version is not None or
            self.Rule or
            self.Event_Filter or
            self.Rate_Filter or
            self.Event_Suppression or
            super(SnortTestMechanismType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='SnortTestMechanismType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SnortTestMechanismType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='snortTM:', name_='SnortTestMechanismType'):
        super(SnortTestMechanismType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SnortTestMechanismType')
        # if 'xmlns' not in already_processed:
        #     already_processed.add('xmlns')
        #     xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
        #     lwrite(xmlns)
        # if 'xsi:type' not in already_processed:
        #     already_processed.add('xsi:type')
        #     xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
        #     lwrite(xsi_type)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='SnortTestMechanismType', fromsubclass_=False, pretty_print=True):
        super(SnortTestMechanismType, self).exportChildren(lwrite, level, nsmap, indicator_binding.XML_NS, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Product_Name is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Product_Name>%s</%s:Product_Name>%s' % (nsmap[namespace_], quote_xml(self.Product_Name), nsmap[namespace_], eol_))
        if self.Version is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Version>%s</%s:Version>%s' % (nsmap[namespace_], quote_xml(self.Version), nsmap[namespace_], eol_))
        for Rule_ in self.Rule:
            Rule_.export(lwrite, level, nsmap, namespace_, name_='Rule', pretty_print=pretty_print)
        for Event_Filter_ in self.Event_Filter:
            Event_Filter_.export(lwrite, level, nsmap, namespace_, name_='Event_Filter', pretty_print=pretty_print)
        for Rate_Filter_ in self.Rate_Filter:
            Rate_Filter_.export(lwrite, level, nsmap, namespace_, name_='Rate_Filter', pretty_print=pretty_print)
        for Event_Suppression_ in self.Event_Suppression:
            Event_Suppression_.export(lwrite, level, nsmap, namespace_, name_='Event_Suppression', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(SnortTestMechanismType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Product_Name':
            Product_Name_ = child_.text
            Product_Name_ = self.gds_validate_string(Product_Name_, node, 'Product_Name')
            self.Product_Name = Product_Name_
        elif nodeName_ == 'Version':
            Version_ = child_.text
            Version_ = self.gds_validate_string(Version_, node, 'Version')
            self.Version = Version_
        elif nodeName_ == 'Rule':
            obj_ = stix_common_binding.EncodedCDATAType.factory()
            obj_.build(child_)
            self.Rule.append(obj_)
        elif nodeName_ == 'Event_Filter':
            obj_ = stix_common_binding.EncodedCDATAType.factory()
            obj_.build(child_)
            self.Event_Filter.append(obj_)
        elif nodeName_ == 'Rate_Filter':
            obj_ = stix_common_binding.EncodedCDATAType.factory()
            obj_.build(child_)
            self.Rate_Filter.append(obj_)
        elif nodeName_ == 'Event_Suppression':
            obj_ = stix_common_binding.EncodedCDATAType.factory()
            obj_.build(child_)
            self.Event_Suppression.append(obj_)
        super(SnortTestMechanismType, self).buildChildren(child_, node, nodeName_, True)
# end class SnortTestMechanismType




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
        rootTag = 'SnortTestMechanismType'
        rootClass = SnortTestMechanismType
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
        rootTag = 'SnortTestMechanismType'
        rootClass = SnortTestMechanismType
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
        rootTag = 'SnortTestMechanismType'
        rootClass = SnortTestMechanismType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="Indicator",
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
    "SnortTestMechanismType"
    ]
