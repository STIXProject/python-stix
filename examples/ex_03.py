#!/usr/bin/env python
# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
'''
File: ex_03.py

Description: Build a STIX Observables document
'''

from stix.core import STIXPackage, STIXHeader
from cybox.common import Hash
from cybox.objects.file_object import File

def main():
    shv = Hash()
    shv.simple_hash_value = "4EC0027BEF4D7E1786A04D021FA8A67F"
    
    f = File()
    h = Hash(shv, Hash.TYPE_MD5)
    f.add_hash(h)
    
    stix_package = STIXPackage()
    stix_header = STIXHeader()
    stix_header.description = "Example 03"
    stix_package.stix_header = stix_header
    stix_package.add_observable(f)
    
    print(stix_package.to_xml())

if __name__ == '__main__':
    main()
