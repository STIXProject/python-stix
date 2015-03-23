# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
from distutils.version import StrictVersion

# external
from lxml import etree

# internal
import stix
import stix.xmlconst as xmlconst

# relative
from . import ignored, is_etree, is_element


class UnknownVersionError(Exception):
    """Raised when a parsed STIX document contains no version information."""
    pass


class UnsupportedVersionError(Exception):
    """Raised when a parsed STIX document contains a version that is
    not supported by this verison of python-stix.

    """
    def __init__(self, message, expected=None, found=None):
        super(UnsupportedVersionError, self).__init__(message)
        self.expected = expected
        self.found = found


class UnsupportedRootElementError(Exception):
    """Raised when an input STIX document does not contain a supported root-
    level element.

    """
    def __init__(self, message, expected=None, found=None):
        super(UnsupportedRootElementError, self).__init__(message)
        self.expected = expected
        self.found = found


# Alias for backwards compatibility
UnsupportedRootElement = UnsupportedRootElementError


def get_xml_parser(encoding=None):
    """Returns an ``etree.ETCompatXMLParser`` instance."""
    parser = etree.ETCompatXMLParser(
        huge_tree=True,
        remove_comments=True,
        strip_cdata=False,
        remove_blank_text=True,
        resolve_entities=False,
        encoding=encoding
    )

    return parser


def get_etree(doc, encoding=None):
    if is_etree(doc):
        return doc
    elif is_element(doc):
        return etree.ElementTree(doc)
    else:
        parser = get_xml_parser(encoding=encoding)
        return etree.parse(doc, parser=parser)


def get_etree_root(doc, encoding=None):
    """Returns an instance of lxml.etree._Element for the given `doc` input.

    Args:
        doc: The input XML document. Can be an instance of
            ``lxml.etree._Element``, ``lxml.etree._ElementTree``, a file-like
            object, or a string filename.
        encoding: The character encoding of `doc`. If ``None``, an attempt
            will be made to determine the character encoding by the XML
            parser.

    Returns:
        An ``lxml.etree._Element`` instance for `doc`.

    Raises:
        IOError: If `doc` cannot be found.
        lxml.ParseError: If `doc` is a malformed XML document.

    """
    tree = get_etree(doc, encoding)
    root = tree.getroot()

    return root


def get_schemaloc_pairs(node):
    """Parses the xsi:schemaLocation attribute on `node`.

    Returns:
        A list of (ns, schemaLocation) tuples for the node.

    Raises:
        KeyError: If `node` does not have an xsi:schemaLocation attribute.

    """
    schemalocs = node.attrib[xmlconst.TAG_SCHEMALOCATION]
    l = schemalocs.split()
    return zip(l[::2], l[1::2])


def get_document_version(doc):
    root = get_etree_root(doc)

    if 'version' in root.attrib:
        return root.attrib['version']

    raise UnknownVersionError(
        "Unable to determine the version if the input STIX document: no "
        "version attribute found on the root element."
    )


def root_tag(doc):
    root = get_etree_root(doc)
    return root.tag


def is_stix(doc):
    root = root_tag(doc)
    return root == xmlconst.TAG_STIX_PACKAGE


class EntityParser(object):
    def __init__(self):
        pass

    def _check_version(self, tree):
        """Returns true of the instance document @tree is a version supported
        by python-stix.

        """
        document_version = get_document_version(tree)
        supported = stix.supported_stix_version()

        if StrictVersion(supported) == StrictVersion(document_version):
            return

        error = (
            "Your python-stix library supports STIX %s. Document version was "
            "%s" % (supported, document_version)
        )

        raise UnsupportedVersionError(
            message=error,
            expected=supported,
            found=document_version
        )

    def _check_root(self, tree):
        if is_stix(tree):
            return

        error = "Document root element must be an instance of STIX_Package"
        raise UnsupportedRootElement(
            message=error,
            expected=xmlconst.TAG_STIX_PACKAGE,
            found=root_tag(tree),
        )

    def _apply_input_namespaces(self, tree, entity):
        root = get_etree_root(tree)
        entity.__input_namespaces__ = dict(root.nsmap.iteritems())

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

    def parse_xml_to_obj(self, xml_file, check_version=True, check_root=True,
                         encoding=None):
        """Creates a STIX binding object from the supplied xml file.

        Args:
            xml_file: A filename/path or a file-like object representing a STIX
                instance document
            check_version: Inspect the version before parsing.
            check_root: Inspect the root element before parsing.
            encoding: The character encoding of the input `xml_file`.

        Raises:
            .UnknownVersionError: If `check_version` is ``True`` and `xml_file`
                does not contain STIX version information.
            .UnsupportedVersionError: If `check_version` is ``False`` and
                `xml_file` contains an unsupported STIX version.
            .UnsupportedRootElement: If `check_root` is ``True`` and `xml_file`
                contains an invalid root element.

        """
        root = get_etree_root(xml_file, encoding=encoding)

        if check_version:
            self._check_version(root)

        if check_root:
            self._check_root(root)

        import stix.bindings.stix_core as stix_core_binding 
        stix_package_obj = stix_core_binding.STIXType().factory()
        stix_package_obj.build(root)

        return stix_package_obj

    def parse_xml(self, xml_file, check_version=True, check_root=True,
                  encoding=None):
        """Creates a python-stix STIXPackage object from the supplied xml_file.

        Args:
            xml_file: A filename/path or a file-like object representing a STIX
                instance document
            check_version: Inspect the version before parsing.
            check_root: Inspect the root element before parsing.
            encoding: The character encoding of the input `xml_file`. If
                ``None``, an attempt will be made to determine the input
                character encoding.

        Raises:
            .UnknownVersionError: If `check_version` is ``True`` and `xml_file`
                does not contain STIX version information.
            .UnsupportedVersionError: If `check_version` is ``False`` and
                `xml_file` contains an unsupported STIX version.
            .UnsupportedRootElement: If `check_root` is ``True`` and `xml_file`
                contains an invalid root element.

        """
        root = get_etree_root(xml_file, encoding=encoding)

        stix_package_obj = self.parse_xml_to_obj(
            xml_file=root,
            check_version=check_version,
            check_root=check_root,
            encoding=encoding
        )
        
        from stix.core import STIXPackage  # resolve circular dependencies
        stix_package = STIXPackage().from_obj(stix_package_obj)

        self._apply_input_namespaces(root, stix_package)
        self._apply_input_schemalocations(root, stix_package)
        
        return stix_package
