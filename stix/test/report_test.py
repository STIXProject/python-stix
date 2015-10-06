# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix import report

from stix.test import EntityTestCase, data_marking_test
from stix.test.common import (kill_chains_test, information_source_test,
    structured_text_tests, related_test)


class HeaderTests(EntityTestCase, unittest.TestCase):
    klass = report.Header
    _full_dict = {
        'title': "A Title",
        'description': "A really, really long description",
        'short_description': 'A really, really short description',
        'handling': data_marking_test.MarkingTests._full_dict,
        'information_source': information_source_test.InformationSourceTests._full_dict,
        'intents': ["foo", "bar"]
    }

    def test_duplicate_package_intent(self):
        # Recreate https://github.com/STIXProject/python-stix/issues/63
        hdr = report.Header(intents=["Indicators - Watchlist"])
        self.assertEqual(1, len(hdr.intents))


class HeaderMultiDescTests(EntityTestCase, unittest.TestCase):
    klass = report.Header
    _full_dict = {
        'description': structured_text_tests.StructuredTextListTests._full_dict,
        'short_description': structured_text_tests.StructuredTextListTests._full_dict
    }


class CampaignsTests(EntityTestCase, unittest.TestCase):
    klass = report.Campaigns

    _full_dict = [
        {'idref': 'example:test-1'}
    ]


class COAsTests(EntityTestCase, unittest.TestCase):
    klass = report.CoursesOfAction

    _full_dict = [
        {'idref': 'example:test-1'}
    ]

class ExploitTargetsTests(EntityTestCase, unittest.TestCase):
    klass = report.ExploitTargets

    _full_dict = [
        {'idref': 'example:test-1'}
    ]

class IncidentsTests(EntityTestCase, unittest.TestCase):
    klass = report.Incidents

    _full_dict = [
        {'idref': 'example:test-1'}
    ]

class IndicatorsTests(EntityTestCase, unittest.TestCase):
    klass = report.Indicators

    _full_dict = [
        {'idref': 'example:test-1'}
    ]


class ThreatActorsTests(EntityTestCase, unittest.TestCase):
    klass = report.ThreatActors

    _full_dict = [
        {'idref': 'example:test-1'}
    ]


class TTPsTests(EntityTestCase, unittest.TestCase):
    klass = report.TTPs

    _full_dict = {
        'kill_chains': kill_chains_test.KillChainsTests._full_dict,
        'ttps': [
            {'idref': 'example:test-1'}
        ]
    }


class ReportTests(EntityTestCase, unittest.TestCase):
    klass = report.Report
    _full_dict = {
        'header': HeaderTests._full_dict,
        'campaigns': CampaignsTests._full_dict,
        'courses_of_action': COAsTests._full_dict,
        'exploit_targets': ExploitTargetsTests._full_dict,
        'incidents': IncidentsTests._full_dict,
        'indicators': IndicatorsTests._full_dict,
        'observables':  {
            'major_version': 2,
            'minor_version': 1,
            'update_version': 0,
            'observables': [
                {
                    'idref': "example:Observable-1"
                }
            ]
        },
        'threat_actors': ThreatActorsTests._full_dict,
        'ttps': TTPsTests._full_dict,
        'related_reports': related_test.RelatedReportsTests._full_dict,
        'version': "1.0"
    }


if __name__ == "__main__":
    unittest.main()
