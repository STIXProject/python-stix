import unittest

from stix.test import EntityTestCase

from stix.core import STIXPackage
from stix.extensions.marking import ais


class AISMarkingStructureNotProprietaryTests(EntityTestCase, unittest.TestCase):
    klass = ais.AISMarkingStructure
    _full_dict = {
        'not_proprietary':
            {
                'cisa_proprietary': 'false',
                'ais_consent': {'consent': 'NONE'},
                'tlp_marking': {'color': 'GREEN'}
            },
        'xsi:type': 'AIS:AISMarkingStructure'
    }


class AISMarkingStructureIsProprietaryTests(EntityTestCase, unittest.TestCase):
    klass = ais.AISMarkingStructure
    _full_dict = {
        'is_proprietary':
            {
                'cisa_proprietary': 'true',
                'ais_consent': {'consent': 'EVERYONE'},
                'tlp_marking': {'color': 'AMBER'}
            },
        'xsi:type': 'AIS:AISMarkingStructure'
    }


class AISMarkingGeneralTests(unittest.TestCase):
    """General tests for ais module helpers."""

    @classmethod
    def setUpClass(cls):
        cls.INDUSTRY_SECTORS = (ais.CHEMICAL_SECTOR, ais.COMMERCIAL_FACILITIES_SECTOR,
                                ais.COMMUNICATIONS_SECTOR,
                                ais.CRITICAL_MANUFACTURING_SECTOR,
                                ais.DAMS_SECTOR, ais.DEFENSE_INDUSTRIAL_BASE_SECTOR,
                                ais.EMERGENCY_SERVICES_SECTOR, ais.ENERGY_SECTOR,
                                ais.FINANCIAL_SERVICES_SECTOR,
                                ais.FOOD_AND_AGRICULTURE_SECTOR,
                                ais.GOVERNMENT_FACILITIES_SECTOR,
                                ais.HEALTH_CARE_AND_PUBLIC_HEALTH_SECTOR,
                                ais.INFORMATION_TECHNOLOGY_SECTOR,
                                ais.NUCLEAR_REACTORS_MATERIALS_AND_WASTE_SECTOR,
                                ais.TRANSPORTATION_SYSTEMS_SECTOR, ais.OTHER,
                                ais.WATER_AND_WASTEWATER_SYSTEMS_SECTOR)

    def test_validate_and_create_industry_type(self):
        self.assertRaises(ValueError, ais._validate_and_create_industry_type, [])
        self.assertRaises(ValueError, ais._validate_and_create_industry_type, "")
        self.assertRaises(ValueError, ais._validate_and_create_industry_type, [""])
        self.assertRaises(ValueError, ais._validate_and_create_industry_type, ["Energy Sector", "Others", "Dams Sector"])
        self.assertRaises(ValueError, ais._validate_and_create_industry_type, "Energy Sector| Others|Dams Sector")
        self.assertRaises(ValueError, ais._validate_and_create_industry_type, 3)
        self.assertRaises(ValueError, ais._validate_and_create_industry_type, "|")
        self.assertRaises(ValueError, ais._validate_and_create_industry_type, ["Energy Sector|Dams Sector"])

        self.assertEqual(ais._validate_and_create_industry_type("eNergY sectOr"), ais.ENERGY_SECTOR)
        self.assertEqual(ais._validate_and_create_industry_type("eNergY sectOr   |Dams sector"), "Energy Sector|Dams Sector")
        self.assertEqual(ais._validate_and_create_industry_type(["eNergY sectOr    ", "    Dams sectOr    "]), "Energy Sector|Dams Sector")
        self.assertEqual(ais._validate_and_create_industry_type([ais.ENERGY_SECTOR, ais.DAMS_SECTOR]), "Energy Sector|Dams Sector")
        self.assertEqual(ais._validate_and_create_industry_type("Energy Sector|Dams Sector"), "Energy Sector|Dams Sector")

        for idx, x in enumerate(self.INDUSTRY_SECTORS):
            self.assertEqual(ais._validate_and_create_industry_type(x), self.INDUSTRY_SECTORS[idx])

    def test_add_ais_marking(self):
        PACKAGE = STIXPackage()

        # Missing kwarg.
        self.assertRaises(ValueError, ais.add_ais_marking, PACKAGE, True, 'NONE', 'GREEN',
                        country_name_code='US',
                        country_name_code_type='ISO 3166-1 alpha-2',
                        admin_area_name_code='US-DC',
                        admin_area_name_code_type='ISO 3166-2',
                        organisation_name='NCCIC')

if __name__ == "__main__":
    unittest.main()
