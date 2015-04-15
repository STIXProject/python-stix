# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
import StringIO

from cybox.common import StructuredText

from stix.test import EntityTestCase, TypedListTestCase, data_marking_test
from stix.test.common import (
    confidence_test, information_source_test, statement_test, related_test
)

import stix.common.vocabs as vocabs
import stix.incident as incident
import stix.incident.history as history
import stix.incident.property_affected as property_affected
import stix.incident.impact_assessment as impact_assessment
import stix.incident.affected_asset as affected_asset
import stix.bindings.incident as incident_binding


INCIDENT_CATEGORIES = """<?xml version="1.0" encoding="UTF-8"?>
<incident:Incident
 xmlns:incident="http://stix.mitre.org/Incident-1"
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xsi:schemaLocation="http://stix.mitre.org/Incident-1 http://stix.mitre.org/XMLSchema/incident/1.0.1/incident.xsd">
 <incident:Categories>
  <incident:Category>Foo</incident:Category>
  <incident:Category>Bar</incident:Category>
 </incident:Categories>
</incident:Incident>
"""


class COATimeTest(EntityTestCase, unittest.TestCase):
    klass = incident.COATime

    _full_dict = {
        'start': {
            'value': "2014-02-04T08:21:33",
            'precision': 'hour',
        },
        'end': {
            'value': "2014-02-04T08:21:33",
            'precision': 'hour',
        },
    }


class COATakenTest(EntityTestCase, unittest.TestCase):
    klass = incident.COATaken

    _full_dict = {
        'time': COATimeTest._full_dict,
        #'coordinators': None,  # need to implement this!
        'course_of_action': {
            'version': '1.1.1',
            'title': 'Test Title',
            'description': 'Test Description',
            'short_description': "Test Short Description",
            'timestamp': '2015-03-06T14:35:23.375304+00:00',
        }
    }


class COAsTakenTest(TypedListTestCase, unittest.TestCase):
    klass = incident._COAsTaken

    _full_dict = [
        COATakenTest._full_dict,
    ]


class COARequestedTest(EntityTestCase, unittest.TestCase):
    klass = incident.COARequested

    _full_dict = {
        'time': COATimeTest._full_dict,
        'priority': "High",
        #'coordinators': None,  # need to implement this!
        'course_of_action': {
            'version': '1.1.1',
            'title': 'Test Title',
            'description': 'Test Description',
            'short_description': "Test Short Description",
            'timestamp': '2015-03-06T14:35:23.375304+00:00',
        }
    }


class COAsRequestedTest(TypedListTestCase, unittest.TestCase):
    klass = incident._COAsRequested

    _full_dict = [
        COARequestedTest._full_dict,
    ]



class JournalEntryTest(EntityTestCase, unittest.TestCase):
    klass = history.JournalEntry

    _full_dict = {
        'value': 'hi',
        'author': 'Paul',
        'time': '2015-03-06T14:35:23.375304+00:00',
        'time_precision': 'hour'
    }


class HistoryItemTest(EntityTestCase, unittest.TestCase):
    klass = history.HistoryItem

    _full_dict = {
        'action_entry': COATakenTest._full_dict,
        'journal_entry': JournalEntryTest._full_dict
    }


class HistoryTest(EntityTestCase, unittest.TestCase):
    klass = history.History

    _full_dict = {
        'history_items': [
            HistoryItemTest._full_dict,
        ]
    }


class AttributedThreatActorsTest(EntityTestCase, unittest.TestCase):
    klass = incident.AttributedThreatActors

    _full_dict = {
        'scope': 'exclusive',
        'threat_actors': [
            related_test.RelatedThreatActorTests._full_dict,
        ]
    }


class RelatedIndicatorsTest(EntityTestCase, unittest.TestCase):
    klass = incident.RelatedIndicators

    _full_dict = {
        'scope': 'exclusive',
        'indicators': [
            related_test.RelatedIndicatorTests._full_dict,
        ]
    }


