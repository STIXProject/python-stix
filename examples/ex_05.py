#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
File: ex_05.py

Description: An example of how to add CIQ Identity information to a STIX Indicator
'''

from datetime import datetime
from stix.indicator import Indicator
from stix.extensions.identity.ciq_identity_3_0 import CIQIdentity3_0Instance, STIXCIQIdentity3_0, PartyName, PersonName
from stix.core import STIXPackage, STIXHeader
from cybox.common import Hash
from cybox.objects.file_object import File

def main():
    f = File()
    f.add_hash("4EC0027BEF4D7E1786A04D021FA8A67F")
    
    indicator = Indicator()
    indicator.title = "File Hash Example"
    indicator.description = "An indicator containing a File observable with an associated hash"
    indicator.set_producer_identity("The MITRE Corporation")
    indicator.set_produced_time(datetime.now())
    indicator.add_object(f)
    
    party_name = PartyName(name_lines=["Foo", "Bar"], person_names=["John Smith", "Jill Smith"], organisation_names=["Foo Inc.", "Bar Corp."])
    ident_spec = STIXCIQIdentity3_0(party_name=party_name)
    ident_spec.add_electronic_address_identifier("jsmith@example.com")
    ident_spec.add_free_text_line("Demonstrating Free Text!")
    ident_spec.add_contact_number("555-555-5555")
    ident_spec.add_contact_number("555-555-5556")
    identity = CIQIdentity3_0Instance(specification=ident_spec)
    indicator.set_producer_identity(identity)
    
    stix_package = STIXPackage()
    stix_header = STIXHeader()
    stix_header.description = "Example 05"
    stix_package.stix_header = stix_header
    stix_package.add_indicator(indicator)
    
    xml = stix_package.to_xml() 
    print(xml)

if __name__ == '__main__':
    main()