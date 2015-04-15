#!/usr/bin/env python
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""
Description: An example of how to add CIQ Identity information to a STIX
Indicator.
"""
# stdlib
from pprint import pprint

# python-cybox
from cybox.objects.file_object import File

# python-stix
import stix.utils as utils
from stix.core import STIXPackage, STIXHeader
from stix.indicator import Indicator
import stix.extensions.identity.ciq_identity_3_0 as stix_ciq


def main():
    # Create a CybOX File Object with a contained hash
    f = File()
    f.add_hash("4EC0027BEF4D7E1786A04D021FA8A67F")

    # Create an Indicator with the File Hash Object created above.
    indicator = Indicator()
    indicator.title = "File Hash Example"
    indicator.description = (
        "An indicator containing a File observable with an associated hash"
    )
    indicator.set_producer_identity("The MITRE Corporation")
    indicator.set_produced_time(utils.dates.now())

    # Add The File Object to the Indicator. This will promote the CybOX Object
    # to a CybOX Observable internally.
    indicator.add_object(f)

    # Build our STIX CIQ Identity object
    party_name = stix_ciq.PartyName(
        name_lines=("Foo", "Bar"),
        person_names=("John Smith", "Jill Smith"),
        organisation_names=("Foo Inc.", "Bar Corp.")
    )
    ident_spec = stix_ciq.STIXCIQIdentity3_0(party_name=party_name)
    ident_spec.add_electronic_address_identifier("jsmith@example.com")
    ident_spec.add_free_text_line("Demonstrating Free Text!")
    ident_spec.add_contact_number("555-555-5555")
    ident_spec.add_contact_number("555-555-5556")

    # Build and add a CIQ Address
    addr = stix_ciq.Address(
        free_text_address='1234 Example Lane.',
        country='USA',
        administrative_area='An Admin Area'
    )
    ident_spec.add_address(addr)

    # Build and add a nationality
    nationality = stix_ciq.Country("Norway")
    ident_spec.add_nationality(nationality)

    identity = stix_ciq.CIQIdentity3_0Instance(specification=ident_spec)

    # Set the Indicator producer identity to our CIQ Identity
    indicator.set_producer_identity(identity)

    # Build our STIX Package
    stix_package = STIXPackage()

    # Build a STIX Header and add a description
    stix_header = STIXHeader()
    stix_header.description = "STIX CIQ Identity Extension Example"

    # Set the STIX Header on our STIX Package
    stix_package.stix_header = stix_header

    # Add our Indicator object. The add() method will inspect the input and
    # append it to the `stix_package.indicators` collection.
    stix_package.add(indicator)
    
    # Print the XML!
    print(stix_package.to_xml())

    # Print a dictionary!
    pprint(stix_package.to_dict())

if __name__ == '__main__':
    main()
