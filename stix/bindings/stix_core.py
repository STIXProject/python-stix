# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:06:27 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.data_marking as data_marking_binding
import cybox.bindings.cybox_core as cybox_core_binding

XML_NS = "http://stix.mitre.org/stix-1"

#
# Data representation classes.
#



class STIXType(GeneratedsSuper):
    """STIXType defines a bundle of information characterized in the
    Structured Threat Information eXpression (STIX)
    language.Specifies a globally unique identifier for this STIX
    Package. Specifies a globally unique identifier of a STIX
    Package specified elsewhere.Specifies the relevant STIX schema
    version for this content."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, timestamp=None, version=None, STIX_Header=None, Observables=None, Indicators=None, TTPs=None, Exploit_Targets=None, Incidents=None, Courses_Of_Action=None, Campaigns=None, Threat_Actors=None, Related_Packages=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.timestamp = _cast(None, timestamp)
        self.version = _cast(None, version)
        self.STIX_Header = STIX_Header
        self.Observables = Observables
        self.Indicators = Indicators
        self.TTPs = TTPs
        self.Exploit_Targets = Exploit_Targets
        self.Incidents = Incidents
        self.Courses_Of_Action = Courses_Of_Action
        self.Campaigns = Campaigns
        self.Threat_Actors = Threat_Actors
        self.Related_Packages = Related_Packages
        self.nsmap = {}
    def factory(*args_, **kwargs_):
        if STIXType.subclass:
            return STIXType.subclass(*args_, **kwargs_)
        else:
            return STIXType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_STIX_Header(self): return self.STIX_Header
    def set_STIX_Header(self, STIX_Header): self.STIX_Header = STIX_Header
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
    def get_Related_Packages(self): return self.Related_Packages
    def set_Related_Packages(self, value): self.Related_Packages = value
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def hasContent_(self):
        if (
            self.STIX_Header is not None or
            self.Observables is not None or
            self.Indicators is not None or
            self.TTPs is not None or
            self.Exploit_Targets is not None or
            self.Incidents is not None or
            self.Courses_Of_Action is not None or
            self.Campaigns is not None or
            self.Threat_Actors is not None or
            self.Related_Packages is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='STIX_Package', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, nsmap, already_processed, namespace_, name_='STIXType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, nsmap, already_processed, namespace_=XML_NS, name_='STIXType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            lwrite(' version=%s' % (quote_attrib(self.version), ))
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))

        #for ns, prefix in nsmap.iteritems():
        #    lwrite(' xmlns:%s="%s"' % (prefix, ns))

    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='STIXType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.STIX_Header is not None:
            self.STIX_Header.export(lwrite, level, nsmap, namespace_, name_='STIX_Header', pretty_print=pretty_print)
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
        if self.Related_Packages is not None:
            self.Related_Packages.export(lwrite, level, nsmap, namespace_, name_='Related_Packages', pretty_print=pretty_print)
            
    def build(self, node):
        already_processed = set()
        self.nsmap = node.nsmap
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
        value = find_attr_value_('timestamp', node)
        if value is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            try:
                self.timestamp = self.gds_parse_datetime(value, node, 'timestamp')
            except ValueError, exp:
                raise ValueError('Bad date-time attribute (timestamp): %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'STIX_Header':
            obj_ = STIXHeaderType.factory()
            obj_.build(child_)
            self.set_STIX_Header(obj_)
        elif nodeName_ == 'Observables':
            obj_ = cybox_core_binding.ObservablesType.factory()
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
            obj_ = stix_common_binding.ExploitTargetsType.factory()
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
        elif nodeName_ == 'Related_Packages':
            obj_ = RelatedPackagesType.factory()
            obj_.build(child_)
            self.set_Related_Packages(obj_)
# end class STIXType


class RelatedPackagesType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Related_Package=None):
        super(RelatedPackagesType, self).__init__(scope=scope)
        if Related_Package is None:
            self.Related_Package = []
        else:
            self.Related_Package = Related_Package
    def factory(*args_, **kwargs_):
        if RelatedPackagesType.subclass:
            return RelatedPackagesType.subclass(*args_, **kwargs_)
        else:
            return RelatedPackagesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Related_Package(self): return self.Related_Package
    def set_Related_Package(self, Related_Package): self.Related_Package = Related_Package
    def add_Related_Package(self, value): self.Related_Package.append(value)
    def insert_Related_Package(self, index, value): self.Related_Package[index] = value
    def hasContent_(self):
        if (
            self.Related_Package or
            super(RelatedPackagesType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedPackagesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedPackagesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stix:', name_='RelatedPackagesType'):
        super(RelatedPackagesType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedPackagesType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedPackagesType', fromsubclass_=False, pretty_print=True):
        super(RelatedPackagesType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Related_Package_ in self.Related_Package:
            Related_Package_.export(lwrite, level, nsmap, namespace_, name_='Related_Package', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedPackagesType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Related_Package':
            obj_ = RelatedPackageType.factory()
            obj_.build(child_)
            self.Related_Package.append(obj_)
        super(RelatedPackagesType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedPackagesType

class RelatedPackageType(stix_common_binding.GenericRelationshipType):
    """Identifies or characterizes a relationship to a Package."""
    subclass = None
    superclass = stix_common_binding.GenericRelationshipType
    def __init__(self, Confidence=None, Information_Source=None, Relationship=None, Package=None):
        super(RelatedPackageType, self).__init__(Confidence=Confidence, Information_Source=Information_Source, Relationship=Relationship)
        self.Package = Package
    def factory(*args_, **kwargs_):
        if RelatedPackageType.subclass:
            return RelatedPackageType.subclass(*args_, **kwargs_)
        else:
            return RelatedPackageType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Package(self): return self.Package
    def set_Package(self, Package): self.Package = Package
    def hasContent_(self):
        if (
            self.Package is not None or
            super(RelatedPackageType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedPackageType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedPackageType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='stix:', name_='RelatedPackageType'):
        super(RelatedPackageType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedPackageType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedPackageType', fromsubclass_=False, pretty_print=True):
        super(RelatedPackageType, self).exportChildren(lwrite, level, nsmap, stix_common_binding.XML_NS, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Package is not None:
            self.Package.export(lwrite, level, nsmap, namespace_, name_='Package', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedPackageType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Package':
            obj_ = STIXType.factory()
            obj_.build(child_)
            self.set_Package(obj_)
        super(RelatedPackageType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedPackageType


class STIXHeaderType(GeneratedsSuper):
    """The STIXHeaderType provides a structure for characterizing a package
    of STIX content."""
    subclass = None
    superclass = None
    def __init__(self, Title=None, Package_Intent=None, Description=None, Short_Description=None, Profiles=None, Handling=None, Information_Source=None):
        self.Title = Title
        if Package_Intent is None:
            self.Package_Intent = []
        else:
            self.Package_Intent = Package_Intent
        self.Description = Description
        self.Handling = Handling
        self.Short_Description = Short_Description
        self.Profiles = Profiles
        self.Information_Source = Information_Source
    def factory(*args_, **kwargs_):
        if STIXHeaderType.subclass:
            return STIXHeaderType.subclass(*args_, **kwargs_)
        else:
            return STIXHeaderType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Package_Intent(self): return self.Package_Intent
    def set_Package_Intent(self, Package_Intent): self.Package_Intent = Package_Intent
    def add_Package_Intent(self, value): self.Package_Intent.append(value)
    def insert_Package_Intent(self, index, value): self.Package_Intent[index] = value
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_Profiles(self): return self.Profiles
    def set_Profiles(self, Profiles): self.Profiles = Profiles
    def get_Handling(self): return self.Handling
    def set_Handling(self, Handling): self.Handling = Handling
    def get_Information_Source(self): return self.Information_Source
    def set_Information_Source(self, Information_Source): self.Information_Source = Information_Source
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Package_Intent or
            self.Description is not None or
            self.Short_Description is not None or
            self.Profiles is not None or
            self.Handling is not None or
            self.Information_Source is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='STIXHeaderType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='STIXHeaderType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_=XML_NS, name_='STIXHeaderType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='STIXHeaderType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_], quote_xml(self.Title), nsmap[namespace_], eol_))
        for Package_Intent_ in self.Package_Intent:
            Package_Intent_.export(lwrite, level, nsmap, namespace_, name_='Package_Intent', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Short_Description is not None:
            self.Short_Description.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
        if self.Profiles is not None:
            self.Profiles.export(lwrite, level, nsmap, namespace_, name_='Profiles', pretty_print=pretty_print)
        if self.Handling is not None:
            self.Handling.export(lwrite, level, nsmap, namespace_, name_='Handling', pretty_print=pretty_print)
        if self.Information_Source is not None:
            self.Information_Source.export(lwrite, level, nsmap, namespace_, name_='Information_Source', pretty_print=pretty_print)
    def build(self, node):
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
        elif nodeName_ == 'Package_Intent':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Package_Intent.append(obj_)
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Short_Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Short_Description(obj_)
        elif nodeName_ == 'Profiles':
            obj_ = stix_common_binding.ProfilesType.factory()
            obj_.build(child_)
            self.set_Profiles(obj_)
        elif nodeName_ == 'Handling':
            obj_ = data_marking_binding.MarkingType.factory()
            obj_.build(child_)
            self.set_Handling(obj_)
        elif nodeName_ == 'Information_Source':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Information_Source(obj_)
# end class STIXHeaderType

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
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
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
                obj_ = stix_common_binding.IndicatorBaseType.factory() # not abstract

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
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
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
                obj_ = stix_common_binding.TTPBaseType.factory() # not abstract

            obj_.build(child_)
            self.TTP.append(obj_)
        elif nodeName_ == 'Kill_Chains':
            obj_ = stix_common_binding.KillChainsType.factory()
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
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
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
                obj_ = stix_common_binding.IncidentBaseType.factory() # not abstract

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
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
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
                obj_ = stix_common_binding.CourseOfActionBaseType.factory() # not abstract

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
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
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
                obj_ = stix_common_binding.CampaignBaseType.factory() # not abstract

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
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
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
                obj_ = stix_common_binding.ThreatActorBaseType.factory() # not abstract

            obj_.build(child_)
            self.Threat_Actor.append(obj_)
# end class ThreatActorsType


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

def parse(inFileName, nsmap=None):
    if not nsmap:
        from stix.utils.nsparser import DEFAULT_STIX_NS_TO_PREFIX
        nsmap = DEFAULT_STIX_NS_TO_PREFIX

    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'STIX_Package'
        rootClass = STIXType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, nsmap, name_=rootTag,
    #     namespacedef_='',
    #     pretty_print=True)
    return rootObj

def parseEtree(inFileName):
    doc = parsexml_(inFileName)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'STIX_Package'
        rootClass = STIXType
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
        rootTag = 'STIX_Package'
        rootClass = STIXType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="STIX_Package",
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
    "STIXType",
    "STIXHeaderType",
    "IndicatorsType",
    "TTPsType",
    "IncidentsType",
    "CoursesOfActionType",
    "CampaignsType",
    "ThreatActorsType"
    ]
