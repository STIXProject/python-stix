# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
from mixbox.vendor.six import StringIO, text_type

from stix.threat_actor import ThreatActor
import stix.extensions.identity.ciq_identity_3_0 as ciq
from stix.test import EntityTestCase
from stix.core import STIXPackage


class CIQIdentity3_0InstanceTests(EntityTestCase, unittest.TestCase):
    klass = ciq.CIQIdentity3_0Instance
    _full_dict = {
        'id': 'example:ciqidentity-1',
        'name': 'John Smith',
        'roles': ['Programmer', 'Analyst'],
        'specification': {
            'party_name': {
                'name_lines': [
                    {'value': 'Foo'},
                    {'value': 'Bar'}
                ],
                'organisation_names': [
                    {
                        'name_elements': [
                            {
                                'element_type': 'FullName',
                                'value': 'Foo Inc.'
                            }
                        ],
                        'subdivision_names': [
                            {
                                'type': 'Department',
                                'value': 'InfoSec'
                            }
                        ]
                    }
                ],
                'person_names': [
                    {
                        'name_elements': [
                            {'value': 'John Smith'}
                        ]
                    },
                    {
                        'name_elements': [
                            {'value': 'Jill Smith'}
                        ]
                    }
                ]
            },
            'organisation_info': {
               'industry_type': 'test industry'
            },
            'languages': [
                {'value': 'test language'}
            ],
            'addresses': [
                {
                    'free_text_address': {
                        'address_lines': ['1234 Example Lane.']
                    },
                    'country': {
                        'name_elements': [
                            {'value': 'name 1'},
                            {'value': 'name 2'}
                        ]
                    },
                    'administrative_area': {
                        'name_elements': [
                            {'value': 'admin area name 1'},
                            {'value': 'admin area name 2'}
                        ]
                    }
                }
            ],
            'electronic_address_identifiers': [
                {
                    'type': 'EMAIL',
                    'value': 'an eai v'
                }
            ],
            'free_text_lines': [
                {
                    'type': 'ftl type',
                    'value': 'ftl value'
                }
            ],
            'contact_numbers': [
                {
                    'communication_media_type': 'Fax',
                    'contact_number_elements': [
                        {
                            'value': 'a contact number',
                            'type': 'Pin'
                        }
                    ]
                }
            ],
            'nationalities': [
                {
                    'name_elements': [
                        {'value': 'name 1'},
                        {'value': 'name 2'}
                    ]
                }
            ]
        },
        'xsi:type': 'ciqIdentity:CIQIdentity3.0InstanceType'
    }


class IdentityInThreatActorTests(EntityTestCase, unittest.TestCase):
    klass = ThreatActor
    _full_dict = {
        "id": "example:threatactor-c96266cf-ccb3-43f3-b44e-26dbd66273e5",
        "identity": {
            "specification": {
                "addresses": [
                    {
                        "administrative_area": {
                            "name_elements": [{"value": "California"}
                            ]
                        },
                        "country": {
                            "name_elements": [{"value": "United States"}]
                        }
                    }
                ],
                "electronic_address_identifiers": [
                    {"value": "disco-team@stealthemail.com"},
                    {"value": "facebook.com/thediscoteam"},
                    {"value": "twitter.com/realdiscoteam"}
                ],
                "languages": [{"value": "Spanish"}],
                "party_name": {
                    "organisation_names": [
                        {
                            "name_elements": [{"value": "Disco Tean"}],
                            "type": "CommonUse"
                        },
                        {
                            "name_elements": [{"value": "Equipo del Discoteca"}],
                            "type": "UnofficialName"
                        }
                    ]
                }
            },
            "xsi:type": "ciqIdentity:CIQIdentity3.0InstanceType"
        },
        "timestamp": "2016-10-04T19:43:57.382126+00:00",
        "title": "Disco Team Threat Actor Group"
    }

    def test_identity_from_xml(self):
        obj = self.klass.from_dict(self._full_dict)
        sp = STIXPackage()
        sp.add(obj)
        s = StringIO(sp.to_xml())
        pkg = STIXPackage.from_xml(s)
        self.assertTrue("CIQIdentity3.0InstanceType" in text_type(pkg.to_xml()))


if __name__ == "__main__":
    unittest.main()
