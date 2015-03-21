# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:06:29 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.data_marking as data_marking_binding

XML_NS = "http://stix.mitre.org/ThreatActor-1"


#
# Data representation classes.
#

class ObservedTTPsType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Observed_TTP=None):
        super(ObservedTTPsType, self).__init__(scope=scope)
        if Observed_TTP is None:
            self.Observed_TTP = []
        else:
            self.Observed_TTP = Observed_TTP
    def factory(*args_, **kwargs_):
        if ObservedTTPsType.subclass:
            return ObservedTTPsType.subclass(*args_, **kwargs_)
        else:
            return ObservedTTPsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Observed_TTP(self): return self.Observed_TTP
    def set_Observed_TTP(self, Observed_TTP): self.Observed_TTP = Observed_TTP
    def add_Observed_TTP(self, value): self.Observed_TTP.append(value)
    def insert_Observed_TTP(self, index, value): self.Observed_TTP[index] = value
    def hasContent_(self):
        if (
            self.Observed_TTP or
            super(ObservedTTPsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ObservedTTPsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ObservedTTPsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ta:', name_='ObservedTTPsType'):
        super(ObservedTTPsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ObservedTTPsType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ObservedTTPsType', fromsubclass_=False, pretty_print=True):
        super(ObservedTTPsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Observed_TTP_ in self.Observed_TTP:
            Observed_TTP_.export(lwrite, level, nsmap, namespace_, name_='Observed_TTP', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(ObservedTTPsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Observed_TTP':
            obj_ = stix_common_binding.RelatedTTPType.factory()
            obj_.build(child_)
            self.Observed_TTP.append(obj_)
        super(ObservedTTPsType, self).buildChildren(child_, node, nodeName_, True)
# end class ObservedTTPsType

class AssociatedCampaignsType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Associated_Campaign=None):
        super(AssociatedCampaignsType, self).__init__(scope=scope)
        if Associated_Campaign is None:
            self.Associated_Campaign = []
        else:
            self.Associated_Campaign = Associated_Campaign
    def factory(*args_, **kwargs_):
        if AssociatedCampaignsType.subclass:
            return AssociatedCampaignsType.subclass(*args_, **kwargs_)
        else:
            return AssociatedCampaignsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Associated_Campaign(self): return self.Associated_Campaign
    def set_Associated_Campaign(self, Associated_Campaign): self.Associated_Campaign = Associated_Campaign
    def add_Associated_Campaign(self, value): self.Associated_Campaign.append(value)
    def insert_Associated_Campaign(self, index, value): self.Associated_Campaign[index] = value
    def hasContent_(self):
        if (
            self.Associated_Campaign or
            super(AssociatedCampaignsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AssociatedCampaignsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AssociatedCampaignsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ta:', name_='AssociatedCampaignsType'):
        super(AssociatedCampaignsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='AssociatedCampaignsType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AssociatedCampaignsType', fromsubclass_=False, pretty_print=True):
        super(AssociatedCampaignsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Associated_Campaign_ in self.Associated_Campaign:
            Associated_Campaign_.export(lwrite, level, nsmap, namespace_, name_='Associated_Campaign', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(AssociatedCampaignsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Associated_Campaign':
            obj_ = stix_common_binding.RelatedCampaignType.factory()
            obj_.build(child_)
            self.Associated_Campaign.append(obj_)
        super(AssociatedCampaignsType, self).buildChildren(child_, node, nodeName_, True)
# end class AssociatedCampaignsType

class AssociatedActorsType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Associated_Actor=None):
        super(AssociatedActorsType, self).__init__(scope=scope)
        if Associated_Actor is None:
            self.Associated_Actor = []
        else:
            self.Associated_Actor = Associated_Actor
    def factory(*args_, **kwargs_):
        if AssociatedActorsType.subclass:
            return AssociatedActorsType.subclass(*args_, **kwargs_)
        else:
            return AssociatedActorsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Associated_Actor(self): return self.Associated_Actor
    def set_Associated_Actor(self, Associated_Actor): self.Associated_Actor = Associated_Actor
    def add_Associated_Actor(self, value): self.Associated_Actor.append(value)
    def insert_Associated_Actor(self, index, value): self.Associated_Actor[index] = value
    def hasContent_(self):
        if (
            self.Associated_Actor or
            super(AssociatedActorsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AssociatedActorsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AssociatedActorsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ta:', name_='AssociatedActorsType'):
        super(AssociatedActorsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='AssociatedActorsType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AssociatedActorsType', fromsubclass_=False, pretty_print=True):
        super(AssociatedActorsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Associated_Actor_ in self.Associated_Actor:
            Associated_Actor_.export(lwrite, level, nsmap, namespace_, name_='Associated_Actor', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(AssociatedActorsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Associated_Actor':
            obj_ = stix_common_binding.RelatedThreatActorType.factory()
            obj_.build(child_)
            self.Associated_Actor.append(obj_)
        super(AssociatedActorsType, self).buildChildren(child_, node, nodeName_, True)
# end class AssociatedActorsType

class ThreatActorType(stix_common_binding.ThreatActorBaseType):
    """Specifies the relevant STIX-ThreatActor schema version for this
    content."""
    subclass = None
    superclass = stix_common_binding.ThreatActorBaseType
    def __init__(self, idref=None, id=None, timestamp=None, version=None, Title=None, Description=None, Short_Description=None, Identity=None, Type=None, Motivation=None, Sophistication=None, Intended_Effect=None, Planning_And_Operational_Support=None, Observed_TTPs=None, Associated_Campaigns=None, Associated_Actors=None, Handling=None, Confidence=None, Information_Source=None, Related_Packages=None):
        super(ThreatActorType, self).__init__(idref=idref, id=id, timestamp=timestamp)
        self.xmlns          = "http://stix.mitre.org/ThreatActor-1"
        self.xmlns_prefix   = "ta"
        self.xml_type       = "ThreatActorType"
        self.version = _cast(None, version)
        self.Title = Title
        self.Description = Description
        self.Short_Description = Short_Description
        self.Identity = Identity
        if Type is None:
            self.Type = []
        else:
            self.Type = Type
        if Motivation is None:
            self.Motivation = []
        else:
            self.Motivation = Motivation
        if Sophistication is None:
            self.Sophistication = []
        else:
            self.Sophistication = Sophistication
        if Intended_Effect is None:
            self.Intended_Effect = []
        else:
            self.Intended_Effect = Intended_Effect
        if Planning_And_Operational_Support is None:
            self.Planning_And_Operational_Support = []
        else:
            self.Planning_And_Operational_Support = Planning_And_Operational_Support
        self.Observed_TTPs = Observed_TTPs
        self.Associated_Campaigns = Associated_Campaigns
        self.Associated_Actors = Associated_Actors
        self.Handling = Handling
        self.Confidence = Confidence
        self.Information_Source = Information_Source
        self.Related_Packages = Related_Packages
    def factory(*args_, **kwargs_):
        if ThreatActorType.subclass:
            return ThreatActorType.subclass(*args_, **kwargs_)
        else:
            return ThreatActorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_Identity(self): return self.Identity
    def set_Identity(self, Identity): self.Identity = Identity
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def add_Type(self, value): self.Type.append(value)
    def insert_Type(self, index, value): self.Type[index] = value
    def get_Motivation(self): return self.Motivation
    def set_Motivation(self, Motivation): self.Motivation = Motivation
    def add_Motivation(self, value): self.Motivation.append(value)
    def insert_Motivation(self, index, value): self.Motivation[index] = value
    def get_Sophistication(self): return self.Sophistication
    def set_Sophistication(self, Sophistication): self.Sophistication = Sophistication
    def add_Sophistication(self, value): self.Sophistication.append(value)
    def insert_Sophistication(self, index, value): self.Sophistication[index] = value
    def get_Intended_Effect(self): return self.Intended_Effect
    def set_Intended_Effect(self, Intended_Effect): self.Intended_Effect = Intended_Effect
    def add_Intended_Effect(self, value): self.Intended_Effect.append(value)
    def insert_Intended_Effect(self, index, value): self.Intended_Effect[index] = value
    def get_Planning_And_Operational_Support(self): return self.Planning_And_Operational_Support
    def set_Planning_And_Operational_Support(self, Planning_And_Operational_Support): self.Planning_And_Operational_Support = Planning_And_Operational_Support
    def add_Planning_And_Operational_Support(self, value): self.Planning_And_Operational_Support.append(value)
    def insert_Planning_And_Operational_Support(self, index, value): self.Planning_And_Operational_Support[index] = value
    def get_Observed_TTPs(self): return self.Observed_TTPs
    def set_Observed_TTPs(self, Observed_TTPs): self.Observed_TTPs = Observed_TTPs
    def get_Associated_Campaigns(self): return self.Associated_Campaigns
    def set_Associated_Campaigns(self, Associated_Campaigns): self.Associated_Campaigns = Associated_Campaigns
    def get_Associated_Actors(self): return self.Associated_Actors
    def set_Associated_Actors(self, Associated_Actors): self.Associated_Actors = Associated_Actors
    def get_Handling(self): return self.Handling
    def set_Handling(self, Handling): self.Handling = Handling
    def get_Confidence(self): return self.Confidence
    def set_Confidence(self, Confidence): self.Confidence = Confidence
    def get_Information_Source(self): return self.Information_Source
    def set_Information_Source(self, Information_Source): self.Information_Source = Information_Source
    def get_Related_Packages(self): return self.Related_Packages
    def set_Related_Packages(self, Related_Packages): self.Related_Packages = Related_Packages
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Description is not None or
            self.Short_Description is not None or
            self.Identity is not None or
            self.Type or
            self.Motivation or
            self.Sophistication or
            self.Intended_Effect or
            self.Planning_And_Operational_Support or
            self.Observed_TTPs is not None or
            self.Associated_Campaigns is not None or
            self.Associated_Actors is not None or
            self.Handling is not None or
            self.Confidence is not None or
            self.Information_Source is not None or
            self.Related_Packages is not None or
            super(ThreatActorType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='Threat_Actor', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='Threat_Actor')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='ta:', name_='Threat_Actor'):
        super(ThreatActorType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='Threat_Actor')
        # if 'xmlns' not in already_processed:
        #     already_processed.add('xmlns')
        #     xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
        #     lwrite(xmlns)
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
            lwrite(xsi_type)
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            lwrite(' version=%s' % (quote_attrib(self.version), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ThreatActorType', fromsubclass_=False, pretty_print=True):
        super(ThreatActorType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
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
        if self.Identity is not None:
            self.Identity.export(lwrite, level, nsmap, namespace_, name_='Identity', pretty_print=pretty_print)
        for Type_ in self.Type:
            Type_.export(lwrite, level, nsmap, namespace_, name_='Type', pretty_print=pretty_print)
        for Motivation_ in self.Motivation:
            Motivation_.export(lwrite, level, nsmap, namespace_, name_='Motivation', pretty_print=pretty_print)
        for Sophistication_ in self.Sophistication:
            Sophistication_.export(lwrite, level, nsmap, namespace_, name_='Sophistication', pretty_print=pretty_print)
        for Intended_Effect_ in self.Intended_Effect:
            Intended_Effect_.export(lwrite, level, nsmap, namespace_, name_='Intended_Effect', pretty_print=pretty_print)
        for Planning_And_Operational_Support_ in self.Planning_And_Operational_Support:
            Planning_And_Operational_Support_.export(lwrite, level, nsmap, namespace_, name_='Planning_And_Operational_Support', pretty_print=pretty_print)
        if self.Observed_TTPs is not None:
            self.Observed_TTPs.export(lwrite, level, nsmap, namespace_, name_='Observed_TTPs', pretty_print=pretty_print)
        if self.Associated_Campaigns is not None:
            self.Associated_Campaigns.export(lwrite, level, nsmap, namespace_, name_='Associated_Campaigns', pretty_print=pretty_print)
        if self.Associated_Actors is not None:
            self.Associated_Actors.export(lwrite, level, nsmap, namespace_, name_='Associated_Actors', pretty_print=pretty_print)
        if self.Handling is not None:
            self.Handling.export(lwrite, level, nsmap, namespace_, name_='Handling', pretty_print=pretty_print)
        if self.Confidence is not None:
            self.Confidence.export(lwrite, level, nsmap, namespace_, name_='Confidence', pretty_print=pretty_print)
        if self.Information_Source is not None:
            self.Information_Source.export(lwrite, level, nsmap, namespace_, name_='Information_Source', pretty_print=pretty_print)
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
        super(ThreatActorType, self).buildAttributes(node, attrs, already_processed)
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
                    from .extensions.identity import ciq_identity_3_0
                    obj_ = ciq_identity_3_0.CIQIdentity3_0InstanceType.factory()
            else:
                obj_ = stix_common_binding.IdentityType.factory() # IdentityType is not abstract

            obj_.build(child_)
            self.set_Identity(obj_)
        elif nodeName_ == 'Type':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.Type.append(obj_)
        elif nodeName_ == 'Motivation':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.Motivation.append(obj_)
        elif nodeName_ == 'Sophistication':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.Sophistication.append(obj_)
        elif nodeName_ == 'Intended_Effect':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.Intended_Effect.append(obj_)
        elif nodeName_ == 'Planning_And_Operational_Support':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.Planning_And_Operational_Support.append(obj_)
        elif nodeName_ == 'Observed_TTPs':
            obj_ = ObservedTTPsType.factory()
            obj_.build(child_)
            self.set_Observed_TTPs(obj_)
        elif nodeName_ == 'Associated_Campaigns':
            obj_ = AssociatedCampaignsType.factory()
            obj_.build(child_)
            self.set_Associated_Campaigns(obj_)
        elif nodeName_ == 'Associated_Actors':
            obj_ = AssociatedActorsType.factory()
            obj_.build(child_)
            self.set_Associated_Actors(obj_)
        elif nodeName_ == 'Handling':
            obj_ = data_marking_binding.MarkingType.factory()
            obj_.build(child_)
            self.set_Handling(obj_)
        elif nodeName_ == 'Confidence':
            obj_ = stix_common_binding.ConfidenceType.factory()
            obj_.build(child_)
            self.set_Confidence(obj_)
        elif nodeName_ == 'Information_Source':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Information_Source(obj_)
        elif nodeName_ == 'Related_Packages':
            obj_ = stix_common_binding.RelatedPackageRefsType.factory()
            obj_.build(child_)
            self.set_Related_Packages(obj_)
        super(ThreatActorType, self).buildChildren(child_, node, nodeName_, True)
# end class ThreatActorType

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
        rootTag = 'Threat_Actor'
        rootClass = ThreatActorType
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
        rootTag = 'Threat_Actor'
        rootClass = ThreatActorType
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
        rootTag = 'Threat_Actor'
        rootClass = ThreatActorType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="Threat_Actor",
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
    "ObservedTTPsType",
    "AssociatedCampaignsType",
    "AssociatedActorsType",
    "ThreatActorType"
    ]
