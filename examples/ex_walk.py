#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
File: ex_walk.py

Walks a STIXPackage object
'''
import io
from pprint import pprint

from stix.core import STIXPackage
from stix.indicator import Indicator
import stix.bindings.stix_core as stix_core_binding

def main():
    fn = 'ex_01.xml'
    stix_package = STIXPackage.from_xml(fn)
   
    for child in stix_package.walk():
        print type(child), child

    result = stix_package.find("example:Object-1980ce43-8e03-490b-863a-ea404d12242e")
    if result:
        print "Found:", type(result), result
    else:
        print "Not found:"

if __name__ == '__main__':
    main()

