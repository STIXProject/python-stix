# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import (
    EntityTestCase, campaign_test, coa_test, exploit_target_test,
    incident_test, indicator_test, threat_actor_test, ttp_test
)
from stix.test.common import kill_chains_test

from . import stix_header_test

from stix import core
from stix.core import stix_package


class CampaignsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.Campaigns

    _full_dict = [
        campaign_test.CampaignTest._full_dict
    ]


class COAsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.CoursesOfAction

    _full_dict = [
        coa_test.COATests._full_dict
    ]

class ExploitTargetsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.ExploitTargets

    _full_dict = [
        exploit_target_test.ExploitTargetTests._full_dict
    ]

class IncidentsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.Incidents

    _full_dict = [
        incident_test.IncidentTest._full_dict
    ]

class IndicatorsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.Indicators

    _full_dict = [
        indicator_test.IndicatorTest._full_dict
    ]


class ThreatActorsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.ThreatActors

    _full_dict = [
        threat_actor_test.ThreatActorTests._full_dict
    ]

class TTPsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.TTPs

    _full_dict = {
        'kill_chains': kill_chains_test.KillChainsTests._full_dict,
        'ttps': [
            ttp_test.TTPTests._full_dict
        ]
    }


class STIXPackageTests(EntityTestCase, unittest.TestCase):
    klass = core.STIXPackage
    _full_dict = {
        'stix_header': stix_header_test.STIXHeaderTests._full_dict,
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
        'version': "1.1.1"
    }


if __name__ == "__main__":
    unittest.main()
