# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:06:20 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.data_marking as data_marking_binding


XML_NS = "http://stix.mitre.org/Campaign-1"

#
# Data representation classes.
#

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
    def exportAttributes(self, lwrite, level, already_processed, namespace_='campaign:', name_='NamesType'):
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
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Name.append(obj_)
# end class NamesType

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
    def exportAttributes(self, lwrite, level, already_processed, namespace_='campaign:', name_='AssociatedCampaignsType'):
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
    def exportAttributes(self, lwrite, level, already_processed, namespace_='campaign:', name_='RelatedIndicatorsType'):
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
    def exportAttributes(self, lwrite, level, already_processed, namespace_='campaign:', name_='RelatedIncidentsType'):
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
    def exportAttributes(self, lwrite, level, already_processed, namespace_='campaign:', name_='RelatedTTPsType'):
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

class AttributionType(stix_common_binding.GenericRelationshipListType):
    """AttributionType specifies suspected Threat Actors attributed to a
    given Campaign."""
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Attributed_Threat_Actor=None):
        super(AttributionType, self).__init__(scope=scope)
        if Attributed_Threat_Actor is None:
            self.Attributed_Threat_Actor = []
        else:
            self.Attributed_Threat_Actor = Attributed_Threat_Actor
    def factory(*args_, **kwargs_):
        if AttributionType.subclass:
            return AttributionType.subclass(*args_, **kwargs_)
        else:
            return AttributionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Attributed_Threat_Actor(self): return self.Attributed_Threat_Actor
    def set_Attributed_Threat_Actor(self, Attributed_Threat_Actor): self.Attributed_Threat_Actor = Attributed_Threat_Actor
    def add_Attributed_Threat_Actor(self, value): self.Attributed_Threat_Actor.append(value)
    def insert_Attributed_Threat_Actor(self, index, value): self.Attributed_Threat_Actor[index] = value
    def hasContent_(self):
        if (
            self.Attributed_Threat_Actor or
            super(AttributionType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AttributionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AttributionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='campaign:', name_='AttributionType'):
        super(AttributionType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='AttributionType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AttributionType', fromsubclass_=False, pretty_print=True):
        super(AttributionType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Attributed_Threat_Actor_ in self.Attributed_Threat_Actor:
            Attributed_Threat_Actor_.export(lwrite, level, nsmap, namespace_, name_='Attributed_Threat_Actor', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(AttributionType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Attributed_Threat_Actor':
            obj_ = stix_common_binding.RelatedThreatActorType.factory()
            obj_.build(child_)
            self.Attributed_Threat_Actor.append(obj_)
        super(AttributionType, self).buildChildren(child_, node, nodeName_, True)
# end class AttributionType

class CampaignType(stix_common_binding.CampaignBaseType):
    """The CampaignType characterizes a single cyber threat
    Campaign.Specifies the relevant STIX-Campaign schema version for
    this content."""
    subclass = None
    superclass = stix_common_binding.CampaignBaseType
    def __init__(self, idref=None, id=None, timestamp=None, version=None, Title=None, Description=None, Short_Description=None, Names=None, Intended_Effect=None, Status=None, Related_TTPs=None, Related_Incidents=None, Related_Indicators=None, Attribution=None, Associated_Campaigns=None, Confidence=None, Activity=None, Information_Source=None, Handling=None, Related_Packages=None):
        super(CampaignType, self).__init__(idref=idref, id=id, timestamp=timestamp)
        self.xmlns          = "http://stix.mitre.org/Campaign-1"
        self.xmlns_prefix   = "campaign"
        self.xml_type       = "CampaignType"
        self.version = _cast(None, version)
        self.Title = Title
        self.Description = Description
        self.Short_Description = Short_Description
        self.Names = Names
        if Intended_Effect is None:
            self.Intended_Effect = []
        else:
            self.Intended_Effect = Intended_Effect
        self.Status = Status
        self.Related_TTPs = Related_TTPs
        self.Related_Incidents = Related_Incidents
        self.Related_Indicators = Related_Indicators
        if Attribution is None:
            self.Attribution = []
        else:
            self.Attribution = Attribution
        self.Associated_Campaigns = Associated_Campaigns
        self.Confidence = Confidence
        if Activity is None:
            self.Activity = []
        else:
            self.Activity = Activity
        self.Information_Source = Information_Source
        self.Handling = Handling
        self.Related_Packages = Related_Packages
    def factory(*args_, **kwargs_):
        if CampaignType.subclass:
            return CampaignType.subclass(*args_, **kwargs_)
        else:
            return CampaignType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_Names(self): return self.Names
    def set_Names(self, Names): self.Names = Names
    def get_Intended_Effect(self): return self.Intended_Effect
    def set_Intended_Effect(self, Intended_Effect): self.Intended_Effect = Intended_Effect
    def add_Intended_Effect(self, value): self.Intended_Effect.append(value)
    def insert_Intended_Effect(self, index, value): self.Intended_Effect[index] = value
    def get_Status(self): return self.Status
    def set_Status(self, Status): self.Status = Status
    def get_Related_TTPs(self): return self.Related_TTPs
    def set_Related_TTPs(self, Related_TTPs): self.Related_TTPs = Related_TTPs
    def get_Related_Incidents(self): return self.Related_Incidents
    def set_Related_Incidents(self, Related_Incidents): self.Related_Incidents = Related_Incidents
    def get_Related_Indicators(self): return self.Related_Indicators
    def set_Related_Indicators(self, Related_Indicators): self.Related_Indicators = Related_Indicators
    def get_Attribution(self): return self.Attribution
    def set_Attribution(self, Attribution): self.Attribution = Attribution
    def add_Attribution(self, value): self.Attribution.append(value)
    def insert_Attribution(self, index, value): self.Attribution[index] = value
    def get_Associated_Campaigns(self): return self.Associated_Campaigns
    def set_Associated_Campaigns(self, Associated_Campaigns): self.Associated_Campaigns = Associated_Campaigns
    def get_Confidence(self): return self.Confidence
    def set_Confidence(self, Confidence): self.Confidence = Confidence
    def get_Activity(self): return self.Activity
    def set_Activity(self, Activity): self.Activity = Activity
    def add_Activity(self, value): self.Activity.append(value)
    def insert_Activity(self, index, value): self.Activity[index] = value
    def get_Information_Source(self): return self.Information_Source
    def set_Information_Source(self, Information_Source): self.Information_Source = Information_Source
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
            self.Names is not None or
            self.Intended_Effect or
            self.Status is not None or
            self.Related_TTPs is not None or
            self.Related_Incidents is not None or
            self.Related_Indicators is not None or
            self.Attribution or
            self.Associated_Campaigns is not None or
            self.Confidence is not None or
            self.Activity or
            self.Information_Source is not None or
            self.Handling is not None or
            self.Related_Packages is not None or
            super(CampaignType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='Campaign', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='Campaign')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='campaign:', name_='Campaign'):
        super(CampaignType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='Campaign')
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
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CampaignType', fromsubclass_=False, pretty_print=True):
        super(CampaignType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
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
        if self.Names is not None:
            self.Names.export(lwrite, level, nsmap, namespace_, name_='Names', pretty_print=pretty_print)
        for Intended_Effect_ in self.Intended_Effect:
            Intended_Effect_.export(lwrite, level, nsmap, namespace_, name_='Intended_Effect', pretty_print=pretty_print)
        if self.Status is not None:
            self.Status.export(lwrite, level, nsmap, namespace_, name_='Status', pretty_print=pretty_print)
        if self.Related_TTPs is not None:
            self.Related_TTPs.export(lwrite, level, nsmap, namespace_, name_='Related_TTPs', pretty_print=pretty_print)
        if self.Related_Incidents is not None:
            self.Related_Incidents.export(lwrite, level, nsmap, namespace_, name_='Related_Incidents', pretty_print=pretty_print)
        if self.Related_Indicators is not None:
            self.Related_Indicators.export(lwrite, level, nsmap, namespace_, name_='Related_Indicators', pretty_print=pretty_print)
        for Attribution_ in self.Attribution:
            Attribution_.export(lwrite, level, nsmap, namespace_, name_='Attribution', pretty_print=pretty_print)
        if self.Associated_Campaigns is not None:
            self.Associated_Campaigns.export(lwrite, level, nsmap, namespace_, name_='Associated_Campaigns', pretty_print=pretty_print)
        if self.Confidence is not None:
            self.Confidence.export(lwrite, level, nsmap, namespace_, name_='Confidence', pretty_print=pretty_print)
        for Activity_ in self.get_Activity():
            Activity_.export(lwrite, level, nsmap, namespace_, name_='Activity', pretty_print=pretty_print)
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
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = value
        super(CampaignType, self).buildAttributes(node, attrs, already_processed)
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
        elif nodeName_ == 'Names':
            obj_ = NamesType.factory()
            obj_.build(child_)
            self.set_Names(obj_)
        elif nodeName_ == 'Intended_Effect':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.Intended_Effect.append(obj_)
        elif nodeName_ == 'Status':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.set_Status(obj_)
        elif nodeName_ == 'Related_TTPs':
            obj_ = RelatedTTPsType.factory()
            obj_.build(child_)
            self.set_Related_TTPs(obj_)
        elif nodeName_ == 'Related_Incidents':
            obj_ = RelatedIncidentsType.factory()
            obj_.build(child_)
            self.set_Related_Incidents(obj_)
        elif nodeName_ == 'Related_Indicators':
            obj_ = RelatedIndicatorsType.factory()
            obj_.build(child_)
            self.set_Related_Indicators(obj_)
        elif nodeName_ == 'Attribution':
            obj_ = AttributionType.factory()
            obj_.build(child_)
            self.Attribution.append(obj_)
        elif nodeName_ == 'Associated_Campaigns':
            obj_ = AssociatedCampaignsType.factory()
            obj_.build(child_)
            self.set_Associated_Campaigns(obj_)
        elif nodeName_ == 'Confidence':
            obj_ = stix_common_binding.ConfidenceType.factory()
            obj_.build(child_)
            self.set_Confidence(obj_)
        elif nodeName_ == 'Activity':
            obj_ = stix_common_binding.ActivityType.factory()
            obj_.build(child_)
            self.Activity.append(obj_)
        elif nodeName_ == 'Information_Source':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Information_Source(obj_)
        elif nodeName_ == 'Handling':
            obj_ = data_marking_binding.MarkingType.factory()
            obj_.build(child_)
            self.set_Handling(obj_)
        elif nodeName_ == "Related_Packages":
            obj_ = stix_common_binding.RelatedPackageRefsType.factory()
            obj_.build(child_)
            self.set_Related_Packages(obj_)
        super(CampaignType, self).buildChildren(child_, node, nodeName_, True)
# end class CampaignType

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
        rootTag = 'Campaign'
        rootClass = CampaignType
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
        rootTag = 'Campaign'
        rootClass = CampaignType
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
        rootTag = 'Campaign'
        rootClass = CampaignType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="Campaign",
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
    "NamesType",
    "AssociatedCampaignsType",
    "RelatedIndicatorsType",
    "RelatedIncidentsType",
    "RelatedTTPsType",
    "AttributionType",
    "CampaignType"
    ]
