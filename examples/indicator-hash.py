#!/usr/bin/env python
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""
Description: Build a STIX Indicator document containing a File observable with
an associated hash.
"""

# python-cybox
from cybox.objects.file_object import File

# python-stix
import stix.utils as utils
from stix.core import STIXPackage, STIXHeader
from stix.indicator import Indicator


def main():
    # Create a CyboX File Object
    f = File()

    # This automatically detects that it's an MD5 hash based on the length
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

    # Create a STIX Package
    stix_package = STIXPackage()

    # Create the STIX Header and add a description.
    stix_header = STIXHeader()
    stix_header.description = "File Hash Indicator Example"
    stix_package.stix_header = stix_header

    # Add our Indicator object. The add() method will inspect the input and
    # append it to the `stix_package.indicators` collection.
    stix_package.add(indicator)

    # Print the XML!
    print(stix_package.to_xml())


if __name__ == '__main__':
    main()
