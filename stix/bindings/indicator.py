# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated Thu Apr 11 15:06:25 2013 by generateDS.py version 2.9a.
#

import sys
from stix.bindings import *
import cybox.bindings.cybox_core as cybox_core_binding
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.data_marking as data_marking_binding

XML_NS  = "http://stix.mitre.org/Indicator-2"

#
# Data representation classes.
#

class ValidTimeType(GeneratedsSuper):
    """A basic representation of a temporal window when the thing (e.g.,
    indicator) is valid."""
    subclass = None
    superclass = None
    def __init__(self, Start_Time=None, End_Time=None):
        self.Start_Time = Start_Time
        self.End_Time = End_Time
    def factory(*args_, **kwargs_):
        if ValidTimeType.subclass:
            return ValidTimeType.subclass(*args_, **kwargs_)
        else:
            return ValidTimeType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Start_Time(self): return self.Start_Time
    def set_Start_Time(self, Start_Time): self.Start_Time = Start_Time
    def get_End_Time(self): return self.End_Time
    def set_End_Time(self, End_Time): self.End_Time = End_Time
    def hasContent_(self):
        if (
            self.Start_Time is not None or
            self.End_Time is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ValidTimeType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='ValidTimeType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='indicator:', name_='ValidTimeType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='ValidTimeType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Start_Time is not None:
            self.Start_Time.export(lwrite, level, nsmap, namespace_, name_='Start_Time', pretty_print=pretty_print)
        if self.End_Time is not None:
            self.End_Time.export(lwrite, level, nsmap, namespace_, name_='End_Time', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Start_Time':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_Start_Time(obj_)
        elif nodeName_ == 'End_Time':
            obj_ = stix_common_binding.DateTimeWithPrecisionType.factory()
            obj_.build(child_)
            self.set_End_Time(obj_)
# end class ValidTimeType


class CompositeIndicatorExpressionType(GeneratedsSuper):
    """Type for allowing content creators to create composite indicator
    expressions using basic boolean logic. Specifies the logical
    composition operator for this composite cyber threat Indicator."""
    subclass = None
    superclass = None
    def __init__(self, operator=None, Indicator=None):
        self.operator = _cast(None, operator)
        if Indicator is None:
            self.Indicator = []
        else:
            self.Indicator = Indicator
    def factory(*args_, **kwargs_):
        if CompositeIndicatorExpressionType.subclass:
            return CompositeIndicatorExpressionType.subclass(*args_, **kwargs_)
        else:
            return CompositeIndicatorExpressionType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Indicator(self): return self.Indicator
    def set_Indicator(self, Indicator): self.Indicator = Indicator
    def add_Indicator(self, value): self.Indicator.append(value)
    def insert_Indicator(self, index, value): self.Indicator[index] = value
    def get_operator(self): return self.operator
    def set_operator(self, operator): self.operator = operator
    def hasContent_(self):
        if (
            self.Indicator
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CompositeIndicatorExpressionType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='CompositeIndicatorExpressionType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_=XML_NS, name_='CompositeIndicatorExpressionType'):
        if self.operator is not None and 'operator' not in already_processed:
            already_processed.add('operator')
            lwrite(' operator=%s' % (quote_attrib(self.operator), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='CompositeIndicatorExpressionType', fromsubclass_=False, pretty_print=True):
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
        value = find_attr_value_('operator', node)
        if value is not None and 'operator' not in already_processed:
            already_processed.add('operator')
            self.operator = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Indicator':
            obj_ = IndicatorType.factory()
            obj_.build(child_)
            self.Indicator.append(obj_)
# end class CompositeIndicatorExpressionType

class TestMechanismType(GeneratedsSuper):
    """The TestMechanismType specifies a non-standard Test Mechanism
    effective at identifying the cyber Observables specified in this
    cyber threat Indicator. This type is defined as abstract and is
    intended to be extended to enable the expression of any
    structured or unstructured test mechanism. STIX provides five
    default options, Generic, OpenIOC, OVAL, Snort, and YARA.
    Additionally, those who wish to use another format may do so by
    using either the existing Generic test mechanism and putting the
    mechanism specification in the CDATA block or by defining a new
    extension to this type. The information for the STIX-provided
    extensions is: 1. Generic: The Generic test mechanism allows for
    the specification of any generic test mechanism through the use
    of a raw CDATA section. The type is named
    GenericTestMechanismType and is in the
    http://stix.mitre.org/extensions/TestMechanism#Generic-1
    namespace. The extension is defined in the file
    extensions/test_mechanism/generic.xsd or at the URL http://stix.
    mitre.org/XMLSchema/extensions/test_mechanism/generic/1.0/generi
    c.xsd. 2. OpenIOC: The OpenIOC test mechanism allows for the
    specification of an OpenIOC test by importing the OpenIOC
    schema. The type is named IOCTestMechanismType and is in the
    http://stix.mitre.org/extensions/TestMechanism#OpenIOC-1
    namespace. The extension is defined in the file
    extensions/test_mechanism/openioc-1.0.xsd or at the URL http://s
    tix.mitre.org/XMLSchema/extensions/test_mechanism/openioc-1.0/1.
    0/openioc-1.0.xsd. 3. OVAL: The OVAL test mechanism allows for
    the specification of an OVAL definition through importing the
    OVAL schemas. The type is named OVALTestMechanismType and is in
    the http://stix.mitre.org/extensions/TestMechanism#OVAL-1
    namespace. The extension is defined in the file
    extensions/test_mechanism/oval-5.10.1.xsd or at the URL http://s
    tix.mitre.org/XMLSchema/extensions/test_mechanism/oval-5.10.1/1.
    0/oval-5.10.1.xsd. 4. Snort: The Snort test mechanism allows for
    the specification of a snort signature through the use of a raw
    CDATA section. The type is named SnortTestMechanismType and is
    in the http://stix.mitre.org/extensions/TestMechanism#Snort-1
    namespace. The extension is defined in the file
    extensions/test_mechanism/snort.xsd or at the URL http://stix.mi
    tre.org/XMLSchema/extensions/test_mechanism/snort/1.0/snort.xsd.
    5. YARA: The YARA test mechanism allows for the specification of
    a YARA test through the use of a raw CDATA section. The type is
    named YaraTestMechanismType and is in the
    http://stix.mitre.org/extensions/TestMechanism#YARA-1 namespace.
    The extension is defined in the file
    extensions/test_mechanism/yara.xsd or at the URL http://stix.mit
    re.org/XMLSchema/extensions/test_mechanism/yara/1.0/yara.xsd.
    Specifies a unique ID for this Test Mechanism.Specifies a
    reference to the ID of a Test Mechanism specified elsewhere."""
    subclass = None
    superclass = None
    def __init__(self, idref=None, id=None, Efficacy=None, Producer=None, xsi_type=None):
        self.idref = _cast(None, idref)
        self.id = _cast(None, id)
        self.Efficacy = Efficacy
        self.Producer = Producer
        self.xsi_type = xsi_type
    def factory(*args_, **kwargs_):
        if TestMechanismType.subclass:
            return TestMechanismType.subclass(*args_, **kwargs_)
        else:
            return TestMechanismType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Efficacy(self): return self.Efficacy
    def set_Efficacy(self, Efficacy): self.Efficacy = Efficacy
    def get_Producer(self): return self.Producer
    def set_Producer(self, Producer): self.Producer = Producer
    def get_idref(self): return self.idref
    def set_idref(self, idref): self.idref = idref
    def get_id(self): return self.id
    def set_id(self, id): self.id = id
    def get_xsi_type(self): return self.xsi_type
    def set_xsi_type(self, xsi_type): self.xsi_type = xsi_type
    def hasContent_(self):
        if (
            self.Efficacy is not None and
            self.Producer is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TestMechanismType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TestMechanismType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='indicator:', name_='TestMechanismType'):
        if self.idref is not None and 'idref' not in already_processed:
            already_processed.add('idref')
            lwrite(' idref=%s' % (quote_attrib(self.idref), ))
        if self.id is not None and 'id' not in already_processed:
            already_processed.add('id')
            lwrite(' id=%s' % (quote_attrib(self.id), ))
        if self.xsi_type is not None and 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            lwrite('  xsi:type="%s"' % self.xsi_type)

    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TestMechanismType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Efficacy is not None:
            self.Efficacy.export(lwrite, level, nsmap, namespace_, name_='Efficacy', pretty_print=pretty_print)
        if self.Producer is not None:
            self.Producer.export(lwrite, level, nsmap, namespace_, name_='Producer', pretty_print=pretty_print)
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
        #=======================================================================
        # value = find_attr_value_('xsi:type', node)
        # if value is not None and 'xsi:type' not in already_processed:
        #    already_processed.add('xsi:type')
        #    self.xsi_type = value
        #=======================================================================
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Efficacy':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.set_Efficacy(obj_)
        elif nodeName_ == 'Producer':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Producer(obj_)
# end class TestMechanismType

class SightingsType(GeneratedsSuper):
    """The total number of times this Indicator was reported as sighted."""
    subclass = None
    superclass = None
    def __init__(self, sightings_count=None, Sighting=None):
        self.sightings_count = _cast(int, sightings_count)
        if Sighting is None:
            self.Sighting = []
        else:
            self.Sighting = Sighting
    def factory(*args_, **kwargs_):
        if SightingsType.subclass:
            return SightingsType.subclass(*args_, **kwargs_)
        else:
            return SightingsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Sighting(self): return self.Sighting
    def set_Sighting(self, Sighting): self.Sighting = Sighting
    def add_Sighting(self, value): self.Sighting.append(value)
    def insert_Sighting(self, index, value): self.Sighting[index] = value
    def get_sightings_count(self): return self.sightings_count
    def set_sightings_count(self, sightings_count): self.sightings_count = sightings_count
    def hasContent_(self):
        if (
            self.Sighting
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='SightingsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SightingsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='indicator:', name_='SightingsType'):
        if self.sightings_count is not None and 'sightings_count' not in already_processed:
            already_processed.add('sightings_count')
            lwrite(' sightings_count="%s"' % self.gds_format_integer(self.sightings_count, input_name='sightings_count'))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='SightingsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Sighting_ in self.Sighting:
            Sighting_.export(lwrite, level, nsmap, namespace_, name_='Sighting', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('sightings_count', node)
        if value is not None and 'sightings_count' not in already_processed:
            already_processed.add('sightings_count')
            try:
                self.sightings_count = int(value)
            except ValueError, exp:
                raise_parse_error(node, 'Bad integer attribute: %s' % exp)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Sighting':
            obj_ = SightingType.factory()
            obj_.build(child_)
            self.Sighting.append(obj_)
# end class SightingsType

class SightingType(GeneratedsSuper):
    """Describes a single sighting of an indicator.This field provides the
    date and time of the Indicator sighting.In order to avoid
    ambiguity, it is strongly suggest that all timestamps include a
    specification of the timezone if it is known.Represents the
    precision of the associated timestamp value. If omitted, the
    default is "second", meaning the timestamp is precise to the
    full field value. Digits in the timestamp that are required by
    the xs:dateTime datatype but are beyond the specified precision
    should be zeroed out."""
    subclass = None
    superclass = None
    def __init__(self, timestamp=None, timestamp_precision='second', Source=None, Reference=None, Confidence=None, Description=None, Related_Observables=None):
        self.timestamp = _cast(None, timestamp)
        self.timestamp_precision = _cast(None, timestamp_precision)
        self.Source = Source
        self.Reference = Reference
        self.Confidence = Confidence
        self.Description = Description
        self.Related_Observables = Related_Observables
    def factory(*args_, **kwargs_):
        if SightingType.subclass:
            return SightingType.subclass(*args_, **kwargs_)
        else:
            return SightingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Source(self): return self.Source
    def set_Source(self, Source): self.Source = Source
    def get_Reference(self): return self.Reference
    def set_Reference(self, Reference): self.Reference = Reference
    def get_Confidence(self): return self.Confidence
    def set_Confidence(self, Confidence): self.Confidence = Confidence
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Related_Observables(self): return self.Related_Observables
    def set_Related_Observables(self, Related_Observables): self.Related_Observables = Related_Observables
    def get_timestamp(self): return self.timestamp
    def set_timestamp(self, timestamp): self.timestamp = timestamp
    def get_timestamp_precision(self): return self.timestamp_precision
    def set_timestamp_precision(self, timestamp_precision): self.timestamp_precision = timestamp_precision
    def hasContent_(self):
        if (
            self.Source is not None or
            self.Reference is not None or
            self.Confidence is not None or
            self.Description is not None or
            self.Related_Observables is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='SightingType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SightingType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='indicator:', name_='SightingType'):
        if self.timestamp is not None and 'timestamp' not in already_processed:
            already_processed.add('timestamp')
            lwrite(' timestamp="%s"' % self.gds_format_datetime(self.timestamp, input_name='timestamp'))
        if self.timestamp_precision is not None and 'timestamp_precision' not in already_processed:
            already_processed.add('timestamp_precision')
            lwrite(' timestamp_precision=%s' % (quote_attrib(self.timestamp_precision), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='SightingType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Source is not None:
            self.Source.export(lwrite, level, nsmap, namespace_, name_='Source', pretty_print=pretty_print)
        if self.Reference is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Reference>%s</%s:Reference>%s' % (nsmap[namespace_], quote_xml(self.Reference), nsmap[namespace_], eol_))
        if self.Confidence is not None:
            self.Confidence.export(lwrite, level, nsmap, namespace_, name_='Confidence', pretty_print=pretty_print)
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Related_Observables is not None:
            self.Related_Observables.export(lwrite, level, nsmap, namespace_, name_='Related_Observables', pretty_print=pretty_print)
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
        if nodeName_ == 'Source':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Source(obj_)
        elif nodeName_ == 'Reference':
            Reference_ = child_.text
            Reference_ = self.gds_validate_string(Reference_, node, 'Reference')
            self.Reference = Reference_
        elif nodeName_ == 'Confidence':
            obj_ = stix_common_binding.ConfidenceType.factory()
            obj_.build(child_)
            self.set_Confidence(obj_)
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Related_Observables':
            obj_ = RelatedObservablesType.factory()
            obj_.build(child_)
            self.set_Related_Observables(obj_)
# end class SightingType



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
    def exportAttributes(self, lwrite, level, already_processed, namespace_='indicator:', name_='RelatedObservablesType'):
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

class TestMechanismsType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, Test_Mechanism=None):
        if Test_Mechanism is None:
            self.Test_Mechanism = []
        else:
            self.Test_Mechanism = Test_Mechanism
    def factory(*args_, **kwargs_):
        if TestMechanismsType.subclass:
            return TestMechanismsType.subclass(*args_, **kwargs_)
        else:
            return TestMechanismsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Test_Mechanism(self): return self.Test_Mechanism
    def set_Test_Mechanism(self, Test_Mechanism): self.Test_Mechanism = Test_Mechanism
    def add_Test_Mechanism(self, value): self.Test_Mechanism.append(value)
    def insert_Test_Mechanism(self, index, value): self.Test_Mechanism[index] = value
    def hasContent_(self):
        if (
            self.Test_Mechanism
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TestMechanismsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TestMechanismsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='indicator:', name_='TestMechanismsType'):
        pass
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TestMechanismsType', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Test_Mechanism_ in self.get_Test_Mechanism():
            Test_Mechanism_.export(lwrite, level, nsmap, namespace_, name_='Test_Mechanism', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        pass
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Test_Mechanism':
            type_name_ = child_.attrib.get('{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                    
                if type_name_ == "OVAL5.10TestMechanismType":
                    import stix.bindings.extensions.test_mechanism.oval_5_10 as oval_5_10_tm_binding
                    obj_ = oval_5_10_tm_binding.OVAL5_10TestMechanismType.factory()
                elif type_name_ == "YaraTestMechanismType":
                    import stix.bindings.extensions.test_mechanism.yara as yara_tm_binding
                    obj_ = yara_tm_binding.YaraTestMechanismType.factory()
                elif type_name_ == "SnortTestMechanismType":
                    import stix.bindings.extensions.test_mechanism.snort as snort_tm_binding
                    obj_ = snort_tm_binding.SnortTestMechanismType.factory()
                elif type_name_ == "OpenIOC2010TestMechanismType":
                    import stix.bindings.extensions.test_mechanism.open_ioc_2010 as openioc_tm_binding
                    obj_ = openioc_tm_binding.OpenIOC2010TestMechanismType.factory()
                elif type_name_ == "GenericTestMechanismType":
                    import stix.bindings.extensions.test_mechanism.generic as generic_tm_binding
                    obj_ = generic_tm_binding.GenericTestMechanismType.factory()
                else:
                    raise NotImplementedError('Class not implemented for <Test_Mechanism> element: ' + type_name_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <Test_Mechanism> element: no xsi:type attribute found')

            obj_.build(child_)
            self.Test_Mechanism.append(obj_)
# end class TestMechanismsType

class SuggestedCOAsType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Suggested_COA=None):
        super(SuggestedCOAsType, self).__init__(scope=scope)
        if Suggested_COA is None:
            self.Suggested_COA = []
        else:
            self.Suggested_COA = Suggested_COA
    def factory(*args_, **kwargs_):
        if SuggestedCOAsType.subclass:
            return SuggestedCOAsType.subclass(*args_, **kwargs_)
        else:
            return SuggestedCOAsType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Suggested_COA(self): return self.Suggested_COA
    def set_Suggested_COA(self, Suggested_COA): self.Suggested_COA = Suggested_COA
    def add_Suggested_COA(self, value): self.Suggested_COA.append(value)
    def insert_Suggested_COA(self, index, value): self.Suggested_COA[index] = value
    def hasContent_(self):
        if (
            self.Suggested_COA or
            super(SuggestedCOAsType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='SuggestedCOAsType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='SuggestedCOAsType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='indicator:', name_='SuggestedCOAsType'):
        super(SuggestedCOAsType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='SuggestedCOAsType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='SuggestedCOAsType', fromsubclass_=False, pretty_print=True):
        super(SuggestedCOAsType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Suggested_COA_ in self.Suggested_COA:
            Suggested_COA_.export(lwrite, level, nsmap, namespace_, name_='Suggested_COA', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(SuggestedCOAsType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Suggested_COA':
            obj_ = stix_common_binding.RelatedCourseOfActionType.factory()
            obj_.build(child_)
            self.Suggested_COA.append(obj_)
        super(SuggestedCOAsType, self).buildChildren(child_, node, nodeName_, True)
# end class SuggestedCOAsType

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
    def exportAttributes(self, lwrite, level, already_processed, namespace_='indicator:', name_='RelatedIndicatorsType'):
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

class IndicatorType(stix_common_binding.IndicatorBaseType):
    """The IndicatorType characterizes a cyber threat indicator made up of
    a pattern identifying certain observable conditions as well as
    contextual information about the patterns meaning, how and when
    it should be acted on, etc. Content creators should either
    create a "simple indicator" containing one observable, or a
    "composite indicator" containing multiple indicators.Specifies
    the relevant STIX-Indicator schema version for this content.The
    negate field applies when using an Indicator as a pattern and
    specifies the absence of the pattern."""
    subclass = None
    superclass = stix_common_binding.IndicatorBaseType
    def __init__(self, idref=None, id=None, timestamp=None, negate=False, version=None, Title=None, Type=None, Alternative_ID=None, Description=None, Short_Description=None, Valid_Time_Position=None, Observable=None, Composite_Indicator_Expression=None, Indicated_TTP=None, Kill_Chain_Phases=None, Test_Mechanisms=None, Likely_Impact=None, Suggested_COAs=None, Handling=None, Confidence=None, Sightings=None, Related_Indicators=None, Related_Campaigns=None, Related_Packages=None, Producer=None):
        super(IndicatorType, self).__init__(idref=idref, id=id, timestamp=timestamp)
        self.xmlns          = "http://stix.mitre.org/Indicator-2"
        self.xmlns_prefix   = "indicator"
        self.xml_type       = "IndicatorType"

        self.negate = _cast(bool, negate)
        self.version = _cast(None, version)
        self.Title = Title
        if Type is None:
            self.Type = []
        else:
            self.Type = Type
        if Alternative_ID is None:
            self.Alternative_ID = []
        else:
            self.Alternative_ID = Alternative_ID
        self.Description = Description
        self.Short_Description = Short_Description
        if Valid_Time_Position is None:
            self.Valid_Time_Position = []
        else:
            self.Valid_Time_Position = Valid_Time_Position
        self.Observable = Observable
        self.Composite_Indicator_Expression = Composite_Indicator_Expression
        if Indicated_TTP is None:
            self.Indicated_TTP = []
        else:
            self.Indicated_TTP = Indicated_TTP
        self.Kill_Chain_Phases = Kill_Chain_Phases
        self.Test_Mechanisms = Test_Mechanisms
        self.Likely_Impact = Likely_Impact
        self.Suggested_COAs = Suggested_COAs
        self.Handling = Handling
        self.Confidence = Confidence
        self.Sightings = Sightings
        self.Related_Indicators = Related_Indicators
        self.Related_Campaigns = Related_Campaigns
        self.Related_Packages = Related_Packages
        self.Producer = Producer
    def factory(*args_, **kwargs_):
        if IndicatorType.subclass:
            return IndicatorType.subclass(*args_, **kwargs_)
        else:
            return IndicatorType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Title(self): return self.Title
    def set_Title(self, Title): self.Title = Title
    def get_Type(self): return self.Type
    def set_Type(self, Type): self.Type = Type
    def add_Type(self, value): self.Type.append(value)
    def insert_Type(self, index, value): self.Type[index] = value
    def get_Alternative_ID(self): return self.Alternative_ID
    def set_Alternative_ID(self, Alternative_ID): self.Alternative_ID = Alternative_ID
    def add_Alternative_ID(self, value): self.Alternative_ID.append(value)
    def insert_Alternative_ID(self, index, value): self.Alternative_ID[index] = value
    def get_Description(self): return self.Description
    def set_Description(self, Description): self.Description = Description
    def get_Short_Description(self): return self.Short_Description
    def set_Short_Description(self, Short_Description): self.Short_Description = Short_Description
    def get_Valid_Time_Position(self): return self.Valid_Time_Position
    def set_Valid_Time_Position(self, Valid_Time_Position): self.Valid_Time_Position = Valid_Time_Position
    def add_Valid_Time_Position(self, value): self.Valid_Time_Position.append(value)
    def insert_Valid_Time_Position(self, index, value): self.Valid_Time_Position[index] = value
    def get_Observable(self): return self.Observable
    def set_Observable(self, Observable): self.Observable = Observable
    def get_Composite_Indicator_Expression(self): return self.Composite_Indicator_Expression
    def set_Composite_Indicator_Expression(self, Composite_Indicator_Expression): self.Composite_Indicator_Expression = Composite_Indicator_Expression
    def get_Indicated_TTP(self): return self.Indicated_TTP
    def set_Indicated_TTP(self, Indicated_TTP): self.Indicated_TTP = Indicated_TTP
    def add_Indicated_TTP(self, value): self.Indicated_TTP.append(value)
    def insert_Indicated_TTP(self, index, value): self.Indicated_TTP[index] = value
    def get_Kill_Chain_Phases(self): return self.Kill_Chain_Phases
    def set_Kill_Chain_Phases(self, Kill_Chain_Phases): self.Kill_Chain_Phases = Kill_Chain_Phases
    def get_Test_Mechanisms(self): return self.Test_Mechanisms
    def set_Test_Mechanisms(self, Test_Mechanisms): self.Test_Mechanisms = Test_Mechanisms
    def get_Likely_Impact(self): return self.Likely_Impact
    def set_Likely_Impact(self, Likely_Impact): self.Likely_Impact = Likely_Impact
    def get_Suggested_COAs(self): return self.Suggested_COAs
    def set_Suggested_COAs(self, Suggested_COAs): self.Suggested_COAs = Suggested_COAs
    def get_Handling(self): return self.Handling
    def set_Handling(self, Handling): self.Handling = Handling
    def get_Confidence(self): return self.Confidence
    def set_Confidence(self, Confidence): self.Confidence = Confidence
    def get_Sightings(self): return self.Sightings
    def set_Sightings(self, Sightings): self.Sightings = Sightings
    def get_Related_Indicators(self): return self.Related_Indicators
    def set_Related_Indicators(self, Related_Indicators): self.Related_Indicators = Related_Indicators
    def get_Related_Campaigns(self): return self.Related_Campaigns
    def set_Related_Campaigns(self, Related_Campaigns): self.Related_Campaigns = Related_Campaigns
    def get_Related_Packages(self): return self.Related_Packages
    def set_Related_Packages(self, Related_Packages): self.Related_Packages = Related_Packages
    def get_Producer(self): return self.Producer
    def set_Producer(self, Producer): self.Producer = Producer
    def get_negate(self): return self.negate
    def set_negate(self, negate): self.negate = negate
    def get_version(self): return self.version
    def set_version(self, version): self.version = version
    def hasContent_(self):
        if (
            self.Title is not None or
            self.Type or
            self.Alternative_ID or
            self.Description is not None or
            self.Short_Description is not None or
            self.Valid_Time_Position or
            self.Observable is not None or
            self.Composite_Indicator_Expression is not None or
            self.Indicated_TTP or
            self.Kill_Chain_Phases is not None or
            self.Test_Mechanisms is not None or
            self.Likely_Impact is not None or
            self.Suggested_COAs is not None or
            self.Handling is not None or
            self.Confidence is not None or
            self.Sightings is not None or
            self.Related_Indicators is not None or
            self.Related_Campaigns is not None or
            self.Related_Packages is not None or
            self.Producer is not None or
            super(IndicatorType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='Indicator', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='Indicator')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='indicator:', name_='Indicator'):
        super(IndicatorType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='Indicator')
        #if 'xmlns' not in already_processed:
        #    already_processed.add('xmlns')
        #    xmlns = " xmlns:%s='%s'" % (self.xmlns_prefix, self.xmlns)
        #    lwrite(xmlns)
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
            lwrite(xsi_type)
        if self.negate not in (None, False) and 'negate' not in already_processed:
            already_processed.add('negate')
            lwrite(' negate="%s"' % self.gds_format_boolean(self.negate, input_name='negate'))
        if self.version is not None and 'version' not in already_processed:
            already_processed.add('version')
            lwrite(' version=%s' % (quote_attrib(self.version), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IndicatorType', fromsubclass_=False, pretty_print=True):
        super(IndicatorType, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Title is not None:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Title>%s</%s:Title>%s' % (nsmap[namespace_], quote_xml(self.Title), nsmap[namespace_], eol_))
        for Type_ in self.Type:
            Type_.export(lwrite, level, nsmap, namespace_, name_='Type', pretty_print=pretty_print)
        for Alternative_ID_ in self.Alternative_ID:
            showIndent(lwrite, level, pretty_print)
            lwrite('<%s:Alternative_ID>%s</%s:Alternative_ID>%s' % (nsmap[namespace_], quote_xml(Alternative_ID_), nsmap[namespace_], eol_))
        if self.Description is not None:
            self.Description.export(lwrite, level, nsmap, namespace_, name_='Description', pretty_print=pretty_print)
        if self.Short_Description is not None:
            self.Short_Description.export(lwrite, level, nsmap, namespace_, name_='Short_Description', pretty_print=pretty_print)
        for Valid_Time_Position_ in self.Valid_Time_Position:
            Valid_Time_Position_.export(lwrite, level, nsmap, namespace_, name_='Valid_Time_Position', pretty_print=pretty_print)
        if self.Observable is not None:
            self.Observable.export(lwrite, level, "%s:" % (nsmap[namespace_]), name_='Observable', pretty_print=pretty_print)
        if self.Composite_Indicator_Expression is not None:
            self.Composite_Indicator_Expression.export(lwrite, level, nsmap, namespace_, name_='Composite_Indicator_Expression', pretty_print=pretty_print)
        for Indicated_TTP_ in self.Indicated_TTP:
            Indicated_TTP_.export(lwrite, level, nsmap, namespace_, name_='Indicated_TTP', pretty_print=pretty_print)
        if self.Kill_Chain_Phases is not None:
            self.Kill_Chain_Phases.export(lwrite, level, nsmap, namespace_, name_='Kill_Chain_Phases', pretty_print=pretty_print)
        if self.Test_Mechanisms is not None:
            self.Test_Mechanisms.export(lwrite, level, nsmap, namespace_, name_='Test_Mechanisms', pretty_print=pretty_print)
        if self.Likely_Impact is not None:
            self.Likely_Impact.export(lwrite, level, nsmap, namespace_, name_='Likely_Impact', pretty_print=pretty_print)
        if self.Suggested_COAs is not None:
            self.Suggested_COAs.export(lwrite, level, nsmap, namespace_, name_='Suggested_COAs', pretty_print=pretty_print)
        if self.Handling is not None:
            self.Handling.export(lwrite, level, nsmap, namespace_, name_='Handling', pretty_print=pretty_print)
        if self.Confidence is not None:
            self.Confidence.export(lwrite, level, nsmap, namespace_, name_='Confidence', pretty_print=pretty_print)
        if self.Sightings is not None:
            self.Sightings.export(lwrite, level, nsmap, namespace_, name_='Sightings', pretty_print=pretty_print)
        if self.Related_Indicators is not None:
            self.Related_Indicators.export(lwrite, level, nsmap, namespace_, name_='Related_Indicators', pretty_print=pretty_print)
        if self.Related_Campaigns is not None:
            self.Related_Campaigns.export(lwrite, level, nsmap, namespace_, name_='Related_Campaigns', pretty_print=pretty_print)
        if self.Related_Packages is not None:
            self.Related_Packages.export(lwrite, level, nsmap, namespace_, name_='Related_Packages', pretty_print=pretty_print)
        if self.Producer is not None:
            self.Producer.export(lwrite, level, nsmap, namespace_, name_='Producer', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('negate', node)
        if value is not None and 'negate' not in already_processed:
            already_processed.add('negate')
            if value in ('true', '1'):
                self.negate = True
            elif value in ('false', '0'):
                self.negate = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
        value = find_attr_value_('version', node)
        if value is not None and 'version' not in already_processed:
            already_processed.add('version')
            self.version = value
        super(IndicatorType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Title':
            Title_ = child_.text
            self.Title = Title_
        elif nodeName_ == 'Type':
            obj_ = stix_common_binding.ControlledVocabularyStringType.factory()
            obj_.build(child_)
            self.Type.append(obj_)
        elif nodeName_ == 'Alternative_ID':
            Alternative_ID_ = child_.text
            Alternative_ID_ = self.gds_validate_string(Alternative_ID_, node, 'Alternative_ID')
            self.Alternative_ID.append(Alternative_ID_)
        elif nodeName_ == 'Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Description(obj_)
        elif nodeName_ == 'Short_Description':
            obj_ = stix_common_binding.StructuredTextType.factory()
            obj_.build(child_)
            self.set_Short_Description(obj_)
        elif nodeName_ == 'Valid_Time_Position':
            obj_ = ValidTimeType.factory()
            obj_.build(child_)
            self.Valid_Time_Position.append(obj_)
        elif nodeName_ == 'Observable':
            obj_ = cybox_core_binding.ObservableType.factory()
            obj_.build(child_)
            self.set_Observable(obj_)
        elif nodeName_ == 'Composite_Indicator_Expression':
            obj_ = CompositeIndicatorExpressionType.factory()
            obj_.build(child_)
            self.set_Composite_Indicator_Expression(obj_)
        elif nodeName_ == 'Indicated_TTP':
            obj_ = stix_common_binding.RelatedTTPType.factory()
            obj_.build(child_)
            self.Indicated_TTP.append(obj_)
        elif nodeName_ == 'Kill_Chain_Phases':
            obj_ = stix_common_binding.KillChainPhasesReferenceType.factory()
            obj_.build(child_)
            self.set_Kill_Chain_Phases(obj_)
        elif nodeName_ == 'Test_Mechanisms':
            obj_ = TestMechanismsType.factory()
            obj_.build(child_)
            self.set_Test_Mechanisms(obj_)
        elif nodeName_ == 'Likely_Impact':
            obj_ = stix_common_binding.StatementType.factory()
            obj_.build(child_)
            self.set_Likely_Impact(obj_)
        elif nodeName_ == 'Suggested_COAs':
            obj_ = SuggestedCOAsType.factory()
            obj_.build(child_)
            self.set_Suggested_COAs(obj_)
        elif nodeName_ == 'Handling':
            obj_ = data_marking_binding.MarkingType.factory()
            obj_.build(child_)
            self.set_Handling(obj_)
        elif nodeName_ == 'Confidence':
            obj_ = stix_common_binding.ConfidenceType.factory()
            obj_.build(child_)
            self.set_Confidence(obj_)
        elif nodeName_ == 'Sightings':
            obj_ = SightingsType.factory()
            obj_.build(child_)
            self.set_Sightings(obj_)
        elif nodeName_ == 'Related_Indicators':
            obj_ = RelatedIndicatorsType.factory()
            obj_.build(child_)
            self.set_Related_Indicators(obj_)
        elif nodeName_ == 'Related_Campaigns':
            obj_ = RelatedCampaignReferencesType.factory()
            obj_.build(child_)
            self.set_Related_Campaigns(obj_)
        elif nodeName_ == 'Related_Packages':
            obj_ = stix_common_binding.RelatedPackageRefsType.factory()
            obj_.build(child_)
            self.set_Related_Packages(obj_)
        elif nodeName_ == 'Producer':
            obj_ = stix_common_binding.InformationSourceType.factory()
            obj_.build(child_)
            self.set_Producer(obj_)
        super(IndicatorType, self).buildChildren(child_, node, nodeName_, True)
# end class IndicatorType

class RelatedCampaignReferencesType(stix_common_binding.GenericRelationshipListType):
    subclass = None
    superclass = stix_common_binding.GenericRelationshipListType
    def __init__(self, scope='exclusive', Related_Campaign=None):
        super(RelatedCampaignReferencesType, self).__init__(scope=scope)
        if Related_Campaign is None:
            self.Related_Campaign = []
        else:
            self.Related_Campaign = Related_Campaign
    def factory(*args_, **kwargs_):
        if RelatedCampaignReferencesType.subclass:
            return RelatedCampaignReferencesType.subclass(*args_, **kwargs_)
        else:
            return RelatedCampaignReferencesType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Related_Campaign(self): return self.Related_Campaign
    def set_Related_Campaign(self, Related_Campaign): self.Related_Campaign = Related_Campaign
    def add_Related_Campaign(self, value): self.Related_Campaign.append(value)
    def insert_Related_Campaign(self, index, value): self.Related_Campaign[index] = value
    def hasContent_(self):
        if (
            self.Related_Campaign or
            super(RelatedCampaignReferencesType, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedCampaignReferencesType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedCampaignReferencesType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='indicator:', name_='RelatedCampaignReferencesType'):
        super(RelatedCampaignReferencesType, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='RelatedCampaignReferencesType')
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='RelatedCampaignReferencesType', fromsubclass_=False, pretty_print=True):
        super(RelatedCampaignReferencesType, self).exportChildren(lwrite, level, nsmap, stix_common_binding.XML_NS, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        for Related_Campaign_ in self.Related_Campaign:
            Related_Campaign_.export(lwrite, level, nsmap, namespace_, name_='Related_Campaign', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(RelatedCampaignReferencesType, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Related_Campaign':
            obj_ = stix_common_binding.RelatedCampaignReferenceType.factory()
            obj_.build(child_)
            self.Related_Campaign.append(obj_)
        super(RelatedCampaignReferencesType, self).buildChildren(child_, node, nodeName_, True)
# end class RelatedCampaignReferencesType


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
        rootTag = 'Indicator'
        rootClass = IndicatorType
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
        rootTag = 'Indicator'
        rootClass = IndicatorType
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
        rootTag = 'Indicator'
        rootClass = IndicatorType
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
    "ValidTimeType",
    "CompositeIndicatorExpressionType",
    "TestMechanismType",
    "SightingsType",
    "SightingType",
    "TestMechanismsType",
    "SuggestedCOAsType",
    "RelatedIndicatorsType",
    "IndicatorType"
    ]
