# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.xmlconst import TAG_STIX_PACKAGE

import mixbox.parser
# Import these from mixbox for backward compatibility
from mixbox.parser import (UnknownVersionError, UnsupportedVersionError,
                           UnsupportedRootElementError)

# Alias for backwards compatibility
UnsupportedRootElement = UnsupportedRootElementError


class EntityParser(mixbox.parser.EntityParser):

    def supported_tags(self):
        return [TAG_STIX_PACKAGE]

    def get_version(self, root):
        return root.attrib.get('version')

    def supported_versions(self, tag=TAG_STIX_PACKAGE):
        return stix.supported_stix_version()

    def get_entity_class(self, tag=TAG_STIX_PACKAGE):
        return stix.core.STIXPackage
