#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#
# Generated Thu Apr 11 15:06:30 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import cybox.bindings.cybox_core as cybox_core_binding
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.data_marking as data_marking_binding

XML_NS = "http://stix.mitre.org/TTP-1"

#
# Data representation classes.
#

class AttackPatternType(GeneratedsSuper):
    """Captures prose information about an individual attack pattern as
    well as a CAPEC reference.In addition to capturing basic
    information, this type is intended to be extended to enable the
    structured description of an attack pattern instance using the
    XML Schema extension feature. The STIX default extension uses
    the Common Attack Pattern Enumeration and Classification (CAPEC)
    schema to do so. The extension that defines this is captured in
    the CAPEC2.7InstanceType in the
    http://stix.mitre.org/extensions/AP#CAPEC2.7-1 namespace. This
    type is defined in the
    extensions/attack_pattern/capec_2.7_attack_pattern.xsd file or
    at the URL http://stix.mitre.org/XMLSchema/extensions/attack_pat
    tern/capec_2.7/1.0/capec_2.7_attack_pattern.xsd.Specifies a
    unique ID for this Attack Pattern.Specifies a reference to the
    ID for this Attack Pattern specified elsewhere.This field
    specifies a reference to a particular entry within the Common
    Attack Pattern Enumeration and Classification (CAPEC)"""
    subclass =       None
    superclass = None
    def __init__(self, idref=None, capec_id=None, id=None, Title=None, Description=None, Short_Description=None):
        self.idref = _cast(None, idref)
        self.capec_id = _cast(None, capec_id)
        self.id = _cast(None, id)
        self.Title = Title
        self.Description = Description
        self.Short_Description = Short_Description
    def factory(*args_, **kwargs_):
        if AttackPatternType.subclass:
            return AttackPatternType.subclass(*args_, **kwargs_)
        else:
            return AttackPatternType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_capec_id(self): return self.capec_id
    def set_capec_id(self, capec_id): self.capec_id = capec_id
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Description is not None or
            self.Short_Description is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AttackPatternType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AttackPatternType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='AttackPatternType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.capec_id is not None and 'capec_id' not in already_processed:
            already_processed.add('capec_id')
            lwrite(' capec_id=%s' % (quote_attrib(self.capec_id), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AttackPatternType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_], quote_xml(self.Title), nsmap[namespace_], eol_))
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Short_Description is not None:
            self.Short_Description.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
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
        value = find_attr_value_('capec_id', node)
        if value is not None and 'capec_id' not in already_processed:
            already_processed.add('capec_id')
            self.capec_id = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Short_Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Short_Description(obj_)
# end class AttackPatternType


