#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
'''
Description: Build a STIX Document with Tool Information
'''

from stix.core import STIXPackage, STIXHeader
from stix.common import InformationSource
from cybox.common import ToolInformationList, ToolInformation

def main():
    stix_package = STIXPackage()
    stix_header = STIXHeader()

    # Add tool information
    stix_header.information_source = InformationSource()
    stix_header.information_source.tools = ToolInformationList()
    stix_header.information_source.tools.append(ToolInformation("python-stix ex_04.py", "The MITRE Corporation"))

    stix_header.description = "Example "
    stix_package.stix_header = stix_header

    print(stix_package.to_xml())
    print(stix_package.to_dict())

if __name__ == '__main__':
    main()
