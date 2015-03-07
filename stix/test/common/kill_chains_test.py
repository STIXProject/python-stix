# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase

from stix.common.kill_chains import (
    KillChain, KillChainPhase,  KillChainPhaseReference,
    KillChainPhasesReference, KillChains
)

class KillChainTests(EntityTestCase, unittest.TestCase):
    klass = KillChain
    _full_dict = {
        'definer': 'Myself',
        'kill_chain_phases': [
            {'name': 'Infect Machine'},
            {'name': 'Exfiltrate Data'}
        ],
       'name': 'Organization-specific Kill Chain'
    }


class KillChainsTests(EntityTestCase, unittest.TestCase):
    klass = KillChains
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
    klass = KillChainPhase
    _full_dict = {
        'name': 'Reconnaissance',
        'ordinality': 1,
        'phase_id': 'stix:TTP-af1016d6-a744-4ed7-ac91-00fe2272185a'
    }


class KillChainPhaseReferenceTests(EntityTestCase, unittest.TestCase):
    klass = KillChainPhaseReference

    _full_dict = {
        'kill_chain_id': 'stix:TTP-af3e707f-2fb9-49e5-8c37-14026ca0a5ff',
        'phase_id': 'stix:TTP-786ca8f9-2d9a-4213-b38e-399af4a2e5d6'
    }


class KillChainPhaseReferencesTests(EntityTestCase, unittest.TestCase):
    klass = KillChainPhasesReference

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


if __name__ == "__main__":
    unittest.main()
