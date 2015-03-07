# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase, data_marking_test
from stix.test.common import related_test, identity_test

import stix.ttp as ttp
from stix.ttp import (
    resource, infrastructure, exploit_targets, malware_instance, exploit,
    attack_pattern, behavior
)


class ExploitTargetsTests(EntityTestCase, unittest.TestCase):
    klass = exploit_targets.ExploitTargets

    _full_dict = {
        'scope': 'inclusive',
        'exploit_targets': [
            related_test.RelatedExploitTargetTests._full_dict
        ]
    }


class PersonasTests(EntityTestCase, unittest.TestCase):
    klass = resource.Personas

    _full_dict = [
        identity_test.IdentityTests._full_dict
    ]


class InfrastructureTests(EntityTestCase, unittest.TestCase):
    klass = infrastructure.Infrastructure

    _full_dict = {
        'title': 'Title',
        'description': 'Description',
        'short_description': 'Short Description',
        'types': ['foo', 'bar'],
        'observable_characterization':  {
            'major_version': 2,
            'minor_version': 1,
            'update_version': 0,
            'observables': [
                {
                    'idref': "example:Observable-1"
                }
            ]
        }
    }


class ResourcesTests(EntityTestCase, unittest.TestCase):
    klass = ttp.Resource

    _full_dict = {
        'personas': PersonasTests._full_dict,
        'tools':  [
            {
                'title': "Tool"
            }
        ],
        'infrastructure': InfrastructureTests._full_dict
    }


class MalwareInstanceTests(EntityTestCase, unittest.TestCase):
    klass = malware_instance.MalwareInstance

    _full_dict =  _full_dict = {
        'id': 'example:test-1',
        'title': 'Title',
        'description': 'Description',
        'short_description': 'Short Description',
        'types': ['foo', 'bar']
    }


class MalwareInstancesTests(EntityTestCase, unittest.TestCase):
    klass = behavior.MalwareInstances

    _full_dict = [
        MalwareInstanceTests._full_dict
    ]


class ExploitTests(EntityTestCase, unittest.TestCase):
    klass = exploit.Exploit

    _full_dict = {
        'id': 'example:test-1',
        'title': 'Title',
        'description': 'Description',
        'short_description': 'Short Description',
    }


class ExploitsTests(EntityTestCase, unittest.TestCase):
    klass = behavior.Exploits

    _full_dict = [
        ExploitTests._full_dict
    ]


class AttackPatternTests(EntityTestCase, unittest.TestCase):
    klass = attack_pattern.AttackPattern

    _full_dict = {
        'id': 'example:test-1',
        'title': 'Title',
        'description': 'Description',
        'short_description': 'Short Description',
        'capec_id': '12345'
    }


class AttackPatternsTests(EntityTestCase, unittest.TestCase):
    klass = behavior.AttackPatterns

    _full_dict = [
        AttackPatternTests._full_dict
    ]


class BehaviorTests(EntityTestCase, unittest.TestCase):
    klass = behavior.Behavior

    _full_dict = {
        'malware_instances': MalwareInstancesTests._full_dict,
        'exploits': ExploitsTests._full_dict,
        'attack_patterns': AttackPatternsTests._full_dict
    }

class TTPTests(EntityTestCase, unittest.TestCase):
    klass = ttp.TTP
    _full_dict = {
        'id': 'example:ttp-1',
        'version': '1.1',
        'title': "TTP1",
        'description': "This is a long description about a ttp",
        'short_description': "a TTP",
        'resources': ResourcesTests._full_dict,
        'handling': data_marking_test.MarkingTests._full_dict,
        'exploit_targets': ExploitTargetsTests._full_dict,
        'behavior': BehaviorTests._full_dict
    }

if __name__ == "__main__":
    unittest.main()
