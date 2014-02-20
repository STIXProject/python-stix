#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
File: ex_05.py

Description: An example of how to add CIQ Identity information to a STIX Indicator
'''

from datetime import datetime
from stix.indicator import Indicator
from stix.extensions.identity import CIQIdentity3_0Instance, STIXCIQIdentity3_0, PartyName, PersonName
from stix.core import STIXPackage, STIXHeader
from cybox.common import Hash
from cybox.objects.file_object import File

def main():
    shv = Hash()
    shv.simple_hash_value = "4EC0027BEF4D7E1786A04D021FA8A67F"
    
    f = File()
    h = Hash(shv, Hash.TYPE_MD5)
    f.add_hash(h)
    
    indicator = Indicator()
    indicator.title = "File Hash Example"
    indicator.description = "An indicator containing a File observable with an associated hash"
    indicator.set_producer_identity("The MITRE Corporation")
    indicator.set_produced_time(datetime.now())
    indicator.add_object(f)
    
    party_name = PartyName(name_lines=["Foo", "Bar"], person_names=["John Smith", "Jill Smith"], organisation_names=["Foo Inc.", "Bar Corp."])
    ident_spec = STIXCIQIdentity3_0(party_name=party_name)
    identity = CIQIdentity3_0Instance(specification=ident_spec)
    indicator.set_producer_identity(identity)
    
    stix_package = STIXPackage()
    stix_header = STIXHeader()
    stix_header.description = "Example 02"
    stix_package.stix_header = stix_header
    stix_package.add_indicator(indicator)
    
    
    
    print(stix_package.to_xml())

if __name__ == '__main__':
    main()
