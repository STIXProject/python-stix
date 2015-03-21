#!/usr/bin/env python
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""
File: vocabstrings.py

Demonstrates uses of VocabString for STIX Controlled Vocabularies.
"""
from stix.core import STIXHeader
from stix.common.vocabs import VocabString, PackageIntent


def main():
    # Create STIXHeader instance
    header = STIXHeader()
    header.package_intents.append(PackageIntent.TERM_INDICATORS)

    # To add a Package_Intent value that exists outside of the
    # PackageIntentVocab controlled vocabulary, we pass in an
    # instance of VocabString.
    #
    # This will create a new Package_Intent field without an
    # xsi:type and will not perform any validation of input terms.
    #
    # Passing in an instance of VocabString works for every
    # ControlledVocabularyStringType field (or in python-stix,
    # every VocabString field).

    non_default_value = VocabString("NON STANDARD PACKAGE INTENT")
    header.package_intents.append(non_default_value)

    # Print XML!
    print header.to_xml()

    # NOTE: Passing in a str value that is not included in the list
    # of default CV terms will raise a ValueError. This is why we pass
    # in a VocabString instance.
    #
    # Example:
    try:
        msg = (
            "[-] Attempting to add an str instance that does not exist "
            "in the PackageIntent ALLOWED_VALUES list"
        )
        print(msg)

        header.package_intents.append("THIS WILL THROW A VALUEERROR")
    except Exception as ex:
        print "[!] As expected, that failed. Here's the Exception message:"
        print "[!]", str(ex)

if __name__ == '__main__':
    main()

