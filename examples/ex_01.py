#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
File: ex_01.py

Description: Round-trip example. This script takes a STIX instance document from XML to
a binding object, then to a api object and then to a dictionary. That dictionary is then
converted back into an api object, which is then used to generate an XML document.
'''
import io
from pprint import pprint

from stix.core import STIXPackage
from stix.indicator import Indicator
import stix.bindings.stix_core as stix_core_binding

def main():
    fn = 'ex_01.xml'
    stix_package = STIXPackage.from_xml(fn)
    stix_dict = stix_package.to_dict() # parse to dictionary
    pprint(stix_dict)
    
    stix_package_two = STIXPackage.from_dict(stix_dict) # create python-stix object from dictionary
    xml = stix_package_two.to_xml() # generate xml from python-stix object
    print(xml)
    
if __name__ == '__main__':
    main()
