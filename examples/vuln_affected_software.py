#!/usr/bin/env python
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""
File: vuln_affected_software.py

Description: Demonstrates the setting of the `affected_software` property
on the stix.exploit_target.vulnerability.Vulnerability class.

"""
# python-cybox
from cybox.core import Observable
from cybox.objects.product_object import Product

# python-stix
from stix.core import STIXPackage
from stix.exploit_target import ExploitTarget
from stix.exploit_target.vulnerability import Vulnerability


# Build a Product Object that characterizes our affected software
software = Product()
software.product = "Foobar"
software.version = "3.0"
software.edition = "GOTY"

# Wrap the Product Object in an Observable instance
observable = Observable(software)

# Attach the Product observable to the affected_sofware list of
# RelatedObservable instances. This wraps our Observable in a
# RelatedObservable layer.
vuln = Vulnerability()
vuln.affected_software.append(observable)

# Create the Exploit Target
et = ExploitTarget()

# Attach our Vulnerability to the Exploit Target
et.vulnerabilities.append(vuln)

# Build a STIX Package
package = STIXPackage()

# Attach the Exploit Target instance to the Package
package.exploit_targets.append(et)

# Print!
print package.to_xml()