class LeveragedTTPsTest(EntityTestCase, unittest.TestCase):
    klass = incident.LeveragedTTPs

    _full_dict = {
        'scope': 'exclusive',
        'ttps': [
            related_test.RelatedTTPTests._full_dict,
        ]
    }


class ExternalIDsTest(TypedListTestCase, unittest.TestCase):
    klass = incident._ExternalIDs

    _full_dict = [
        {
            'source': 'foo',
            'value': '478392-feb3ca-98a9ef-984392742'
        },
        {
            'source': 'bar',
            'value': '478392-feb3ca-98a9ef-984392742'
        },
    ]


class VictimsTest(TypedListTestCase, unittest.TestCase):
    klass = incident._Victims

    _full_dict = [
        {'name': 'Spooderman'},
        {'name': 'Spooderman'}
    ]


class TimeTest(EntityTestCase, unittest.TestCase):
    klass = incident.Time

    _full_dict = {
            'containment_achieved': '2005-02-21T10:25:10.894398',
            'first_data_exfiltration': '2002-02-21T10:25:10.894398',
            'first_malicious_action': '2000-02-21T10:25:10.894398',
            'incident_closed': '2008-02-21T10:25:10.894398',
            'incident_discovery': '2003-02-21T10:25:10.894398',
            'incident_opened': '2004-02-21T10:25:10.894398',
            'incident_reported': '2007-02-21T10:25:10.894398',
            'initial_compromise': '2001-02-21T10:25:10.894398',
            'restoration_achieved': '2006-02-21T10:25:10.894398'
    }


class CategoriesTest(EntityTestCase, unittest.TestCase):
    klass = incident.IncidentCategories

    _full_dict = [
        {
            'value': vocabs.IncidentCategory.TERM_DENIAL_OF_SERVICE,
            'xsi:type': vocabs.IncidentCategory._XSI_TYPE
        },
    ]


class InformationSourcesTest(TypedListTestCase, unittest.TestCase):
    klass = incident._InformationSources

    _full_dict = [
        {
            'description': 'Test',
            'identity': {
                'name': 'Spooderman'
            }
        },
    ]


class TotalLossEstimationTest(EntityTestCase, unittest.TestCase):
    klass = impact_assessment.TotalLossEstimation

    _full_dict = {
        'actual_total_loss_estimation': {
            'amount': '50.45',
            'iso_currency_code': 'USD'
        },
        'initial_reported_total_loss_estimation': {
            'amount': '99.99',
            'iso_currency_code': 'USD'
        }
    }


class IndirectImpactSummaryTest(EntityTestCase, unittest.TestCase):
    klass = impact_assessment.IndirectImpactSummary

    _full_dict = {
        'brand_and_market_damage': {
            'value': 'No',
            'xsi:type': 'stixVocabs:SecurityCompromiseVocab-1.0'
        },
        'increased_operating_costs': {
            'value': 'No',
            'xsi:type': 'stixVocabs:SecurityCompromiseVocab-1.0'
        },
        'legal_and_regulatory_costs': {
            'value': 'Unknown',
            'xsi:type': 'stixVocabs:SecurityCompromiseVocab-1.0'
        },
        'loss_of_competitive_advantage': {
            'value': 'Yes',
            'xsi:type': 'stixVocabs:SecurityCompromiseVocab-1.0'
        }
    }


class DirectImpactSummaryTest(EntityTestCase, unittest.TestCase):
    klass = impact_assessment.DirectImpactSummary

    _full_dict = {
        'asset_losses': {
            'value': 'Minor',
            'xsi:type': 'stixVocabs:ImpactRatingVocab-1.0'
        },
        'business_mission_disruption': {
            'value': 'Major',
            'xsi:type': 'stixVocabs:ImpactRatingVocab-1.0'
        },
        'response_and_recovery_costs': {
            'value': 'Moderate',
            'xsi:type': 'stixVocabs:ImpactRatingVocab-1.0'
        }
    }