class MalwareInstanceType(GeneratedsSuper):
    """Captures basic information about an individual malware instance.In
    addition to capturing basic information, this type is intended
    to be extended to enable the structured description of a malware
    instance using the XML Schema extension feature. The STIX
    default extension uses the Malware Attribute Enumeration and
    Classification (MAEC) schema to do so. The extension that
    defines this is captured in the MAEC4.1InstanceType in the
    http://stix.mitre.org/extensions/Malware#MAEC4.1-1 namespace.
    This type is defined in the
    extensions/malware/maec_4.1_malware.xsd file or at the URL http:
    //stix.mitre.org/XMLSchema/extensions/malware/maec_4.1/1.0/maec_
    4.1_malware.xsd.Specifies a unique ID for this Malware
    Instance.Specifies a reference to the ID for this Malware
    Instance specified elsewhere."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, Type=None, Name=None, Title=None, Description=None, Short_Description=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        if Type is None:
            self.Type = []
        else:
            self.Type = Type
        if Name is None:
            self.Name = []
        else:
            self.Name = Name
        self.Title = Title
        self.Description = Description
        self.Short_Description = Short_Description
    def factory(*args_, **kwargs_):
        if MalwareInstanceType.subclass:
            return MalwareInstanceType.subclass(*args_, **kwargs_)
        else:
            return MalwareInstanceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def add_Type(self, value): self.Type.append(value)
    def insert_Type(self, index, value): self.Type[index] = value
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def add_Name(self, value): self.Name.append(value)
    def insert_Name(self, index, value): self.Name[index] = value
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.Type or
            self.Name or
            self.Title is not None or
            self.Description is not None or
            self.Short_Description is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='MalwareInstanceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MalwareInstanceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='MalwareInstanceType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='MalwareInstanceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Type_ in self.Type:
            Type_.export(lwrite, level, nsmap, namespace_, name_='Type', pretty_print=pretty_print)
        for Name_ in self.Name:
            Name_.export(lwrite, level, nsmap, namespace_, name_='Name', pretty_print=pretty_print)
        if self.Title is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_], quote_xml(self.Title), nsmap[namespace_], eol_))
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Short_Description is not None:
            self.Short_Description.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
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
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Type':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Type.append(obj_)
        elif nodeName_ == 'Name':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Name.append(obj_)
        elif nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Short_Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Short_Description(obj_)
# end class MalwareInstanceType

class ExploitType(GeneratedsSuper):
    """Characterizes a description of an individual exploit.In addition to
    capturing basic information, this type is intended to be
    extended to enable the structured description of an exploit
    using the XML Schema extension feature. No extension is provided
    by STIX to support this, however those wishing to represent
    structured exploit information may develop such an
    extension.Specifies a unique ID for this Exploit
    Instance.Specifies a reference to the ID for this Exploit
    Instance specified elsewhere."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, Title=None, Description=None, Short_Description=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.Title = Title
        self.Description = Description
        self.Short_Description = Short_Description
    def factory(*args_, **kwargs_):
        if ExploitType.subclass:
            return ExploitType.subclass(*args_, **kwargs_)
        else:
            return ExploitType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Description is not None or
            self.Short_Description is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExploitType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ExploitType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='ExploitType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExploitType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_], quote_xml(self.Title), nsmap[namespace_], eol_))
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Short_Description is not None:
            self.Short_Description.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
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
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Short_Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Short_Description(obj_)
# end class ExploitType


