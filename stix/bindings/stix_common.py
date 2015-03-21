# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:06:26 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import cybox.bindings.cybox_common as cybox_common_binding
import cybox.bindings.cybox_core as cybox_core_binding

XML_NS = "http://stix.mitre.org/common-1"

#
# Data representation classes.
#

class GenericRelationshipType(GeneratedsSuper):
    """Allows the expression of relationships between STIX components. It
    is extended by each component relationship type to add the
    component itself."""
    subclass = None
    superclass = None
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, extensiontype_=None):
        self.Confidence = Confidence
        self.Information_Source = Information_Source
        self.Relationship = Relationship
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if GenericRelationshipType.subclass:
            return GenericRelationshipType.subclass(*args_, **kwargs_)
        else:
            return GenericRelationshipType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Confidence(self): return self.Confidence
    def set_Confidence(self, Confidence): self.Confidence = Confidence
    def get_Information_Source(self): return self.Information_Source
    def set_Information_Source(self, Information_Source): self.Information_Source = Information_Source
    def get_Relationship(self): return self.Relationship
    def set_Relationship(self, Relationship): self.Relationship = Relationship
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.Confidence is not None or
            self.Information_Source is not None or
            self.Relationship is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='GenericRelationshipType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='GenericRelationshipType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='GenericRelationshipType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            lwrite('  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite('  xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='GenericRelationshipType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Confidence is not None:
            self.Confidence.export(lwrite, level, nsmap, namespace_, name_='Confidence', pretty_print=pretty_print)
        if self.Information_Source is not None:
            self.Information_Source.export(lwrite, level, nsmap, namespace_, name_='Information_Source', pretty_print=pretty_print)
        if self.Relationship is not None:
            self.Relationship.export(lwrite, level, nsmap, namespace_, name_='Relationship', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Confidence':
            obj_ = ConfidenceType.factory()
            obj_.build(child_)
            self.set_Confidence(obj_)
        elif nodeName_ == 'Information_Source':
            obj_ = InformationSourceType.factory()
            obj_.build(child_)
            self.set_Information_Source(obj_)
        elif nodeName_ == 'Relationship':
            obj_ = ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Relationship(obj_)
# end class GenericRelationshipType


class DateTimeWithPrecisionType(GeneratedsSuper):
    """This type is used as a replacement for the standard xs:dateTime type
    but allows for the representation of the precision of the
    dateTime. If the precision is given, consumers must ignore the
    portions of this field that is more precise than the given
    precision. Producers should zero-out (fill with zeros) digits in
    the dateTime that are required by the xs:dateTime datatype but
    are beyond the specified precision.In order to avoid ambiguity,
    it is strongly suggested that all dateTimes include a
    specification of the timezone if it is known.The precision of
    the associated dateTime. If omitted, the default is "second",
    meaning the full field value (including fractional seconds)."""
    subclass = None
    superclass = None
    def __init__(self, precision='second', valueOf_=None):
        self.precision = _cast(None, precision)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if DateTimeWithPrecisionType.subclass:
            return DateTimeWithPrecisionType.subclass(*args_, **kwargs_)
        else:
            return DateTimeWithPrecisionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_precision(self): return self.precision
    def set_precision(self, precision): self.precision = precision
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='DateTimeWithPrecisionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DateTimeWithPrecisionType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='DateTimeWithPrecisionType'):
        if self.precision is not None and 'precision' not in already_processed:
            already_processed.add('precision')
            lwrite(' precision=%s' % (quote_attrib(self.precision), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='DateTimeWithPrecisionType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('precision', node)
        if value is not None and 'precision' not in already_processed:
            already_processed.add('precision')
            self.precision = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class DateTimeWithPrecisionType

class ProfilesType(GeneratedsSuper):
    """The ProfilesType represents a list of STIX Profiles"""
    subclass = None
    superclass = None
    def __init__(self, Profile=None):
        if Profile is None:
            self.Profile = []
        else:
            self.Profile = Profile
    def factory(*args_, **kwargs_):
        if ProfilesType.subclass:
            return ProfilesType.subclass(*args_, **kwargs_)
        else:
            return ProfilesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Profile(self): return self.Profile
    def set_Profile(self, Profile): self.Profile = Profile
    def add_Profile(self, value): self.Profile.append(value)
    def insert_Profile(self, index, value): self.Profile[index] = value
    def hasContent_(self):
        if (
            self.Profile
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ProfilesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ProfilesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='ProfilesType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ProfilesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Profile_ in self.Profile:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Profile>%s</%s:Profile>%s' % (nsmap[namespace_],quote_xml(Profile_), nsmap[namespace_], eol_))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Profile':
            Profile_ = child_.text
            Profile_ = self.gds_validate_string(Profile_, node, 'Profile')
            self.Profile.append(Profile_)
# end class ProfilesType


class RelatedPackageRefType(GenericRelationshipType):
    """Identifies or characterizes a relationship to a Package.Specifies a
    globally unique identifier of a STIX Package specified
    elsewhere.In conjunction with the idref, this field may be used
    to reference a specific version of a STIX Package defined
    elsewhere. The referenced version timestamp is contained in the
    STIX_Header/Information_Source/Time/Produced_Time field of the
    related package and must be an exact match.This field must only
    be used in conjunction with the idref field."""
    subclass = None
    superclass = GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, idref=None, timestamp=None):
        super(RelatedPackageRefType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.idref = _cast(None, idref)
        self.timestamp = _cast(None, timestamp)
        pass
    def factory(*args_, **kwargs_):
        if RelatedPackageRefType.subclass:
            return RelatedPackageRefType.subclass(*args_, **kwargs_)
        else:
            return RelatedPackageRefType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def hasContent_(self):
        if (
            super(RelatedPackageRefType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedPackageRefType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedPackageRefType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedPackageRefType'):
        super(RelatedPackageRefType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedPackageRefType')
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedPackageRefType', fromsubclass_=False, pretty_print=True):
        super(RelatedPackageRefType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
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
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
        super(RelatedPackageRefType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(RelatedPackageRefType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class RelatedPackageRefType


class RelatedPackageRefsType(GeneratedsSuper):
    """Identifies or characterizes relationships to set of related
    Packages."""
    subclass = None
    superclass = None
    def __init__(self, Package_Reference=None):
        if Package_Reference is None:
            self.Package_Reference = []
        else:
            self.Package_Reference = Package_Reference
    def factory(*args_, **kwargs_):
        if RelatedPackageRefsType.subclass:
            return RelatedPackageRefsType.subclass(*args_, **kwargs_)
        else:
            return RelatedPackageRefsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Package_Reference(self): return self.Package_Reference
    def set_Package_Reference(self, Package_Reference): self.Package_Reference = Package_Reference
    def add_Package_Reference(self, value): self.Package_Reference.append(value)
    def insert_Package_Reference(self, index, value): self.Package_Reference[index] = value
    def hasContent_(self):
        if (
            self.Package_Reference
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedPackageRefsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedPackageRefsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedPackageRefsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedPackageRefsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Package_Reference_ in self.Package_Reference:
            Package_Reference_.export(lwrite, level, nsmap, namespace_, name_='Package_Reference', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Package_Reference':
            obj_ = RelatedPackageRefType.factory()
            obj_.build(child_)
            self.Package_Reference.append(obj_)
# end class RelatedPackageRefsType

class ToolInformationType(cybox_common_binding.ToolInformationType):
    """The ToolInformationType is intended to characterize the properties
    of a hardware or software tool, including those related to
    instances of its use.The id field specifies a unique ID for this
    Tool.The idref field specifies reference to a unique ID for this
    Tool.When idref is specified, the id attribute must not be
    specified, and any instance of this type should not hold content
    unless an extension of the type allows it."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, Name=None, Type=None, Description=None, References=None, Vendor=None, Version=None, Service_Pack=None, Tool_Specific_Data=None, Tool_Hashes=None, Tool_Configuration=None, Execution_Environment=None, Errors=None, Metadata=None, Compensation_Model=None, Title=None, Short_Description=None, extensiontype_=None):
        super(ToolInformationType, self).__init__(idref=idref, id=id, Name=Name, Type=Type, Description=Description, References=References, Vendor=Vendor, Version=Version, Service_Pack=Service_Pack, Tool_Specific_Data=Tool_Specific_Data, Execution_Environment=Execution_Environment, Errors=Errors, Metadata=Metadata, Compensation_Model=Compensation_Model)
        self.Title = Title
        self.Short_Description = Short_Description
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if ToolInformationType.subclass:
            return ToolInformationType.subclass(*args_, **kwargs_)
        else:
            return ToolInformationType(*args_, **kwargs_)

    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def hasContent_(self):
        if (
            super(ToolInformationType, self).hasContent_() or
            self.Title is not None or
            self.Short_Description is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ToolInformationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ToolInformationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='ToolInformationType'):
        super(ToolInformationType, self).exportAttributes(lwrite, level, already_processed, namespace_="cyboxCommon:", name_=name_)
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            lwrite(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite(' xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ToolInformationType', fromsubclass_=False, pretty_print=True):
        super(ToolInformationType, self).exportChildren(lwrite, level, namespace_="cyboxCommon:", name_=name_, fromsubclass_=True, pretty_print=pretty_print) # exporting cyboxCommon-defined children
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_],quote_xml(self.Title), nsmap[namespace_], eol_))
        if self.Short_Description is not None:
            self.Short_Description.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(ToolInformationType, self).buildAttributes(node, attrs, already_processed)
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(ToolInformationType, self).buildChildren(child_, node, nodeName_, fromsubclass_=True)
        if nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'Short_Description':
            obj_ = StructuredTextType.factory()
            obj_.build(child_)
            self.set_Short_Description(obj_)
# end class ToolInformationType

class InformationSourceType(GeneratedsSuper):
    """The InformationSourceType details the source of a given data entry."""
    subclass = None
    superclass = None
    def __init__(self, Description=None, Identity=None, Role=None, Contributing_Sources=None, Time=None, Tools=None, References=None):
        self.Description = Description
        self.Identity = Identity
        if Role is None:
            self.Role = []
        else:
            self.Role = Role
        self.Contributing_Sources = Contributing_Sources
        self.Time = Time
        self.Tools = Tools
        self.References = References
    def factory(*args_, **kwargs_):
        if InformationSourceType.subclass:
            return InformationSourceType.subclass(*args_, **kwargs_)
        else:
            return InformationSourceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Identity(self): return self.Identity
    def set_Identity(self, Identity): self.Identity = Identity
    def get_Role(self): return self.Role
    def set_Role(self, Role): self.Role = Role
    def add_Role(self, value): self.Role.append(value)
    def insert_Role(self, index, value): self.Role[index] = value
    def get_Contributing_Sources(self): return self.Contributing_Sources
    def set_Contributing_Sources(self, Contributing_Sources): self.Contributing_Sources = Contributing_Sources
    def get_Time(self): return self.Time
    def set_Time(self, Time): self.Time = Time
    def get_Tools(self): return self.Tools
    def set_Tools(self, Tools): self.Tools = Tools
    def get_References(self): return self.References
    def set_References(self, References): self.References = References
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Identity is not None or
            self.Role or
            self.Contributing_Sources is not None or
            self.Time is not None or
            self.Tools is not None or
            self.References is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='InformationSourceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='InformationSourceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='InformationSourceType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='InformationSourceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Identity is not None:
            self.Identity.export(lwrite, level, nsmap, namespace_, name_='Identity', pretty_print=pretty_print)
        for Role_ in self.Role:
            Role_.export(lwrite, level, nsmap, namespace_, name_='Role', pretty_print=pretty_print)
        if self.Contributing_Sources is not None:
            self.Contributing_Sources.export(lwrite, level, nsmap, namespace_, name_='Contributing_Sources', pretty_print=pretty_print)
        if self.Time is not None:
            self.Time.export(lwrite, level, "%s:" % (nsmap[namespace_]), name_='Time', pretty_print=pretty_print)
        if self.Tools is not None:
            self.Tools.export(lwrite, level, "%s:" % (nsmap[namespace_]), name_='Tools', pretty_print=pretty_print)
        if self.References is not None:
            self.References.export(lwrite, level, nsmap, namespace_, name_='References', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Description':
            obj_ = StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Identity':
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
                    import stix.bindings.extensions.identity.ciq_identity_3_0 as ciq_identity_binding
                    obj_ = ciq_identity_binding.CIQIdentity3_0InstanceType.factory()
            else:
                obj_ = IdentityType.factory() # IdentityType is not abstract

            obj_.build(child_)
            self.set_Identity(obj_)
        elif nodeName_ == 'Role':
            obj_ = ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Role.append(obj_)
        elif nodeName_ == 'Contributing_Sources':
            obj_ = ContributingSourcesType.factory()
            obj_.build(child_)
            self.set_Contributing_Sources(obj_)
        elif nodeName_ == 'Time':
            obj_ = cybox_common_binding.TimeType.factory()
            obj_.build(child_)
            self.set_Time(obj_)
        elif nodeName_ == 'Tools':
            obj_ = cybox_common_binding.ToolsInformationType.factory()
            obj_.build(child_)
            self.set_Tools(obj_)
        elif nodeName_ == 'References':
            obj_ = ReferencesType.factory()
            obj_.build(child_)
            self.set_References(obj_)
# end class InformationSourceType

class ConfidenceType(GeneratedsSuper):
    """The ConfidenceType specifies a level of Confidence held in some
    assertion.Specifies the time of this Confidence assertion."""
    subclass = None
    superclass = None
    def __init__(self, timestamp=None, timestamp_precision='second', Value=None, Description=None, Source=None, Confidence_Assertion_Chain=None):
        self.timestamp = _cast(None, timestamp)
        self.timestamp_precision = _cast(None, timestamp_precision)
        self.Value = Value
        self.Description = Description
        self.Source = Source
        self.Confidence_Assertion_Chain = Confidence_Assertion_Chain
    def factory(*args_, **kwargs_):
        if ConfidenceType.subclass:
            return ConfidenceType.subclass(*args_, **kwargs_)
        else:
            return ConfidenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Value(self): return self.Value
    def set_Value(self, Value): self.Value = Value
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Source(self): return self.Source
    def set_Source(self, Source): self.Source = Source
    def get_Confidence_Assertion_Chain(self): return self.Confidence_Assertion_Chain
    def set_Confidence_Assertion_Chain(self, Confidence_Assertion_Chain): self.Confidence_Assertion_Chain = Confidence_Assertion_Chain
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def get_timestamp_precision(self): return self.timestamp_precision
    def set_timestamp_precision(self, timestamp_precision): self.timestamp_precision = timestamp_precision
    def hasContent_(self):
        if (
            self.Value is not None or
            self.Description is not None or
            self.Source is not None or
            self.Confidence_Assertion_Chain is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ConfidenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ConfidenceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='ConfidenceType'):
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
        if self.timestamp_precision not in (None, 'second') and 'timestamp_precision' not in already_processed:
            already_processed.add('timestamp_precision')
            lwrite(' timestamp_precision=%s' % (quote_attrib(self.timestamp_precision), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ConfidenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Value is not None:
            self.Value.export(lwrite, level, nsmap, namespace_, name_='Value', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Source is not None:
            self.Source.export(lwrite, level, nsmap, namespace_, name_='Source', pretty_print=pretty_print)
        if self.Confidence_Assertion_Chain is not None:
            self.Confidence_Assertion_Chain.export(lwrite, level, nsmap, namespace_, name_='Confidence_Assertion_Chain', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
        
        value = find_attr_value_('timestamp_precision', node)
        if value is not None and 'timestamp_precision' not in already_processed:
            already_processed.add('timestamp_precision')
            self.timestamp_precision = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Value':
            obj_ = ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Value(obj_)
        elif nodeName_ == 'Description':
            obj_ = StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Source':
            obj_ = InformationSourceType.factory()
            obj_.build(child_)
            self.set_Source(obj_)
        elif nodeName_ == 'Confidence_Assertion_Chain':
            obj_ = ConfidenceAssertionChainType.factory()
            obj_.build(child_)
            self.set_Confidence_Assertion_Chain(obj_)
# end class ConfidenceType

class ActivityType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Date_Time=None, Description=None):
        self.Date_Time = Date_Time
        self.Description = Description
    def factory(*args_, **kwargs_):
        if ActivityType.subclass:
            return ActivityType.subclass(*args_, **kwargs_)
        else:
            return ActivityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Date_Time(self): return self.Date_Time
    def set_Date_Time(self, Date_Time): self.Date_Time = Date_Time
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def hasContent_(self):
        if (
            self.Date_Time is not None or
            self.Description is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ActivityType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ActivityType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='ActivityType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ActivityType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Date_Time is not None:
            self.Date_Time.export(lwrite, level, nsmap, namespace_, name_='Date_Time', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Date_Time':
            obj_ = DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Date_Time(obj_)
        elif nodeName_ == 'Description':
            obj_ = StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
# end class ActivityType

class KillChainsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Kill_Chain=None):
        if Kill_Chain is None:
            self.Kill_Chain = []
        else:
            self.Kill_Chain = Kill_Chain
    def factory(*args_, **kwargs_):
        if KillChainsType.subclass:
            return KillChainsType.subclass(*args_, **kwargs_)
        else:
            return KillChainsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Kill_Chain(self): return self.Kill_Chain
    def set_Kill_Chain(self, Kill_Chain): self.Kill_Chain = Kill_Chain
    def add_Kill_Chain(self, value): self.Kill_Chain.append(value)
    def insert_Kill_Chain(self, index, value): self.Kill_Chain[index] = value
    def hasContent_(self):
        if (
            self.Kill_Chain
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='KillChainsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='KillChainsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='KillChainsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='KillChainsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Kill_Chain_ in self.Kill_Chain:
            Kill_Chain_.export(lwrite, level, nsmap, namespace_, name_='Kill_Chain', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Kill_Chain':
            obj_ = KillChainType.factory()
            obj_.build(child_)
            self.Kill_Chain.append(obj_)
# end class KillChainsType

class KillChainType(GeneratedsSuper):
    """The KillChainType characterizes a specific Kill Chain definition for
    reference within specific TTP entries, Indicators and
    elsewhere.A globally unique identifier for this kill chain
    definition.A descriptive name for this kill chain definition.The
    organization or individual responsible for this kill chain
    definition.A resource reference for this kill chain
    definition.The number of phases in this kill chain definition."""
    subclass = None
    superclass = None
    def __init__(self, reference=None, number_of_phases=None, id=None, definer=None, name=None, Kill_Chain_Phase=None):
        self.reference = _cast(None, reference)
        self.number_of_phases = _cast(None, number_of_phases)
        self.id = _cast(None, id)
        self.definer = _cast(None, definer)
        self.name = _cast(None, name)
        if Kill_Chain_Phase is None:
            self.Kill_Chain_Phase = []
        else:
            self.Kill_Chain_Phase = Kill_Chain_Phase
    def factory(*args_, **kwargs_):
        if KillChainType.subclass:
            return KillChainType.subclass(*args_, **kwargs_)
        else:
            return KillChainType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Kill_Chain_Phase(self): return self.Kill_Chain_Phase
    def set_Kill_Chain_Phase(self, Kill_Chain_Phase): self.Kill_Chain_Phase = Kill_Chain_Phase
    def add_Kill_Chain_Phase(self, value): self.Kill_Chain_Phase.append(value)
    def insert_Kill_Chain_Phase(self, index, value): self.Kill_Chain_Phase[index] = value
    def get_reference(self): return self.reference
    def set_reference(self, reference): self.reference = reference
    def get_number_of_phases(self): return self.number_of_phases
    def set_number_of_phases(self, number_of_phases): self.number_of_phases = number_of_phases
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_definer(self): return self.definer
    def set_definer(self, definer): self.definer = definer
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def hasContent_(self):
        if (
            self.Kill_Chain_Phase
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='KillChainType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='KillChainType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='KillChainType'):
        if self.reference is not None and 'reference' not in already_processed:
            already_processed.add('reference')
            lwrite(' reference=%s' % (quote_attrib(self.reference), ))
        if self.number_of_phases is not None and 'number_of_phases' not in already_processed:
            already_processed.add('number_of_phases')
            lwrite(' number_of_phases=%s' % (quote_attrib(self.number_of_phases), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.definer is not None and 'definer' not in already_processed:
            already_processed.add('definer')
            lwrite(' definer=%s' % (quote_attrib(self.definer), ))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            lwrite(' name=%s' % (quote_attrib(self.name), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='KillChainType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Kill_Chain_Phase_ in self.Kill_Chain_Phase:
            Kill_Chain_Phase_.export(lwrite, level, nsmap, namespace_, name_='Kill_Chain_Phase', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('reference', node)
        if value is not None and 'reference' not in already_processed:
            already_processed.add('reference')
            self.reference = value
        value = find_attr_value_('number_of_phases', node)
        if value is not None and 'number_of_phases' not in already_processed:
            already_processed.add('number_of_phases')
            self.number_of_phases = value
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('definer', node)
        if value is not None and 'definer' not in already_processed:
            already_processed.add('definer')
            self.definer = value
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Kill_Chain_Phase':
            obj_ = KillChainPhaseType.factory()
            obj_.build(child_)
            self.Kill_Chain_Phase.append(obj_)
# end class KillChainType

class KillChainPhaseType(GeneratedsSuper):
    """The KillChainPhaseType characterizes an individual phase within a
    kill chain definition.This field specifies the ID for the
    relevant kill chain phase.This field specifies the descriptive
    name of the relevant kill chain phase.This field specifies the
    ordinality (e.g. 1, 2 or 3) of this phase within this kill chain
    definition."""
    subclass = None
    superclass = None
    def __init__(self, ordinality=None, name=None, phase_id=None, extensiontype_=None):
        self.ordinality = _cast(int, ordinality)
        self.name = _cast(None, name)
        self.phase_id = _cast(None, phase_id)
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if KillChainPhaseType.subclass:
            return KillChainPhaseType.subclass(*args_, **kwargs_)
        else:
            return KillChainPhaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_ordinality(self): return self.ordinality
    def set_ordinality(self, ordinality): self.ordinality = ordinality
    def get_name(self): return self.name
    def set_name(self, name): self.name = name
    def get_phase_id(self): return self.phase_id
    def set_phase_id(self, phase_id): self.phase_id = phase_id
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='KillChainPhaseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='KillChainPhaseType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='KillChainPhaseType'):
        if self.ordinality is not None and 'ordinality' not in already_processed:
            already_processed.add('ordinality')
            lwrite(' ordinality="%s"' % self.gds_format_integer(self.ordinality, input_name='ordinality'))
        if self.name is not None and 'name' not in already_processed:
            already_processed.add('name')
            lwrite(' name=%s' % (quote_attrib(self.name), ))
        if self.phase_id is not None and 'phase_id' not in already_processed:
            already_processed.add('phase_id')
            lwrite(' phase_id=%s' % (quote_attrib(self.phase_id), ))
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            lwrite('  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite('  xsi:type="%s"' % self.extensiontype_)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='KillChainPhaseType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('ordinality', node)
        if value is not None and 'ordinality' not in already_processed:
            already_processed.add('ordinality')
            try:
                self.ordinality = int(value)
            except ValueError, exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
        value = find_attr_value_('name', node)
        if value is not None and 'name' not in already_processed:
            already_processed.add('name')
            self.name = value
        value = find_attr_value_('phase_id', node)
        if value is not None and 'phase_id' not in already_processed:
            already_processed.add('phase_id')
            self.phase_id = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.extensiontype_ = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class KillChainPhaseType

class KillChainPhasesReferenceType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Kill_Chain_Phase=None):
        if Kill_Chain_Phase is None:
            self.Kill_Chain_Phase = []
        else:
            self.Kill_Chain_Phase = Kill_Chain_Phase
    def factory(*args_, **kwargs_):
        if KillChainPhasesReferenceType.subclass:
            return KillChainPhasesReferenceType.subclass(*args_, **kwargs_)
        else:
            return KillChainPhasesReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Kill_Chain_Phase(self): return self.Kill_Chain_Phase
    def set_Kill_Chain_Phase(self, Kill_Chain_Phase): self.Kill_Chain_Phase = Kill_Chain_Phase
    def add_Kill_Chain_Phase(self, value): self.Kill_Chain_Phase.append(value)
    def insert_Kill_Chain_Phase(self, index, value): self.Kill_Chain_Phase[index] = value
    def hasContent_(self):
        if (
            self.Kill_Chain_Phase
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='KillChainPhasesReferenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='KillChainPhasesReferenceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='KillChainPhasesReferenceType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='KillChainPhasesReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Kill_Chain_Phase_ in self.Kill_Chain_Phase:
            Kill_Chain_Phase_.export(lwrite, level, nsmap, namespace_, name_='Kill_Chain_Phase', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Kill_Chain_Phase':
            obj_ = KillChainPhaseReferenceType.factory()
            obj_.build(child_)
            self.Kill_Chain_Phase.append(obj_)
# end class KillChainPhasesReferenceType

class KillChainPhaseReferenceType(KillChainPhaseType):
    """This field specifies the ID for the relevant defined kill chain.This
    field specifies the descriptive name of the relevant kill chain."""
    subclass = None
    superclass = KillChainPhaseType
    def __init__(self, ordinality=None, name=None, phase_id=None, kill_chain_name=None, kill_chain_id=None):
        super(KillChainPhaseReferenceType, self).__init__(ordinality=ordinality, name=name, phase_id=phase_id)
        self.kill_chain_name = _cast(None, kill_chain_name)
        self.kill_chain_id = _cast(None, kill_chain_id)
        pass
    def factory(*args_, **kwargs_):
        if KillChainPhaseReferenceType.subclass:
            return KillChainPhaseReferenceType.subclass(*args_, **kwargs_)
        else:
            return KillChainPhaseReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_kill_chain_name(self): return self.kill_chain_name
    def set_kill_chain_name(self, kill_chain_name): self.kill_chain_name = kill_chain_name
    def get_kill_chain_id(self): return self.kill_chain_id
    def set_kill_chain_id(self, kill_chain_id): self.kill_chain_id = kill_chain_id
    def hasContent_(self):
        if (
            super(KillChainPhaseReferenceType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='KillChainPhaseReferenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='KillChainPhaseReferenceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='KillChainPhaseReferenceType'):
        super(KillChainPhaseReferenceType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='KillChainPhaseReferenceType')
        if self.kill_chain_name is not None and 'kill_chain_name' not in already_processed:
            already_processed.add('kill_chain_name')
            lwrite(' kill_chain_name=%s' % (quote_attrib(self.kill_chain_name), ))
        if self.kill_chain_id is not None and 'kill_chain_id' not in already_processed:
            already_processed.add('kill_chain_id')
            lwrite(' kill_chain_id=%s' % (quote_attrib(self.kill_chain_id), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='KillChainPhaseReferenceType', fromsubclass_=False, pretty_print=True):
        super(KillChainPhaseReferenceType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('kill_chain_name', node)
        if value is not None and 'kill_chain_name' not in already_processed:
            already_processed.add('kill_chain_name')
            self.kill_chain_name = value
        value = find_attr_value_('kill_chain_id', node)
        if value is not None and 'kill_chain_id' not in already_processed:
            already_processed.add('kill_chain_id')
            self.kill_chain_id = value
        super(KillChainPhaseReferenceType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(KillChainPhaseReferenceType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class KillChainPhaseReferenceType

class IdentityType(GeneratedsSuper):
    """The IdentityType is used to express identity information for both
    individuals and organizations. This type is extended through the
    xsi:type mechanism. The default type is
    CIQIdentity3.0InstanceType in the
    http://stix.mitre.org/extensions/Identity#CIQIdentity3.0-1
    namespace. This type is defined in the
    extensions/identity/ciq_identity_3.0.xsd file or at the URL http
    ://stix.mitre.org/XMLSchema/extensions/identity/ciq_identity_3.0
    /1.0/ciq_identity_3.0.xsd. Those who wish to express a simple
    name may also do so by not specifying an xsi:type and using the
    Name field of this type. Specifies a unique ID for this
    Identity.Specifies a reference to a unique ID defined elsewhere."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, Name=None, Related_Identities=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.Name = Name
        self.Related_Identities = Related_Identities
        self.xsi_type = None
    def factory(*args_, **kwargs_):
        if IdentityType.subclass:
            return IdentityType.subclass(*args_, **kwargs_)
        else:
            return IdentityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def get_Related_Identities(self): return self.Related_Identities
    def set_Related_Identities(self, Related_Identities): self.Related_Identities = Related_Identities
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (
            self.Name is not None or
            self.Related_Identities is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IdentityType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IdentityType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='IdentityType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IdentityType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Name is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Name>%s</%s:Name>%s' % (nsmap[namespace_], quote_xml(self.Name), nsmap[namespace_], eol_))
        if self.Related_Identities is not None:
            self.Related_Identities.export(lwrite, level, nsmap, namespace_, name_='Related_Identities', pretty_print=pretty_print)
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
        if nodeName_ == 'Name':
            Name_ = child_.text
            Name_ = self.gds_validate_string(Name_, node, 'Name')
            self.Name = Name_
        elif nodeName_ == 'Related_Identities':
            obj_ = RelatedIdentitiesType.factory()
            obj_.build(child_)
            self.set_Related_Identities(obj_)
# end class IdentityType

class GenericRelationshipListType(GeneratedsSuper):
    """Allows the expression of a list of relationships between STIX
    components. It's extended throughout STIX and should not be used
    directly. Indicates how multiple related items should be
    interpreted in this relationship. If "inclusive" is specified,
    then a single conceptual relationship is being defined between
    the subject and the collection of objects indicated by the
    related items (i.e. the relationship is not necessarily relevant
    for any one particular object being referenced, but for the
    aggregated collection of objects referenced). If "exclusive" is
    specified, then multiple relationships are being defined between
    the specific subject and each object individually."""
    subclass = None
    superclass = None
    def __init__(self, scope='exclusive'):
        self.scope = _cast(None, scope)
        pass
    def factory(*args_, **kwargs_):
        if GenericRelationshipListType.subclass:
            return GenericRelationshipListType.subclass(*args_, **kwargs_)
        else:
            return GenericRelationshipListType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_scope(self): return self.scope
    def set_scope(self, scope): self.scope = scope
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='GenericRelationshipListType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='GenericRelationshipListType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='GenericRelationshipListType'):
        if self.scope is not None and 'scope' not in already_processed:
            already_processed.add('scope')
            lwrite(' scope=%s' % (quote_attrib(self.scope), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='GenericRelationshipListType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('scope', node)
        if value is not None and 'scope' not in already_processed:
            already_processed.add('scope')
            self.scope = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class GenericRelationshipListType


class RelatedCampaignType(GenericRelationshipType):
    """Identifies or characterizes a relationship to a campaign."""
    subclass = None
    superclass = GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, Campaign=None):
        super(RelatedCampaignType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.Campaign = Campaign
    def factory(*args_, **kwargs_):
        if RelatedCampaignType.subclass:
            return RelatedCampaignType.subclass(*args_, **kwargs_)
        else:
            return RelatedCampaignType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Campaign(self): return self.Campaign
    def set_Campaign(self, Campaign): self.Campaign = Campaign
    def hasContent_(self):
        if (
            self.Campaign is not None or
            super(RelatedCampaignType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedCampaignType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedCampaignType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedCampaignType'):
        super(RelatedCampaignType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedCampaignType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedCampaignType', fromsubclass_=False, pretty_print=True):
        super(RelatedCampaignType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Campaign is not None:
            self.Campaign.export(lwrite, level, nsmap, namespace_, name_='Campaign', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedCampaignType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Campaign':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "CampaignType":
                    import stix.bindings.campaign as campaign_binding
                    obj_ = campaign_binding.CampaignType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = CampaignBaseType.factory() # not abstract

            obj_.build(child_)
            self.set_Campaign(obj_)
        super(RelatedCampaignType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedCampaignType

class RelatedCourseOfActionType(GenericRelationshipType):
    """Identifies or characterizes a relationship to a course of action."""
    subclass = None
    superclass = GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, Course_Of_Action=None):
        super(RelatedCourseOfActionType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.Course_Of_Action = Course_Of_Action
    def factory(*args_, **kwargs_):
        if RelatedCourseOfActionType.subclass:
            return RelatedCourseOfActionType.subclass(*args_, **kwargs_)
        else:
            return RelatedCourseOfActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Course_Of_Action(self): return self.Course_Of_Action
    def set_Course_Of_Action(self, Course_Of_Action): self.Course_Of_Action = Course_Of_Action
    def hasContent_(self):
        if (
            self.Course_Of_Action is not None or
            super(RelatedCourseOfActionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedCourseOfActionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedCourseOfActionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedCourseOfActionType'):
        super(RelatedCourseOfActionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedCourseOfActionType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedCourseOfActionType', fromsubclass_=False, pretty_print=True):
        super(RelatedCourseOfActionType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Course_Of_Action is not None:
            self.Course_Of_Action.export(lwrite, level, nsmap, namespace_, name_='Course_Of_Action', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedCourseOfActionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Course_Of_Action':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "CourseOfActionType":
                    import stix.bindings.course_of_action as coa_binding
                    obj_ = coa_binding.CourseOfActionType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = CourseOfActionBaseType.factory() # not abstract

            obj_.build(child_)
            self.set_Course_Of_Action(obj_)
        super(RelatedCourseOfActionType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedCourseOfActionType

class RelatedExploitTargetType(GenericRelationshipType):
    """Identifies or characterizes a relationship to an exploit target."""
    subclass = None
    superclass = GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, Exploit_Target=None):
        super(RelatedExploitTargetType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.Exploit_Target = Exploit_Target
    def factory(*args_, **kwargs_):
        if RelatedExploitTargetType.subclass:
            return RelatedExploitTargetType.subclass(*args_, **kwargs_)
        else:
            return RelatedExploitTargetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Exploit_Target(self): return self.Exploit_Target
    def set_Exploit_Target(self, Exploit_Target): self.Exploit_Target = Exploit_Target
    def hasContent_(self):
        if (
            self.Exploit_Target is not None or
            super(RelatedExploitTargetType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedExploitTargetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedExploitTargetType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedExploitTargetType'):
        super(RelatedExploitTargetType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedExploitTargetType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedExploitTargetType', fromsubclass_=False, pretty_print=True):
        super(RelatedExploitTargetType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Exploit_Target is not None:
            self.Exploit_Target.export(lwrite, level, nsmap, namespace_, name_='Exploit_Target', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedExploitTargetType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Exploit_Target':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "ExploitTargetType":
                    import stix.bindings.exploit_target as et_binding
                    obj_ = et_binding.ExploitTargetType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = ExploitTargetBaseType.factory() # not abstract

            obj_.build(child_)
            self.set_Exploit_Target(obj_)
        super(RelatedExploitTargetType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedExploitTargetType

class RelatedIncidentType(GenericRelationshipType):
    """Identifies or characterizes a relationship to an incident."""
    subclass = None
    superclass = GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, Incident=None):
        super(RelatedIncidentType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.Incident = Incident
    def factory(*args_, **kwargs_):
        if RelatedIncidentType.subclass:
            return RelatedIncidentType.subclass(*args_, **kwargs_)
        else:
            return RelatedIncidentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Incident(self): return self.Incident
    def set_Incident(self, Incident): self.Incident = Incident
    def hasContent_(self):
        if (
            self.Incident is not None or
            super(RelatedIncidentType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIncidentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedIncidentType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedIncidentType'):
        super(RelatedIncidentType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedIncidentType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIncidentType', fromsubclass_=False, pretty_print=True):
        super(RelatedIncidentType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Incident is not None:
            self.Incident.export(lwrite, level, nsmap, namespace_, name_='Incident', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedIncidentType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Incident':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "IncidentType":
                    import stix.bindings.incident as incident_binding
                    obj_ = incident_binding.IncidentType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = IncidentBaseType.factory() # not abstract

            obj_.build(child_)
            self.set_Incident(obj_)
        super(RelatedIncidentType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedIncidentType

class RelatedIndicatorType(GenericRelationshipType):
    """Identifies or characterizes a relationship to an indicator."""
    subclass = None
    superclass = GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, Indicator=None):
        super(RelatedIndicatorType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.Indicator = Indicator
    def factory(*args_, **kwargs_):
        if RelatedIndicatorType.subclass:
            return RelatedIndicatorType.subclass(*args_, **kwargs_)
        else:
            return RelatedIndicatorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Indicator(self): return self.Indicator
    def set_Indicator(self, Indicator): self.Indicator = Indicator
    def hasContent_(self):
        if (
            self.Indicator is not None or
            super(RelatedIndicatorType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIndicatorType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedIndicatorType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedIndicatorType'):
        super(RelatedIndicatorType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedIndicatorType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIndicatorType', fromsubclass_=False, pretty_print=True):
        super(RelatedIndicatorType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Indicator is not None:
            self.Indicator.export(lwrite, level, nsmap, namespace_, name_='Indicator', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedIndicatorType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Indicator':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "IndicatorType":
                    import stix.bindings.indicator as indicator_binding
                    obj_ = indicator_binding.IndicatorType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = IndicatorBaseType.factory() # not abstract

            obj_.build(child_)
            self.set_Indicator(obj_)
        super(RelatedIndicatorType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedIndicatorType

class RelatedObservableType(GenericRelationshipType):
    """Identifies or characterizes a relationship to a cyber observable."""
    subclass = None
    superclass = GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, Observable=None):
        super(RelatedObservableType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.Observable = Observable
    def factory(*args_, **kwargs_):
        if RelatedObservableType.subclass:
            return RelatedObservableType.subclass(*args_, **kwargs_)
        else:
            return RelatedObservableType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Observable(self): return self.Observable
    def set_Observable(self, Observable): self.Observable = Observable
    def hasContent_(self):
        if (
            self.Observable is not None or
            super(RelatedObservableType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedObservableType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedObservableType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedObservableType'):
        super(RelatedObservableType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedObservableType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedObservableType', fromsubclass_=False, pretty_print=True):
        super(RelatedObservableType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Observable is not None:
            self.Observable.export(lwrite, level, "%s:" % (nsmap[namespace_]), name_='Observable', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedObservableType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Observable':
            obj_ = cybox_core_binding.ObservableType.factory()
            obj_.build(child_)
            self.set_Observable(obj_)
        super(RelatedObservableType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedObservableType

class RelatedThreatActorType(GenericRelationshipType):
    """Identifies or characterizes a relationship to a threat actor."""
    subclass = None
    superclass = GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, Threat_Actor=None):
        super(RelatedThreatActorType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.Threat_Actor = Threat_Actor
    def factory(*args_, **kwargs_):
        if RelatedThreatActorType.subclass:
            return RelatedThreatActorType.subclass(*args_, **kwargs_)
        else:
            return RelatedThreatActorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Threat_Actor(self): return self.Threat_Actor
    def set_Threat_Actor(self, Threat_Actor): self.Threat_Actor = Threat_Actor
    def hasContent_(self):
        if (
            self.Threat_Actor is not None or
            super(RelatedThreatActorType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedThreatActorType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedThreatActorType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedThreatActorType'):
        super(RelatedThreatActorType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedThreatActorType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedThreatActorType', fromsubclass_=False, pretty_print=True):
        super(RelatedThreatActorType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Threat_Actor is not None:
            self.Threat_Actor.export(lwrite, level, nsmap, namespace_, name_='Threat_Actor', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedThreatActorType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Threat_Actor':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "ThreatActorType":
                    import stix.bindings.threat_actor as ta_binding
                    obj_ = ta_binding.ThreatActorType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = ThreatActorBaseType.factory() # not abstract

            obj_.build(child_)
            self.set_Threat_Actor(obj_)
        super(RelatedThreatActorType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedThreatActorType

class RelatedTTPType(GenericRelationshipType):
    """Identifies or characterizes a relationship to an TTP."""
    subclass = None
    superclass = GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, TTP=None):
        super(RelatedTTPType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.TTP = TTP
    def factory(*args_, **kwargs_):
        if RelatedTTPType.subclass:
            return RelatedTTPType.subclass(*args_, **kwargs_)
        else:
            return RelatedTTPType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_TTP(self): return self.TTP
    def set_TTP(self, TTP): self.TTP = TTP
    def hasContent_(self):
        if (
            self.TTP is not None or
            super(RelatedTTPType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedTTPType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedTTPType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedTTPType'):
        super(RelatedTTPType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedTTPType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedTTPType', fromsubclass_=False, pretty_print=True):
        super(RelatedTTPType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.TTP is not None:
            self.TTP.export(lwrite, level, nsmap, namespace_, name_='TTP', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedTTPType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'TTP':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "TTPType":
                    import stix.bindings.ttp as ttp_binding
                    obj_ = ttp_binding.TTPType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = TTPBaseType.factory() # not abstract

            obj_.build(child_)
            self.set_TTP(obj_)
        super(RelatedTTPType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedTTPType

class RelatedIdentityType(GenericRelationshipType):
    """Identifies or characterizes a relationship to an Identity."""
    subclass = None
    superclass = GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, Identity=None):
        super(RelatedIdentityType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.Identity = Identity
    def factory(*args_, **kwargs_):
        if RelatedIdentityType.subclass:
            return RelatedIdentityType.subclass(*args_, **kwargs_)
        else:
            return RelatedIdentityType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Identity(self): return self.Identity
    def set_Identity(self, Identity): self.Identity = Identity
    def hasContent_(self):
        if (
            self.Identity is not None or
            super(RelatedIdentityType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIdentityType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedIdentityType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedIdentityType'):
        super(RelatedIdentityType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedIdentityType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIdentityType', fromsubclass_=False, pretty_print=True):
        super(RelatedIdentityType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Identity is not None:
            self.Identity.export(lwrite, level, nsmap, namespace_, name_='Identity', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedIdentityType, self).buildAttributes(node, attrs, already_processed)
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
                obj_ = IdentityType.factory() # IdentityType is not abstract

            obj_.build(child_)
            self.set_Identity(obj_)
        super(RelatedIdentityType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedIdentityType

class IndicatorBaseType(GeneratedsSuper):
    """This type represents the STIX Indicator component. It is extended
    using the XML Schema Extension feature by the STIX Indicator
    type itself. Users of this type who wish to express a full
    indicator using STIX must do so using the xsi:type extension
    feature. The STIX-defined Indicator type is IndicatorType in the
    http://stix.mitre.org/Indicator-1 namespace. This type is
    defined in the indicator.xsd file or at the URL
    http://stix.mitre.org/XMLSchema/indicator/1.2/indicator.xsd.
    Alternatively, uses that require simply specifying an idref as a
    reference to an indicator defined elsewhere can do so without
    specifying an xsi:type. Specifies a unique ID for this
    Indicator.Specifies a reference to the ID of an Indicator
    specified elsewhere."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, timestamp=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.timestamp = _cast(None, timestamp)
    def factory(*args_, **kwargs_):
        if IndicatorBaseType.subclass:
            return IndicatorBaseType.subclass(*args_, **kwargs_)
        else:
            return IndicatorBaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IndicatorBaseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IndicatorBaseType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='IndicatorBaseType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IndicatorBaseType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IndicatorBaseType

class IncidentBaseType(GeneratedsSuper):
    """This type represents the STIX Incident component. It is extended
    using the XML Schema Extension feature by the STIX Incident type
    itself. Users of this type who wish to express a full incident
    using STIX must do so using the xsi:type extension feature. The
    STIX-defined Incident type is IncidentType in the
    http://stix.mitre.org/Incident-1 namespace. This type is defined
    in the incident.xsd file or at the URL http://stix.mitre.org/XML
    Schema/incident/1.1/incident.xsd.Alternatively, uses that
    require simply specifying an idref as a reference to an incident
    defined elsewhere can do so without specifying an
    xsi:type.Specifies a globally unique identifier for this cyber
    threat Incident.Specifies a globally unique identifier for a
    cyber threat Incident specified elsewhere.When idref is
    specified, the id attribute must not be specified, and any
    instance of this Incident should not hold content.In conjunction
    with the idref, this field may be used to reference a specific
    version of an incident defined elsewhere. The referenced version
    timestamp is contained in the
    Information_Source/Time/Produced_Time field of the related
    incident and must be an exact match.This field must only be used
    in conjunction with the idref field."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, timestamp=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.timestamp = _cast(None, timestamp)
        pass
    def factory(*args_, **kwargs_):
        if IncidentBaseType.subclass:
            return IncidentBaseType.subclass(*args_, **kwargs_)
        else:
            return IncidentBaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IncidentBaseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IncidentBaseType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='IncidentBaseType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IncidentBaseType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class IncidentBaseType


class TTPBaseType(GeneratedsSuper):
    """This type represents the STIX TTP component. It is extended using
    the XML Schema Extension feature by the STIX TTP type itself.
    Users of this type who wish to express a full TTP using STIX
    must do so using the xsi:type extension feature. The STIX-
    defined TTP type is TTPType in the http://stix.mitre.org/TTP-1
    namespace. This type is defined in the ttp.xsd file or at the
    URL
    http://stix.mitre.org/XMLSchema/ttp/1.1/ttp.xsd.Alternatively,
    uses that require simply specifying an idref as a reference to a
    TTP defined elsewhere can do so without specifying an
    xsi:type.Specifies a globally unique identifier for this TTP
    item. Specifies a globally unique identifier of a TTP item
    specified elsewhere.When idref is specified, the id attribute
    must not be specified, and any instance of this TTP item should
    not hold content.In conjunction with the idref, this field may
    be used to reference a specific version of a TTP defined
    elsewhere. The referenced version timestamp is contained in the
    Information_Source/Time/Produced_Time field of the related TTP
    and must be an exact match.This field must only be used in
    conjunction with the idref field."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, timestamp=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.timestamp = _cast(None, timestamp)
        pass
    def factory(*args_, **kwargs_):
        if TTPBaseType.subclass:
            return TTPBaseType.subclass(*args_, **kwargs_)
        else:
            return TTPBaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TTPBaseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TTPBaseType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='TTPBaseType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TTPBaseType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class TTPBaseType

class ExploitTargetBaseType(GeneratedsSuper):
    """This type represents the STIX Exploit Target component. It is
    extended using the XML Schema Extension feature by the STIX
    Exploit Target type itself. Users of this type who wish to
    express a full exploit target using STIX must do so using the
    xsi:type extension feature. The STIX-defined Exploit Target type
    is ExploitTargetType in the
    http://stix.mitre.org/ExploitTarget-1 namespace. This type is
    defined in the exploit_target.xsd file or at the URL http://stix
    .mitre.org/XMLSchema/exploit_target/1.1/exploit_target.xsd.Alter
    natively, uses that require simply specifying an idref as a
    reference to an exploit target defined elsewhere can do so
    without specifying an xsi:type.Specifies a globally unique
    identifier for this ExploitTarget. Specifies a globally unique
    identifier of an ExploitTarget specified elsewhere.When idref is
    specified, the id attribute must not be specified, and any
    instance of this ExploitTarget should not hold content.In
    conjunction with the idref, this field may be used to reference
    a specific version of an exploit target defined elsewhere. The
    referenced version timestamp is contained in the
    Information_Source/Time/Produced_Time field of the related
    exploit target and must be an exact match.This field must only
    be used in conjunction with the idref field."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, timestamp=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.timestamp = _cast(None, timestamp)
        pass
    def factory(*args_, **kwargs_):
        if ExploitTargetBaseType.subclass:
            return ExploitTargetBaseType.subclass(*args_, **kwargs_)
        else:
            return ExploitTargetBaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExploitTargetBaseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ExploitTargetBaseType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='ExploitTargetBaseType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExploitTargetBaseType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ExploitTargetBaseType

class CourseOfActionBaseType(GeneratedsSuper):
    """This type represents the STIX Course of Action component. It is
    extended using the XML Schema Extension feature by the STIX
    Course of Action type itself. Users of this type who wish to
    express a full course of action using STIX must do so using the
    xsi:type extension feature. The STIX-defined Course of Action
    type is CourseOfActionType in the
    http://stix.mitre.org/CourseOfAction-1 namespace. This type is
    defined in the course_of_action.xsd file or at the URL http://st
    ix.mitre.org/XMLSchema/course_of_action/1.1/course_of_action.xsd
    .Alternatively, uses that require simply specifying an idref as
    a reference to a course of action defined elsewhere can do so
    without specifying an xsi:type.Specifies a globally unique
    identifier for this COA. Specifies a globally unique identifier
    of a COA specified elsewhere.When idref is specified, the id
    attribute must not be specified, and any instance of this COA
    should not hold content.In conjunction with the idref, this
    field may be used to reference a specific version of a course of
    action defined elsewhere. The referenced version timestamp is
    contained in the Information_Source/Time/Produced_Time field of
    the related course of action and must be an exact match.This
    field must only be used in conjunction with the idref field."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, timestamp=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.timestamp = _cast(None, timestamp)
        pass
    def factory(*args_, **kwargs_):
        if CourseOfActionBaseType.subclass:
            return CourseOfActionBaseType.subclass(*args_, **kwargs_)
        else:
            return CourseOfActionBaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CourseOfActionBaseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CourseOfActionBaseType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='CourseOfActionBaseType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CourseOfActionBaseType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class CourseOfActionBaseType

class RelatedCampaignReferenceType(GenericRelationshipType):
    """Identifies or characterizes a relationship by reference to a
    campaign."""
    subclass = None
    superclass = GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, Campaign=None):
        super(RelatedCampaignReferenceType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.Campaign = Campaign
    def factory(*args_, **kwargs_):
        if RelatedCampaignReferenceType.subclass:
            return RelatedCampaignReferenceType.subclass(*args_, **kwargs_)
        else:
            return RelatedCampaignReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Campaign(self): return self.Campaign
    def set_Campaign(self, Campaign): self.Campaign = Campaign
    def hasContent_(self):
        if (
            self.Campaign is not None or
            super(RelatedCampaignReferenceType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedCampaignReferenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedCampaignReferenceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedCampaignReferenceType'):
        super(RelatedCampaignReferenceType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedCampaignReferenceType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedCampaignReferenceType', fromsubclass_=False, pretty_print=True):
        super(RelatedCampaignReferenceType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Campaign is not None:
            self.Campaign.export(lwrite, level, nsmap, namespace_, name_='Campaign', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedCampaignReferenceType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Campaign':
            obj_ = CampaignReferenceType.factory()
            obj_.build(child_)
            self.set_Campaign(obj_)
        super(RelatedCampaignReferenceType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedCampaignReferenceType

class CampaignReferenceType(GeneratedsSuper):
    """Characterizes a reference to a campaign.Specifies a globally unique
    identifier for a cyber threat campaign defined elsewhere.In
    conjunction with the idref, this field may be used to reference
    a specific version of a campaign defined elsewhere. The
    referenced version timestamp is contained in the
    Information_Source/Time/Produced_Time field of the related
    campaign and must be an exact match.This field must only be used
    in conjunction with the idref field."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, timestamp=None, Names=None):
        self.idref = _cast(None, idref)
        self.timestamp = _cast(None, timestamp)
        self.Names = Names
    def factory(*args_, **kwargs_):
        if CampaignReferenceType.subclass:
            return CampaignReferenceType.subclass(*args_, **kwargs_)
        else:
            return CampaignReferenceType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Names(self): return self.Names
    def set_Names(self, Names): self.Names = Names
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def hasContent_(self):
        if (
            self.Names is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CampaignReferenceType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CampaignReferenceType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='CampaignReferenceType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CampaignReferenceType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Names is not None:
            self.Names.export(lwrite, level, nsmap, namespace_, name_='Names', pretty_print=pretty_print)
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
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Names':
            obj_ = NamesType.factory()
            obj_.build(child_)
            self.set_Names(obj_)
# end class CampaignReferenceType

class NamesType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Name=None):
        if Name is None:
            self.Name = []
        else:
            self.Name = Name
    def factory(*args_, **kwargs_):
        if NamesType.subclass:
            return NamesType.subclass(*args_, **kwargs_)
        else:
            return NamesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Name(self): return self.Name
    def set_Name(self, Name): self.Name = Name
    def add_Name(self, value): self.Name.append(value)
    def insert_Name(self, index, value): self.Name[index] = value
    def hasContent_(self):
        if (
            self.Name
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='NamesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NamesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='NamesType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='NamesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Name_ in self.Name:
            Name_.export(lwrite, level, nsmap, namespace_, name_='Name', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Name':
            obj_ = ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Name.append(obj_)
# end class NamesType

class CampaignBaseType(GeneratedsSuper):
    """This type represents the STIX Campaign component. It is extended
    using the XML Schema Extension feature by the STIX Campaign type
    itself. Users of this type who wish to express a full campaign
    using STIX must do so using the xsi:type extension feature. The
    STIX-defined Campaign type is CampaignType in the
    http://stix.mitre.org/Campaign-1 namespace. This type is defined
    in the campaign.xsd file or at the URL http://stix.mitre.org/XML
    Schema/campaign/1.1/campaign.xsd.Alternatively, uses that
    require simply specifying an idref as a reference to a campaign
    defined elsewhere can do so without specifying an
    xsi:type.Specifies a globally unique identifier for this cyber
    threat Campaign.Specifies a globally unique identifier for a
    cyber threat Campaign specified elsewhere.When idref is
    specified, the id attribute must not be specified, and any
    instance of this Campaign should not hold content.In conjunction
    with the idref, this field may be used to reference a specific
    version of a campaign defined elsewhere. The referenced version
    timestamp is contained in the
    Information_Source/Time/Produced_Time field of the related
    campaign and must be an exact match.This field must only be used
    in conjunction with the idref field."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, timestamp=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.timestamp = _cast(None, timestamp)
        pass
    def factory(*args_, **kwargs_):
        if CampaignBaseType.subclass:
            return CampaignBaseType.subclass(*args_, **kwargs_)
        else:
            return CampaignBaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CampaignBaseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CampaignBaseType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='CampaignBaseType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CampaignBaseType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class CampaignBaseType


class ThreatActorBaseType(GeneratedsSuper):
    """This type represents the STIX Threat Actor component. It is extended
    using the XML Schema Extension feature by the STIX Threat Actor
    type itself. Users of this type who wish to express a full
    threat actor using STIX must do so using the xsi:type extension
    feature. The STIX-defined Threat Actor type is ThreatActorType
    in the http://stix.mitre.org/ThreatActor-1 namespace. This type
    is defined in the threat_actor.xsd file or at the URL http://sti
    x.mitre.org/XMLSchema/threat_actor/1.1/threat_actor.xsd.Alternat
    ively, uses that require simply specifying an idref as a
    reference to a threat actor defined elsewhere can do so without
    specifying an xsi:type.Specifies a globally unique identifier
    for this ThreatActor. Specifies a globally unique identifier of
    a ThreatActor specified elsewhere.When idref is specified, the
    id attribute must not be specified, and any instance of this
    ThreatActor should not hold content.In conjunction with the
    idref, this field may be used to reference a specific version of
    a threat actor defined elsewhere. The referenced version
    timestamp is contained in the
    Information_Source/Time/Produced_Time field of the related
    threat actor and must be an exact match.This field must only be
    used in conjunction with the idref field."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, timestamp=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.timestamp = _cast(None, timestamp)
        pass
    def factory(*args_, **kwargs_):
        if ThreatActorBaseType.subclass:
            return ThreatActorBaseType.subclass(*args_, **kwargs_)
        else:
            return ThreatActorBaseType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ThreatActorBaseType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ThreatActorBaseType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='ThreatActorBaseType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ThreatActorBaseType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('id', node)
        if value is not None and 'id' not in already_processed:
            already_processed.add('id')
            self.id = value
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ThreatActorBaseType


class ExploitTargetsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Exploit_Target=None):
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
            self.Exploit_Target
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
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='ExploitTargetsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExploitTargetsType', fromsubclass_=False, pretty_print=True):
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
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Exploit_Target':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "ExploitTargetType":
                    import stix.bindings.exploit_target as exploit_target_binding
                    obj_ = exploit_target_binding.ExploitTargetType.factory()
                else:
                    raise NotImplementedError('Class not implemented for element type: ' + type_name_)
            else:
                obj_ = ExploitTargetBaseType.factory() # not abstract

            obj_.build(child_)
            self.Exploit_Target.append(obj_)

# end class ExploitTargetsType


class AddressAbstractType(GeneratedsSuper):
    """The AddressAbstractType is used to express geographic address
    information. This type is intended to be extended through the
    xsi:type mechanism. The default type is
    CIQAddress3.0InstanceType in the
    http://stix.mitre.org/extensions/Address#CIQAddress3.0-1
    namespace. This type is defined in the
    extensions/identity/ciq_address_3.0.xsd file or at the URL http:
    //stix.mitre.org/XMLSchema/extensions/address/ciq_address_3.0/1.
    0/ciq_address_3.0.xsd."""
    subclass = None
    superclass = None
    def __init__(self):
        pass
    def factory(*args_, **kwargs_):
        if AddressAbstractType.subclass:
            return AddressAbstractType.subclass(*args_, **kwargs_)
        else:
            return AddressAbstractType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AddressAbstractType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AddressAbstractType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='AddressAbstractType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AddressAbstractType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class AddressAbstractType

class ContributingSourcesType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Source=None):
        if Source is None:
            self.Source = []
        else:
            self.Source = Source
    def factory(*args_, **kwargs_):
        if ContributingSourcesType.subclass:
            return ContributingSourcesType.subclass(*args_, **kwargs_)
        else:
            return ContributingSourcesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Source(self): return self.Source
    def set_Source(self, Source): self.Source = Source
    def add_Source(self, value): self.Source.append(value)
    def insert_Source(self, index, value): self.Source[index] = value
    def hasContent_(self):
        if (
            self.Source
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ContributingSourcesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ContributingSourcesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='ContributingSourcesType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ContributingSourcesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Source_ in self.Source:
            Source_.export(lwrite, level, nsmap, namespace_, name_='Source', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Source':
            obj_ = InformationSourceType.factory()
            obj_.build(child_)
            self.Source.append(obj_)
# end class ContributingSourcesType

class ReferencesType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Reference=None):
        if Reference is None:
            self.Reference = []
        else:
            self.Reference = Reference
    def factory(*args_, **kwargs_):
        if ReferencesType.subclass:
            return ReferencesType.subclass(*args_, **kwargs_)
        else:
            return ReferencesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Reference(self): return self.Reference
    def set_Reference(self, Reference): self.Reference = Reference
    def add_Reference(self, value): self.Reference.append(value)
    def insert_Reference(self, index, value): self.Reference[index] = value
    def hasContent_(self):
        if (
            self.Reference
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ReferencesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ReferencesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='ReferencesType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ReferencesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Reference_ in self.Reference:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Reference>%s</%s:Reference>%s' % (nsmap[namespace_], quote_xml(Reference_), nsmap[namespace_], eol_))
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Reference':
            Reference_ = child_.text
            Reference_ = self.gds_validate_string(Reference_, node, 'Reference')
            self.Reference.append(Reference_)
# end class ReferencesType

class RelatedIdentitiesType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Related_Identity=None):
        if Related_Identity is None:
            self.Related_Identity = []
        else:
            self.Related_Identity = Related_Identity
    def factory(*args_, **kwargs_):
        if RelatedIdentitiesType.subclass:
            return RelatedIdentitiesType.subclass(*args_, **kwargs_)
        else:
            return RelatedIdentitiesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Related_Identity(self): return self.Related_Identity
    def set_Related_Identity(self, Related_Identity): self.Related_Identity = Related_Identity
    def add_Related_Identity(self, value): self.Related_Identity.append(value)
    def insert_Related_Identity(self, index, value): self.Related_Identity[index] = value
    def hasContent_(self):
        if (
            self.Related_Identity
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIdentitiesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedIdentitiesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='RelatedIdentitiesType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIdentitiesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Related_Identity_ in self.Related_Identity:
            Related_Identity_.export(lwrite, level, nsmap, namespace_, name_='Related_Identity', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Related_Identity':
            obj_ = RelatedIdentityType.factory()
            obj_.build(child_)
            self.Related_Identity.append(obj_)
# end class RelatedIdentitiesType

class ConfidenceAssertionChainType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Confidence_Assertion=None):
        if Confidence_Assertion is None:
            self.Confidence_Assertion = []
        else:
            self.Confidence_Assertion = Confidence_Assertion
    def factory(*args_, **kwargs_):
        if ConfidenceAssertionChainType.subclass:
            return ConfidenceAssertionChainType.subclass(*args_, **kwargs_)
        else:
            return ConfidenceAssertionChainType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Confidence_Assertion(self): return self.Confidence_Assertion
    def set_Confidence_Assertion(self, Confidence_Assertion): self.Confidence_Assertion = Confidence_Assertion
    def add_Confidence_Assertion(self, value): self.Confidence_Assertion.append(value)
    def insert_Confidence_Assertion(self, index, value): self.Confidence_Assertion[index] = value
    def hasContent_(self):
        if (
            self.Confidence_Assertion
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ConfidenceAssertionChainType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ConfidenceAssertionChainType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='ConfidenceAssertionChainType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ConfidenceAssertionChainType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Confidence_Assertion_ in self.Confidence_Assertion:
            Confidence_Assertion_.export(lwrite, level, nsmap, namespace_, name_='Confidence_Assertion', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Confidence_Assertion':
            obj_ = ConfidenceType.factory()
            obj_.build(child_)
            self.Confidence_Assertion.append(obj_)
# end class ConfidenceAssertionChainType

class StatementType(GeneratedsSuper):
    """StatementType allows the expression of a statement with an
    associated value, description, source, confidence, and
    timestamp. Specifies the time this statement was asserted.In
    order to avoid ambiguity, it is strongly suggest that all
    timestamps include a specification of the timezone if it is
    known.Represents the precision of the associated timestamp
    value. If omitted, the default is "second", meaning the
    timestamp is precise to the full field value. Digits in the
    timestamp that are required by the xs:dateTime datatype but are
    beyond the specified precision should be zeroed out."""
    subclass = None
    superclass = None
    def __init__(self, timestamp=None, timestamp_precision='second', Value=None, Description=None, Source=None, Confidence=None):
        self.timestamp = _cast(None, timestamp)
        self.timestamp_precision = _cast(None, timestamp_precision)
        self.Value = Value
        self.Description = Description
        self.Source = Source
        self.Confidence = Confidence
    def factory(*args_, **kwargs_):
        if StatementType.subclass:
            return StatementType.subclass(*args_, **kwargs_)
        else:
            return StatementType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Value(self): return self.Value
    def set_Value(self, Value): self.Value = Value
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Source(self): return self.Source
    def set_Source(self, Source): self.Source = Source
    def get_Confidence(self): return self.Confidence
    def set_Confidence(self, Confidence): self.Confidence = Confidence
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def get_timestamp_precision(self): return self.timestamp_precision
    def set_timestamp_precision(self, timestamp_precision): self.timestamp_precision = timestamp_precision
    def hasContent_(self):
        if (
            self.Value is not None or
            self.Description is not None or
            self.Source is not None or
            self.Confidence is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='StatementType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='StatementType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='StatementType'):
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
        if self.timestamp_precision not in (None, 'second') and 'timestamp_precision' not in already_processed:
            already_processed.add('timestamp_precision')
            lwrite(' timestamp_precision=%s' % (quote_attrib(self.timestamp_precision), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='StatementType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Value is not None:
            self.Value.export(lwrite, level, nsmap, namespace_, name_='Value', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Source is not None:
            self.Source.export(lwrite, level, nsmap, namespace_, name_='Source', pretty_print=pretty_print)
        if self.Confidence is not None:
            self.Confidence.export(lwrite, level, nsmap, namespace_, name_='Confidence', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
        value = find_attr_value_('timestamp_precision', node)
        if value is not None and 'timestamp_precision' not in already_processed:
            already_processed.add('timestamp_precision')
            self.timestamp_precision = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Value':
            obj_ = ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Value(obj_)
        elif nodeName_ == 'Description':
            obj_ = StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Source':
            obj_ = InformationSourceType.factory()
            obj_.build(child_)
            self.set_Source(obj_)
        elif nodeName_ == 'Confidence':
            obj_ = ConfidenceType.factory()
            obj_.build(child_)
            self.set_Confidence(obj_)
# end class StatementType

class StructuredTextType(GeneratedsSuper):
    """The StructuredTextType is a type representing a generalized
    structure for capturing structured or unstructured textual
    information such as descriptions of things. It mirrors a similar
    type in CybOX 2.0 used to indicate a particular structuring
    format (e.g., HTML5) used within an instance of StructuredTextType. 
    Note that if the markup tags used by this format would be interpreted 
    as XML information (such as the bracket-based tags of HTML) the text 
    area should be enclosed in a CDATA section to prevent the markup from 
    interferring with XMLvalidation of the CybOX document. If this 
    attribute is absent, the implication is that no markup is being used."""
    subclass = None
    superclass = None
    def __init__(self, structuring_format=None, valueOf_=None):
        self.structuring_format = _cast(None, structuring_format)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if StructuredTextType.subclass:
            return StructuredTextType.subclass(*args_, **kwargs_)
        else:
            return StructuredTextType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_structuring_format(self): return self.structuring_format
    def set_structuring_format(self, structuring_format): self.structuring_format = structuring_format
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='StructuredTextType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='StructuredTextType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='StructuredTextType'):
        if self.structuring_format is not None and 'structuring_format' not in already_processed:
            already_processed.add('structuring_format')
            lwrite(' structuring_format=%s' % (quote_attrib(self.structuring_format), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='StructuredTextType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('structuring_format', node)
        if value is not None and 'structuring_format' not in already_processed:
            already_processed.add('structuring_format')
            self.structuring_format = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class StructuredTextType

class EncodedCDATAType(GeneratedsSuper):
    """This type is used to represent data in an XML CDATA block. Data in a
    CDATA block may either be represented as-is or, in cases where
    it may contain characters that are not valid in CDATA, it may be
    encoded in Base64 per RFC4648. Data encoded in Base64 must be
    denoted as such using the encoded attribute. If true, specifies
    that the content encoded in the element is encoded using Base64
    per RFC4648."""
    subclass = None
    superclass = None
    def __init__(self, encoded=False, valueOf_=None):
        self.encoded = _cast(bool, encoded)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if EncodedCDATAType.subclass:
            return EncodedCDATAType.subclass(*args_, **kwargs_)
        else:
            return EncodedCDATAType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_encoded(self): return self.encoded
    def set_encoded(self, encoded): self.encoded = encoded
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='EncodedCDATAType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EncodedCDATAType')
        if self.hasContent_():
            lwrite('>')

            if self.valueOf_ and not (self.valueOf_.strip().startswith("<![CDATA[")):
                value = CDATA_START + self.valueOf_ + CDATA_END
            else:
                value = self.valueOf_

            lwrite(quote_xml(value))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='EncodedCDATAType'):
        if self.encoded is not None and 'encoded' not in already_processed:
            already_processed.add('encoded')
            lwrite(' encoded="%s"' % self.gds_format_boolean(self.encoded, input_name='encoded'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='EncodedCDATAType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('encoded', node)
        if value is not None and 'encoded' not in already_processed:
            already_processed.add('encoded')
            if value in ('true', '1'):
                self.encoded = True
            elif value in ('false', '0'):
                self.encoded = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class EncodedCDATAType

class ControlledVocabularyStringType(GeneratedsSuper):
    """The ControlledVocabularyStringType is used as the basis for defining
    controlled vocabularies.The vocab_name field specifies the name
    of the controlled vocabulary.The vocab_reference field specifies
    the URI to the location of where the controlled vocabulary is
    defined, e.g., in an externally located XML schema file."""
    subclass = None
    superclass = None
    def __init__(self, vocab_reference=None, vocab_name=None, valueOf_=None, xsi_type=None):
        self.vocab_reference = _cast(None, vocab_reference)
        self.vocab_name = _cast(None, vocab_name)
        self.valueOf_ = valueOf_
        self.xsi_type = xsi_type
    def factory(*args_, **kwargs_):
        if ControlledVocabularyStringType.subclass:
            return ControlledVocabularyStringType.subclass(*args_, **kwargs_)
        else:
            return ControlledVocabularyStringType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_vocab_reference(self): return self.vocab_reference
    def set_vocab_reference(self, vocab_reference): self.vocab_reference = vocab_reference
    def get_vocab_name(self): return self.vocab_name
    def set_vocab_name(self, vocab_name): self.vocab_name = vocab_name
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def get_xsi_type(self): return self.xsi_type
    def set_xsi_type(self, xsi_type): self.xsi_type = xsi_type
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ControlledVocabularyStringType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ControlledVocabularyStringType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stixCommon:', name_='ControlledVocabularyStringType'):
        if self.xsi_type is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            lwrite(' xsi:type=%s' % quote_attrib(self.xsi_type))
        if self.vocab_reference is not None and 'vocab_reference' not in already_processed:
            already_processed.add('vocab_reference')
            lwrite(' vocab_reference=%s' % (quote_attrib(self.vocab_reference), ))
        if self.vocab_name is not None and 'vocab_name' not in already_processed:
            already_processed.add('vocab_name')
            lwrite(' vocab_name=%s' % (quote_attrib(self.vocab_name), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ControlledVocabularyStringType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('vocab_reference', node)
        if value is not None and 'vocab_reference' not in already_processed:
            already_processed.add('vocab_reference')
            self.vocab_reference = value
        value = find_attr_value_('vocab_name', node)
        if value is not None and 'vocab_name' not in already_processed:
            already_processed.add('vocab_name')
            self.vocab_name = value
        value = find_attr_value_('xsi:type', node)
        if value is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            self.xsi_type = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ControlledVocabularyStringType

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
        rootTag = 'InformationSourceType'
        rootClass = InformationSourceType
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
        rootTag = 'InformationSourceType'
        rootClass = InformationSourceType
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
        rootTag = 'InformationSourceType'
        rootClass = InformationSourceType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="InformationSourceType",
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
    "GenericRelationshipType",
    "DateTimeWithPrecisionType",
    "ProfilesType",
    "RelatedPackageRefType",
    "RelatedPackageRefsType",
    "ToolInformationType",
    "InformationSourceType",
    "ConfidenceType",
    "ActivityType",
    "KillChainsType",
    "KillChainType",
    "KillChainPhaseType",
    "KillChainPhasesReferenceType",
    "KillChainPhaseReferenceType",
    "IdentityType",
    "GenericRelationshipListType",
    "RelatedCampaignType",
    "RelatedCourseOfActionType",
    "RelatedExploitTargetType",
    "RelatedIncidentType",
    "RelatedIndicatorType",
    "RelatedObservableType",
    "RelatedThreatActorType",
    "RelatedTTPType",
    "RelatedIdentityType",
    "IndicatorBaseType",
    "IncidentBaseType",
    "TTPBaseType",
    "ExploitTargetBaseType",
    "CourseOfActionBaseType",
    "RelatedCampaignReferenceType",
    "CampaignReferenceType",
    "NamesType",
    "CampaignBaseType",
    "ThreatActorBaseType",
    "ExploitTargetsType",
    "AddressAbstractType",
    "ContributingSourcesType",
    "ReferencesType",
    "RelatedIdentitiesType",
    "ConfidenceAssertionChainType",
    "StatementType",
    "StructuredTextType",
    "EncodedCDATAType",
    "ControlledVocabularyStringType"
    ]