class EffectsTest(EntityTestCase, unittest.TestCase):
    klass = impact_assessment.Effects

    _full_dict = [
        {
            'value': 'User Data Loss',
            'xsi:type': 'stixVocabs:IncidentEffectVocab-1.0'
        },
        {
            'value': 'Data Breach or Compromise',
            'xsi:type': 'stixVocabs:IncidentEffectVocab-1.0'
        }
    ]


class ImpactAssessmentTest(EntityTestCase, unittest.TestCase):
    klass = incident.ImpactAssessment

    _full_dict = {
        'effects': EffectsTest._full_dict,
        'indirect_impact_summary': IndirectImpactSummaryTest._full_dict,
        'direct_impact_summary': DirectImpactSummaryTest._full_dict,
        'total_loss_estimation': TotalLossEstimationTest._full_dict,
        'impact_qualification': {
            'value': 'Catastrophic',
            'xsi:type': 'stixVocabs:ImpactQualificationVocab-1.0'
        },
    }


class AssetTypeTest(EntityTestCase, unittest.TestCase):
    klass = affected_asset.AssetType

    _full_dict = {
        'count_affected': 1,
        'value': 'Foobar'
    }


class NonPublicDataCompromisedTest(EntityTestCase, unittest.TestCase):
    klass = property_affected.NonPublicDataCompromised

    _full_dict = {
        'value': 'Yes',
        'data_encrypted': True
    }


class PropertyAffectedTest(EntityTestCase, unittest.TestCase):
    klass = property_affected.PropertyAffected

    _full_dict = {
        'description_of_effect': 'Foobar',
        'duration_of_availability_loss': {
            'value': 'Days',
            'xsi:type': 'stixVocabs:LossDurationVocab-1.0'
        },
        'non_public_data_compromised': NonPublicDataCompromisedTest._full_dict,
        'type_of_availability_loss': {
            'value': 'Loss',
            'xsi:type': 'stixVocabs:AvailabilityLossTypeVocab-1.1.1'
        }
    }


class NatureOfSecurityEffectTest(EntityTestCase, unittest.TestCase):
    klass = affected_asset.NatureOfSecurityEffect

    _full_dict = [
        PropertyAffectedTest._full_dict
    ]


class AffectedAssetTest(EntityTestCase, unittest.TestCase):
    klass = affected_asset.AffectedAsset

    _full_dict = {
        'type': AssetTypeTest._full_dict,
        'nature_of_security_effect': NatureOfSecurityEffectTest._full_dict,
        'ownership_class': {
            'value': 'Unknown',
            'xsi:type': 'stixVocabs:OwnershipClassVocab-1.0'
        },
        'location_class': {
            'value': 'Unknown',
            'xsi:type': 'stixVocabs:LocationClassVocab-1.0'
        },
        'management_class': {
            'value': 'Unknown',
            'xsi:type': 'stixVocabs:ManagementClassVocab-1.0'
        }
    }


class AffectedAssetsTest(EntityTestCase, unittest.TestCase):
    klass = incident.AffectedAssets

    _full_dict = [
        AffectedAssetTest._full_dict
    ]


class RelatedObservablesTest(EntityTestCase, unittest.TestCase):
    klass = incident.RelatedObservables

    _full_dict = {
        'scope': 'inclusive',
        'observables': [
            related_test.RelatedObservableTests._full_dict
        ]
    }


class RelatedIncidentsTests(EntityTestCase, unittest.TestCase):
    klass = incident.RelatedIncidents

    _full_dict = {
        'incidents': [
            related_test.RelatedIncidentTests._full_dict
        ]
    }


class IntendedEffectsTests(TypedListTestCase, unittest.TestCase):
    klass = incident._IntendedEffects

    _full_dict = [
        statement_test.StatementTests._full_dict
    ]


class DiscoveryMethodsTests(TypedListTestCase, unittest.TestCase):
    klass = incident.DiscoveryMethods

    _full_dict = [
        {
            'value': 'Unknown',
            'xsi:type': 'stixVocabs:LocationClassVocab-1.0'
        }
    ]


