# Hand jammed, copy of GenerateDS 2.9a output

# Generated Thu Aug 4 07:57:22 by a developer


import sys
from stix.bindings import *
import stix.bindings.data_marking as data_marking_binding

XML_NS = "http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2"

#
# Data representation classes.
#

class IsProprietary(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, CISA_Proprietary=None, AISConsent=None, TLPMarking=None):
        self.CISA_Proprietary = _cast(bool, CISA_Proprietary)
        self.AISConsent = AISConsent
        self.TLPMarking = TLPMarking
    def factory(*args_, **kwargs_):
        if IsProprietary.subclass:
            return IsProprietary.subclass(*args_, **kwargs_)
        else:
            return IsProprietary(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_AISConsent(self): return self.AISConsent
    def set_AISConsent(self, AISConsent): self.AISConsent = AISConsent
    def get_TLPMarking(self): return self.TLPMarking
    def set_TLPMarking(self, TLPMarking): self.TLPMarking = TLPMarking
    def get_CISA_Proprietary(self): return self.CISA_Proprietary
    def set_CISA_Proprietary(self, CISA_Proprietary): self.CISA_Proprietary = CISA_Proprietary
    def hasContent_(self):
        if (
            self.AISConsent is not None or
            self.TLPMarking is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='IsProprietary', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='IsProprietary')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, namespace_, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='AISMarking:', name_='IsProprietary'):
        if self.CISA_Proprietary is not None and 'CISA_Proprietary' not in already_processed:
            already_processed.add('CISA_Proprietary')
            lwrite(' CISA_Proprietary="%s"' % self.gds_format_boolean(self.CISA_Proprietary, input_name='CISA_Proprietary'))
    def exportChildren(self, lwrite, level, nsmap, namespace_='AISMarking:', name_='IsProprietary', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.AISConsent is not None:
            self.AISConsent.export(lwrite, level, nsmap, namespace_, name_='AISConsent', pretty_print=pretty_print)
        if self.TLPMarking is not None:
            self.TLPMarking.export(lwrite, level, nsmap, namespace_, name_='TLPMarking', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('CISA_Proprietary', node)
        if value is not None and 'CISA_Proprietary' not in already_processed:
            already_processed.add('CISA_Proprietary')
            if value in ('true', '1'):
                self.CISA_Proprietary = True
            elif value in ('false', '0'):
                self.CISA_Proprietary = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'AISConsent':
            obj_ = AISConsentType.factory()
            obj_.build(child_)
            self.set_AISConsent(obj_)
        elif nodeName_ == 'TLPMarking':
            obj_ = TLPMarkingType.factory()
            obj_.build(child_)
            self.set_TLPMarking(obj_)
# end class IsProprietary


class NotProprietary(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, CISA_Proprietary=None, AISConsent=None, TLPMarking=None):
        self.CISA_Proprietary = _cast(bool, CISA_Proprietary)
        self.AISConsent = AISConsent
        self.TLPMarking = TLPMarking
    def factory(*args_, **kwargs_):
        if NotProprietary.subclass:
            return NotProprietary.subclass(*args_, **kwargs_)
        else:
            return NotProprietary(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_AISConsent(self): return self.AISConsent
    def set_AISConsent(self, AISConsent): self.AISConsent = AISConsent
    def get_TLPMarking(self): return self.TLPMarking
    def set_TLPMarking(self, TLPMarking): self.TLPMarking = TLPMarking
    def get_CISA_Proprietary(self): return self.CISA_Proprietary
    def set_CISA_Proprietary(self, CISA_Proprietary): self.CISA_Proprietary = CISA_Proprietary
    def hasContent_(self):
        if (
            self.AISConsent is not None or
            self.TLPMarking is not None
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='NotProprietary', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='NotProprietary')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite.write('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='AISMarking:', name_='NotProprietary'):
        if self.CISA_Proprietary is not None and 'CISA_Proprietary' not in already_processed:
            already_processed.add('CISA_Proprietary')
            lwrite(' CISA_Proprietary="%s"' % self.gds_format_boolean(self.CISA_Proprietary, input_name='CISA_Proprietary'))
    def exportChildren(self, lwrite, level, nsmap, namespace_='AISMarking:', name_='NotProprietary', fromsubclass_=False, pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.AISConsent is not None:
            self.AISConsent.export(lwrite, level, nsmap, namespace_, name_='AISConsent', pretty_print=pretty_print)
        if self.TLPMarking is not None:
            self.TLPMarking.export(lwrite, level, nsmap, namespace_, name_='TLPMarking', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('CISA_Proprietary', node)
        if value is not None and 'CISA_Proprietary' not in already_processed:
            already_processed.add('CISA_Proprietary')
            if value in ('true', '1'):
                self.CISA_Proprietary = True
            elif value in ('false', '0'):
                self.CISA_Proprietary = False
            else:
                raise_parse_error(node, 'Bad boolean attribute')
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'AISConsent':
            obj_ = AISConsentType.factory()
            obj_.build(child_)
            self.set_AISConsent(obj_)
        elif nodeName_ == 'TLPMarking':
            obj_ = TLPMarkingType.factory()
            obj_.build(child_)
            self.set_TLPMarking(obj_)
# end class NotProprietary

class AISConsentType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, consent=None):
        self.consent = _cast(None, consent)
        pass
    def factory(*args_, **kwargs_):
        if AISConsentType.subclass:
            return AISConsentType.subclass(*args_, **kwargs_)
        else:
            return AISConsentType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_consent(self): return self.consent
    def set_consent(self, consent): self.consent = consent
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AISConsentType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AISConsentType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='AISMarking:', name_='AISConsentType'):
        if self.consent is not None and 'consent' not in already_processed:
            already_processed.add('consent')
            lwrite(' consent=%s' % (self.gds_format_string(quote_attrib(self.consent).encode(ExternalEncoding), input_name='consent'), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_='AISMarking:', name_='AISConsentType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('consent', node)
        if value is not None and 'consent' not in already_processed:
            already_processed.add('consent')
            self.consent = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class AISConsentType

class TLPMarkingType(GeneratedsSuper):
    subclass = None
    superclass = None
    def __init__(self, color=None):
        self.color = _cast(None, color)
        pass
    def factory(*args_, **kwargs_):
        if TLPMarkingType.subclass:
            return TLPMarkingType.subclass(*args_, **kwargs_)
        else:
            return TLPMarkingType(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_color(self): return self.color
    def set_color(self, color): self.color = color
    def hasContent_(self):
        if (

            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='TLPMarkingType', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='TLPMarkingType')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, namespace_, name_, pretty_print=pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='AISMarking:', name_='TLPMarkingType'):
        if self.color is not None and 'color' not in already_processed:
            already_processed.add('color')
            lwrite(' color=%s' % (quote_attrib(self.color), ))
    def exportChildren(self, lwrite, level, nsmap, namespace_='AISMarking:', name_='TLPMarkingType', fromsubclass_=False, pretty_print=True):
        pass
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        value = find_attr_value_('color', node)
        if value is not None and 'color' not in already_processed:
            already_processed.add('color')
            self.color = value
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        pass
# end class TLPMarkingType

class AISMarkingStructure(data_marking_binding.MarkingStructureType):
    """The AISMarkingStructure is an implementation of the data marking
    schema that allows determining consent to share information
    source attribution."""
    subclass = None
    superclass = data_marking_binding.MarkingStructureType
    def __init__(self, idref=None, marking_model_ref=None, marking_model_name=None, id=None, Is_Proprietary=None, Not_Proprietary=None):
        super(AISMarkingStructure, self).__init__(idref, marking_model_ref, marking_model_name, id, )
        self.xmlns = XML_NS
        self.xmlns_prefix = "AIS"
        self.xml_type = "AISMarkingStructure"
        self.Is_Proprietary = Is_Proprietary
        self.Not_Proprietary = Not_Proprietary
    def factory(*args_, **kwargs_):
        if AISMarkingStructure.subclass:
            return AISMarkingStructure.subclass(*args_, **kwargs_)
        else:
            return AISMarkingStructure(*args_, **kwargs_)
    factory = staticmethod(factory)
    def get_Is_Proprietary(self): return self.Is_Proprietary
    def set_Is_Proprietary(self, Is_Proprietary): self.Is_Proprietary = Is_Proprietary
    def get_Not_Proprietary(self): return self.Not_Proprietary
    def set_Not_Proprietary(self, Not_Proprietary): self.Not_Proprietary = Not_Proprietary
    def hasContent_(self):
        if (
            self.Is_Proprietary is not None or
            self.Not_Proprietary is not None or
            super(AISMarkingStructure, self).hasContent_()
            ):
            return True
        else:
            return False
    def export(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AISMarkingStructure', namespacedef_='', pretty_print=True):
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        showIndent(lwrite, level, pretty_print)
        lwrite('<%s:%s%s' % (nsmap[namespace_], name_, namespacedef_ and ' ' + namespacedef_ or '', ))
        already_processed = set()
        self.exportAttributes(lwrite, level, already_processed, namespace_, name_='AISMarkingStructure')
        if self.hasContent_():
            lwrite('>%s' % (eol_, ))
            self.exportChildren(lwrite, level + 1, nsmap, XML_NS, name_, pretty_print=pretty_print)
            showIndent(lwrite, level, pretty_print)
            lwrite('</%s:%s>%s' % (nsmap[namespace_], name_, eol_))
        else:
            lwrite('/>%s' % (eol_, ))
    def exportAttributes(self, lwrite, level, already_processed, namespace_='AISMarking:', name_='AISMarkingStructure'):
        super(AISMarkingStructure, self).exportAttributes(lwrite, level, already_processed, namespace_, name_='AISMarkingStructure')
        if 'xsi:type' not in already_processed:
            already_processed.add('xsi:type')
            xsi_type = " xsi:type='%s:%s'" % (self.xmlns_prefix, self.xml_type)
            lwrite(xsi_type)
    def exportChildren(self, lwrite, level, nsmap, namespace_=XML_NS, name_='AISMarkingStructure', fromsubclass_=False, pretty_print=True):
        super(AISMarkingStructure, self).exportChildren(lwrite, level, nsmap, namespace_, name_, True, pretty_print=pretty_print)
        if pretty_print:
            eol_ = '\n'
        else:
            eol_ = ''
        if self.Is_Proprietary is not None:
            self.Is_Proprietary.export(lwrite, level, nsmap, namespace_, name_='Is_Proprietary', pretty_print=pretty_print)
        if self.Not_Proprietary is not None:
            self.Not_Proprietary.export(lwrite, level, nsmap, namespace_, name_='Not_Proprietary', pretty_print=pretty_print)
    def build(self, node):
        already_processed = set()
        self.buildAttributes(node, node.attrib, already_processed)
        for child in node:
            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]
            self.buildChildren(child, node, nodeName_)
    def buildAttributes(self, node, attrs, already_processed):
        super(AISMarkingStructure, self).buildAttributes(node, attrs, already_processed)
    def buildChildren(self, child_, node, nodeName_, fromsubclass_=False):
        if nodeName_ == 'Is_Proprietary':
            obj_ = IsProprietary.factory()
            obj_.build(child_)
            self.set_Is_Proprietary(obj_)
        elif nodeName_ == 'Not_Proprietary':
            obj_ = NotProprietary.factory()
            obj_.build(child_)
            self.set_Not_Proprietary(obj_)
        super(AISMarkingStructure, self).buildChildren(child_, node, nodeName_, True)
# end class AISMarkingStructure


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
        rootTag = 'AISConsentMarkingStructure'
        rootClass = AISMarkingStructure
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
        rootTag = 'AISConsentMarkingStructure'
        rootClass = AISMarkingStructure
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
        rootTag = 'AISConsentMarkingStructure'
        rootClass = AISMarkingStructure
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # sys.stdout.write('<?xml version="1.0" ?>\n')
    # rootObj.export(sys.stdout, 0, name_="TLPMarkingStructureType",
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
    "AISConsentType",
    "AISHandling",
    "AISMarkingStructure",
    "IsProprietary",
    "NotProprietary",
    "TLPMarkingType",
    ]
