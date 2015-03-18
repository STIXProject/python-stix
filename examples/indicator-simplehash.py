#!/usr/bin/env python
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
"""
Description: Build a STIX File Hash Observables document. Note that this
does NOT create an Indicator and instead will add the File Hash Observable
to the top-level Observables collection found in the STIX Package.
"""
# python-cybox
from cybox.common import Hash
from cybox.objects.file_object import File

# python-stix
from stix.core import STIXPackage, STIXHeader


def main():
    # Create our CybOX Simple Hash Value
    shv = Hash()
    shv.simple_hash_value = "4EC0027BEF4D7E1786A04D021FA8A67F"

    # Create a CybOX File Object and add the Hash we created above.
    f = File()
    h = Hash(shv, Hash.TYPE_MD5)
    f.add_hash(h)

    # Create the STIX Package
    stix_package = STIXPackage()

    # Create the STIX Header and add a description.
    stix_header = STIXHeader()
    stix_header.description = "Simple File Hash Observable Example"
    stix_package.stix_header = stix_header

    # Add the File Hash Observable to the STIX Package. The add() method will
    # inspect the input and add it to the top-level stix_package.observables
    # collection.
    stix_package.add(f)

    # Print the XML!
    print(stix_package.to_xml())


if __name__ == '__main__':
    main()