class IncidentTest(EntityTestCase, unittest.TestCase):
    klass = incident.Incident
    _full_dict = {
        'id': 'example:test-1',
        'version': '1.1.1',
        'timestamp': '2014-05-05T14:50:25.992383+00:00',
        'title': 'Test Title',
        'description': 'The Datacenter was broken into.',
        'short_description': 'Short Description Title',
        'handling': data_marking_test.MarkingTests._full_dict,
        'external_ids': ExternalIDsTest._full_dict,
        'attributed_threat_actors': AttributedThreatActorsTest._full_dict,
        'categories': CategoriesTest._full_dict,
        'coa_taken': COAsTakenTest._full_dict,
        'coa_requested': COAsRequestedTest._full_dict,
        'coordinators': InformationSourcesTest._full_dict,
        'impact_assessment': ImpactAssessmentTest._full_dict,
        'leveraged_ttps': LeveragedTTPsTest._full_dict,
        'related_indicators': RelatedIndicatorsTest._full_dict,
        'reporter': information_source_test.InformationSourceTests._full_dict,
        'responders': InformationSourcesTest._full_dict,
        'time': TimeTest._full_dict,
        'victims': VictimsTest._full_dict,
        'information_source': information_source_test.InformationSourceTests._full_dict,
        'security_compromise': {
            "value": "Suspected",
            "xsi:type":"stixVocabs:SecurityCompromiseVocab-1.0"
        },
        'status':  {
            "value": "New",
            "xsi:type": 'stixVocabs:IncidentStatusVocab-1.0'
        },
        'history': HistoryTest._full_dict,
        'affected_assets': AffectedAssetsTest._full_dict,
        'related_observables': RelatedObservablesTest._full_dict,
        'related_incidents': RelatedIncidentsTests._full_dict,
        'intended_effects': IntendedEffectsTests._full_dict,
        'discovery_methods': DiscoveryMethodsTests._full_dict,
        'confidence': confidence_test.ConfidenceTests._full_dict
    }

    def test_parse_category(self):
        incident = incident_binding.parseString(INCIDENT_CATEGORIES)
        self.assertTrue(incident is not None)
        self.assertEqual(2, len(incident.Categories.Category))

        categories = incident.Categories.Category
        self.assertEqual('Foo', categories[0].valueOf_)
        self.assertEqual('Bar', categories[1].valueOf_)

    def test_description_output(self):
        incident = incident_binding.IncidentType()

        assets = incident_binding.AffectedAssetsType()
        asset = incident_binding.AffectedAssetType()

        description = StructuredText("A Description")
        asset.Structured_Description = description.to_obj()

        assets.add_Affected_Asset(asset)
        incident.Affected_Assets = assets

        s = StringIO.StringIO()

        incident.export(s.write, 0, {'http://stix.mitre.org/Incident-1': 'incident'})
        xml = s.getvalue()
        self.assertTrue("A Description" in xml, "Description not exported")

    def test_add_related_observable(self):
        from cybox.core import Observable
        from stix.common.related import RelatedObservable

        i = self.klass()

        self.assertEqual(0, len(i.related_observables))
        i.add_related_observable(Observable())
        self.assertEqual(1, len(i.related_observables))


        related = RelatedObservable(Observable())
        i.add_related_observable(related)
        self.assertEqual(2, len(i.related_observables))

        # Test that this fails
        self.assertRaises(
            ValueError,
            i.add_related_observable,
            "THIS SHOULD FAIL"
        )

    def test_add_related_indicator(self):
        from stix.indicator import Indicator
        from stix.common.related import RelatedIndicator

        i = self.klass()

        self.assertEqual(0, len(i.related_indicators))
        i.add_related_indicator(Indicator())
        self.assertEqual(1, len(i.related_indicators))

        related = RelatedIndicator(Indicator())
        i.add_related_indicator(related)
        self.assertEqual(2, len(i.related_indicators))

        # Test that this fails
        self.assertRaises(
            ValueError,
            i.add_related_indicator,
            "THIS SHOULD FAIL"
        )



if __name__ == "__main__":
    unittest.main()
