import unittest
from stix.core import STIXPackage, STIXHeader
from stix.data_marking import Marking, MarkingSpecification
from stix.extensions.marking.ais_marking import AISMarkingStructure
from StringIO import StringIO

FALSE_EVERYONE_AMBER = (False, 'EVERYONE', 'AMBER')
FALSE_EVERYONE_WHITE = (False, 'EVERYONE', 'WHITE')
FALSE_EVERYONE_GREEN = (False, 'EVERYONE', 'GREEN')
FALSE_NONE_AMBER = (False, 'NONE', 'AMBER')

CISA_PROPRIETARY = 'cisa_proprietary'
CONSENT = 'consent'
COLOR = 'tlp_color'

EVERYONE = 'EVERYONE'
USG = 'USG'
NONE = 'NONE'

WHITE = 'WHITE'
GREEN = 'GREEN'
AMBER = 'AMBER'

# Index values
CISA_PROPRIETARY = 0
CONSENT = 1
TLP_COLOR = 2


class AISMarkingStructureConsumeTests(unittest.TestCase):

    def _test_base(self, filename, expected_values):
        stix_package = STIXPackage.from_xml(filename)
        for marking_structure in stix_package.stix_header.handling.markings:
            if 'AISMarkingStructure' not in marking_structure._XSI_TYPE:
                continue  # skip any non-AIS markings

            self.assertEqual(marking_structure.cisa_proprietary,
                             expected_values[CISA_PROPRIETARY],
                             msg="Expected CISA %s; got CISA %s" %
                                 (marking_structure.cisa_proprietary, expected_values[CISA_PROPRIETARY]))

            self.assertEqual(marking_structure.consent,
                             expected_values[CONSENT],
                             msg="Expected Consent %s; got Consent %s" %
                                 (marking_structure.consent, expected_values[CONSENT]))

            self.assertEqual(marking_structure.tlp_color,
                             expected_values[TLP_COLOR],
                             msg="Expected TLP %s; got TLP %s" %
                                 (marking_structure.tlp_color, expected_values[TLP_COLOR]))

    def test_ais_0(self):
        return self._test_base('stix_ais_0.xml', FALSE_EVERYONE_AMBER)

    def test_ais_1(self):
        return self._test_base('stix_ais_1.xml', FALSE_EVERYONE_AMBER)

    def test_ais_2(self):
        return self._test_base('stix_ais_2.xml', FALSE_EVERYONE_AMBER)

    def test_ais_3(self):
        return self._test_base('stix_ais_3.xml', FALSE_EVERYONE_AMBER)

    def test_ais_4(self):
        return self._test_base('stix_ais_4.xml', FALSE_EVERYONE_AMBER)

    def test_ais_5(self):
        return self._test_base('stix_ais_5.xml', FALSE_EVERYONE_AMBER)

    def test_ais_6(self):
        return self._test_base('stix_ais_6.xml', FALSE_EVERYONE_AMBER)

    def test_ais_7(self):
        return self._test_base('stix_ais_7.xml', FALSE_EVERYONE_AMBER)

    def test_ais_8(self):
        return self._test_base('stix_ais_8.xml', FALSE_EVERYONE_AMBER)

    def test_ais_9(self):
        return self._test_base('stix_ais_9.xml', FALSE_EVERYONE_WHITE)

    def test_ais_10(self):
        return self._test_base('stix_ais_10.xml', FALSE_EVERYONE_WHITE)

    def test_ais_11(self):
        return self._test_base('stix_ais_11.xml', FALSE_EVERYONE_WHITE)

    def test_ais_12(self):
        return self._test_base('stix_ais_12.xml', FALSE_EVERYONE_AMBER)

    def test_ais_13(self):
        return self._test_base('stix_ais_13.xml', FALSE_EVERYONE_WHITE)

    def test_ais_14(self):
        return self._test_base('stix_ais_14.xml', FALSE_EVERYONE_AMBER)

    def test_ais_15(self):
        return self._test_base('stix_ais_15.xml', FALSE_EVERYONE_AMBER)

    def test_ais_16(self):
        return self._test_base('stix_ais_16.xml', FALSE_EVERYONE_AMBER)

    def test_ais_17(self):
        return self._test_base('stix_ais_17.xml', FALSE_EVERYONE_AMBER)

    def test_ais_18(self):
        return self._test_base('stix_ais_18.xml', FALSE_EVERYONE_AMBER)

    def test_ais_19(self):
        return self._test_base('stix_ais_19.xml', FALSE_EVERYONE_AMBER)

    def test_ais_20(self):
        return self._test_base('stix_ais_20.xml', FALSE_EVERYONE_WHITE)

    def test_ais_21(self):
        return self._test_base('stix_ais_21.xml', FALSE_EVERYONE_AMBER)

    def test_ais_22(self):
        return self._test_base('stix_ais_22.xml', FALSE_EVERYONE_AMBER)

    def test_ais_23(self):
        return self._test_base('stix_ais_23.xml', FALSE_EVERYONE_AMBER)

    def test_ais_24(self):
        return self._test_base('stix_ais_24.xml', FALSE_EVERYONE_WHITE)

    def test_ais_25(self):
        return self._test_base('stix_ais_25.xml', FALSE_EVERYONE_GREEN)

    def test_ais_26(self):
        return self._test_base('stix_ais_26.xml', FALSE_EVERYONE_WHITE)

    def test_ais_27(self):
        return self._test_base('stix_ais_27.xml', FALSE_EVERYONE_AMBER)

    def test_ais_28(self):
        return self._test_base('stix_ais_28.xml', FALSE_EVERYONE_AMBER)

    def test_ais_29(self):
        return self._test_base('stix_ais_29.xml', FALSE_EVERYONE_AMBER)

    def test_ais_30(self):
        return self._test_base('stix_ais_30.xml', FALSE_EVERYONE_AMBER)

    def test_ais_31(self):
        return self._test_base('stix_ais_31.xml', FALSE_EVERYONE_AMBER)

    def test_ais_32(self):
        return self._test_base('stix_ais_32.xml', FALSE_EVERYONE_AMBER)

    def test_ais_33(self):
        return self._test_base('stix_ais_33.xml', FALSE_EVERYONE_AMBER)

    def test_ais_34(self):
        return self._test_base('stix_ais_34.xml', FALSE_EVERYONE_AMBER)

    def test_sqli_sample(self):
        return self._test_base('SQLi-Sample-005.xml', FALSE_NONE_AMBER)


