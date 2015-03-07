# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase, TypedListTestCase, data_marking_test
from stix.test.common import (
    confidence_test, information_source_test, related_test,identity_test
)

import stix.threat_actor as ta


class TypesTests(TypedListTestCase, unittest.TestCase):
    klass = ta._Types

    _full_dict = [
        {
            'value': {
                "value" : "Hacker",
                "xsi:type" : "stixVocabs:ThreatActorTypeVocab-1.0"
            }
        },
    ]


class MotivationsTests(TypedListTestCase, unittest.TestCase):
    klass = ta._Motivations

    _full_dict = [
         {
             'value': {
                 "value" : "Ego",
                 "xsi:type" : "stixVocabs:MotivationVocab-1.1"
             }
         },
    ]


class SophisticationTests(TypedListTestCase, unittest.TestCase):
    klass = ta._Sophistications

    _full_dict = [
         {
             'value': {
                 "value" : "Novice",
                 "xsi:type" : "stixVocabs:ThreatActorSophisticationVocab-1.0"
             }
         },
    ]


class IntendedEffectsTests(TypedListTestCase, unittest.TestCase):
    klass = ta._IntendedEffects

    _full_dict = [
        {
            'value': {
                "value" : "Destruction",
                "xsi:type" : "stixVocabs:IntendedEffectVocab-1.0"
            }
        }
    ]


class PlanningAndOperationalSupportTests(TypedListTestCase, unittest.TestCase):
    klass = ta._PlanningAndOperationalSupports

    _full_dict = [
        {
            'value': {
                "value" : "Data Exploitation",
                "xsi:type" : 'stixVocabs:PlanningAndOperationalSupportVocab-1.0.1'
            }
        },
    ]


class ObservedTTPsTests(EntityTestCase, unittest.TestCase):
    klass = ta.ObservedTTPs

    _full_dict = {
        'scope': 'inclusive',
        'ttps': [
            related_test.RelatedTTPTests._full_dict
        ]
    }


class AssocaitedCampaignsTests(EntityTestCase, unittest.TestCase):
    klass = ta.AssociatedCampaigns

    _full_dict = {
        'scope': 'inclusive',
        'campaigns': [
            related_test.RelatedCampaignTests._full_dict
        ]
    }


class AssociatedActorsTests(EntityTestCase, unittest.TestCase):
    klass = ta.AssociatedActors

    _full_dict = {
        'scope': 'inclusive',
        'threat_actors': [
            related_test.RelatedThreatActorTests._full_dict
        ]
    }


class ThreatActorTests(EntityTestCase, unittest.TestCase):
    klass = ta.ThreatActor
    _full_dict = {
        'id': 'example:ThreatActor-1',
        'timestamp': "2014-01-31T06:14:46",
        'version': '1.1',
        'title': "BadGuy1",
        'description': "This is a long description about a threat actor.",
        'short_description': "A bad guy",
        'identity': identity_test.IdentityTests._full_dict,
        'types': TypesTests._full_dict,
        'motivations': MotivationsTests._full_dict,
        'sophistications': SophisticationTests._full_dict,
        'intended_effects': IntendedEffectsTests._full_dict,
        'planning_and_operational_supports': PlanningAndOperationalSupportTests._full_dict,
        'observed_ttps': ObservedTTPsTests._full_dict,
        'associated_campaigns': AssocaitedCampaignsTests._full_dict,
        'associated_actors': AssociatedActorsTests._full_dict,
        'handling': data_marking_test.MarkingTests._full_dict,
        'confidence': confidence_test.ConfidenceTests._full_dict,
        'information_source': information_source_test.InformationSourceTests._full_dict,
        'related_packages': related_test.RelatedPackageRefsTests._full_dict
    }


if __name__ == "__main__":
    unittest.main()
