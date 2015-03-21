# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:06:21 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import cybox.bindings.cybox_core as cybox_core_binding
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.data_marking as data_marking_binding

XML_NS = "http://stix.mitre.org/CourseOfAction-1"

#
# Data representation classes.
#

class StructuredCOAType(GeneratedsSuper):
    """The StructuredCOAType enables the specification of an actionable
    structured representation for the CourseOfAction potentially for
    automated consumption and implementation. This type is defined
    as an abstract type and is intended to be extended using the XML
    Schema extension mechanism to allow for the expression of a
    variety of structured COA types. Instance documents representing
    structured COAs use the xsi:type attribute to specify which
    implementation of this type they wish to use. STIX has provided
    one implementation to allow for the passing of proprietary or
    externally defined structured courses of action in a CDATA
    block. This implementation is captured in the Generic Structured
    COA extension, which provides the GenericStructuredCOAType in
    the http://stix.mitre.org/extensions/StructuredCOA#Generic-1
    namespace. The extension is defined in the
    extensions/structured_coa/generic.xsd file or at the URL http://
    stix.mitre.org/XMLSchema/extensions/structured_coa/generic/1.0/g
    eneric.xsd. Specifies a unique ID for this
    StructuredCOA.Specifies a reference to the ID for this
    StructuredCOA specified elsewhere."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None):
        self.xmlns          = "http://stix.mitre.org/CourseOfAction-1"
        self.xmlns_prefix   = "coa"
        self.xml_type       = "CourseOfActionType"
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        pass
    def factory(*args_, **kwargs_):
        if StructuredCOAType.subclass:
            return StructuredCOAType.subclass(*args_, **kwargs_)
        else:
            return StructuredCOAType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='StructuredCOAType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='StructuredCOAType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='coa:', name_='StructuredCOAType'):
        # if 'xmlns' not in already_processed:
        #     already_processed.add('xmlns')
        #     xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
        #     lwrite(xmlns)
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
            lwrite(xsi_type)
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='StructuredCOAType', fromsubclass_=False, pretty_print=True):
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
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class StructuredCOAType

class ObjectiveType(GeneratedsSuper):
    """The ObjectiveType characterizes the objective of this
    CourseOfAction."""
    subclass = None
    superclass = None
    def __init__(self, Description=None, Short_Description=None, Applicability_Confidence=None):
        self.Description = Description
        self.Short_Description = Short_Description
        self.Applicability_Confidence = Applicability_Confidence
    def factory(*args_, **kwargs_):
        if ObjectiveType.subclass:
            return ObjectiveType.subclass(*args_, **kwargs_)
        else:
            return ObjectiveType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_Applicability_Confidence(self): return self.Applicability_Confidence
    def set_Applicability_Confidence(self, Applicability_Confidence): self.Applicability_Confidence = Applicability_Confidence
    def hasContent_(self):
        if (
            self.Description is not None or
            self.Applicability_Confidence is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ObjectiveType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ObjectiveType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='coa:', name_='ObjectiveType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ObjectiveType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Short_Description is not None:
            self.Short_Description.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
        if self.Applicability_Confidence is not None:
            self.Applicability_Confidence.export(lwrite, level, nsmap, namespace_, name_='Applicability_Confidence', pretty_print=pretty_print)
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
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Short_Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Short_Description(obj_)
        elif nodeName_ == 'Applicability_Confidence':
            obj_ = stix_common_binding.ConfidenceType.factory()
            obj_.build(child_)
            self.set_Applicability_Confidence(obj_)
# end class ObjectiveType

class CourseOfActionType(stix_common_binding.CourseOfActionBaseType):
    """The CourseOfActionType characterizes a Course of Action to be taken
    in regards to one of more cyber threats. NOTE: This construct is
    still in its early stages of maturity and will require a good
    deal of review and refinement.Specifies the relevant STIX-COA
    schema version for this content."""
    subclass = None
    superclass = stix_common_binding.CourseOfActionBaseType
    def __init__(self, idref=None, id=None, timestamp=None, version=None, Title=None, Stage=None, Type=None, Description=None, Short_Description=None, Objective=None, Parameter_Observables=None, Structured_COA=None, Impact=None, Cost=None, Efficacy=None, Information_Source=None, Handling=None, Related_COAs=None, Related_Packages=None):
        super(CourseOfActionType, self).__init__(idref=idref, id=id, timestamp=timestamp)
        self.xmlns          = "http://stix.mitre.org/CourseOfAction-1"
        self.xmlns_prefix   = "coa"
        self.xml_type       = "CourseOfActionType"
        self.version = _cast(None, version)
        self.Title = Title
        self.Stage = Stage
        self.Type = Type
        self.Description = Description
        self.Short_Description = Short_Description
        self.Objective = Objective
        self.Parameter_Observables = Parameter_Observables
        self.Structured_COA = Structured_COA
        self.Impact = Impact
        self.Cost = Cost
        self.Efficacy = Efficacy
        self.Information_Source = Information_Source
        self.Handling = Handling
        self.Related_COAs = Related_COAs
        self.Related_Packages = Related_Packages
    def factory(*args_, **kwargs_):
        if CourseOfActionType.subclass:
            return CourseOfActionType.subclass(*args_, **kwargs_)
        else:
            return CourseOfActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Stage(self): return self.Stage
    def set_Stage(self, Stage): self.Stage = Stage
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_Objective(self): return self.Objective
    def set_Objective(self, Objective): self.Objective = Objective
    def get_Parameter_Observables(self): return self.Parameter_Observables
    def set_Parameter_Observables(self, Parameter_Observables): self.Parameter_Observables = Parameter_Observables
    def get_Structured_COA(self): return self.Structured_COA
    def set_Structured_COA(self, Structured_COA): self.Structured_COA = Structured_COA
    def get_Impact(self): return self.Impact
    def set_Impact(self, Impact): self.Impact = Impact
    def get_Cost(self): return self.Cost
    def set_Cost(self, Cost): self.Cost = Cost
    def get_Efficacy(self): return self.Efficacy
    def set_Efficacy(self, Efficacy): self.Efficacy = Efficacy
    def get_Information_Source(self): return self.Information_Source
    def set_Information_Source(self, Information_Source): self.Information_Source = Information_Source
    def get_Handling(self): return self.Handling
    def set_Handling(self, Handling): self.Handling = Handling
    def get_Related_COAs(self): return self.Related_COAs
    def set_Related_COAs(self, Related_COAs): self.Related_COAs = Related_COAs
    def get_Related_Packages(self): return self.Related_Packages
    def set_Related_Packages(self, Related_Packages): self.Related_Packages = Related_Packages
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Stage is not None or
            self.Type is not None or
            self.Description is not None or
            self.Short_Description is not None or
            self.Objective is not None or
            self.Parameter_Observables is not None or
            self.Structured_COA is not None or
            self.Impact is not None or
            self.Cost is not None or
            self.Efficacy is not None or
            self.Information_Source is not None or
            self.Handling is not None or
            self.Related_COAs is not None or
            self.Related_Packages is not None or
            super(CourseOfActionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='Course_Of_Action', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='Course_Of_Action')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='coa:', name_='Course_Of_Action'):
        super(CourseOfActionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='Course_Of_Action')
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
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CourseOfActionType', fromsubclass_=False, pretty_print=True):
        super(CourseOfActionType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_], quote_xml(self.Title), nsmap[namespace_], eol_))
        if self.Stage is not None:
            self.Stage.export(lwrite, level, nsmap, namespace_, name_='Stage', pretty_print=pretty_print)
        if self.Type is not None:
            self.Type.export(lwrite, level, nsmap, namespace_, name_='Type', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Short_Description is not None:
            self.Short_Description.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
        if self.Objective is not None:
            self.Objective.export(lwrite, level, nsmap, namespace_, name_='Objective', pretty_print=pretty_print)
        if self.Parameter_Observables is not None:
            self.Parameter_Observables.export(lwrite, level, "%s:" % (nsmap[namespace_]), name_='Parameter_Observables', pretty_print=pretty_print)
        if self.Structured_COA is not None:
            self.Structured_COA.export(lwrite, level, nsmap, namespace_, name_='Structured_COA', pretty_print=pretty_print)
        if self.Impact is not None:
            self.Impact.export(lwrite, level, nsmap, namespace_, name_='Impact', pretty_print=pretty_print)
        if self.Cost is not None:
            self.Cost.export(lwrite, level, nsmap, namespace_, name_='Cost', pretty_print=pretty_print)
        if self.Efficacy is not None:
            self.Efficacy.export(lwrite, level, nsmap, namespace_, name_='Efficacy', pretty_print=pretty_print)
        if self.Information_Source is not None:
            self.Information_Source.export(lwrite, level, nsmap, namespace_, name_='Information_Source', pretty_print=pretty_print)
        if self.Handling is not None:
            self.Handling.export(lwrite, level, nsmap, namespace_, name_='Handling', pretty_print=pretty_print)
        if self.Related_COAs is not None:
            self.Related_COAs.export(lwrite, level, nsmap, namespace_, name_='Related_COAs', pretty_print=pretty_print)
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
        super(CourseOfActionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'Stage':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Stage(obj_)
        elif nodeName_ == 'Type':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Short_Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Short_Description(obj_)
        elif nodeName_ == 'Objective':
            obj_ = ObjectiveType.factory()
            obj_.build(child_)
            self.set_Objective(obj_)
        elif nodeName_ == "Parameter_Observables":
            obj_ = cybox_core_binding.ObservablesType.factory()
            obj_.build(child_)
            self.set_Parameter_Observables(obj_)
        elif nodeName_ == 'Structured_COA':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "GenericStructuredCOAType":
                    from .extensions.structured_coa import generic
                    obj_ = generic.GenericStructuredCOAType.factory()
                else:
                    raise NotImplementedError('No implementation class for Structured_COA: ' + type_name_)
            else:
                raise NotImplementedError('Structured_COA type not declared: missing xsi_type attribute') 

            obj_.build(child_)
            self.set_Structured_COA(obj_)
        elif nodeName_ == 'Impact':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.set_Impact(obj_)
        elif nodeName_ == 'Cost':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.set_Cost(obj_)
        elif nodeName_ == 'Efficacy':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.set_Efficacy(obj_)
        elif nodeName_ == 'Information_Source':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Information_Source(obj_)
        elif nodeName_ == 'Handling':
            obj_ = data_marking_binding.MarkingType.factory()
            obj_.build(child_)
            self.set_Handling(obj_)
        elif nodeName_ == 'Related_COAs':
            obj_ = RelatedCOAsType.factory()
            obj_.build(child_)
            self.set_Related_COAs(obj_)
        elif nodeName_ == 'Related_Packages':
            obj_ = stix_common_binding.RelatedPackageRefsType.factory()
            obj_.build(child_)
            self.set_Related_Packages(obj_)
        super(CourseOfActionType, self).buildChildren(child_, node, nodeName_, True)
# end class CourseOfActionType


class RelatedCOAsType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Related_COA=None):
        super(RelatedCOAsType, self).__init__(scope=scope)
        if Related_COA is None:
            self.Related_COA = []
        else:
            self.Related_COA = Related_COA
    def factory(*args_, **kwargs_):
        if RelatedCOAsType.subclass:
            return RelatedCOAsType.subclass(*args_, **kwargs_)
        else:
            return RelatedCOAsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Related_COA(self): return self.Related_COA
    def set_Related_COA(self, Related_COA): self.Related_COA = Related_COA
    def add_Related_COA(self, value): self.Related_COA.append(value)
    def insert_Related_COA(self, index, value): self.Related_COA[index] = value
    def hasContent_(self):
        if (
            self.Related_COA or
            super(RelatedCOAsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedCOAsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedCOAsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='coa:', name_='RelatedCOAsType'):
        super(RelatedCOAsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedCOAsType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedCOAsType', fromsubclass_=False, pretty_print=True):
        super(RelatedCOAsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Related_COA_ in self.Related_COA:
            Related_COA_.export(lwrite, level, nsmap, namespace_, name_='Related_COA', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedCOAsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Related_COA':
            obj_ = stix_common_binding.RelatedCourseOfActionType.factory()
            obj_.build(child_)
            self.Related_COA.append(obj_)
        super(RelatedCOAsType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedCOAsType

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
        rootTag = 'Course_Of_Action'
        rootClass = CourseOfActionType
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
        rootTag = 'Course_Of_Action'
        rootClass = CourseOfActionType
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
        rootTag = 'Course_Of_Action'
        rootClass = CourseOfActionType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="Course_Of_Action",
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
    "StructuredCOAType",
    "ObjectiveType",
    "CourseOfActionType"
    ]
