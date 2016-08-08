# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Mon Apr 27 08:13:59 2015 by generateDS.py version 2.9a.
#

from cybox.bindings import cybox_core
from mixbox.binding_utils import *

from stix.bindings import lookup_extension, register_extension
import stix.bindings.stix_common as common_binding
import stix.bindings.data_marking as data_marking_binding

XML_NS = "http://stix.mitre.org/Report-1"

#
# Data representation classes.
#

class HeaderType(GeneratedsSuper):
    """The HeaderType provides a structure for characterizing the
    contextual information in a Report of STIX content."""
    subclass = None
    superclass = None
    def __init__(self, Title=None, Intent=None, Description=None, Short_Description=None, Handling=None, Information_Source=None):
        self.Title = Title
        if Intent is None:
            self.Intent = []
        else:
            self.Intent = Intent
        if Description is None:
            self.Description = []
        else:
            self.Description = Description
        if Short_Description is None:
            self.Short_Description = []
        else:
            self.Short_Description = Short_Description
        self.Handling = Handling
        self.Information_Source = Information_Source
    def factory(*args_, **kwargs_):
        if HeaderType.subclass:
            return HeaderType.subclass(*args_, **kwargs_)
        else:
            return HeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Intent(self): return self.Intent
    def set_Intent(self, Intent): self.Intent = Intent
    def add_Intent(self, value): self.Intent.append(value)
    def insert_Intent(self, index, value): self.Intent[index] = value
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def add_Description(self, value): self.Description.append(value)
    def insert_Description(self, index, value): self.Description[index] = value
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def add_Short_Description(self, value): self.Short_Description.append(value)
    def insert_Short_Description(self, index, value): self.Short_Description[index] = value
    def get_Handling(self): return self.Handling
    def set_Handling(self, Handling): self.Handling = Handling
    def get_Information_Source(self): return self.Information_Source
    def set_Information_Source(self, Information_Source): self.Information_Source = Information_Source
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Intent or
            self.Description or
            self.Short_Description or
            self.Handling is not None or
            self.Information_Source is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='HeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='HeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='report:', name_='HeaderType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='HeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_], quote_xml(self.Title), nsmap[namespace_], eol_))
        for Intent_ in self.Intent:
            Intent_.export(lwrite, level, nsmap, namespace_, name_='Intent', pretty_print=pretty_print)
        for Description_ in self.Description:
            Description_.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        for Short_Description_ in self.Short_Description:
            Short_Description_.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
        if self.Handling is not None:
            self.Handling.export(lwrite, level, nsmap, namespace_, name_='Handling', pretty_print=pretty_print)
        if self.Information_Source is not None:
            self.Information_Source.export(lwrite, level, nsmap, namespace_, name_='Information_Source', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Title':
            Title_ = child_.text
            Title_ = self.gds_validate_string(Title_, node, 'Title')
            self.Title = Title_
        elif nodeName_ == 'Intent':
            obj_ = common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Intent.append(obj_)
        elif nodeName_ == 'Description':
            obj_ = common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.Description.append(obj_)
        elif nodeName_ == 'Short_Description':
            obj_ = common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.Short_Description.append(obj_)
        elif nodeName_ == 'Handling':
            obj_ = data_marking_binding.MarkingType.factory()
            obj_.build(child_)
            self.set_Handling(obj_)
        elif nodeName_ == 'Information_Source':
            obj_ = common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Information_Source(obj_)
# end class HeaderType


class IndicatorsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Indicator=None):
        if Indicator is None:
            self.Indicator = []
        else:
            self.Indicator = Indicator
    def factory(*args_, **kwargs_):
        if IndicatorsType.subclass:
            return IndicatorsType.subclass(*args_, **kwargs_)
        else:
            return IndicatorsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Indicator(self): return self.Indicator
    def set_Indicator(self, Indicator): self.Indicator = Indicator
    def add_Indicator(self, value): self.Indicator.append(value)
    def insert_Indicator(self, index, value): self.Indicator[index] = value
    def hasContent_(self):
        if (
            self.Indicator
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IndicatorsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IndicatorsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_=XML_NS, name_='IndicatorsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IndicatorsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Indicator_ in self.Indicator:
            Indicator_.export(lwrite, level, nsmap, namespace_, name_='Indicator', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Indicator':
            obj_ = lookup_extension(child_, common_binding.IndicatorBaseType).factory()
            obj_.build(child_)
            self.Indicator.append(obj_)
# end class IndicatorsType


class TTPsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, TTP=None, Kill_Chains=None):
        if TTP is None:
            self.TTP = []
        else:
            self.TTP = TTP
        self.Kill_Chains = Kill_Chains
    def factory(*args_, **kwargs_):
        if TTPsType.subclass:
            return TTPsType.subclass(*args_, **kwargs_)
        else:
            return TTPsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_TTP(self): return self.TTP
    def set_TTP(self, TTP): self.TTP = TTP
    def add_TTP(self, value): self.TTP.append(value)
    def insert_TTP(self, index, value): self.TTP[index] = value
    def get_Kill_Chains(self): return self.Kill_Chains
    def set_Kill_Chains(self, Kill_Chains): self.Kill_Chains = Kill_Chains
    def hasContent_(self):
        if (
            self.TTP or
            self.Kill_Chains is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TTPsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TTPsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_=XML_NS, name_='TTPsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TTPsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for TTP_ in self.TTP:
            TTP_.export(lwrite, level, nsmap, namespace_, name_='TTP', pretty_print=pretty_print)
        if self.Kill_Chains is not None:
            self.Kill_Chains.export(lwrite, level, nsmap, namespace_, name_='Kill_Chains', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'TTP':
            from . import ttp
            obj_ = lookup_extension(child_, common_binding.TTPBaseType).factory()
            obj_.build(child_)
            self.TTP.append(obj_)
        elif nodeName_ == 'Kill_Chains':
            obj_ = common_binding.KillChainsType.factory()
            obj_.build(child_)
            self.set_Kill_Chains(obj_)
# end class TTPsType

class IncidentsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Incident=None):
        if Incident is None:
            self.Incident = []
        else:
            self.Incident = Incident
    def factory(*args_, **kwargs_):
        if IncidentsType.subclass:
            return IncidentsType.subclass(*args_, **kwargs_)
        else:
            return IncidentsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Incident(self): return self.Incident
    def set_Incident(self, Incident): self.Incident = Incident
    def add_Incident(self, value): self.Incident.append(value)
    def insert_Incident(self, index, value): self.Incident[index] = value
    def hasContent_(self):
        if (
            self.Incident
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IncidentsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IncidentsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_=XML_NS, name_='IncidentsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IncidentsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Incident_ in self.Incident:
            Incident_.export(lwrite, level, nsmap, namespace_, name_='Incident', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Incident':
            from . import incident
            obj_ = lookup_extension(child_, common_binding.IncidentBaseType).factory()
            obj_.build(child_)
            self.Incident.append(obj_)
# end class IncidentsType

class CoursesOfActionType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Course_Of_Action=None):
        if Course_Of_Action is None:
            self.Course_Of_Action = []
        else:
            self.Course_Of_Action = Course_Of_Action
    def factory(*args_, **kwargs_):
        if CoursesOfActionType.subclass:
            return CoursesOfActionType.subclass(*args_, **kwargs_)
        else:
            return CoursesOfActionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Course_Of_Action(self): return self.Course_Of_Action
    def set_Course_Of_Action(self, Course_Of_Action): self.Course_Of_Action = Course_Of_Action
    def add_Course_Of_Action(self, value): self.Course_Of_Action.append(value)
    def insert_Course_Of_Action(self, index, value): self.Course_Of_Action[index] = value
    def hasContent_(self):
        if (
            self.Course_Of_Action
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CoursesOfActionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CoursesOfActionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_=XML_NS, name_='CoursesOfActionType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CoursesOfActionType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Course_Of_Action_ in self.Course_Of_Action:
            Course_Of_Action_.export(lwrite, level, nsmap, namespace_, name_='Course_Of_Action', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Course_Of_Action':
            from . import course_of_action
            obj_ = lookup_extension(child_, common_binding.CourseOfActionBaseType).factory()
            obj_.build(child_)
            self.Course_Of_Action.append(obj_)
# end class CoursesOfActionType

class CampaignsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Campaign=None):
        if Campaign is None:
            self.Campaign = []
        else:
            self.Campaign = Campaign
    def factory(*args_, **kwargs_):
        if CampaignsType.subclass:
            return CampaignsType.subclass(*args_, **kwargs_)
        else:
            return CampaignsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Campaign(self): return self.Campaign
    def set_Campaign(self, Campaign): self.Campaign = Campaign
    def add_Campaign(self, value): self.Campaign.append(value)
    def insert_Campaign(self, index, value): self.Campaign[index] = value
    def hasContent_(self):
        if (
            self.Campaign
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CampaignsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CampaignsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_=XML_NS, name_='CampaignsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CampaignsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Campaign_ in self.Campaign:
            Campaign_.export(lwrite, level, nsmap, namespace_, name_='Campaign', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Campaign':
            from . import campaign
            obj_ = lookup_extension(child_, common_binding.CampaignBaseType).factory()
            obj_.build(child_)
            self.Campaign.append(obj_)
# end class CampaignsType

class ThreatActorsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Threat_Actor=None):
        if Threat_Actor is None:
            self.Threat_Actor = []
        else:
            self.Threat_Actor = Threat_Actor
    def factory(*args_, **kwargs_):
        if ThreatActorsType.subclass:
            return ThreatActorsType.subclass(*args_, **kwargs_)
        else:
            return ThreatActorsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Threat_Actor(self): return self.Threat_Actor
    def set_Threat_Actor(self, Threat_Actor): self.Threat_Actor = Threat_Actor
    def add_Threat_Actor(self, value): self.Threat_Actor.append(value)
    def insert_Threat_Actor(self, index, value): self.Threat_Actor[index] = value
    def hasContent_(self):
        if (
            self.Threat_Actor
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ThreatActorsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ThreatActorsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_=XML_NS, name_='ThreatActorsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ThreatActorsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Threat_Actor_ in self.Threat_Actor:
            Threat_Actor_.export(lwrite, level, nsmap, namespace_, name_='Threat_Actor', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Threat_Actor':
            from . import threat_actor
            obj_ = lookup_extension(child_, common_binding.ThreatActorBaseType).factory()
            obj_.build(child_)
            self.Threat_Actor.append(obj_)
# end class ThreatActorsType


@register_extension
class ReportType(common_binding.ReportBaseType):
    """ReportType defines a contextual wrapper for a grouping of STIX
    content.Specifies the relevant Report schema version for this
    content."""
    subclass = None
    superclass = common_binding.ReportBaseType

    xmlns          = XML_NS
    xmlns_prefix   = "report"
    xml_type       = "ReportType"
    xsi_type       = "%s:%s" % (xmlns_prefix, xml_type)

    def __init__(self, timestamp=None, idref=None, id=None, version=None, Header=None, Observables=None, Indicators=None, TTPs=None, Exploit_Targets=None, Incidents=None, Courses_Of_Action=None, Campaigns=None, Threat_Actors=None, Related_Reports=None):
        super(ReportType, self).__init__(timestamp, idref, id, )
        self.version = _cast(None, version)
        self.Header = Header
        self.Observables = Observables
        self.Indicators = Indicators
        self.TTPs = TTPs
        self.Exploit_Targets = Exploit_Targets
        self.Incidents = Incidents
        self.Courses_Of_Action = Courses_Of_Action
        self.Campaigns = Campaigns
        self.Threat_Actors = Threat_Actors
        self.Related_Reports = Related_Reports
    def factory(*args_, **kwargs_):
        if ReportType.subclass:
            return ReportType.subclass(*args_, **kwargs_)
        else:
            return ReportType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Header(self): return self.Header
    def set_Header(self, Header): self.Header = Header
    def get_Observables(self): return self.Observables
    def set_Observables(self, Observables): self.Observables = Observables
    def get_Indicators(self): return self.Indicators
    def set_Indicators(self, Indicators): self.Indicators = Indicators
    def get_TTPs(self): return self.TTPs
    def set_TTPs(self, TTPs): self.TTPs = TTPs
    def get_Exploit_Targets(self): return self.Exploit_Targets
    def set_Exploit_Targets(self, Exploit_Targets): self.Exploit_Targets = Exploit_Targets
    def get_Incidents(self): return self.Incidents
    def set_Incidents(self, Incidents): self.Incidents = Incidents
    def get_Courses_Of_Action(self): return self.Courses_Of_Action
    def set_Courses_Of_Action(self, Courses_Of_Action): self.Courses_Of_Action = Courses_Of_Action
    def get_Campaigns(self): return self.Campaigns
    def set_Campaigns(self, Campaigns): self.Campaigns = Campaigns
    def get_Threat_Actors(self): return self.Threat_Actors
    def set_Threat_Actors(self, Threat_Actors): self.Threat_Actors = Threat_Actors
    def get_Related_Reports(self): return self.Related_Reports
    def set_Related_Reports(self, Related_Reports): self.Related_Reports = Related_Reports
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def hasContent_(self):
        if (
            self.Header is not None or
            self.Observables is not None or
            self.Indicators is not None or
            self.TTPs is not None or
            self.Exploit_Targets is not None or
            self.Incidents is not None or
            self.Courses_Of_Action is not None or
            self.Campaigns is not None or
            self.Threat_Actors is not None or
            self.Related_Reports is not None or
            super(ReportType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ReportType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ReportType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='report:', name_='ReportType'):
        super(ReportType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='ReportType')
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
            lwrite(xsi_type)
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            lwrite(' version=%s' % (quote_attrib(self.version), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ReportType', fromsubclass_=False, pretty_print=True):
        super(ReportType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Header is not None:
            self.Header.export(lwrite, level, nsmap, namespace_, name_='Header', pretty_print=pretty_print)
        if self.Observables is not None:
            self.Observables.export(lwrite, level, "%s:" % (nsmap[namespace_]), name_='Observables', pretty_print=pretty_print) # no nsmap parameter, so we use this hack to pass the right namespace prefix
        if self.Indicators is not None:
            self.Indicators.export(lwrite, level, nsmap, namespace_, name_='Indicators', pretty_print=pretty_print)
        if self.TTPs is not None:
            self.TTPs.export(lwrite, level, nsmap, namespace_, name_='TTPs', pretty_print=pretty_print)
        if self.Exploit_Targets is not None:
            self.Exploit_Targets.export(lwrite, level, nsmap, namespace_, name_='Exploit_Targets', pretty_print=pretty_print)
        if self.Incidents is not None:
            self.Incidents.export(lwrite, level, nsmap, namespace_, name_='Incidents', pretty_print=pretty_print)
        if self.Courses_Of_Action is not None:
            self.Courses_Of_Action.export(lwrite, level, nsmap, namespace_, name_='Courses_Of_Action', pretty_print=pretty_print)
        if self.Campaigns is not None:
            self.Campaigns.export(lwrite, level, nsmap, namespace_, name_='Campaigns', pretty_print=pretty_print)
        if self.Threat_Actors is not None:
            self.Threat_Actors.export(lwrite, level, nsmap, namespace_, name_='Threat_Actors', pretty_print=pretty_print)
        if self.Related_Reports is not None:
            self.Related_Reports.export(lwrite, level, nsmap, namespace_, name_='Related_Reports', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
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
        super(ReportType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Header':
            obj_ = HeaderType.factory()
            obj_.build(child_)
            self.set_Header(obj_)
        elif nodeName_ == 'Observables':
            obj_ = cybox_core.ObservablesType.factory()
            obj_.build(child_)
            self.set_Observables(obj_)
        elif nodeName_ == 'Indicators':
            obj_ = IndicatorsType.factory()
            obj_.build(child_)
            self.set_Indicators(obj_)
        elif nodeName_ == 'TTPs':
            obj_ = TTPsType.factory()
            obj_.build(child_)
            self.set_TTPs(obj_)
        elif nodeName_ == 'Exploit_Targets':
            obj_ = common_binding.ExploitTargetsType.factory()
            obj_.build(child_)
            self.set_Exploit_Targets(obj_)
        elif nodeName_ == 'Incidents':
            obj_ = IncidentsType.factory()
            obj_.build(child_)
            self.set_Incidents(obj_)
        elif nodeName_ == 'Courses_Of_Action':
            obj_ = CoursesOfActionType.factory()
            obj_.build(child_)
            self.set_Courses_Of_Action(obj_)
        elif nodeName_ == 'Campaigns':
            obj_ = CampaignsType.factory()
            obj_.build(child_)
            self.set_Campaigns(obj_)
        elif nodeName_ == 'Threat_Actors':
            obj_ = ThreatActorsType.factory()
            obj_.build(child_)
            self.set_Threat_Actors(obj_)
        elif nodeName_ == 'Related_Reports':
            obj_ = RelatedReportsType.factory()
            obj_.build(child_)
            self.set_Related_Reports(obj_)
        super(ReportType, self).buildChildren(child_, node, nodeName_, True)
# end class ReportType


class RelatedReportsType(common_binding.GenericRelationshipListType):
    subclass = None
    superclass = common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Related_Report=None):
        super(RelatedReportsType, self).__init__(scope, )
        if Related_Report is None:
            self.Related_Report = []
        else:
            self.Related_Report = Related_Report
    def factory(*args_, **kwargs_):
        if RelatedReportsType.subclass:
            return RelatedReportsType.subclass(*args_, **kwargs_)
        else:
            return RelatedReportsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Related_Report(self): return self.Related_Report
    def set_Related_Report(self, Related_Report): self.Related_Report = Related_Report
    def add_Related_Report(self, value): self.Related_Report.append(value)
    def insert_Related_Report(self, index, value): self.Related_Report[index] = value
    def hasContent_(self):
        if (
            self.Related_Report or
            super(RelatedReportsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedReportsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedReportsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='report:', name_='RelatedReportsType'):
        super(RelatedReportsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedReportsType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedReportsType', fromsubclass_=False, pretty_print=True):
        super(RelatedReportsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Related_Report_ in self.Related_Report:
            Related_Report_.export(lwrite, level, nsmap, namespace_, name_='Related_Report', pretty_print=pretty_print)
    def build(self, node):
        self.__sourcenode__ = node
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedReportsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Related_Report':
            obj_ = common_binding.RelatedReportType.factory()
            obj_.build(child_)
            self.Related_Report.append(obj_)
        super(RelatedReportsType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedReportsType


GDSClassesMapping = {}


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = GDSClassesMapping.get(tag)
    if rootClass is None:
        rootClass = globals().get(tag)
    return tag, rootClass

#
# def parse(inFileName):
#     doc = parsexml_(inFileName)
#     rootNode = doc.getroot()
#     rootTag, rootClass = get_root_tag(rootNode)
#     if rootClass is None:
#         rootTag = 'Report'
#         rootClass = ReportType
#     rootObj = rootClass.factory()
#     rootObj.build(rootNode)
#     # Enable Python to collect the space used by the DOM.
#     # doc = None
#     # sys.stdout.write('<?xml version="1.0" ?>\n')
#     # rootObj.export(sys.stdout, 0, name_=rootTag,
#     #     namespacedef_='',
#     #     pretty_print=True)
#     return rootObj


def parseString(inString):
    from mixbox.vendor.six import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'Report'
        rootClass = ReportType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # # Enable Python to collect the space used by the DOM.
    # doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="Report",
    #     namespacedef_='')
    return rootObj
