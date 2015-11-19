# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase, TypedListTestCase, assert_warnings
import stix.test.data_marking_test as data_marking_test
from stix.test.common import (
    confidence_test, information_source_test, statement_test, related_test,
    activity_test
)

from stix.test import assert_warnings
from stix.core import STIXPackage
import stix.campaign as campaign


class NamesTests(EntityTestCase, unittest.TestCase):
    klass = campaign.Names

    _full_dict = {
        'names': [
            "Dancing Hippos",
            "Crazy Squirrels",
            {
                'value': "Medium",
                'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'
            }
        ]
    }


class IntendedEffectsTests(TypedListTestCase, unittest.TestCase):
    klass = campaign.Campaign

    _partial_dict = [
        statement_test.StatementTests._full_dict
    ]
    
    _full_dict = {
        'intended_effects': _partial_dict,    
    }

class RelatedTTPsTest(EntityTestCase, unittest.TestCase):
    klass = campaign.RelatedTTPs

    _full_dict = {
        'scope': 'exclusive',
        'ttps': [
            related_test.RelatedTTPTests._full_dict,
        ]
    }


class RelatedIncidentsTests(EntityTestCase, unittest.TestCase):
    klass = campaign.RelatedIncidents

    _full_dict = {
        'incidents': [
            related_test.RelatedIncidentTests._full_dict
        ]
    }


class RelatedIndicatorsTests(EntityTestCase, unittest.TestCase):
    klass = campaign.RelatedIndicators

    _full_dict = {
        'indicators': [
            related_test.RelatedIndicatorTests._full_dict
        ]
    }

class AttributionTests(EntityTestCase, unittest.TestCase):
    klass = campaign.Attribution

    _full_dict = {
        'scope': 'exclusive',
        'threat_actors': [
            related_test.RelatedThreatActorTests._full_dict,
        ]
    }


class AttributionListTests(TypedListTestCase, unittest.TestCase):
    klass = campaign.Campaign

    _full_dict = { 'attribution': [
        AttributionTests._full_dict
    ] }


class AssociatedCampaignsTests(EntityTestCase, unittest.TestCase):
    klass = campaign.AssociatedCampaigns

    _full_dict = {
        'scope': 'inclusive',
        'campaigns': [
            related_test.RelatedCampaignTests._full_dict
        ]
    }


class ActivityTests(TypedListTestCase, unittest.TestCase):
    klass = campaign.Activity

    _full_dict = activity_test.ActivityTests._full_dict
    


class CampaignTest(EntityTestCase, unittest.TestCase):
    klass = campaign.Campaign
    _full_dict = {
        'id': "example:test-1",
        'timestamp': "2014-01-31T06:14:46",
        'version': '1.2',
        'title': 'Purple Elephant',
        'description': 'A pretty novice set of actors.',
        'short_description': 'novices',
        'names': NamesTests._full_dict,
        'intended_effects': IntendedEffectsTests._partial_dict,
        'status': {
            'value': "Ongoing",
            'xsi:type':'stixVocabs:CampaignStatusVocab-1.0'
        },
        'related_ttps': RelatedTTPsTest._full_dict,
        'related_incidents': RelatedIncidentsTests._full_dict,
        'related_indicators': RelatedIndicatorsTests._full_dict,
        'attribution': [AttributionTests._full_dict],
        'associated_campaigns': AssociatedCampaignsTests._full_dict,
        'confidence': confidence_test.ConfidenceTests._full_dict,
        'activity': [ActivityTests._full_dict],
        'information_source': information_source_test.InformationSourceTests._full_dict,
        'handling': data_marking_test.MarkingTests._full_dict,
        'related_packages': related_test.RelatedPackageRefsTests._full_dict
    }

    def test_add_description(self):
        o1 = self.klass()
        o2 = self.klass()

        o1.add_description("Test")
        o2.descriptions.add("Test")

        self.assertEqual(
            o1.descriptions.to_dict(),
            o2.descriptions.to_dict()
        )

    def test_add_short_description(self):
        o1 = self.klass()
        o2 = self.klass()

        o1.add_short_description("Test")
        o2.short_descriptions.add("Test")

        self.assertEqual(
            o1.short_descriptions.to_dict(),
            o2.short_descriptions.to_dict()
        )

    @assert_warnings
    def test_deprecated_related_packages(self):
        c = campaign.Campaign()
        c.related_packages.append(STIXPackage())

    @assert_warnings
    def test_deprecated_related_indicators(self):
        from stix.indicator import Indicator

        c = campaign.Campaign()
        c.related_indicators.append(Indicator())
        self.assertEqual(1, len(c.related_indicators))


if __name__ == "__main__":
    unittest.main()