class InfrastructureType(GeneratedsSuper):
    """Specifies a unique ID for this class or instance of
    Infrastructure.Specifies a reference to the ID for this class or
    instance of Infrastructure specified elsewhere."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, Title=None, Type=None, Description=None, Short_Description=None, Observable_Characterization=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.Title = Title
        if Type is None:
            self.Type = []
        else:
            self.Type = Type
        self.Description = Description
        self.Short_Description = Short_Description
        self.Observable_Characterization = Observable_Characterization
    def factory(*args_, **kwargs_):
        if InfrastructureType.subclass:
            return InfrastructureType.subclass(*args_, **kwargs_)
        else:
            return InfrastructureType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def add_Type(self, value): self.Type.append(value)
    def insert_Type(self, index, value): self.Type[index] = value
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_Observable_Characterization(self): return self.Observable_Characterization
    def set_Observable_Characterization(self, Observable_Characterization): self.Observable_Characterization = Observable_Characterization
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Type or
            self.Description is not None or
            self.Short_Description is not None or
            self.Observable_Characterization is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='InfrastructureType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='InfrastructureType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='InfrastructureType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='InfrastructureType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_], quote_xml(self.Title), nsmap[namespace_], eol_))
        for Type_ in self.Type:
            Type_.export(lwrite, level, nsmap, namespace_, name_='Type', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Short_Description is not None:
            self.Short_Description.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
        if self.Observable_Characterization is not None:
            self.Observable_Characterization.export(lwrite, level, "%s:" % (nsmap[namespace_]), name_='Observable_Characterization', pretty_print=pretty_print)
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
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'Type':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Type.append(obj_)
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Short_Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Short_Description(obj_)
        elif nodeName_ == 'Observable_Characterization':
            obj_ = cybox_core_binding.ObservablesType.factory()
            obj_.build(child_)
            self.set_Observable_Characterization(obj_)
# end class InfrastructureType


class ToolsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Tool=None):
        if Tool is None:
            self.Tool = []
        else:
            self.Tool = Tool
    def factory(*args_, **kwargs_):
        if ToolsType.subclass:
            return ToolsType.subclass(*args_, **kwargs_)
        else:
            return ToolsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Tool(self): return self.Tool
    def set_Tool(self, Tool): self.Tool = Tool
    def add_Tool(self, value): self.Tool.append(value)
    def insert_Tool(self, index, value): self.Tool[index] = value
    def hasContent_(self):
        if (
            self.Tool
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ToolsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ToolsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='ToolsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ToolsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Tool_ in self.Tool:
            Tool_.export(lwrite, level, nsmap, namespace_, name_='Tool', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Tool':
            obj_ = stix_common_binding.ToolInformationType.factory()
            obj_.build(child_)
            self.Tool.append(obj_)
# end class ToolsType

class ExploitsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Exploit=None):
        if Exploit is None:
            self.Exploit = []
        else:
            self.Exploit = Exploit
    def factory(*args_, **kwargs_):
        if ExploitsType.subclass:
            return ExploitsType.subclass(*args_, **kwargs_)
        else:
            return ExploitsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Exploit(self): return self.Exploit
    def set_Exploit(self, Exploit): self.Exploit = Exploit
    def add_Exploit(self, value): self.Exploit.append(value)
    def insert_Exploit(self, index, value): self.Exploit[index] = value
    def hasContent_(self):
        if (
            self.Exploit
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExploitsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ExploitsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='ExploitsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExploitsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Exploit_ in self.Exploit:
            Exploit_.export(lwrite, level, nsmap, namespace_, name_='Exploit', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Exploit':
            obj_ = ExploitType.factory()
            obj_.build(child_)
            self.Exploit.append(obj_)
# end class ExploitsType

class MalwareType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Malware_Instance=None):
        if Malware_Instance is None:
            self.Malware_Instance = []
        else:
            self.Malware_Instance = Malware_Instance
    def factory(*args_, **kwargs_):
        if MalwareType.subclass:
            return MalwareType.subclass(*args_, **kwargs_)
        else:
            return MalwareType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Malware_Instance(self): return self.Malware_Instance
    def set_Malware_Instance(self, Malware_Instance): self.Malware_Instance = Malware_Instance
    def add_Malware_Instance(self, value): self.Malware_Instance.append(value)
    def insert_Malware_Instance(self, index, value): self.Malware_Instance[index] = value
    def hasContent_(self):
        if (
            self.Malware_Instance
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='MalwareType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='MalwareType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='MalwareType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='MalwareType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Malware_Instance_ in self.Malware_Instance:
            Malware_Instance_.export(lwrite, level, nsmap, namespace_, name_='Malware_Instance', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Malware_Instance':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "MAEC4.1InstanceType":
                    from .extensions.malware import maec_4_1
                    obj_ = maec_4_1.MAEC4_1InstanceType.factory()
            else:
                obj_ = MalwareInstanceType.factory() # MalwareInstanceType is not abstract

            obj_.build(child_)
            self.Malware_Instance.append(obj_)
# end class MalwareType

class AttackPatternsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Attack_Pattern=None):
        if Attack_Pattern is None:
            self.Attack_Pattern = []
        else:
            self.Attack_Pattern = Attack_Pattern
    def factory(*args_, **kwargs_):
        if AttackPatternsType.subclass:
            return AttackPatternsType.subclass(*args_, **kwargs_)
        else:
            return AttackPatternsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attack_Pattern(self): return self.Attack_Pattern
    def set_Attack_Pattern(self, Attack_Pattern): self.Attack_Pattern = Attack_Pattern
    def add_Attack_Pattern(self, value): self.Attack_Pattern.append(value)
    def insert_Attack_Pattern(self, index, value): self.Attack_Pattern[index] = value
    def hasContent_(self):
        if (
            self.Attack_Pattern
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AttackPatternsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AttackPatternsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='AttackPatternsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AttackPatternsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Attack_Pattern_ in self.Attack_Pattern:
            Attack_Pattern_.export(lwrite, level, nsmap, namespace_, name_='Attack_Pattern', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Attack_Pattern':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "CAPEC2.7InstanceType":
                    from .extensions.attack_pattern import capec_2_7
                    obj_ = capec_2_7.CAPEC2_7InstanceType.factory()
                else:
                    raise NotImplementedError('No implementation for type: ' + type_name_)
            else:
                obj_ = AttackPatternType.factory() # AttackPattern is not abstract

            obj_.build(child_)
            self.Attack_Pattern.append(obj_)
# end class AttackPatternsType

class ResourceType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Tools=None, Infrastructure=None, Personas=None):
        self.Tools = Tools
        self.Infrastructure = Infrastructure
        self.Personas = Personas
    def factory(*args_, **kwargs_):
        if ResourceType.subclass:
            return ResourceType.subclass(*args_, **kwargs_)
        else:
            return ResourceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Tools(self): return self.Tools
    def set_Tools(self, Tools): self.Tools = Tools
    def get_Infrastructure(self): return self.Infrastructure
    def set_Infrastructure(self, Infrastructure): self.Infrastructure = Infrastructure
    def get_Personas(self): return self.Personas
    def set_Personas(self, Personas): self.Personas = Personas
    def hasContent_(self):
        if (
            self.Tools is not None or
            self.Infrastructure is not None or
            self.Personas is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ResourceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ResourceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='ResourceType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ResourceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Tools is not None:
            self.Tools.export(lwrite, level, nsmap, namespace_, name_='Tools', pretty_print=pretty_print)
        if self.Infrastructure is not None:
            self.Infrastructure.export(lwrite, level, nsmap, namespace_, name_='Infrastructure', pretty_print=pretty_print)
        if self.Personas is not None:
            self.Personas.export(lwrite, level, nsmap, namespace_, name_='Personas', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Tools':
            obj_ = ToolsType.factory()
            obj_.build(child_)
            self.set_Tools(obj_)
        elif nodeName_ == 'Infrastructure':
            obj_ = InfrastructureType.factory()
            obj_.build(child_)
            self.set_Infrastructure(obj_)
        elif nodeName_ == 'Personas':
            obj_ = PersonasType.factory()
            obj_.build(child_)
            self.set_Personas(obj_)
# end class ResourceType

class PersonasType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Persona=None):
        if Persona is None:
            self.Persona = []
        else:
            self.Persona = Persona
    def factory(*args_, **kwargs_):
        if PersonasType.subclass:
            return PersonasType.subclass(*args_, **kwargs_)
        else:
            return PersonasType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Persona(self): return self.Persona
    def set_Persona(self, Persona): self.Persona = Persona
    def add_Persona(self, value): self.Persona.append(value)
    def insert_Persona(self, index, value): self.Persona[index] = value
    def hasContent_(self):
        if (
            self.Persona
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='PersonasType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PersonasType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='PersonasType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='PersonasType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Persona_ in self.Persona:
            Persona_.export(lwrite, level, nsmap, namespace_, name_='Persona', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Persona':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "CIQIdentity3.0InstanceType":
                    from .extensions.identity import ciq_identity_3_0
                    obj_ = ciq_identity_3_0.CIQIdentity3_0InstanceType.factory()
            else:
                obj_ = stix_common_binding.IdentityType.factory() # IdentityType is not abstract

            obj_.build(child_)
            self.Persona.append(obj_)
# end class PersonasType

class BehaviorType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Attack_Patterns=None, Malware=None, Exploits=None):
        self.Attack_Patterns = Attack_Patterns
        self.Malware = Malware
        self.Exploits = Exploits
    def factory(*args_, **kwargs_):
        if BehaviorType.subclass:
            return BehaviorType.subclass(*args_, **kwargs_)
        else:
            return BehaviorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attack_Patterns(self): return self.Attack_Patterns
    def set_Attack_Patterns(self, Attack_Patterns): self.Attack_Patterns = Attack_Patterns
    def get_Malware(self): return self.Malware
    def set_Malware(self, Malware): self.Malware = Malware
    def get_Exploits(self): return self.Exploits
    def set_Exploits(self, Exploits): self.Exploits = Exploits
    def hasContent_(self):
        if (
            self.Attack_Patterns is not None or
            self.Malware is not None or
            self.Exploits is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='BehaviorType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='BehaviorType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='BehaviorType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='BehaviorType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Attack_Patterns is not None:
            self.Attack_Patterns.export(lwrite, level, nsmap, namespace_, name_='Attack_Patterns', pretty_print=pretty_print)
        if self.Malware is not None:
            self.Malware.export(lwrite, level, nsmap, namespace_, name_='Malware', pretty_print=pretty_print)
        if self.Exploits is not None:
            self.Exploits.export(lwrite, level, nsmap, namespace_, name_='Exploits', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Attack_Patterns':
            obj_ = AttackPatternsType.factory()
            obj_.build(child_)
            self.set_Attack_Patterns(obj_)
        elif nodeName_ == 'Malware':
            obj_ = MalwareType.factory()
            obj_.build(child_)
            self.set_Malware(obj_)
        elif nodeName_ == 'Exploits':
            obj_ = ExploitsType.factory()
            obj_.build(child_)
            self.set_Exploits(obj_)
# end class BehaviorType

class VictimTargetingType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Identity=None, Targeted_Systems=None, Targeted_Information=None, Targeted_Technical_Details=None):
        self.Identity = Identity
        if Targeted_Systems is None:
            self.Targeted_Systems = []
        else:
            self.Targeted_Systems = Targeted_Systems
        if Targeted_Information is None:
            self.Targeted_Information = []
        else:
            self.Targeted_Information = Targeted_Information
        self.Targeted_Technical_Details = Targeted_Technical_Details
    def factory(*args_, **kwargs_):
        if VictimTargetingType.subclass:
            return VictimTargetingType.subclass(*args_, **kwargs_)
        else:
            return VictimTargetingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Identity(self): return self.Identity
    def set_Identity(self, Identity): self.Identity = Identity
    def get_Targeted_Systems(self): return self.Targeted_Systems
    def set_Targeted_Systems(self, Targeted_Systems): self.Targeted_Systems = Targeted_Systems
    def add_Targeted_Systems(self, value): self.Targeted_Systems.append(value)
    def insert_Targeted_Systems(self, index, value): self.Targeted_Systems[index] = value
    def get_Targeted_Information(self): return self.Targeted_Information
    def set_Targeted_Information(self, Targeted_Information): self.Targeted_Information = Targeted_Information
    def add_Targeted_Information(self, value): self.Targeted_Information.append(value)
    def insert_Targeted_Information(self, index, value): self.Targeted_Information[index] = value
    def get_Targeted_Technical_Details(self): return self.Targeted_Technical_Details
    def set_Targeted_Technical_Details(self, Targeted_Technical_Details): self.Targeted_Technical_Details = Targeted_Technical_Details
    def hasContent_(self):
        if (
            self.Identity is not None or
            self.Targeted_Systems or
            self.Targeted_Information or
            self.Targeted_Technical_Details is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='VictimTargetingType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='VictimTargetingType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='VictimTargetingType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='VictimTargetingType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Identity is not None:
            self.Identity.export(lwrite, level, nsmap, namespace_, name_='Identity', pretty_print=pretty_print)
        for Targeted_Systems_ in self.Targeted_Systems:
            Targeted_Systems_.export(lwrite, level, nsmap, namespace_, name_='Targeted_Systems', pretty_print=pretty_print)
        for Targeted_Information_ in self.Targeted_Information:
            Targeted_Information_.export(lwrite, level, nsmap, namespace_, name_='Targeted_Information', pretty_print=pretty_print)
        if self.Targeted_Technical_Details is not None:
            self.Targeted_Technical_Details.export(lwrite, level, "%s:" % (nsmap[namespace_]), name_='Targeted_Technical_Details', pretty_print=pretty_print)

    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Identity':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "CIQIdentity3.0InstanceType":
                    from .extensions.identity import ciq_identity_3_0
                    obj_ = ciq_identity_3_0.CIQIdentity3_0InstanceType.factory()
            else:
                obj_ = stix_common_binding.IdentityType.factory() # IdentityType is not abstract

            obj_.build(child_)
            self.set_Identity(obj_)
        elif nodeName_ == 'Targeted_Systems':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Targeted_Systems.append(obj_)
        elif nodeName_ == 'Targeted_Information':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Targeted_Information.append(obj_)
        elif nodeName_ == 'Targeted_Technical_Details':
            obj_ = cybox_core_binding.ObservablesType.factory()
            obj_.build(child_)
            self.set_Targeted_Technical_Details(obj_)
# end class VictimTargetingType

class RelatedTTPsType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Related_TTP=None):
        super(RelatedTTPsType, self).__init__(scope=scope)
        if Related_TTP is None:
            self.Related_TTP = []
        else:
            self.Related_TTP = Related_TTP
    def factory(*args_, **kwargs_):
        if RelatedTTPsType.subclass:
            return RelatedTTPsType.subclass(*args_, **kwargs_)
        else:
            return RelatedTTPsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Related_TTP(self): return self.Related_TTP
    def set_Related_TTP(self, Related_TTP): self.Related_TTP = Related_TTP
    def add_Related_TTP(self, value): self.Related_TTP.append(value)
    def insert_Related_TTP(self, index, value): self.Related_TTP[index] = value
    def hasContent_(self):
        if (
            self.Related_TTP or
            super(RelatedTTPsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedTTPsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedTTPsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='RelatedTTPsType'):
        super(RelatedTTPsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedTTPsType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedTTPsType', fromsubclass_=False, pretty_print=True):
        super(RelatedTTPsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Related_TTP_ in self.Related_TTP:
            Related_TTP_.export(lwrite, level, nsmap, namespace_, name_='Related_TTP', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedTTPsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Related_TTP':
            obj_ = stix_common_binding.RelatedTTPType.factory()
            obj_.build(child_)
            self.Related_TTP.append(obj_)
        super(RelatedTTPsType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedTTPsType

class TTPType(stix_common_binding.TTPBaseType):
    """TTPType characterizes an individual adversary TTP.Specifies the
    relevant STIX-TTP schema version for this content."""
    subclass = None
    superclass = stix_common_binding.TTPBaseType
    def __init__(self, idref=None, id=None, timestamp=None, version=None, Title=None, Description=None, Short_Description=None, Intended_Effect=None, Behavior=None, Resources=None, Victim_Targeting=None, Exploit_Targets=None, Related_TTPs=None, Kill_Chain_Phases=None, Information_Source=None, Kill_Chains=None, Handling=None, Related_Packages=None):
        super(TTPType, self).__init__(idref=idref, id=id, timestamp=timestamp)
        self.xmlns          = "http://stix.mitre.org/TTP-1"
        self.xmlns_prefix   = "ttp"
        self.xml_type       = "TTPType"
        self.version = _cast(None, version)

        self.Title = Title
        self.Description = Description
        self.Short_Description = Short_Description
        if Intended_Effect is None:
            self.Intended_Effect = []
        else:
            self.Intended_Effect = Intended_Effect
        self.Behavior = Behavior
        self.Resources = Resources
        self.Victim_Targeting = Victim_Targeting
        self.Exploit_Targets = Exploit_Targets
        self.Related_TTPs = Related_TTPs
        self.Kill_Chain_Phases = Kill_Chain_Phases
        self.Information_Source = Information_Source
        self.Kill_Chains = Kill_Chains
        self.Handling = Handling
        self.Related_Packages = Related_Packages
    def factory(*args_, **kwargs_):
        if TTPType.subclass:
            return TTPType.subclass(*args_, **kwargs_)
        else:
            return TTPType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_Intended_Effect(self): return self.Intended_Effect
    def set_Intended_Effect(self, Intended_Effect): self.Intended_Effect = Intended_Effect
    def add_Intended_Effect(self, value): self.Intended_Effect.append(value)
    def insert_Intended_Effect(self, index, value): self.Intended_Effect[index] = value
    def get_Behavior(self): return self.Behavior
    def set_Behavior(self, Behavior): self.Behavior = Behavior
    def get_Resources(self): return self.Resources
    def set_Resources(self, Resources): self.Resources = Resources
    def get_Victim_Targeting(self): return self.Victim_Targeting
    def set_Victim_Targeting(self, Victim_Targeting): self.Victim_Targeting = Victim_Targeting
    def get_Exploit_Targets(self): return self.Exploit_Targets
    def set_Exploit_Targets(self, Exploit_Targets): self.Exploit_Targets = Exploit_Targets
    def get_Related_TTPs(self): return self.Related_TTPs
    def set_Related_TTPs(self, Related_TTPs): self.Related_TTPs = Related_TTPs
    def get_Kill_Chain_Phases(self): return self.Kill_Chain_Phases
    def set_Kill_Chain_Phases(self, Kill_Chain_Phases): self.Kill_Chain_Phases = Kill_Chain_Phases
    def get_Information_Source(self): return self.Information_Source
    def set_Information_Source(self, Information_Source): self.Information_Source = Information_Source
    def get_Kill_Chains(self): return self.Kill_Chains
    def set_Kill_Chains(self, Kill_Chains): self.Kill_Chains = Kill_Chains
    def get_Handling(self): return self.Handling
    def set_Handling(self, Handling): self.Handling = Handling
    def get_Related_Packages(self): return self.Related_Packages
    def set_Related_Packages(self, Related_Packages): self.Related_Packages = Related_Packages
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Description is not None or
            self.Short_Description is not None or
            self.Intended_Effect or
            self.Behavior is not None or
            self.Resources is not None or
            self.Victim_Targeting is not None or
            self.Exploit_Targets is not None or
            self.Related_TTPs is not None or
            self.Kill_Chain_Phases is not None or
            self.Information_Source is not None or
            self.Kill_Chains is not None or
            self.Handling is not None or
            self.Related_Packages is not None or
            super(TTPType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TTP', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TTP')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='TTP'):
        super(TTPType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='TTP')
        #if 'xmlns' not in already_processed:
        #    already_processed.add('xmlns')
        #    xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
        #    lwrite(xmlns)
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
            lwrite(xsi_type)
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            lwrite(' version=%s' % (quote_attrib(self.version), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TTPType', fromsubclass_=False, pretty_print=True):
        super(TTPType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_], quote_xml(self.Title), nsmap[namespace_], eol_))
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Short_Description is not None:
            self.Short_Description.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
        for Intended_Effect_ in self.Intended_Effect:
            Intended_Effect_.export(lwrite, level, nsmap, namespace_, name_='Intended_Effect', pretty_print=pretty_print)
        if self.Behavior is not None:
            self.Behavior.export(lwrite, level, nsmap, namespace_, name_='Behavior', pretty_print=pretty_print)
        if self.Resources is not None:
            self.Resources.export(lwrite, level, nsmap, namespace_, name_='Resources', pretty_print=pretty_print)
        if self.Victim_Targeting is not None:
            self.Victim_Targeting.export(lwrite, level, nsmap, namespace_, name_='Victim_Targeting', pretty_print=pretty_print)
        if self.Exploit_Targets is not None:
            self.Exploit_Targets.export(lwrite, level, nsmap, namespace_, name_='Exploit_Targets', pretty_print=pretty_print)
        if self.Related_TTPs is not None:
            self.Related_TTPs.export(lwrite, level, nsmap, namespace_, name_='Related_TTPs', pretty_print=pretty_print)
        if self.Kill_Chain_Phases is not None:
            self.Kill_Chain_Phases.export(lwrite, level, nsmap, namespace_, name_='Kill_Chain_Phases', pretty_print=pretty_print)
        if self.Information_Source is not None:
            self.Information_Source.export(lwrite, level, nsmap, namespace_, name_='Information_Source', pretty_print=pretty_print)
        if self.Kill_Chains is not None:
            self.Kill_Chains.export(lwrite, level, nsmap, namespace_, name_='Kill_Chains', pretty_print=pretty_print)
        if self.Handling is not None:
            self.Handling.export(lwrite, level, nsmap, namespace_, name_='Handling', pretty_print=pretty_print)
        if self.Related_Packages is not None:
            self.Related_Packages.export(lwrite, level, nsmap, namespace_, name_='Related_Packages', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = value
        super(TTPType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Short_Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Short_Description(obj_)
        elif nodeName_ == 'Intended_Effect':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.Intended_Effect.append(obj_)
        elif nodeName_ == 'Behavior':
            obj_ = BehaviorType.factory()
            obj_.build(child_)
            self.set_Behavior(obj_)
        elif nodeName_ == 'Resources':
            obj_ = ResourceType.factory()
            obj_.build(child_)
            self.set_Resources(obj_)
        elif nodeName_ == 'Victim_Targeting':
            obj_ = VictimTargetingType.factory()
            obj_.build(child_)
            self.set_Victim_Targeting(obj_)
        elif nodeName_ == 'Exploit_Targets':
            obj_ = ExploitTargetsType.factory()
            obj_.build(child_)
            self.set_Exploit_Targets(obj_)
        elif nodeName_ == 'Related_TTPs':
            obj_ = RelatedTTPsType.factory()
            obj_.build(child_)
            self.set_Related_TTPs(obj_)
        elif nodeName_ == 'Kill_Chain_Phases':
            obj_ = stix_common_binding.KillChainPhasesReferenceType.factory()
            obj_.build(child_)
            self.set_Kill_Chain_Phases(obj_)
        elif nodeName_ == 'Information_Source':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Information_Source(obj_)
        elif nodeName_ == 'Kill_Chains':
            obj_ = stix_common_binding.KillChainsType.factory()
            obj_.build(child_)
            self.set_Kill_Chains(obj_)
        elif nodeName_ == 'Handling':
            obj_ = data_marking_binding.MarkingType.factory()
            obj_.build(child_)
            self.set_Handling(obj_)
        elif nodeName_ == 'Related_Packages':
            obj_ = stix_common_binding.RelatedPackageRefsType.factory()
            obj_.build(child_)
            self.set_Related_Packages(obj_)
        super(TTPType, self).buildChildren(child_, node, nodeName_, True)
# end class TTPType

class ExploitTargetsType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, Exploit_Target=None, scope=None):
        super(ExploitTargetsType, self).__init__(scope=scope)
        if Exploit_Target is None:
            self.Exploit_Target = []
        else:
            self.Exploit_Target = Exploit_Target
    def factory(*args_, **kwargs_):
        if ExploitTargetsType.subclass:
            return ExploitTargetsType.subclass(*args_, **kwargs_)
        else:
            return ExploitTargetsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Exploit_Target(self): return self.Exploit_Target
    def set_Exploit_Target(self, Exploit_Target): self.Exploit_Target = Exploit_Target
    def add_Exploit_Target(self, value): self.Exploit_Target.append(value)
    def insert_Exploit_Target(self, index, value): self.Exploit_Target[index] = value
    def hasContent_(self):
        if (
            self.Exploit_Target or
            super(ExploitTargetsType, self).hasContent()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExploitTargetsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ExploitTargetsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ttp:', name_='ExploitTargetsType'):
        super(ExploitTargetsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_)
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExploitTargetsType', fromsubclass_=False, pretty_print=True):
        super(ExploitTargetsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, fromsubclass_=True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Exploit_Target_ in self.Exploit_Target:
            Exploit_Target_.export(lwrite, level, nsmap, namespace_, name_='Exploit_Target', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(ExploitTargetsType, self).buildAttributes(node, attrs, already_processed)
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Exploit_Target':
            obj_ = stix_common_binding.RelatedExploitTargetType.factory()
            obj_.build(child_)
            self.Exploit_Target.append(obj_)
# end class ExploitTargetsType


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
        rootTag = 'TTP'
        rootClass = TTPType
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
        rootTag = 'TTP'
        rootClass = TTPType
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
        rootTag = 'TTP'
        rootClass = TTPType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="TTP",
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
    "AttackPatternType",
    "MalwareInstanceType",
    "ExploitType",
    "InfrastructureType",
    "ToolsType",
    "ExploitsType",
    "MalwareType",
    "AttackPatternsType",
    "ResourceType",
    "BehaviorType",
    "VictimTargetingType",
    "RelatedTTPsType",
    "TTPType"
    ]
