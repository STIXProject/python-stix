# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase

from stix.extensions.marking.terms_of_use_marking import TermsOfUseMarkingStructure


class TermsOfUseMarkingStructureTests(EntityTestCase, unittest.TestCase):
    klass = TermsOfUseMarkingStructure
    _full_dict = {
        'terms_of_use': "You may not use this content for anything.",
        'xsi:type': "TOUMarking:TermsOfUseMarkingStructureType",
    }


if __name__ == "__main__":
    unittest.main()

