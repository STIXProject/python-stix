# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import copy
import unittest

from mixbox.vendor.six import BytesIO

from stix.test import EntityTestCase, assert_warnings
from stix.test import report_test
from stix.test.common import kill_chains_test, related_test

from . import stix_header_test

from stix import core
from stix.core import stix_package
from stix.campaign import Campaign
from stix.coa import CourseOfAction
from stix.exploit_target import ExploitTarget
from stix.indicator import Indicator
from stix.incident import Incident
from stix.threat_actor import ThreatActor
from stix.ttp import TTP
from stix.utils import silence_warnings, now


class CampaignsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.Campaigns

    _full_dict = [
        {'idref': 'example:test-1'}
    ]


class COAsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.CoursesOfAction

    _full_dict = [
        {'idref': 'example:test-1'}
    ]

class ExploitTargetsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.ExploitTargets

    _full_dict = [
        {'idref': 'example:test-1'}
    ]

class IncidentsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.Incidents

    _full_dict = [
        {'idref': 'example:test-1'}
    ]

class IndicatorsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.Indicators

    _full_dict = [
        {'idref': 'example:test-1'}
    ]


class ThreatActorsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.ThreatActors

    _full_dict = [
        {'idref': 'example:test-1'}
    ]

class TTPsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.TTPs

    _full_dict = {
        'kill_chains': kill_chains_test.KillChainsTests._full_dict,
        'ttps': [
            {'idref': 'example:test-1'}
        ]
    }


class ReportsTests(EntityTestCase, unittest.TestCase):
    klass = stix_package.Reports

    _full_dict = [
        report_test.ReportTests._full_dict
    ]


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
        'related_packages': related_test.RelatedPackagesTests._full_dict,
        'reports': ReportsTests._full_dict,
        'version': "1.2"
    }


    @silence_warnings
    def test_deepcopy(self):
        """Test copy.deepcopy() against parsed document.

        Previous versions of python-stix would cause an exception with
        copy.deepcopy() when applied to a parsed STIX component which contained
        timestamp information.

        This was due to the lack of a __reduce__ function defined on the
        bindings._FixedTZOffset class.

        """
        package = core.STIXPackage.from_xml(
            BytesIO(
                core.STIXPackage().to_xml()
            )
        )

        copied = copy.deepcopy(package)
        self.assertEqual(package.timestamp, copied.timestamp)

    @assert_warnings
    def test_deprecated_idref(self):
        p = core.STIXPackage()
        p.idref = "test"
        self.assertEqual(p.idref, "test")

    @assert_warnings
    def test_deprecated_timestamp(self):
        p = core.STIXPackage()
        ts = now()
        p.timestamp = ts
        self.assertEqual(ts, p.timestamp)

    @assert_warnings
    def test_campaign_idref_deprecation(self):
        package = core.STIXPackage()
        package.add(Campaign(idref='test-idref-dep'))

    @assert_warnings
    def test_coa_idref_deprecation(self):
        package = core.STIXPackage()
        package.add(CourseOfAction(idref='test-idref-dep'))

    @assert_warnings
    def test_et_idref_deprecation(self):
        package = core.STIXPackage()
        package.add(ExploitTarget(idref='test-idref-dep'))

    @assert_warnings
    def test_incident_idref_deprecation(self):
        package = core.STIXPackage()
        package.add(Incident(idref='test-idref-dep'))

    @assert_warnings
    def test_indicator_idref_deprecation(self):
        package = core.STIXPackage()
        package.add(Indicator(idref='test-idref-dep'))

    @assert_warnings
    def test_ta_idref_deprecation(self):
        package = core.STIXPackage()
        package.add(ThreatActor(idref='test-idref-dep'))

    @assert_warnings
    def test_ttp_idref_deprecation(self):
        package = core.STIXPackage()
        package.add(TTP(idref='test-idref-dep'))

    @assert_warnings
    def test_related_package_idref_deprecation(self):
        package = core.STIXPackage()
        package.add_related_package(core.STIXPackage(idref='foo'))


if __name__ == "__main__":
    unittest.main()
