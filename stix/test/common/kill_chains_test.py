# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase
from stix.common import kill_chains


class KillChainTests(EntityTestCase, unittest.TestCase):
    klass = kill_chains.KillChain
    _full_dict = {
        'definer': 'Myself',
        'kill_chain_phases': [
            {'name': 'Infect Machine'},
            {'name': 'Exfiltrate Data'}
        ],
       'name': 'Organization-specific Kill Chain'
    }

    def test_equal(self):
        chain1 = kill_chains.KillChain(id_="test", name="foo", definer="bar", reference="foobar.com")
        chain2 = kill_chains.KillChain(id_="test", name="foo", definer="bar", reference="foobar.com")

        self.assertEqual(chain1, chain2)

        chain1.kill_chain_phases.append(kill_chains.KillChainPhase(phase_id="test"))
        chain2.kill_chain_phases.append(kill_chains.KillChainPhase(phase_id="test"))

        self.assertEqual(chain1, chain2)

    def test_not_equal(self):
        chain1 = kill_chains.KillChain(id_="test", name="foo", definer="bar", reference="foobar.com")
        chain2 = kill_chains.KillChain(id_="TEST", name="FOO", definer="BAR", reference="FOOBAR.ORG")

        self.assertNotEqual(chain1, chain2)


class KillChainsTests(EntityTestCase, unittest.TestCase):
    klass = kill_chains.KillChains
    _full_dict = {
        'kill_chains': [
            {
                'name': 'Organization-specific Kill Chain',
                'definer': 'Myself',
                'kill_chain_phases': [
                    {'name': 'Infect Machine'},
                    {'name': 'Exfiltrate Data'}
                ],
            },
            {
                'name': 'Another organization-specific Kill Chain',
                'definer': 'Yourself',
                'kill_chain_phases': [
                    {'name': 'Defect Machine'},
                    {'name': 'Import Data'}
                ],
            },

        ]
    }


class KillChainPhaseTests(EntityTestCase, unittest.TestCase):
    klass = kill_chains.KillChainPhase
    _full_dict = {
        'name': 'Reconnaissance',
        'ordinality': 1,
        'phase_id': 'stix:test-1'
    }

    def test_equal(self):
        phase1 = kill_chains.KillChainPhase(phase_id='stix:test-1', ordinality=1, name='Reconnaissance')
        phase2 = kill_chains.KillChainPhase(phase_id='stix:test-1', ordinality=1, name='Reconnaissance')
        self.assertEqual(phase1, phase2)

        phase1 = kill_chains.KillChainPhase.from_dict(phase1.to_dict())
        phase2 = kill_chains.KillChainPhase.from_dict(phase2.to_dict())
        self.assertEqual(phase1, phase2)

    def test_not_equal(self):
        phase1 = kill_chains.KillChainPhase(phase_id='stix:test-1', ordinality=1, name='Reconnaissance')
        phase2 = kill_chains.KillChainPhase(phase_id='stix:test-2', ordinality=2, name='Weaponize')

        self.assertNotEqual(phase1, phase2)


class KillChainPhaseReferenceTests(EntityTestCase, unittest.TestCase):
    klass = kill_chains.KillChainPhaseReference

    _full_dict = {
        'kill_chain_id': 'stix:TTP-af3e707f-2fb9-49e5-8c37-14026ca0a5ff',
        'phase_id': 'stix:TTP-786ca8f9-2d9a-4213-b38e-399af4a2e5d6'
    }


class KillChainPhasesReferenceTests(EntityTestCase, unittest.TestCase):
    klass = kill_chains.KillChainPhasesReference

    _full_dict = {
        'kill_chain_phases': [
            {
                'kill_chain_id': 'stix:TTP-af3e707f-2fb9-49e5-8c37-14026ca0a5ff',
                'phase_id': 'stix:TTP-786ca8f9-2d9a-4213-b38e-399af4a2e5d6'
            },
            {
                'kill_chain_id': 'stix:TTP-af3e707f-2fb9-49e5-8c37-14026ca0a5ff',
                'phase_id': 'stix:TTP-786ca8f9-2d9a-4213-b38e-399af4a2e5d6'
            },
        ]
    }

    def test_add_phase(self):
        phase = kill_chains.PHASE_DELIVERY
        refs = kill_chains.KillChainPhasesReference()
        refs.append(phase)

        self.assertTrue(isinstance(refs[0], kill_chains.KillChainPhaseReference))
        self.assertTrue(refs[0].phase_id, kill_chains.PHASE_DELIVERY.phase_id)

if __name__ == "__main__":
    unittest.main()
