#!/usr/bin/env python
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
"""
Description: Demonstrate the use and parsing of custom VocabString controlled
vocabulary implementations.
"""

# builtin
from StringIO import StringIO

# python-stix modules
from stix.core import STIXPackage
from stix.common import vocabs

XML = \
"""
<stix:STIX_Package
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:stix="http://stix.mitre.org/stix-1"
    xmlns:customVocabs="http://customvocabs.com/vocabs-1"
    xmlns:example="http://example.com/"
    xsi:schemaLocation="
    http://stix.mitre.org/stix-1 ../stix_core.xsd
    http://customvocabs.com/vocabs-1 ../my_vocabs.xsd"
    id="example:STIXPackage-33fe3b22-0201-47cf-85d0-97c02164528d"
    timestamp="2014-05-08T09:00:00.000000Z"
    version="1.1.1">
    <stix:STIX_Header>
        <stix:Package_Intent xsi:type="customVocabs:CustomVocab-1.0">FOO</stix:Package_Intent>
    </stix:STIX_Header>
</stix:STIX_Package>
"""

# Create a VocabString class for our CustomVocab-1.0 vocabular
class CustomVocab(vocabs.VocabString):
    _namespace = 'http://customvocabs.com/vocabs-1'
    _XSI_TYPE = 'customVocabs:CustomVocab-1.0'
    _ALLOWED_VALUES = ('FOO', 'BAR')

# Register our Custom Vocabulary class so parsing and serialization works
vocabs.add_vocab(CustomVocab)

# Parse the input document
sio = StringIO(XML)
package = STIXPackage.from_xml(sio)

# Retrieve the first (and only) Package_Intent entry
package_intent = package.stix_header.package_intents[0]

# Print information about the input Package_Intent
print type(package_intent), package_intent.xsi_type, package_intent

# Add another Package Intent
bar = CustomVocab('BAR')
package.stix_header.add_package_intent(bar)

schemalocs = {'http://customvocabs.com/vocabs-1': '/path/to/customVocabs.xsd'}

# This will include the 'BAR' CustomVocab entry
print package.to_xml(schemaloc_dict=schemalocs)
