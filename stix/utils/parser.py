# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from lxml import etree
from distutils.version import StrictVersion
from stix.utils import ignored

NS_XSI = "http://www.w3.org/2001/XMLSchema-instance"
TAG_XSI_TYPE = "{%s}type" % NS_XSI
TAG_SCHEMALOCATION = "{%s}schemaLocation" % NS_XSI

class UnknownVersionError(Exception):
    pass


class UnsupportedVersionError(Exception):
    def __init__(self, message, expected=None, found=None):
        super(UnsupportedVersionError, self).__init__(message)
        self.expected = expected
        self.found = found


class UnsupportedRootElementError(Exception):
    def __init__(self, message, expected=None, found=None):
        super(UnsupportedRootElementError, self).__init__(message)
        self.expected = expected
        self.found = found


UnsupportedRootElement = UnsupportedRootElementError # for backwards compatibility


def get_xml_parser():
    """Returns an ``etree.ETCompatXMLParser`` instance."""
    parser = etree.ETCompatXMLParser(
        huge_tree=True,
        remove_comments=True,
        strip_cdata=False,
        remove_blank_text=True,
        resolve_entities=False,
    )

    return parser


def get_etree_root(doc):
    """Returns an instance of lxml.etree._Element for the given `doc` input.

    Args:
        doc: The input XML document. Can be an instance of
            ``lxml.etree._Element``, ``lxml.etree._ElementTree``, a file-like
            object, or a string filename.

    Returns:
        An ``lxml.etree._Element`` instance for `doc`.

    Raises:
        IOError: If `doc` cannot be found.
        lxml.ParseError: If `doc` is a malformed XML document.

    """
    if isinstance(doc, etree._Element):
        root = doc
    elif isinstance(doc, etree._ElementTree):
        root = doc.getroot()
    else:
        parser = get_xml_parser()
        tree = etree.parse(doc, parser=parser)
        root = tree.getroot()

    return root


def get_schemaloc_pairs(node):
    """Parses the xsi:schemaLocation attribute on `node`.

    Returns:
        A list of (ns, schemaLocation) tuples for the node.

    Raises:
        KeyError: If `node` does not have an xsi:schemaLocation attribute.

    """
    schemalocs = node.attrib[TAG_SCHEMALOCATION]
    l = schemalocs.split()
    pairs = zip(l[::2], l[1::2])

    return pairs


class EntityParser(object):
    def __init__(self):
        pass

    def _check_version(self, tree):
        """Returns true of the instance document @tree is a version supported
        by python-stix.

        """
        root = get_etree_root(tree)

        if 'version' not in root.attrib:
            raise UnknownVersionError(
                "No version attribute set on root STIX_Package element. "
                "Unable to determine version compatibility with python-stix."
            )

        python_stix_version = stix.__version__ # ex: '1.1.0.0'
        supported_stix_version = python_stix_version[:-2] # ex: '1.1.0'
        document_version = root.attrib['version']

        if StrictVersion(supported_stix_version) != StrictVersion(document_version):
            error = (
                "Your python-stix library supports STIX %s. Document "
                "version was %s" % (supported_stix_version, document_version),
            )
            raise UnsupportedVersionError(
                message=error,
                expected=supported_stix_version,
                found=document_version
            )

        return True

    def _check_root(self, tree):
        root = get_etree_root(tree)
        expected_tag = "{http://stix.mitre.org/stix-1}STIX_Package"

        if root.tag != expected_tag:
            raise UnsupportedRootElement(
                "Document root element must be an instance of STIX_Package",
                expected=expected_tag,
                found=root.tag
            )

        return True

    def _apply_input_namespaces(self, tree, entity):
        root = get_etree_root(tree)

        entity.__input_namespaces__ = {}
        for alias, ns in root.nsmap.iteritems():
            entity.__input_namespaces__[ns] = alias


    def _apply_input_schemalocations(self, tree, entity):
        """Attaches an __input_schemalocations__ dictionary to the input entity.

        Args:
            tree: The input etree instance
            entity: The entity to attach the schemlocation dictionary to

        """
        root = get_etree_root(tree)

        with ignored(KeyError):
            pairs = get_schemaloc_pairs(root)
            entity.__input_schemalocations__ = dict(pairs)

    def parse_xml_to_obj(self, xml_file, check_version=True, check_root=True):
        """Creates a STIX binding object from the supplied xml file.

        Args:
            xml_file: A filename/path or a file-like object representing a STIX
                instance document
            check_version: Inspect the version before parsing.
            check_root: Inspect the root element before parsing.

        Raises:
            .UnknownVersionError: If `check_version` is ``True`` and `xml_file`
                does not contain STIX version information.
            .UnsupportedVersionError: If `check_version` is ``False`` and
                `xml_file` contains an unsupported STIX version.
            .UnsupportedRootElement: If `check_root` is ``True`` and `xml_file`
                contains an invalid root element.

        """
        root = get_etree_root(xml_file)

        if check_version:
            self._check_version(root)

        if check_root:
            self._check_root(root)

        import stix.bindings.stix_core as stix_core_binding 
        stix_package_obj = stix_core_binding.STIXType().factory()
        stix_package_obj.build(root)

        return stix_package_obj

    def parse_xml(self, xml_file, check_version=True, check_root=True):
        """Creates a python-stix STIXPackage object from the supplied xml_file.

        Args:
            xml_file: A filename/path or a file-like object representing a STIX
                instance document
            check_version: Inspect the version before parsing.
            check_root: Inspect the root element before parsing.

        Raises:
            .UnknownVersionError: If `check_version` is ``True`` and `xml_file`
                does not contain STIX version information.
            .UnsupportedVersionError: If `check_version` is ``False`` and
                `xml_file` contains an unsupported STIX version.
            .UnsupportedRootElement: If `check_root` is ``True`` and `xml_file`
                contains an invalid root element.

        """
        root = get_etree_root(xml_file)

        stix_package_obj = self.parse_xml_to_obj(
            xml_file=root,
            check_version=check_version,
            check_root=check_root
        )
        
        from stix.core import STIXPackage # resolve circular dependencies
        stix_package = STIXPackage().from_obj(stix_package_obj)

        self._apply_input_namespaces(root, stix_package)
        self._apply_input_schemalocations(root, stix_package)
        
        return stix_package
