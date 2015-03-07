# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:06:24 2013 by generateDS.py version 2.9a.
#
import sys
from stix.bindings import *
import cybox.bindings.cybox_core as cybox_core_binding
import cybox.bindings.cybox_common as cybox_common_binding
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.data_marking as data_marking_binding

XML_NS = "http://stix.mitre.org/Incident-1"

#
# Data representation classes.
#

class PropertyAffectedType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Property=None, Description_Of_Effect=None, Type_Of_Availability_Loss=None, Duration_Of_Availability_Loss=None, Non_Public_Data_Compromised=None):
        self.Property = Property
        self.Description_Of_Effect = Description_Of_Effect
        self.Type_Of_Availability_Loss = Type_Of_Availability_Loss
        self.Duration_Of_Availability_Loss = Duration_Of_Availability_Loss
        self.Non_Public_Data_Compromised = Non_Public_Data_Compromised
    def factory(*args_, **kwargs_):
        if PropertyAffectedType.subclass:
            return PropertyAffectedType.subclass(*args_, **kwargs_)
        else:
            return PropertyAffectedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Property(self): return self.Property
    def set_Property(self, Property): self.Property = Property
    def get_Description_Of_Effect(self): return self.Description_Of_Effect
    def set_Description_Of_Effect(self, Description_Of_Effect): self.Description_Of_Effect = Description_Of_Effect
    def get_Type_Of_Availability_Loss(self): return self.Type_Of_Availability_Loss
    def set_Type_Of_Availability_Loss(self, Type_Of_Availability_Loss): self.Type_Of_Availability_Loss = Type_Of_Availability_Loss
    def get_Duration_Of_Availability_Loss(self): return self.Duration_Of_Availability_Loss
    def set_Duration_Of_Availability_Loss(self, Duration_Of_Availability_Loss): self.Duration_Of_Availability_Loss = Duration_Of_Availability_Loss
    def get_Non_Public_Data_Compromised(self): return self.Non_Public_Data_Compromised
    def set_Non_Public_Data_Compromised(self, Non_Public_Data_Compromised): self.Non_Public_Data_Compromised = Non_Public_Data_Compromised
    def hasContent_(self):
        if (
            self.Property is not None or
            self.Description_Of_Effect is not None or
            self.Type_Of_Availability_Loss is not None or
            self.Duration_Of_Availability_Loss is not None or
            self.Non_Public_Data_Compromised is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='PropertyAffectedType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='PropertyAffectedType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='PropertyAffectedType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='PropertyAffectedType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Property is not None:
            self.Property.export(lwrite, level, nsmap, namespace_, name_='Property', pretty_print=pretty_print)
        if self.Description_Of_Effect is not None:
            self.Description_Of_Effect.export(lwrite, level, nsmap, namespace_, name_='Description_Of_Effect', pretty_print=pretty_print)
        if self.Type_Of_Availability_Loss is not None:
            self.Type_Of_Availability_Loss.export(lwrite, level, nsmap, namespace_, name_='Type_Of_Availability_Loss', pretty_print=pretty_print)
        if self.Duration_Of_Availability_Loss is not None:
            self.Duration_Of_Availability_Loss.export(lwrite, level, nsmap, namespace_, name_='Duration_Of_Availability_Loss', pretty_print=pretty_print)
        if self.Non_Public_Data_Compromised is not None:
            self.Non_Public_Data_Compromised.export(lwrite, level, nsmap, namespace_, name_='Non_Public_Data_Compromised', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Property':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Property(obj_)
        elif nodeName_ == 'Description_Of_Effect':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description_Of_Effect(obj_)
        elif nodeName_ == 'Type_Of_Availability_Loss':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Type_Of_Availability_Loss(obj_)
        elif nodeName_ == 'Duration_Of_Availability_Loss':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Duration_Of_Availability_Loss(obj_)
        elif nodeName_ == 'Non_Public_Data_Compromised':
            obj_ = NonPublicDataCompromisedType.factory()
            obj_.build(child_)
            self.set_Non_Public_Data_Compromised(obj_)
# end class PropertyAffectedType

class AffectedAssetType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Type=None, Description=None, Business_Function_Or_Role=None, Ownership_Class=None, Management_Class=None, Location_Class=None, Location=None, Nature_Of_Security_Effect=None, Structured_Description=None):
        self.Type = Type
        self.Description = Description
        self.Business_Function_Or_Role = Business_Function_Or_Role
        self.Ownership_Class = Ownership_Class
        self.Management_Class = Management_Class
        self.Location_Class = Location_Class
        self.Location = Location
        self.Nature_Of_Security_Effect = Nature_Of_Security_Effect
        self.Structured_Description = Structured_Description
    def factory(*args_, **kwargs_):
        if AffectedAssetType.subclass:
            return AffectedAssetType.subclass(*args_, **kwargs_)
        else:
            return AffectedAssetType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Business_Function_Or_Role(self): return self.Business_Function_Or_Role
    def set_Business_Function_Or_Role(self, Business_Function_Or_Role): self.Business_Function_Or_Role = Business_Function_Or_Role
    def get_Ownership_Class(self): return self.Ownership_Class
    def set_Ownership_Class(self, Ownership_Class): self.Ownership_Class = Ownership_Class
    def get_Management_Class(self): return self.Management_Class
    def set_Management_Class(self, Management_Class): self.Management_Class = Management_Class
    def get_Location_Class(self): return self.Location_Class
    def set_Location_Class(self, Location_Class): self.Location_Class = Location_Class
    def get_Location(self): return self.Location
    def set_Location(self, Location): self.Location = Location
    def get_Nature_Of_Security_Effect(self): return self.Nature_Of_Security_Effect
    def set_Nature_Of_Security_Effect(self, Nature_Of_Security_Effect): self.Nature_Of_Security_Effect = Nature_Of_Security_Effect
    def get_Structured_Description(self): return self.Structured_Description
    def set_Structured_Description(self, Structured_Description): self.Structured_Description = Structured_Description
    def hasContent_(self):
        if (
            self.Type is not None or
            self.Description is not None or
            self.Business_Function_Or_Role is not None or
            self.Ownership_Class is not None or
            self.Management_Class is not None or
            self.Location_Class is not None or
            self.Location is not None or
            self.Nature_Of_Security_Effect is not None or
            self.Structured_Description is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AffectedAssetType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AffectedAssetType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='AffectedAssetType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AffectedAssetType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Type is not None:
            self.Type.export(lwrite, level, nsmap, namespace_, name_='Type', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Business_Function_Or_Role is not None:
            self.Business_Function_Or_Role.export(lwrite, level, nsmap, namespace_, name_='Business_Function_Or_Role', pretty_print=pretty_print)
        if self.Ownership_Class is not None:
            self.Ownership_Class.export(lwrite, level, nsmap, namespace_, name_='Ownership_Class', pretty_print=pretty_print)
        if self.Management_Class is not None:
            self.Management_Class.export(lwrite, level, nsmap, namespace_, name_='Management_Class', pretty_print=pretty_print)
        if self.Location_Class is not None:
            self.Location_Class.export(lwrite, level, nsmap, namespace_, name_='Location_Class', pretty_print=pretty_print)
        if self.Location is not None:
            self.Location.export(lwrite, level, nsmap, namespace_, name_='Location', pretty_print=pretty_print)
        if self.Nature_Of_Security_Effect is not None:
            self.Nature_Of_Security_Effect.export(lwrite, level, nsmap, namespace_, name_='Nature_Of_Security_Effect', pretty_print=pretty_print)
        if self.Structured_Description is not None:
            self.Structured_Description.export(lwrite, level, "%s:" % (nsmap[namespace_]), name_='Structured_Description', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Type':
            obj_ = AssetTypeType.factory()
            obj_.build(child_)
            self.set_Type(obj_)
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Business_Function_Or_Role':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Business_Function_Or_Role(obj_)
        elif nodeName_ == 'Ownership_Class':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Ownership_Class(obj_)
        elif nodeName_ == 'Management_Class':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Management_Class(obj_)
        elif nodeName_ == 'Location_Class':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Location_Class(obj_)
        elif nodeName_ == 'Location':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]

                if type_name_ == "CIQAddress3.0InstanceType":
                    import stix.bindings.extensions.address.ciq_address_3_0 as ciq_address_binding
                    obj_ = ciq_address_binding.CIQAddress3_0InstanceType.factory()
                else:
                    raise NotImplementedError('No implementation class found for: ' + type_name_)
            else:
                raise NotImplementedError('Class not implemented for <Location> element')

            obj_.build(child_)
            self.set_Location(obj_)
        elif nodeName_ == 'Nature_Of_Security_Effect':
            obj_ = NatureOfSecurityEffectType.factory()
            obj_.build(child_)
            self.set_Nature_Of_Security_Effect(obj_)
        elif nodeName_ == 'Structured_Description':
            obj_ = cybox_core_binding.ObservablesType.factory()
            obj_.build(child_)
            self.set_Structured_Description(obj_)
# end class AffectedAssetType

class ImpactAssessmentType(GeneratedsSuper):
    """The ImpactAssessmentType specifies a summary assessment of impact
    for this cyber threat Incident."""
    subclass = None
    superclass = None
    def __init__(self, Direct_Impact_Summary=None, Indirect_Impact_Summary=None, Total_Loss_Estimation=None, Impact_Qualification=None, Effects=None, External_Impact_Assessment_Model=None):
        self.Direct_Impact_Summary = Direct_Impact_Summary
        self.Indirect_Impact_Summary = Indirect_Impact_Summary
        self.Total_Loss_Estimation = Total_Loss_Estimation
        self.Impact_Qualification = Impact_Qualification
        self.Effects = Effects
        self.External_Impact_Assessment_Model = External_Impact_Assessment_Model
    def factory(*args_, **kwargs_):
        if ImpactAssessmentType.subclass:
            return ImpactAssessmentType.subclass(*args_, **kwargs_)
        else:
            return ImpactAssessmentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Direct_Impact_Summary(self): return self.Direct_Impact_Summary
    def set_Direct_Impact_Summary(self, Direct_Impact_Summary): self.Direct_Impact_Summary = Direct_Impact_Summary
    def get_Indirect_Impact_Summary(self): return self.Indirect_Impact_Summary
    def set_Indirect_Impact_Summary(self, Indirect_Impact_Summary): self.Indirect_Impact_Summary = Indirect_Impact_Summary
    def get_Total_Loss_Estimation(self): return self.Total_Loss_Estimation
    def set_Total_Loss_Estimation(self, Total_Loss_Estimation): self.Total_Loss_Estimation = Total_Loss_Estimation
    def get_Impact_Qualification(self): return self.Impact_Qualification
    def set_Impact_Qualification(self, Impact_Qualification): self.Impact_Qualification = Impact_Qualification
    def get_Effects(self): return self.Effects
    def set_Effects(self, Effects): self.Effects = Effects
    def get_External_Impact_Assessment_Model(self): return self.External_Impact_Assessment_Model
    def set_External_Impact_Assessment_Model(self, External_Impact_Assessment_Model): self.External_Impact_Assessment_Model = External_Impact_Assessment_Model
    def hasContent_(self):
        if (
            self.Direct_Impact_Summary is not None or
            self.Indirect_Impact_Summary is not None or
            self.Total_Loss_Estimation is not None or
            self.Impact_Qualification is not None or
            self.Effects is not None or
            self.External_Impact_Assessment_Model is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ImpactAssessmentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ImpactAssessmentType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='ImpactAssessmentType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ImpactAssessmentType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Direct_Impact_Summary is not None:
            self.Direct_Impact_Summary.export(lwrite, level, nsmap, namespace_, name_='Direct_Impact_Summary', pretty_print=pretty_print)
        if self.Indirect_Impact_Summary is not None:
            self.Indirect_Impact_Summary.export(lwrite, level, nsmap, namespace_, name_='Indirect_Impact_Summary', pretty_print=pretty_print)
        if self.Total_Loss_Estimation is not None:
            self.Total_Loss_Estimation.export(lwrite, level, nsmap, namespace_, name_='Total_Loss_Estimation', pretty_print=pretty_print)
        if self.Impact_Qualification is not None:
            self.Impact_Qualification.export(lwrite, level, nsmap, namespace_, name_='Impact_Qualification', pretty_print=pretty_print)
        if self.Effects is not None:
            self.Effects.export(lwrite, level, nsmap, namespace_, name_='Effects', pretty_print=pretty_print)
        if self.External_Impact_Assessment_Model is not None:
            self.External_Impact_Assessment_Model.export(lwrite, level, nsmap, namespace_, name_='External_Impact_Assessment_Model', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Direct_Impact_Summary':
            obj_ = DirectImpactSummaryType.factory()
            obj_.build(child_)
            self.set_Direct_Impact_Summary(obj_)
        elif nodeName_ == 'Indirect_Impact_Summary':
            obj_ = IndirectImpactSummaryType.factory()
            obj_.build(child_)
            self.set_Indirect_Impact_Summary(obj_)
        elif nodeName_ == 'Total_Loss_Estimation':
            obj_ = TotalLossEstimationType.factory()
            obj_.build(child_)
            self.set_Total_Loss_Estimation(obj_)
        elif nodeName_ == 'Impact_Qualification':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Impact_Qualification(obj_)
        elif nodeName_ == 'Effects':
            obj_ = EffectsType.factory()
            obj_.build(child_)
            self.set_Effects(obj_)
        elif nodeName_ == 'External_Impact_Assessment_Model':
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()[type_name_]
                obj_ = class_.factory()
                obj_.build(child_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <External_Impact_Assessment_Model> element')
            self.set_External_Impact_Assessment_Model(obj_)
# end class ImpactAssessmentType

class ExternalImpactAssessmentModelType(GeneratedsSuper):
    """The ExternalImpactAssessmentModelType is an abstract type enabling
    the definition through extension of incident impact assessment
    models external to STIX.Specifies the name of the externally
    defined impact assessment model.Specifies a URL reference for
    the externally defined impact assessment model."""
    subclass = None
    superclass = None
    def __init__(self, model_name=None, model_reference=None):
        self.model_name = _cast(None, model_name)
        self.model_reference = _cast(None, model_reference)
        pass
    def factory(*args_, **kwargs_):
        if ExternalImpactAssessmentModelType.subclass:
            return ExternalImpactAssessmentModelType.subclass(*args_, **kwargs_)
        else:
            return ExternalImpactAssessmentModelType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_model_name(self): return self.model_name
    def set_model_name(self, model_name): self.model_name = model_name
    def get_model_reference(self): return self.model_reference
    def set_model_reference(self, model_reference): self.model_reference = model_reference
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExternalImpactAssessmentModelType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ExternalImpactAssessmentModelType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='ExternalImpactAssessmentModelType'):
        if self.model_name is not None and 'model_name' not in already_processed:
            already_processed.add('model_name')
            lwrite(' model_name=%s' % (quote_attrib(self.model_name), ))
        if self.model_reference is not None and 'model_reference' not in already_processed:
            already_processed.add('model_reference')
            lwrite(' model_reference=%s' % (quote_attrib(self.model_reference), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExternalImpactAssessmentModelType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('model_name', node)
        if value is not None and 'model_name' not in already_processed:
            already_processed.add('model_name')
            self.model_name = value
        value = find_attr_value_('model_reference', node)
        if value is not None and 'model_reference' not in already_processed:
            already_processed.add('model_reference')
            self.model_reference = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ExternalImpactAssessmentModelType

class COATakenType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Time=None, Contributors=None, Course_Of_Action=None, extensiontype_=None):
        self.Time = Time
        self.Contributors = Contributors
        self.Course_Of_Action = Course_Of_Action
        self.extensiontype_ = extensiontype_
    def factory(*args_, **kwargs_):
        if COATakenType.subclass:
            return COATakenType.subclass(*args_, **kwargs_)
        else:
            return COATakenType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Time(self): return self.Time
    def set_Time(self, Time): self.Time = Time
    def get_Contributors(self): return self.Contributors
    def set_Contributors(self, Contributors): self.Contributors = Contributors
    def get_Course_Of_Action(self): return self.Course_Of_Action
    def set_Course_Of_Action(self, Course_Of_Action): self.Course_Of_Action = Course_Of_Action
    def get_extensiontype_(self): return self.extensiontype_
    def set_extensiontype_(self, extensiontype_): self.extensiontype_ = extensiontype_
    def hasContent_(self):
        if (
            self.Time is not None or
            self.Contributors is not None or
            self.Course_Of_Action is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='COATakenType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='COATakenType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='COATakenType'):
        if self.extensiontype_ is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            lwrite('  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"')
            lwrite('  xsi:type="%s"' % self.extensiontype_)
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='COATakenType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Time is not None:
            self.Time.export(lwrite, level, nsmap, namespace_, name_='Time', pretty_print=pretty_print)
        if self.Contributors is not None:
            self.Contributors.export(lwrite, level, nsmap, namespace_, name_='Contributors', pretty_print=pretty_print)
        if self.Course_Of_Action is not None:
            self.Course_Of_Action.export(lwrite, level, nsmap, namespace_, name_='Course_Of_Action', pretty_print=pretty_print)
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
        if nodeName_ == 'Time':
            obj_ = COATimeType.factory()
            obj_.build(child_)
            self.set_Time(obj_)
        elif nodeName_ == 'Contributors':
            obj_ = ContributorsType.factory()
            obj_.build(child_)
            self.set_Contributors(obj_)
        elif nodeName_ == 'Course_Of_Action':
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
                obj_ = stix_common_binding.CourseOfActionBaseType.factory() # not abstract

            obj_.build(child_)
            self.set_Course_Of_Action(obj_)
# end class COATakenType

class JournalEntryType(GeneratedsSuper):
    """The JournalEntryType is optional and provides journal notes for
    information discovered during the handling of the
    Incident.Specifies the author of the JournalEntry note.Specifies
    the date and time that the JournalEntry note was written.In
    order to avoid ambiguity, it is strongly suggest that all
    timestamps include a specification of the timezone if it is
    known.Represents the precision of the associated time value. If
    omitted, the default is "second", meaning the timestamp is
    precise to the full field value. Digits in the timestamp that
    are required by the xs:dateTime datatype but are beyond the
    specified precision should be zeroed out."""
    subclass = None
    superclass = None
    def __init__(self, time=None, time_precision='second', author=None, valueOf_=None):
        self.time = _cast(None, time)
        self.time_precision = _cast(None, time_precision)
        self.author = _cast(None, author)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if JournalEntryType.subclass:
            return JournalEntryType.subclass(*args_, **kwargs_)
        else:
            return JournalEntryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_time(self): return self.time
    def set_time(self, time): self.time = time
    def get_time_precision(self): return self.time_precision
    def set_time_precision(self, time_precision): self.time_precision = time_precision
    def get_author(self): return self.author
    def set_author(self, author): self.author = author
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='JournalEntryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='JournalEntryType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='JournalEntryType'):
        if self.time is not None and 'time' not in already_processed:
            already_processed.add('time')
            lwrite(' time="%s"' % self.gds_format_datetime(self.time, input_name='time'))
        if self.time_precision is not None and 'time_precision' not in already_processed:
            already_processed.add('time_precision')
            lwrite(' time_precision=%s' % (quote_attrib(self.time_precision), ))
        if self.author is not None and 'author' not in already_processed:
            already_processed.add('author')
            lwrite(' author=%s' % (quote_attrib(self.author), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='JournalEntryType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('time', node)
        if value is not None and 'time' not in already_processed:
            already_processed.add('time')
            try:
                self.time = self.gds_parse_datetime(value, node, 'time')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (time): %s' % exp)
        value = find_attr_value_('time_precision', node)
        if value is not None and 'time_precision' not in already_processed:
            already_processed.add('time_precision')
            self.time_precision = value
        value = find_attr_value_('author', node)
        if value is not None and 'author' not in already_processed:
            already_processed.add('author')
            self.author = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class JournalEntryType


class COARequestedType(COATakenType):
    """Specifies a suggested level of priority to be applied to this
    requested COA."""
    subclass = None
    superclass = COATakenType
    def __init__(self, Time=None, Contributors=None, Course_Of_Action=None, priority=None):
        super(COARequestedType, self).__init__(Time=Time, Contributors=Contributors, Course_Of_Action=Course_Of_Action)
        self.priority = _cast(None, priority)
        pass
    def factory(*args_, **kwargs_):
        if COARequestedType.subclass:
            return COARequestedType.subclass(*args_, **kwargs_)
        else:
            return COARequestedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_priority(self): return self.priority
    def set_priority(self, priority): self.priority = priority
    def hasContent_(self):
        if (
            super(COARequestedType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='COARequestedType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='COARequestedType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='COARequestedType'):
        super(COARequestedType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='COARequestedType')
        if self.priority is not None and 'priority' not in already_processed:
            already_processed.add('priority')
            lwrite(' priority=%s' % (quote_attrib(self.priority), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='COARequestedType', fromsubclass_=False, pretty_print=True):
        super(COARequestedType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('priority', node)
        if value is not None and 'priority' not in already_processed:
            already_processed.add('priority')
            self.priority = value
        super(COARequestedType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(COARequestedType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class COARequestedType

class ContributorsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Contributor=None):
        if Contributor is None:
            self.Contributor = []
        else:
            self.Contributor = Contributor
    def factory(*args_, **kwargs_):
        if ContributorsType.subclass:
            return ContributorsType.subclass(*args_, **kwargs_)
        else:
            return ContributorsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Contributor(self): return self.Contributor
    def set_Contributor(self, Contributor): self.Contributor = Contributor
    def add_Contributor(self, value): self.Contributor.append(value)
    def insert_Contributor(self, index, value): self.Contributor[index] = value
    def hasContent_(self):
        if (
            self.Contributor
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ContributorsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ContributorsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='ContributorsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ContributorsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Contributor_ in self.Contributor:
            Contributor_.export(lwrite, level, "%s:" % (nsmap[namespace_]), name_='Contributor', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Contributor':
            obj_ = cybox_common_binding.ContributorType.factory()
            obj_.build(child_)
            self.Contributor.append(obj_)
# end class ContributorsType

class COATimeType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Start=None, End=None):
        self.Start = Start
        self.End = End
    def factory(*args_, **kwargs_):
        if COATimeType.subclass:
            return COATimeType.subclass(*args_, **kwargs_)
        else:
            return COATimeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Start(self): return self.Start
    def set_Start(self, Start): self.Start = Start
    def get_End(self): return self.End
    def set_End(self, End): self.End = End
    def hasContent_(self):
        if (
            self.Start is not None or
            self.End is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='COATimeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='COATimeType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='COATimeType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='COATimeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Start is not None:
            self.Start.export(lwrite, level, nsmap, namespace_, name_='Start', pretty_print=pretty_print)
        if self.End is not None:
            self.End.export(lwrite, level, nsmap, namespace_, name_='End', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Start':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Start(obj_)
        elif nodeName_ == 'End':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_End(obj_)
# end class COATimeType

class LossEstimationType(GeneratedsSuper):
    """Specifies the estimated financial loss for the Incident.Specifies
    the ISO 4217 currency code if other than USD"""
    subclass = None
    superclass = None
    def __init__(self, iso_currency_code=None, amount=None):
        self.iso_currency_code = _cast(None, iso_currency_code)
        self.amount = _cast(None, amount)
        pass
    def factory(*args_, **kwargs_):
        if LossEstimationType.subclass:
            return LossEstimationType.subclass(*args_, **kwargs_)
        else:
            return LossEstimationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_iso_currency_code(self): return self.iso_currency_code
    def set_iso_currency_code(self, iso_currency_code): self.iso_currency_code = iso_currency_code
    def get_amount(self): return self.amount
    def set_amount(self, amount): self.amount = amount
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='LossEstimationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='LossEstimationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='LossEstimationType'):
        if self.iso_currency_code is not None and 'iso_currency_code' not in already_processed:
            already_processed.add('iso_currency_code')
            lwrite(' iso_currency_code=%s' % (quote_attrib(self.iso_currency_code), ))
        if self.amount is not None and 'amount' not in already_processed:
            already_processed.add('amount')
            lwrite(' amount=%s' % (quote_attrib(self.amount), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='LossEstimationType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('iso_currency_code', node)
        if value is not None and 'iso_currency_code' not in already_processed:
            already_processed.add('iso_currency_code')
            self.iso_currency_code = value
        value = find_attr_value_('amount', node)
        if value is not None and 'amount' not in already_processed:
            already_processed.add('amount')
            self.amount = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class LossEstimationType

class TotalLossEstimationType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Initial_Reported_Total_Loss_Estimation=None, Actual_Total_Loss_Estimation=None):
        self.Initial_Reported_Total_Loss_Estimation = Initial_Reported_Total_Loss_Estimation
        self.Actual_Total_Loss_Estimation = Actual_Total_Loss_Estimation
    def factory(*args_, **kwargs_):
        if TotalLossEstimationType.subclass:
            return TotalLossEstimationType.subclass(*args_, **kwargs_)
        else:
            return TotalLossEstimationType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Initial_Reported_Total_Loss_Estimation(self): return self.Initial_Reported_Total_Loss_Estimation
    def set_Initial_Reported_Total_Loss_Estimation(self, Initial_Reported_Total_Loss_Estimation): self.Initial_Reported_Total_Loss_Estimation = Initial_Reported_Total_Loss_Estimation
    def get_Actual_Total_Loss_Estimation(self): return self.Actual_Total_Loss_Estimation
    def set_Actual_Total_Loss_Estimation(self, Actual_Total_Loss_Estimation): self.Actual_Total_Loss_Estimation = Actual_Total_Loss_Estimation
    def hasContent_(self):
        if (
            self.Initial_Reported_Total_Loss_Estimation is not None or
            self.Actual_Total_Loss_Estimation is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TotalLossEstimationType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TotalLossEstimationType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='TotalLossEstimationType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TotalLossEstimationType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Initial_Reported_Total_Loss_Estimation is not None:
            self.Initial_Reported_Total_Loss_Estimation.export(lwrite, level, nsmap, namespace_, name_='Initial_Reported_Total_Loss_Estimation', pretty_print=pretty_print)
        if self.Actual_Total_Loss_Estimation is not None:
            self.Actual_Total_Loss_Estimation.export(lwrite, level, nsmap, namespace_, name_='Actual_Total_Loss_Estimation', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Initial_Reported_Total_Loss_Estimation':
            obj_ = LossEstimationType.factory()
            obj_.build(child_)
            self.set_Initial_Reported_Total_Loss_Estimation(obj_)
        elif nodeName_ == 'Actual_Total_Loss_Estimation':
            obj_ = LossEstimationType.factory()
            obj_.build(child_)
            self.set_Actual_Total_Loss_Estimation(obj_)
# end class TotalLossEstimationType

class IndirectImpactSummaryType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Loss_Of_Competitive_Advantage=None, Brand_And_Market_Damage=None, Increased_Operating_Costs=None, Legal_And_Regulatory_Costs=None):
        self.Loss_Of_Competitive_Advantage = Loss_Of_Competitive_Advantage
        self.Brand_And_Market_Damage = Brand_And_Market_Damage
        self.Increased_Operating_Costs = Increased_Operating_Costs
        self.Legal_And_Regulatory_Costs = Legal_And_Regulatory_Costs
    def factory(*args_, **kwargs_):
        if IndirectImpactSummaryType.subclass:
            return IndirectImpactSummaryType.subclass(*args_, **kwargs_)
        else:
            return IndirectImpactSummaryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Loss_Of_Competitive_Advantage(self): return self.Loss_Of_Competitive_Advantage
    def set_Loss_Of_Competitive_Advantage(self, Loss_Of_Competitive_Advantage): self.Loss_Of_Competitive_Advantage = Loss_Of_Competitive_Advantage
    def get_Brand_And_Market_Damage(self): return self.Brand_And_Market_Damage
    def set_Brand_And_Market_Damage(self, Brand_And_Market_Damage): self.Brand_And_Market_Damage = Brand_And_Market_Damage
    def get_Increased_Operating_Costs(self): return self.Increased_Operating_Costs
    def set_Increased_Operating_Costs(self, Increased_Operating_Costs): self.Increased_Operating_Costs = Increased_Operating_Costs
    def get_Legal_And_Regulatory_Costs(self): return self.Legal_And_Regulatory_Costs
    def set_Legal_And_Regulatory_Costs(self, Legal_And_Regulatory_Costs): self.Legal_And_Regulatory_Costs = Legal_And_Regulatory_Costs
    def hasContent_(self):
        if (
            self.Loss_Of_Competitive_Advantage is not None or
            self.Brand_And_Market_Damage is not None or
            self.Increased_Operating_Costs is not None or
            self.Legal_And_Regulatory_Costs is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IndirectImpactSummaryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IndirectImpactSummaryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='IndirectImpactSummaryType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IndirectImpactSummaryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Loss_Of_Competitive_Advantage is not None:
            self.Loss_Of_Competitive_Advantage.export(lwrite, level, nsmap, namespace_, name_='Loss_Of_Competitive_Advantage', pretty_print=pretty_print)
        if self.Brand_And_Market_Damage is not None:
            self.Brand_And_Market_Damage.export(lwrite, level, nsmap, namespace_, name_='Brand_And_Market_Damage', pretty_print=pretty_print)
        if self.Increased_Operating_Costs is not None:
            self.Increased_Operating_Costs.export(lwrite, level, nsmap, namespace_, name_='Increased_Operating_Costs', pretty_print=pretty_print)
        if self.Legal_And_Regulatory_Costs is not None:
            self.Legal_And_Regulatory_Costs.export(lwrite, level, nsmap, namespace_, name_='Legal_And_Regulatory_Costs', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Loss_Of_Competitive_Advantage':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Loss_Of_Competitive_Advantage(obj_)
        elif nodeName_ == 'Brand_And_Market_Damage':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Brand_And_Market_Damage(obj_)
        elif nodeName_ == 'Increased_Operating_Costs':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Increased_Operating_Costs(obj_)
        elif nodeName_ == 'Legal_And_Regulatory_Costs':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Legal_And_Regulatory_Costs(obj_)
# end class IndirectImpactSummaryType

class DirectImpactSummaryType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Asset_Losses=None, Business_Mission_Disruption=None, Response_And_Recovery_Costs=None):
        self.Asset_Losses = Asset_Losses
        self.Business_Mission_Disruption = Business_Mission_Disruption
        self.Response_And_Recovery_Costs = Response_And_Recovery_Costs
    def factory(*args_, **kwargs_):
        if DirectImpactSummaryType.subclass:
            return DirectImpactSummaryType.subclass(*args_, **kwargs_)
        else:
            return DirectImpactSummaryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Asset_Losses(self): return self.Asset_Losses
    def set_Asset_Losses(self, Asset_Losses): self.Asset_Losses = Asset_Losses
    def get_Business_Mission_Disruption(self): return self.Business_Mission_Disruption
    def set_Business_Mission_Disruption(self, Business_Mission_Disruption): self.Business_Mission_Disruption = Business_Mission_Disruption
    def get_Response_And_Recovery_Costs(self): return self.Response_And_Recovery_Costs
    def set_Response_And_Recovery_Costs(self, Response_And_Recovery_Costs): self.Response_And_Recovery_Costs = Response_And_Recovery_Costs
    def hasContent_(self):
        if (
            self.Asset_Losses is not None or
            self.Business_Mission_Disruption is not None or
            self.Response_And_Recovery_Costs is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='DirectImpactSummaryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='DirectImpactSummaryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='DirectImpactSummaryType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='DirectImpactSummaryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Asset_Losses is not None:
            self.Asset_Losses.export(lwrite, level, nsmap, namespace_, name_='Asset_Losses', pretty_print=pretty_print)
        if self.Business_Mission_Disruption is not None:
            self.Business_Mission_Disruption.export(lwrite, level, nsmap, namespace_, name_='Business-Mission_Disruption', pretty_print=pretty_print)
        if self.Response_And_Recovery_Costs is not None:
            self.Response_And_Recovery_Costs.export(lwrite, level, nsmap, namespace_, name_='Response_And_Recovery_Costs', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Asset_Losses':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Asset_Losses(obj_)
        elif nodeName_ == 'Business-Mission_Disruption':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Business_Mission_Disruption(obj_)
        elif nodeName_ == 'Response_And_Recovery_Costs':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Response_And_Recovery_Costs(obj_)
# end class DirectImpactSummaryType

class NatureOfSecurityEffectType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Property_Affected=None):
        if Property_Affected is None:
            self.Property_Affected = []
        else:
            self.Property_Affected = Property_Affected
    def factory(*args_, **kwargs_):
        if NatureOfSecurityEffectType.subclass:
            return NatureOfSecurityEffectType.subclass(*args_, **kwargs_)
        else:
            return NatureOfSecurityEffectType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Property_Affected(self): return self.Property_Affected
    def set_Property_Affected(self, Property_Affected): self.Property_Affected = Property_Affected
    def add_Property_Affected(self, value): self.Property_Affected.append(value)
    def insert_Property_Affected(self, index, value): self.Property_Affected[index] = value
    def hasContent_(self):
        if (
            self.Property_Affected
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='NatureOfSecurityEffectType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NatureOfSecurityEffectType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='NatureOfSecurityEffectType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='NatureOfSecurityEffectType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Property_Affected_ in self.Property_Affected:
            Property_Affected_.export(lwrite, level, nsmap, namespace_, name_='Property_Affected', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Property_Affected':
            obj_ = PropertyAffectedType.factory()
            obj_.build(child_)
            self.Property_Affected.append(obj_)
# end class NatureOfSecurityEffectType

class HistoryItemType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Action_Entry=None, Journal_Entry=None):
        self.Action_Entry = Action_Entry
        self.Journal_Entry = Journal_Entry
    def factory(*args_, **kwargs_):
        if HistoryItemType.subclass:
            return HistoryItemType.subclass(*args_, **kwargs_)
        else:
            return HistoryItemType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Action_Entry(self): return self.Action_Entry
    def set_Action_Entry(self, Action_Entry): self.Action_Entry = Action_Entry
    def get_Journal_Entry(self): return self.Journal_Entry
    def set_Journal_Entry(self, Journal_Entry): self.Journal_Entry = Journal_Entry
    def hasContent_(self):
        if (
            self.Action_Entry is not None or
            self.Journal_Entry is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='HistoryItemType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HistoryItemType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='HistoryItemType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='HistoryItemType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Action_Entry is not None:
            self.Action_Entry.export(lwrite, level, nsmap, namespace_, name_='Action_Entry', pretty_print=pretty_print)
        if self.Journal_Entry is not None:
            self.Journal_Entry.export(lwrite, level, nsmap, namespace_, name_='Journal_Entry', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Action_Entry':
            obj_ = COATakenType.factory()
            obj_.build(child_)
            self.set_Action_Entry(obj_)
        elif nodeName_ == 'Journal_Entry':
            obj_ = JournalEntryType.factory()
            obj_.build(child_)
            self.set_Journal_Entry(obj_)
# end class HistoryItemType

class HistoryType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, History_Item=None):
        if History_Item is None:
            self.History_Item = []
        else:
            self.History_Item = History_Item
    def factory(*args_, **kwargs_):
        if HistoryType.subclass:
            return HistoryType.subclass(*args_, **kwargs_)
        else:
            return HistoryType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_History_Item(self): return self.History_Item
    def set_History_Item(self, History_Item): self.History_Item = History_Item
    def add_History_Item(self, value): self.History_Item.append(value)
    def insert_History_Item(self, index, value): self.History_Item[index] = value
    def hasContent_(self):
        if (
            self.History_Item
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='HistoryType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HistoryType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='HistoryType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='HistoryType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for History_Item_ in self.History_Item:
            History_Item_.export(lwrite, level, nsmap, namespace_, name_='History_Item', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'History_Item':
            obj_ = HistoryItemType.factory()
            obj_.build(child_)
            self.History_Item.append(obj_)
# end class HistoryType

class AffectedAssetsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Affected_Asset=None):
        if Affected_Asset is None:
            self.Affected_Asset = []
        else:
            self.Affected_Asset = Affected_Asset
    def factory(*args_, **kwargs_):
        if AffectedAssetsType.subclass:
            return AffectedAssetsType.subclass(*args_, **kwargs_)
        else:
            return AffectedAssetsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Affected_Asset(self): return self.Affected_Asset
    def set_Affected_Asset(self, Affected_Asset): self.Affected_Asset = Affected_Asset
    def add_Affected_Asset(self, value): self.Affected_Asset.append(value)
    def insert_Affected_Asset(self, index, value): self.Affected_Asset[index] = value
    def hasContent_(self):
        if (
            self.Affected_Asset
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AffectedAssetsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AffectedAssetsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='AffectedAssetsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AffectedAssetsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Affected_Asset_ in self.Affected_Asset:
            Affected_Asset_.export(lwrite, level, nsmap, namespace_, name_='Affected_Asset', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Affected_Asset':
            obj_ = AffectedAssetType.factory()
            obj_.build(child_)
            self.Affected_Asset.append(obj_)
# end class AffectedAssetsType

class TimeType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, First_Malicious_Action=None, Initial_Compromise=None, First_Data_Exfiltration=None, Incident_Discovery=None, Incident_Opened=None, Containment_Achieved=None, Restoration_Achieved=None, Incident_Reported=None, Incident_Closed=None):
        self.First_Malicious_Action = First_Malicious_Action
        self.Initial_Compromise = Initial_Compromise
        self.First_Data_Exfiltration = First_Data_Exfiltration
        self.Incident_Discovery = Incident_Discovery
        self.Incident_Opened = Incident_Opened
        self.Containment_Achieved = Containment_Achieved
        self.Restoration_Achieved = Restoration_Achieved
        self.Incident_Reported = Incident_Reported
        self.Incident_Closed = Incident_Closed
    def factory(*args_, **kwargs_):
        if TimeType.subclass:
            return TimeType.subclass(*args_, **kwargs_)
        else:
            return TimeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_First_Malicious_Action(self): return self.First_Malicious_Action
    def set_First_Malicious_Action(self, First_Malicious_Action): self.First_Malicious_Action = First_Malicious_Action
    def get_Initial_Compromise(self): return self.Initial_Compromise
    def set_Initial_Compromise(self, Initial_Compromise): self.Initial_Compromise = Initial_Compromise
    def get_First_Data_Exfiltration(self): return self.First_Data_Exfiltration
    def set_First_Data_Exfiltration(self, First_Data_Exfiltration): self.First_Data_Exfiltration = First_Data_Exfiltration
    def get_Incident_Discovery(self): return self.Incident_Discovery
    def set_Incident_Discovery(self, Incident_Discovery): self.Incident_Discovery = Incident_Discovery
    def get_Incident_Opened(self): return self.Incident_Opened
    def set_Incident_Opened(self, Incident_Opened): self.Incident_Opened = Incident_Opened
    def get_Containment_Achieved(self): return self.Containment_Achieved
    def set_Containment_Achieved(self, Containment_Achieved): self.Containment_Achieved = Containment_Achieved
    def get_Restoration_Achieved(self): return self.Restoration_Achieved
    def set_Restoration_Achieved(self, Restoration_Achieved): self.Restoration_Achieved = Restoration_Achieved
    def get_Incident_Reported(self): return self.Incident_Reported
    def set_Incident_Reported(self, Incident_Reported): self.Incident_Reported = Incident_Reported
    def get_Incident_Closed(self): return self.Incident_Closed
    def set_Incident_Closed(self, Incident_Closed): self.Incident_Closed = Incident_Closed
    def hasContent_(self):
        if (
            self.First_Malicious_Action is not None or
            self.Initial_Compromise is not None or
            self.First_Data_Exfiltration is not None or
            self.Incident_Discovery is not None or
            self.Incident_Opened is not None or
            self.Containment_Achieved is not None or
            self.Restoration_Achieved is not None or
            self.Incident_Reported is not None or
            self.Incident_Closed is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TimeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TimeType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='TimeType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TimeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.First_Malicious_Action is not None:
            self.First_Malicious_Action.export(lwrite, level, nsmap, namespace_, name_='First_Malicious_Action', pretty_print=pretty_print)
        if self.Initial_Compromise is not None:
            self.Initial_Compromise.export(lwrite, level, nsmap, namespace_, name_='Initial_Compromise', pretty_print=pretty_print)
        if self.First_Data_Exfiltration is not None:
            self.First_Data_Exfiltration.export(lwrite, level, nsmap, namespace_, name_='First_Data_Exfiltration', pretty_print=pretty_print)
        if self.Incident_Discovery is not None:
            self.Incident_Discovery.export(lwrite, level, nsmap, namespace_, name_='Incident_Discovery', pretty_print=pretty_print)
        if self.Incident_Opened is not None:
            self.Incident_Opened.export(lwrite, level, nsmap, namespace_, name_='Incident_Opened', pretty_print=pretty_print)
        if self.Containment_Achieved is not None:
            self.Containment_Achieved.export(lwrite, level, nsmap, namespace_, name_='Containment_Achieved', pretty_print=pretty_print)
        if self.Restoration_Achieved is not None:
            self.Restoration_Achieved.export(lwrite, level, nsmap, namespace_, name_='Restoration_Achieved', pretty_print=pretty_print)
        if self.Incident_Reported is not None:
            self.Incident_Reported.export(lwrite, level, nsmap, namespace_, name_='Incident_Reported', pretty_print=pretty_print)
        if self.Incident_Closed is not None:
            self.Incident_Closed.export(lwrite, level, nsmap, namespace_, name_='Incident_Closed', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'First_Malicious_Action':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_First_Malicious_Action(obj_)
        elif nodeName_ == 'Initial_Compromise':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Initial_Compromise(obj_)
        elif nodeName_ == 'First_Data_Exfiltration':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_First_Data_Exfiltration(obj_)
        elif nodeName_ == 'Incident_Discovery':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Incident_Discovery(obj_)
        elif nodeName_ == 'Incident_Opened':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Incident_Opened(obj_)
        elif nodeName_ == 'Containment_Achieved':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Containment_Achieved(obj_)
        elif nodeName_ == 'Restoration_Achieved':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Restoration_Achieved(obj_)
        elif nodeName_ == 'Incident_Reported':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Incident_Reported(obj_)
        elif nodeName_ == 'Incident_Closed':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Incident_Closed(obj_)
# end class TimeType

class CategoriesType(GeneratedsSuper):
    """Represents a list of incident categories that an incident is tagged
    with."""
    subclass = None
    superclass = None
    def __init__(self, Category=None):
        if Category is None:
            self.Category = []
        else:
            self.Category = Category
    def factory(*args_, **kwargs_):
        if CategoriesType.subclass:
            return CategoriesType.subclass(*args_, **kwargs_)
        else:
            return CategoriesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Category(self): return self.Category
    def set_Category(self, Category): self.Category = Category
    def add_Category(self, value): self.Category.append(value)
    def insert_Category(self, index, value): self.Category[index] = value
    def hasContent_(self):
        if (
            self.Category
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CategoriesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CategoriesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='CategoriesType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CategoriesType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Category_ in self.Category:
            Category_.export(lwrite, level, nsmap, namespace_, name_='Category', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Category':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.add_Category(obj_)
# end class CategoriesType

class EffectsType(GeneratedsSuper):
    """Represents a list of incident effects that an incident is tagged
    with."""
    subclass = None
    superclass = None
    def __init__(self, Effect=None):
        if Effect is None:
            self.Effect = []
        else:
            self.Effect = Effect
    def factory(*args_, **kwargs_):
        if EffectsType.subclass:
            return EffectsType.subclass(*args_, **kwargs_)
        else:
            return EffectsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Effect(self): return self.Effect
    def set_Effect(self, Effect): self.Effect = Effect
    def add_Effect(self, value): self.Effect.append(value)
    def insert_Effect(self, index, value): self.Effect[index] = value
    def hasContent_(self):
        if (
            self.Effect
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='EffectsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='EffectsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='EffectsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='EffectsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Effect_ in self.Effect:
            Effect_.export(lwrite, level, nsmap, namespace_, name_='Effect', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Effect':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Effect.append(obj_)
# end class EffectsType

class AttributedThreatActorsType(stix_common_binding.GenericRelationshipListType):
    """The AttributedThreatActorsType specifies a Threat Actor asserted to
    be attributed for this Incident."""
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Threat_Actor=None):
        super(AttributedThreatActorsType, self).__init__(scope=scope)
        if Threat_Actor is None:
            self.Threat_Actor = []
        else:
            self.Threat_Actor = Threat_Actor
    def factory(*args_, **kwargs_):
        if AttributedThreatActorsType.subclass:
            return AttributedThreatActorsType.subclass(*args_, **kwargs_)
        else:
            return AttributedThreatActorsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Threat_Actor(self): return self.Threat_Actor
    def set_Threat_Actor(self, Threat_Actor): self.Threat_Actor = Threat_Actor
    def add_Threat_Actor(self, value): self.Threat_Actor.append(value)
    def insert_Threat_Actor(self, index, value): self.Threat_Actor[index] = value
    def hasContent_(self):
        if (
            self.Threat_Actor or
            super(AttributedThreatActorsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AttributedThreatActorsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AttributedThreatActorsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='AttributedThreatActorsType'):
        super(AttributedThreatActorsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='AttributedThreatActorsType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AttributedThreatActorsType', fromsubclass_=False, pretty_print=True):
        super(AttributedThreatActorsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Threat_Actor_ in self.Threat_Actor:
            Threat_Actor_.export(lwrite, level, nsmap, namespace_, name_='Threat_Actor', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(AttributedThreatActorsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Threat_Actor':
            obj_ = stix_common_binding.RelatedThreatActorType.factory()
            obj_.build(child_)
            self.Threat_Actor.append(obj_)
        super(AttributedThreatActorsType, self).buildChildren(child_, node, nodeName_, True)
# end class AttributedThreatActorsType

class RelatedIndicatorsType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Related_Indicator=None):
        super(RelatedIndicatorsType, self).__init__(scope=scope)
        if Related_Indicator is None:
            self.Related_Indicator = []
        else:
            self.Related_Indicator = Related_Indicator
    def factory(*args_, **kwargs_):
        if RelatedIndicatorsType.subclass:
            return RelatedIndicatorsType.subclass(*args_, **kwargs_)
        else:
            return RelatedIndicatorsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Related_Indicator(self): return self.Related_Indicator
    def set_Related_Indicator(self, Related_Indicator): self.Related_Indicator = Related_Indicator
    def add_Related_Indicator(self, value): self.Related_Indicator.append(value)
    def insert_Related_Indicator(self, index, value): self.Related_Indicator[index] = value
    def hasContent_(self):
        if (
            self.Related_Indicator or
            super(RelatedIndicatorsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIndicatorsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedIndicatorsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='RelatedIndicatorsType'):
        super(RelatedIndicatorsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedIndicatorsType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIndicatorsType', fromsubclass_=False, pretty_print=True):
        super(RelatedIndicatorsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Related_Indicator_ in self.Related_Indicator:
            Related_Indicator_.export(lwrite, level, nsmap, namespace_, name_='Related_Indicator', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedIndicatorsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Related_Indicator':
            obj_ = stix_common_binding.RelatedIndicatorType.factory()
            obj_.build(child_)
            self.Related_Indicator.append(obj_)
        super(RelatedIndicatorsType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedIndicatorsType

class RelatedObservablesType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Related_Observable=None):
        super(RelatedObservablesType, self).__init__(scope=scope)
        if Related_Observable is None:
            self.Related_Observable = []
        else:
            self.Related_Observable = Related_Observable
    def factory(*args_, **kwargs_):
        if RelatedObservablesType.subclass:
            return RelatedObservablesType.subclass(*args_, **kwargs_)
        else:
            return RelatedObservablesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Related_Observable(self): return self.Related_Observable
    def set_Related_Observable(self, Related_Observable): self.Related_Observable = Related_Observable
    def add_Related_Observable(self, value): self.Related_Observable.append(value)
    def insert_Related_Observable(self, index, value): self.Related_Observable[index] = value
    def hasContent_(self):
        if (
            self.Related_Observable or
            super(RelatedObservablesType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedObservablesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedObservablesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='RelatedObservablesType'):
        super(RelatedObservablesType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedObservablesType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedObservablesType', fromsubclass_=False, pretty_print=True):
        super(RelatedObservablesType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Related_Observable_ in self.Related_Observable:
            Related_Observable_.export(lwrite, level, nsmap, namespace_, name_='Related_Observable', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedObservablesType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Related_Observable':
            obj_ = stix_common_binding.RelatedObservableType.factory()
            obj_.build(child_)
            self.Related_Observable.append(obj_)
        super(RelatedObservablesType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedObservablesType

class LeveragedTTPsType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Leveraged_TTP=None):
        super(LeveragedTTPsType, self).__init__(scope=scope)
        if Leveraged_TTP is None:
            self.Leveraged_TTP = []
        else:
            self.Leveraged_TTP = Leveraged_TTP
    def factory(*args_, **kwargs_):
        if LeveragedTTPsType.subclass:
            return LeveragedTTPsType.subclass(*args_, **kwargs_)
        else:
            return LeveragedTTPsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Leveraged_TTP(self): return self.Leveraged_TTP
    def set_Leveraged_TTP(self, Leveraged_TTP): self.Leveraged_TTP = Leveraged_TTP
    def add_Leveraged_TTP(self, value): self.Leveraged_TTP.append(value)
    def insert_Leveraged_TTP(self, index, value): self.Leveraged_TTP[index] = value
    def hasContent_(self):
        if (
            self.Leveraged_TTP or
            super(LeveragedTTPsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='LeveragedTTPsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='LeveragedTTPsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='LeveragedTTPsType'):
        super(LeveragedTTPsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='LeveragedTTPsType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='LeveragedTTPsType', fromsubclass_=False, pretty_print=True):
        super(LeveragedTTPsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Leveraged_TTP_ in self.Leveraged_TTP:
            Leveraged_TTP_.export(lwrite, level, nsmap, namespace_, name_='Leveraged_TTP', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(LeveragedTTPsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Leveraged_TTP':
            obj_ = stix_common_binding.RelatedTTPType.factory()
            obj_.build(child_)
            self.Leveraged_TTP.append(obj_)
        super(LeveragedTTPsType, self).buildChildren(child_, node, nodeName_, True)
# end class LeveragedTTPsType

class RelatedIncidentsType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Related_Incident=None):
        super(RelatedIncidentsType, self).__init__(scope=scope)
        if Related_Incident is None:
            self.Related_Incident = []
        else:
            self.Related_Incident = Related_Incident
    def factory(*args_, **kwargs_):
        if RelatedIncidentsType.subclass:
            return RelatedIncidentsType.subclass(*args_, **kwargs_)
        else:
            return RelatedIncidentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Related_Incident(self): return self.Related_Incident
    def set_Related_Incident(self, Related_Incident): self.Related_Incident = Related_Incident
    def add_Related_Incident(self, value): self.Related_Incident.append(value)
    def insert_Related_Incident(self, index, value): self.Related_Incident[index] = value
    def hasContent_(self):
        if (
            self.Related_Incident or
            super(RelatedIncidentsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIncidentsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedIncidentsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='RelatedIncidentsType'):
        super(RelatedIncidentsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedIncidentsType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedIncidentsType', fromsubclass_=False, pretty_print=True):
        super(RelatedIncidentsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Related_Incident_ in self.Related_Incident:
            Related_Incident_.export(lwrite, level, nsmap, namespace_, name_='Related_Incident', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedIncidentsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Related_Incident':
            obj_ = stix_common_binding.RelatedIncidentType.factory()
            obj_.build(child_)
            self.Related_Incident.append(obj_)
        super(RelatedIncidentsType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedIncidentsType

class AssetTypeType(stix_common_binding.ControlledVocabularyStringType):
    """This field specifies the number of assets of this type affected.
    This field is implemented through the xsi:type controlled
    vocabulary extension mechanism. The default vocabulary type is
    AssetTypeVocab-1.0 in the
    http://stix.mitre.org/default_vocabularies-1 namespace. This
    type is defined in the stix_default_vocabularies.xsd file or at
    the URL http://stix.mitre.org/XMLSchema/default_vocabularies/1.0
    .0/stix_default_vocabularies.xsd . Users may also define their
    own vocabulary using the type extension mechanism, specify a
    vocabulary name and reference using the attributes, or simply
    use this as a string field."""
    subclass = None
    superclass = stix_common_binding.ControlledVocabularyStringType
    def __init__(self, vocab_reference=None, vocab_name=None, count_affected=None, valueOf_=None):
        super(AssetTypeType, self).__init__(vocab_reference=vocab_reference, vocab_name=vocab_name, valueOf_=valueOf_)
        self.count_affected = _cast(None, count_affected)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if AssetTypeType.subclass:
            return AssetTypeType.subclass(*args_, **kwargs_)
        else:
            return AssetTypeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_count_affected(self): return self.count_affected
    def set_count_affected(self, count_affected): self.count_affected = count_affected
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_ or
            super(AssetTypeType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AssetTypeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AssetTypeType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='AssetTypeType'):
        super(AssetTypeType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='AssetTypeType')
        if self.count_affected is not None and 'count_affected' not in already_processed:
            already_processed.add('count_affected')
            lwrite(' count_affected=%s' % (quote_attrib(self.count_affected), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AssetTypeType', fromsubclass_=False, pretty_print=True):
        super(AssetTypeType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('count_affected', node)
        if value is not None and 'count_affected' not in already_processed:
            already_processed.add('count_affected')
            self.count_affected = value
        super(AssetTypeType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class AssetTypeType

class IncidentType(stix_common_binding.IncidentBaseType):
    """The IncidentType characterizes a single cyber threat
    Incident.Specifies the relevant STIX-Incident schema version for
    this content.Specifies a URL referencing the location for the
    Incident specification."""
    subclass = None
    superclass = stix_common_binding.IncidentBaseType
    def __init__(self, idref=None, id=None, timestamp=None, URL=None, version=None, Title=None, External_ID=None, Time=None, Description=None, Short_Description=None, Categories=None, Reporter=None, Responder=None, Coordinator=None, Victim=None, Affected_Assets=None, Impact_Assessment=None, Status=None, Related_Indicators=None, Related_Observables=None, Leveraged_TTPs=None, Attributed_Threat_Actors=None, Intended_Effect=None, Security_Compromise=None, Discovery_Method=None, Related_Incidents=None, COA_Requested=None, COA_Taken=None, Confidence=None, Contact=None, History=None, Information_Source=None, Handling=None, Related_Packages=None):
        super(IncidentType, self).__init__(timestamp=timestamp, idref=idref, id=id)
        self.xmlns          = "http://stix.mitre.org/Incident-1"
        self.xmlns_prefix   = "incident"
        self.xml_type       = "IncidentType"
        self.URL = _cast(None, URL)
        self.version = _cast(None, version)
        self.Title = Title
        if External_ID is None:
            self.External_ID = []
        else:
            self.External_ID = External_ID
        self.Time = Time
        self.Description = Description
        self.Short_Description = Short_Description
        self.Categories = Categories
        self.Reporter = Reporter
        if Responder is None:
            self.Responder = []
        else:
            self.Responder = Responder
        if Coordinator is None:
            self.Coordinator = []
        else:
            self.Coordinator = Coordinator
        if Victim is None:
            self.Victim = []
        else:
            self.Victim = Victim
        self.Affected_Assets = Affected_Assets
        self.Impact_Assessment = Impact_Assessment
        self.Status = Status
        self.Related_Indicators = Related_Indicators
        self.Related_Observables = Related_Observables
        self.Leveraged_TTPs = Leveraged_TTPs
        self.Attributed_Threat_Actors = Attributed_Threat_Actors
        if Intended_Effect is None:
            self.Intended_Effect = []
        else:
            self.Intended_Effect = Intended_Effect
        self.Security_Compromise = Security_Compromise
        if Discovery_Method is None:
            self.Discovery_Method = []
        else:
            self.Discovery_Method = Discovery_Method
        self.Related_Incidents = Related_Incidents
        if COA_Requested is None:
            self.COA_Requested = []
        else:
            self.COA_Requested = COA_Requested
        if COA_Taken is None:
            self.COA_Taken = []
        else:
            self.COA_Taken = COA_Taken
        self.Confidence = Confidence
        if Contact is None:
            self.Contact = []
        else:
            self.Contact = Contact
        self.History = History
        self.Information_Source = Information_Source
        self.Handling = Handling
        self.Related_Packages = Related_Packages
    def factory(*args_, **kwargs_):
        if IncidentType.subclass:
            return IncidentType.subclass(*args_, **kwargs_)
        else:
            return IncidentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_External_ID(self): return self.External_ID
    def set_External_ID(self, External_ID): self.External_ID = External_ID
    def add_External_ID(self, value): self.External_ID.append(value)
    def insert_External_ID(self, index, value): self.External_ID[index] = value
    def get_Time(self): return self.Time
    def set_Time(self, Time): self.Time = Time
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_Categories(self): return self.Categories
    def set_Categories(self, Categories): self.Categories = Categories
    def get_Reporter(self): return self.Reporter
    def set_Reporter(self, Reporter): self.Reporter = Reporter
    def get_Responder(self): return self.Responder
    def set_Responder(self, Responder): self.Responder = Responder
    def add_Responder(self, value): self.Responder.append(value)
    def insert_Responder(self, index, value): self.Responder[index] = value
    def get_Coordinator(self): return self.Coordinator
    def set_Coordinator(self, Coordinator): self.Coordinator = Coordinator
    def add_Coordinator(self, value): self.Coordinator.append(value)
    def insert_Coordinator(self, index, value): self.Coordinator[index] = value
    def get_Victim(self): return self.Victim
    def set_Victim(self, Victim): self.Victim = Victim
    def add_Victim(self, value): self.Victim.append(value)
    def insert_Victim(self, index, value): self.Victim[index] = value
    def get_Affected_Assets(self): return self.Affected_Assets
    def set_Affected_Assets(self, Affected_Assets): self.Affected_Assets = Affected_Assets
    def get_Impact_Assessment(self): return self.Impact_Assessment
    def set_Impact_Assessment(self, Impact_Assessment): self.Impact_Assessment = Impact_Assessment
    def get_Status(self): return self.Status
    def set_Status(self, Status): self.Status = Status
    def get_Related_Indicators(self): return self.Related_Indicators
    def set_Related_Indicators(self, Related_Indicators): self.Related_Indicators = Related_Indicators
    def get_Related_Observables(self): return self.Related_Observables
    def set_Related_Observables(self, Related_Observables): self.Related_Observables = Related_Observables
    def get_Leveraged_TTPs(self): return self.Leveraged_TTPs
    def set_Leveraged_TTPs(self, Leveraged_TTPs): self.Leveraged_TTPs = Leveraged_TTPs
    def get_Attributed_Threat_Actors(self): return self.Attributed_Threat_Actors
    def set_Attributed_Threat_Actors(self, Attributed_Threat_Actors): self.Attributed_Threat_Actors = Attributed_Threat_Actors
    def get_Intended_Effect(self): return self.Intended_Effect
    def set_Intended_Effect(self, Intended_Effect): self.Intended_Effect = Intended_Effect
    def add_Intended_Effect(self, value): self.Intended_Effect.append(value)
    def insert_Intended_Effect(self, index, value): self.Intended_Effect[index] = value
    def get_Security_Compromise(self): return self.Security_Compromise
    def set_Security_Compromise(self, Security_Compromise): self.Security_Compromise = Security_Compromise
    def get_Discovery_Method(self): return self.Discovery_Method
    def set_Discovery_Method(self, Discovery_Method): self.Discovery_Method = Discovery_Method
    def add_Discovery_Method(self, value): self.Discovery_Method.append(value)
    def insert_Discovery_Method(self, index, value): self.Discovery_Method[index] = value
    def get_Related_Incidents(self): return self.Related_Incidents
    def set_Related_Incidents(self, Related_Incidents): self.Related_Incidents = Related_Incidents
    def get_COA_Requested(self): return self.COA_Requested
    def set_COA_Requested(self, COA_Requested): self.COA_Requested = COA_Requested
    def add_COA_Requested(self, value): self.COA_Requested.append(value)
    def insert_COA_Requested(self, index, value): self.COA_Requested[index] = value
    def get_COA_Taken(self): return self.COA_Taken
    def set_COA_Taken(self, COA_Taken): self.COA_Taken = COA_Taken
    def add_COA_Taken(self, value): self.COA_Taken.append(value)
    def insert_COA_Taken(self, index, value): self.COA_Taken[index] = value
    def get_Confidence(self): return self.Confidence
    def set_Confidence(self, Confidence): self.Confidence = Confidence
    def get_Contact(self): return self.Contact
    def set_Contact(self, Contact): self.Contact = Contact
    def add_Contact(self, value): self.Contact.append(value)
    def insert_Contact(self, index, value): self.Contact[index] = value
    def get_History(self): return self.History
    def set_History(self, History): self.History = History
    def get_Information_Source(self): return self.Information_Source
    def set_Information_Source(self, Information_Source): self.Information_Source = Information_Source
    def get_Handling(self): return self.Handling
    def set_Handling(self, Handling): self.Handling = Handling
    def get_Related_Packages(self): return self.Related_Packages
    def set_Related_Packages(self, Related_Packages): self.Related_Packages = Related_Packages
    def get_URL(self): return self.URL
    def set_URL(self, URL): self.URL = URL
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def hasContent_(self):
        if (
            self.Title is not None or
            self.External_ID or
            self.Time is not None or
            self.Description is not None or
            self.Short_Description is not None or
            self.Categories is not None or
            self.Reporter is not None or
            self.Responder or
            self.Coordinator or
            self.Victim or
            self.Affected_Assets is not None or
            self.Impact_Assessment is not None or
            self.Status is not None or
            self.Related_Indicators is not None or
            self.Related_Observables is not None or
            self.Leveraged_TTPs is not None or
            self.Attributed_Threat_Actors is not None or
            self.Intended_Effect or
            self.Security_Compromise is not None or
            self.Discovery_Method or
            self.Related_Incidents is not None or
            self.COA_Requested or
            self.COA_Taken or
            self.Confidence is not None or
            self.Contact or
            self.History is not None or
            self.Information_Source is not None or
            self.Handling is not None or
            self.Related_Packages is not None or
            super(IncidentType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='Incident', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='Incident')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='Incident'):
        super(IncidentType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='Incident')
#         if 'xmlns' not in already_processed:
#             already_processed.add('xmlns')
#             xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
#             lwrite(xmlns)
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
            lwrite(xsi_type)
        if self.URL is not None and 'URL' not in already_processed:
            already_processed.add('URL')
            lwrite(' URL=%s' % (quote_attrib(self.URL), ))
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            lwrite(' version=%s' % (quote_attrib(self.version), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IncidentType', fromsubclass_=False, pretty_print=True):
        super(IncidentType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_], quote_xml(self.Title), nsmap[namespace_], eol_))
        for External_ID_ in self.External_ID:
            External_ID_.export(lwrite, level, nsmap, namespace_, name_='External_ID', pretty_print=pretty_print)
        if self.Time is not None:
            self.Time.export(lwrite, level, nsmap, namespace_, name_='Time', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Short_Description is not None:
            self.Short_Description.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
        if self.Categories is not None:
            self.Categories.export(lwrite, level, nsmap, namespace_, name_='Categories', pretty_print=pretty_print)
        if self.Reporter is not None:
            self.Reporter.export(lwrite, level, nsmap, namespace_, name_='Reporter', pretty_print=pretty_print)
        for Responder_ in self.Responder:
            Responder_.export(lwrite, level, nsmap, namespace_, name_='Responder', pretty_print=pretty_print)
        for Coordinator_ in self.Coordinator:
            Coordinator_.export(lwrite, level, nsmap, namespace_, name_='Coordinator', pretty_print=pretty_print)
        for Victim_ in self.Victim:
            Victim_.export(lwrite, level, nsmap, namespace_, name_='Victim', pretty_print=pretty_print)
        if self.Affected_Assets is not None:
            self.Affected_Assets.export(lwrite, level, nsmap, namespace_, name_='Affected_Assets', pretty_print=pretty_print)
        if self.Impact_Assessment is not None:
            self.Impact_Assessment.export(lwrite, level, nsmap, namespace_, name_='Impact_Assessment', pretty_print=pretty_print)
        if self.Status is not None:
            self.Status.export(lwrite, level, nsmap, namespace_, name_='Status', pretty_print=pretty_print)
        if self.Related_Indicators is not None:
            self.Related_Indicators.export(lwrite, level, nsmap, namespace_, name_='Related_Indicators', pretty_print=pretty_print)
        if self.Related_Observables is not None:
            self.Related_Observables.export(lwrite, level, nsmap, namespace_, name_='Related_Observables', pretty_print=pretty_print)
        if self.Leveraged_TTPs is not None:
            self.Leveraged_TTPs.export(lwrite, level, nsmap, namespace_, name_='Leveraged_TTPs', pretty_print=pretty_print)
        if self.Attributed_Threat_Actors is not None:
            self.Attributed_Threat_Actors.export(lwrite, level, nsmap, namespace_, name_='Attributed_Threat_Actors', pretty_print=pretty_print)
        for Intended_Effect_ in self.Intended_Effect:
            Intended_Effect_.export(lwrite, level, nsmap, namespace_, name_='Intended_Effect', pretty_print=pretty_print)
        if self.Security_Compromise is not None:
            self.Security_Compromise.export(lwrite, level, nsmap, namespace_, name_='Security_Compromise', pretty_print=pretty_print)
        for Discovery_Method_ in self.Discovery_Method:
            Discovery_Method_.export(lwrite, level, nsmap, namespace_, name_='Discovery_Method', pretty_print=pretty_print)
        if self.Related_Incidents is not None:
            self.Related_Incidents.export(lwrite, level, nsmap, namespace_, name_='Related_Incidents', pretty_print=pretty_print)
        for COA_Requested_ in self.COA_Requested:
            COA_Requested_.export(lwrite, level, nsmap, namespace_, name_='COA_Requested', pretty_print=pretty_print)
        for COA_Taken_ in self.COA_Taken:
            COA_Taken_.export(lwrite, level, nsmap, namespace_, name_='COA_Taken', pretty_print=pretty_print)
        if self.Confidence is not None:
            self.Confidence.export(lwrite, level, nsmap, namespace_, name_='Confidence', pretty_print=pretty_print)
        for Contact_ in self.Contact:
            Contact_.export(lwrite, level, nsmap, namespace_, name_='Contact', pretty_print=pretty_print)
        if self.History is not None:
            self.History.export(lwrite, level, nsmap, namespace_, name_='History', pretty_print=pretty_print)
        if self.Information_Source is not None:
            self.Information_Source.export(lwrite, level, nsmap, namespace_, name_='Information_Source', pretty_print=pretty_print)
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
        value = find_attr_value_('URL', node)
        if value is not None and 'URL' not in already_processed:
            already_processed.add('URL')
            self.URL = value
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = value
        super(IncidentType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'External_ID':
            obj_ = ExternalIDType.factory()
            obj_.build(child_)
            self.External_ID.append(obj_)
        elif nodeName_ == 'Time':
            obj_ = TimeType.factory()
            obj_.build(child_)
            self.set_Time(obj_)
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Short_Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Short_Description(obj_)
        elif nodeName_ == 'Categories':
            obj_ = CategoriesType.factory()
            obj_.build(child_)
            self.set_Categories(obj_)
        elif nodeName_ == 'Reporter':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Reporter(obj_)
        elif nodeName_ == 'Responder':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.Responder.append(obj_)
        elif nodeName_ == 'Coordinator':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.Coordinator.append(obj_)
        elif nodeName_ == 'Victim':
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
                obj_ = stix_common_binding.IdentityType.factory() # IdentityType is not abstract
            obj_.build(child_)
            self.Victim.append(obj_)
        elif nodeName_ == 'Affected_Assets':
            obj_ = AffectedAssetsType.factory()
            obj_.build(child_)
            self.set_Affected_Assets(obj_)
        elif nodeName_ == 'Impact_Assessment':
            obj_ = ImpactAssessmentType.factory()
            obj_.build(child_)
            self.set_Impact_Assessment(obj_)
        elif nodeName_ == 'Status':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Status(obj_)
        elif nodeName_ == 'Related_Indicators':
            obj_ = RelatedIndicatorsType.factory()
            obj_.build(child_)
            self.set_Related_Indicators(obj_)
        elif nodeName_ == 'Related_Observables':
            obj_ = RelatedObservablesType.factory()
            obj_.build(child_)
            self.set_Related_Observables(obj_)
        elif nodeName_ == 'Leveraged_TTPs':
            obj_ = LeveragedTTPsType.factory()
            obj_.build(child_)
            self.set_Leveraged_TTPs(obj_)
        elif nodeName_ == 'Attributed_Threat_Actors':
            obj_ = AttributedThreatActorsType.factory()
            obj_.build(child_)
            self.set_Attributed_Threat_Actors(obj_)
        elif nodeName_ == 'Intended_Effect':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.Intended_Effect.append(obj_)
        elif nodeName_ == 'Security_Compromise':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Security_Compromise(obj_)
        elif nodeName_ == 'Discovery_Method':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Discovery_Method.append(obj_)
        elif nodeName_ == 'Related_Incidents':
            obj_ = RelatedIncidentsType.factory()
            obj_.build(child_)
            self.set_Related_Incidents(obj_)
        elif nodeName_ == 'COA_Requested':
            obj_ = COARequestedType.factory()
            obj_.build(child_)
            self.COA_Requested.append(obj_)
        elif nodeName_ == 'COA_Taken':
            class_obj_ = self.get_class_obj_(child_, COATakenType)
            obj_ = class_obj_.factory()
            obj_.build(child_)
            self.COA_Taken.append(obj_)
        elif nodeName_ == 'Confidence':
            obj_ = stix_common_binding.ConfidenceType.factory()
            obj_.build(child_)
            self.set_Confidence(obj_)
        elif nodeName_ == 'Contact':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.Contact.append(obj_)
        elif nodeName_ == 'History':
            obj_ = HistoryType.factory()
            obj_.build(child_)
            self.set_History(obj_)
        elif nodeName_ == 'Information_Source':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Information_Source(obj_)
        elif nodeName_ == 'Handling':
            obj_ = data_marking_binding.MarkingType.factory()
            obj_.build(child_)
            self.set_Handling(obj_)
        elif nodeName_ == 'Related_Packages':
            obj_ = stix_common_binding.RelatedPackageRefsType.factory()
            obj_.build(child_)
            self.set_Related_Packages(obj_)
        super(IncidentType, self).buildChildren(child_, node, nodeName_, True)
# end class IncidentType

class NonPublicDataCompromisedType(stix_common_binding.ControlledVocabularyStringType):
    """This type represents whether non-public data was compromised or
    exposed and whether that data was encrypted or not.Indicates
    whether the data that was compromised was encrypted or not."""
    subclass = None
    superclass = stix_common_binding.ControlledVocabularyStringType
    def __init__(self, vocab_reference=None, vocab_name=None, data_encrypted=None):
        super(NonPublicDataCompromisedType, self).__init__(vocab_reference=vocab_reference, vocab_name=vocab_name)
        self.data_encrypted = _cast(bool, data_encrypted)
        pass
    def factory(*args_, **kwargs_):
        if NonPublicDataCompromisedType.subclass:
            return NonPublicDataCompromisedType.subclass(*args_, **kwargs_)
        else:
            return NonPublicDataCompromisedType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_data_encrypted(self): return self.data_encrypted
    def set_data_encrypted(self, data_encrypted): self.data_encrypted = data_encrypted
    def hasContent_(self):
        if (
            super(NonPublicDataCompromisedType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='NonPublicDataCompromisedType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NonPublicDataCompromisedType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='NonPublicDataCompromisedType'):
        super(NonPublicDataCompromisedType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='NonPublicDataCompromisedType')
        if self.data_encrypted is not None and 'data_encrypted' not in already_processed:
            already_processed.add('data_encrypted')
            lwrite(' data_encrypted="%s"' % self.gds_format_boolean(self.data_encrypted, input_name='data_encrypted'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='NonPublicDataCompromisedType', fromsubclass_=False, pretty_print=True):
        super(NonPublicDataCompromisedType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('data_encrypted', node)
        if value is not None and 'data_encrypted' not in already_processed:
            already_processed.add('data_encrypted')
            if value in ('true', '1'):
                self.data_encrypted = True
            elif value in ('false', '0'):
                self.data_encrypted = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        super(NonPublicDataCompromisedType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        super(NonPublicDataCompromisedType, self).buildChildren(child_, node, nodeName_, True)
        pass
# end class NonPublicDataCompromisedType

class ExternalIDType(GeneratedsSuper):
    """The ExternalIDType provides a reference to an ID of an incident in a
    remote system.Specifies the source of the External ID."""
    subclass = None
    superclass = None
    def __init__(self, source=None, valueOf_=None):
        self.source = _cast(None, source)
        self.valueOf_ = valueOf_
    def factory(*args_, **kwargs_):
        if ExternalIDType.subclass:
            return ExternalIDType.subclass(*args_, **kwargs_)
        else:
            return ExternalIDType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_source(self): return self.source
    def set_source(self, source): self.source = source
    def get_valueOf_(self): return self.valueOf_
    def set_valueOf_(self, valueOf_): self.valueOf_ = valueOf_
    def hasContent_(self):
        if (
            self.valueOf_
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExternalIDType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ExternalIDType')
        if self.hasContent_():
            lwrite('>')
            lwrite(quote_xml(self.valueOf_))
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='incident:', name_='ExternalIDType'):
        if self.source is not None and 'source' not in already_processed:
            already_processed.add('source')
            lwrite(' source=%s' % (quote_attrib(self.source), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ExternalIDType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        self.valueOf_ = get_all_text_(node)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('source', node)
        if value is not None and 'source' not in already_processed:
            already_processed.add('source')
            self.source = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class ExternalIDType


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
        rootTag = 'Incident'
        rootClass = IncidentType
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
        rootTag = 'Incident'
        rootClass = IncidentType
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
        rootTag = 'Incident'
        rootClass = IncidentType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="Incident",
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
    "PropertyAffectedType",
    "AffectedAssetType",
    "ImpactAssessmentType",
    "ExternalImpactAssessmentModelType",
    "COATakenType",
    "JournalEntryType",
    "COARequestedType",
    "ContributorsType",
    "COATimeType",
    "LossEstimationType",
    "TotalLossEstimationType",
    "IndirectImpactSummaryType",
    "DirectImpactSummaryType",
    "NatureOfSecurityEffectType",
    "HistoryItemType",
    "HistoryType",
    "AffectedAssetsType",
    "TimeType",
    "CategoriesType",
    "EffectsType",
    "AttributedThreatActorsType",
    "RelatedIndicatorsType",
    "RelatedObservablesType",
    "LeveragedTTPsType",
    "RelatedIncidentsType",
    "AssetTypeType",
    "IncidentType"
    ]
