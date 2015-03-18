# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# XML NAMESPACES
NS_XSI = "http://www.w3.org/2001/XMLSchema-instance"

# XML TAGS
TAG_XSI_TYPE = "{%s}type" % NS_XSI
TAG_SCHEMALOCATION = "{%s}schemaLocation" % NS_XSI

# STIX TAGS
TAG_STIX_PACKAGE = "{http://stix.mitre.org/stix-1}STIX_Package"

FALSE = (False, 'false', 0, '0')
TRUE  = (True, 'true', 1, '1')
