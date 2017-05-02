import unittest

from stix.test import EntityTestCase

from stix.extensions.marking.tlp import TLPMarkingStructure


class TLPMarkingStructureTests(EntityTestCase, unittest.TestCase):
    klass = TLPMarkingStructure
    _full_dict = {
        'marking_model_name': 'TLP',
        'marking_model_ref': "http://www.us-cert.gov/tlp/",
        'color': "RED",
        'xsi:type': "tlpMarking:TLPMarkingStructureType",
    }


if __name__ == "__main__":
    unittest.main()

