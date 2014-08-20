#!/usr/bin/env python
# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

'''
Prints certain fields from a STIXPackage object using the python interface
'''
import sys

from stix.core import STIXPackage
from stix.indicator import Indicator
from cybox.core import Object, Observable

def main():
    fn = sys.argv[-1] if len(sys.argv) == 2 else 'sample.xml'
    stix_package = STIXPackage.from_xml(fn)

    indicator_count = 0
    observable_count = 0
    object_count = 0
    for child in stix_package.walk():
        if isinstance(child, Indicator):
            indicator_count += 1
        elif isinstance(child, Observable):
            observable_count += 1
        elif isinstance(child, Object):
            object_count += 1

    print "Indicators:", indicator_count
    print "Observables:", observable_count
    print "Objects:", object_count

if __name__ == '__main__':
    main()