class AISMarkingStructureProduceTests(unittest.TestCase):

    def _test_base(self, cisa_proprietary, consent, tlp_color):
        stix_package = STIXPackage()
        stix_package.stix_header = STIXHeader(description='Test')

        ais = AISMarkingStructure(cisa_proprietary=cisa_proprietary,
                                  consent=consent,
                                  tlp_color=tlp_color)
        marking_specification = MarkingSpecification(controlled_structure='//node() | //@*')
        marking_specification.marking_structures.append(ais)

        handling = Marking()
        handling.add_marking(marking_specification)

        stix_package.stix_header.handling = handling

        stix_xml_stringio = StringIO(stix_package.to_xml())

        sp2 = STIXPackage.from_xml(stix_xml_stringio)
        sp2_marking = sp2.stix_header.handling.markings[0]

        self.assertEqual(sp2_marking.controlled_structure, '//node() | //@*')

        ais_structure = sp2_marking.marking_structures[0]

        self.assertEqual(ais_structure.cisa_proprietary, cisa_proprietary)
        self.assertEqual(ais_structure.consent, consent)
        self.assertEqual(ais_structure.tlp_color, tlp_color)

    def test_1(self):
        return self._test_base(True, EVERYONE, WHITE)

    def test_2(self):
        return self._test_base(True, EVERYONE, GREEN)

    def test_3(self):
        return self._test_base(True, EVERYONE, AMBER)

    def test_4(self):
        return self._test_base(False, EVERYONE, WHITE)

    def test_5(self):
        return self._test_base(False, EVERYONE, GREEN)

    def test_6(self):
        return self._test_base(False, EVERYONE, AMBER)

    def test_7(self):
        return self._test_base(False, USG, WHITE)

    def test_8(self):
        return self._test_base(False, USG, GREEN)

    def test_9(self):
        return self._test_base(False, USG, AMBER)

    def test_10(self):
        return self._test_base(False, None, WHITE)

    def test_11(self):
        return self._test_base(False, None, GREEN)

    def test_12(self):
        return self._test_base(False, None, AMBER)
