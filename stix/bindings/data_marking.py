# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:06:22 2013 by generateDS.py version 2.9a.
#
# stdlib
import sys

# internal
from stix.bindings import *
from stix import xmlconst
from . import stix_common as stix_common_binding

XML_NS  = "http://data-marking.mitre.org/Marking-1"

#
# Data representation classes.
#


class MarkingType(GeneratedsSuper):
    """MarkingType specifies a structure for marking information to be
    applied to portions of XML content."""
    subclass = None
    superclass = None
    def __init__(self, Marking=None):
        if Marking is None:
            self.Marking = []
        else:
            self.Marking = Marking
    def factory(*args_, **kwargs_):
        if MarkingType.subclass:
            return MarkingType.subclass(*args_, **kwargs_)
        else:
            return MarkingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Marking(self): return self.Marking
    def set_Marking(self, Marking): self.Marking = Marking
    def add_Marking(self, value): self.Marking.append(value)
    def insert_Marking(self, index, value): self.Marking[index] = value
    def hasContent_(self):
        if (
            self.Marking
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='MarkingType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MarkingType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='marking:', name_='MarkingType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='MarkingType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Marking_ in self.Marking:
            Marking_.export(lwrite, level, nsmap, namespace_, name_='Marking', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Marking':
            obj_ = MarkingSpecificationType.factory()
            obj_.build(child_)
            self.Marking.append(obj_)
# end class MarkingType


class MarkingStructureType(GeneratedsSuper):
    """The MarkingStructureType contains the marking information to be
    applied to a portion of XML content.This type is defined as
    abstract and is intended to be extended to enable the expression
    of any structured or unstructured data marking mechanism. The
    data marking structure is simply a mechanism for applying
    existing marking systems to nodes. The data marking systems
    themselves define the semantics of what the markings mean, how
    multiple markings to the same node should be applied, and what
    to do if a node is unmarked.It is valid per this specification
    to mark a node with multiple markings from the same system or
    mark a node across multiple marking systems. If a node is marked
    multiple times using the same marking system, that system
    specifies the semantic meaning of multiple markings and (if
    necessary) how conflicts should be resolved. If a node is marked
    across multiple marking systems, each system is considered
    individually applicable. If there are conflicting markings
    across marking systems the behavior is undefined, therefore
    producers should make every effort to ensure documents are
    marked consistently and correctly among all marking systems.STIX
    provides two marking system extensions: Simple, and TLP. Those
    who wish to use another format may do so by defining a new
    extension to this type. The STIX-provided extensions are:1.
    Simple: The Simple marking structures allows for the
    specification of unstructured statements through the use of a
    string field. The type is named SimpleMarkingStructureType and
    is in the http://data-
    marking.mitre.org/extensions/MarkingStructure#Simple-1
    namespace. The extension is defined in the file
    extensions/marking/simple_marking.xsd or at the URL http://stix.
    mitre.org/XMLSchema/extensions/marking/simple_marking/1.1/simple
    _marking.xsd.2. TLP: The TLP marking structure allows for the
    expression of Traffic Light Protocol statements through the use
    of a simple enumeration. The type is named
    TLPMarkingStructureType and is in the http://data-
    marking.mitre.org/extensions/MarkingStructure#TLP-1 namespace.
    The extension is defined in the file
    extensions/marking/tlp_marking.xsd or at the URL http://stix.mit
    re.org/XMLSchema/extensions/marking/tlp/1.1/tlp_marking.xsd.This
    field specifies the name of the marking model to be applied
    within this Marking_Structure.This field contains a reference to
    an authoritative source on the marking model to be applied
    within this Marking_Structure.Specifies a unique ID for this
    Marking_Structure.Specifies a reference to the ID of a
    Marking_Structure defined elsewhere.When idref is specified, the
    id attribute must not be specified, and any instance of this
    Marking_Structure should not hold content."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, marking_model_ref=None, marking_model_name=None):
        self.idref = _cast(None, idref)
        self.marking_model_ref = _cast(None, marking_model_ref)
        self.marking_model_name = _cast(None, marking_model_name)
        self.id = _cast(None, id)
        pass
    def factory(*args_, **kwargs_):
        if MarkingStructureType.subclass:
            return MarkingStructureType.subclass(*args_, **kwargs_)
        else:
            return MarkingStructureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_marking_model_ref(self): return self.marking_model_ref
    def set_marking_model_ref(self, marking_model_ref): self.marking_model_ref = marking_model_ref
    def get_marking_model_name(self): return self.marking_model_name
    def set_marking_model_name(self, marking_model_name): self.marking_model_name = marking_model_name
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='MarkingStructureType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MarkingStructureType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='marking:', name_='MarkingStructureType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.marking_model_ref is not None and 'marking_model_ref' not in already_processed:
            already_processed.add('marking_model_ref')
            lwrite(' marking_model_ref=%s' % (quote_attrib(self.marking_model_ref), ))
        if self.marking_model_name is not None and 'marking_model_name' not in already_processed:
            already_processed.add('marking_model_name')
            lwrite(' marking_model_name=%s' % (quote_attrib(self.marking_model_name), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='MarkingStructureType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('idref', node)
        if value is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            self.idref = value
        value = find_attr_value_('marking_model_ref', node)
        if value is not None and 'marking_model_ref' not in already_processed:
            already_processed.add('marking_model_ref')
            self.marking_model_ref = value
        value = find_attr_value_('marking_model_name', node)
        if value is not None and 'marking_model_name' not in already_processed:
            already_processed.add('marking_model_name')
            self.marking_model_name = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class MarkingStructureType


class MarkingSpecificationType(GeneratedsSuper):
    """Specifies a unique ID for this Marking.Specifies a reference to the
    ID of a Marking defined elsewhere.Specifies the relevant
    Data_Marking schema version for this content."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, version=None, Controlled_Structure=None, Marking_Structure=None, Information_Source=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.version = _cast(None, version)
        self.Controlled_Structure = Controlled_Structure
        if Marking_Structure is None:
            self.Marking_Structure = []
        else:
            self.Marking_Structure = Marking_Structure
        self.Information_Source = Information_Source
    def factory(*args_, **kwargs_):
        if MarkingSpecificationType.subclass:
            return MarkingSpecificationType.subclass(*args_, **kwargs_)
        else:
            return MarkingSpecificationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Controlled_Structure(self): return self.Controlled_Structure
    def set_Controlled_Structure(self, Controlled_Structure): self.Controlled_Structure = Controlled_Structure
    def get_Marking_Structure(self): return self.Marking_Structure
    def set_Marking_Structure(self, Marking_Structure): self.Marking_Structure = Marking_Structure
    def add_Marking_Structure(self, value): self.Marking_Structure.append(value)
    def insert_Marking_Structure(self, index, value): self.Marking_Structure[index] = value
    def get_Information_Source(self): return self.Information_Source
    def set_Information_Source(self, Information_Source): self.Information_Source = Information_Source
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def hasContent_(self):
        if (
            self.Controlled_Structure is not None or
            self.Marking_Structure or
            self.Information_Source is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='MarkingSpecificationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MarkingSpecificationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='marking:', name_='MarkingSpecificationType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            lwrite(' version=%s' % (quote_attrib(self.version), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='MarkingSpecificationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Controlled_Structure is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Controlled_Structure>%s</%s:Controlled_Structure>%s' % (nsmap[namespace_], quote_xml(self.Controlled_Structure), nsmap[namespace_], eol_))
        for Marking_Structure_ in self.get_Marking_Structure():
            Marking_Structure_.export(lwrite, level, nsmap, namespace_, name_='Marking_Structure', pretty_print=pretty_print)
        if self.Information_Source is not None:
            self.Information_Source.export(lwrite, level, nsmap, namespace_, name_='Information_Source', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
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
        if nodeName_ == 'Controlled_Structure':
            Controlled_Structure_ = child_.text
            Controlled_Structure_ = self.gds_validate_string(Controlled_Structure_, node, 'Controlled_Structure')
            self.Controlled_Structure = Controlled_Structure_
        elif nodeName_ == 'Marking_Structure':

            from .extensions.marking import simple_marking
            from .extensions.marking import tlp
            from .extensions.marking import terms_of_use_marking

            # Look for xsi:type. If not there, build an instance of
            # MarkingStructureType
            if xmlconst.TAG_XSI_TYPE not in child_.attrib:
                ref = MarkingStructureType.factory()
                ref.build(child_)
                self.Marking_Structure.append(ref)
                return

            # Extract the xsi:type associated type namespace and type name
            typeinfo = get_type_info(child_)

            if typeinfo not in _EXTENSION_MAP:
                raise NotImplementedError('Marking structure type not implemented ' + typeinfo.typename)

            klass = _EXTENSION_MAP[typeinfo]
            obj_ = klass.factory()
            obj_.build(child_)
            self.Marking_Structure.append(obj_)

        elif nodeName_ == 'Information_Source':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Information_Source(obj_)
# end class MarkingSpecificationType


_EXTENSION_MAP = {}

def add_extension(klass):
    typeinfo = TypeInfo(ns=klass.xmlns, typename=klass.xml_type)
    _EXTENSION_MAP[typeinfo] = klass


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
        rootTag = 'MarkingType'
        rootClass = MarkingType
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
        rootTag = 'MarkingType'
        rootClass = MarkingType
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
        rootTag = 'MarkingType'
        rootClass = MarkingType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="MarkingType",
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
    "MarkingType",
    "MarkingStructureType",
    "MarkingSpecificationType",
    "ExtensionMap",
    "add_extension"
]
