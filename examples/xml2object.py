#!/usr/bin/env python
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""
Description: Round-trip example. This script takes a STIX instance document from XML to
a binding object, then to a api object and then to a dictionary. That dictionary is then
converted back into an api object, which is then used to generate an XML document.
"""
# stdlib
from pprint import pprint

# python-stix
from stix.core import STIXPackage


def main():
    FILENAME = 'sample.xml'

    # Parse input file
    stix_package = STIXPackage.from_xml(FILENAME)

    # Convert STIXPackage to a Python dictionary via the to_dict() method.
    stix_dict = stix_package.to_dict()

    # Print the dictionary!
    pprint(stix_dict)

    # Convert the first STIXPackage dictionary into another STIXPackage via
    # the from_dict() method.
    stix_package_two = STIXPackage.from_dict(stix_dict)

    # Serialize the new STIXPackage object to XML
    xml = stix_package_two.to_xml()

    # Print the XML!
    print(xml)

if __name__ == '__main__':
    main()
