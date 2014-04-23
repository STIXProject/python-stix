# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from StringIO import StringIO
import unittest

from stix.incident import Incident
import stix.bindings.incident as incident_binding
from cybox.common import StructuredText
from cybox.test import EntityTestCase

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


class IncidentTest(EntityTestCase, unittest.TestCase):
    klass = Incident
    _full_dict = {
        'attributed_threat_actors': {
            'scope': 'exclusive',
            'threat_actors': [
                {
                    'threat_actor': {
                        'description': 'A Threat Actor Description',
                        'id': 'example:threatactor-1',
                        'sophistications': [{'value': 'High'}],
                        'title': 'A Threat Actor',
                        'version': '1.1'
                    }
                }
            ]
        },
        'impact_assessment': {
            'direct_impact_summary': {
                'asset_losses' : "Minor",
                'business_mission_disruption' : "Major",
                'response_and_recovery_costs' : "Moderate"
            },
            'indirect_impact_summary': {
                'loss_of_competitive_advantage' : "Yes",
                'brand_and_market_damage' : "No",
                'increased_operating_costs' : "No",
                'legal_and_regulatory_costs' : "Unknown" 
            },
            'total_loss_estimation': {
                'initial_reported_total_loss_estimation' : {
                    'iso_currency_code' : "USD",
                    'amount' : "99.99"
                },
                'actual_total_loss_estimation' : {
                    'iso_currency_code' : "USD",
                    'amount' : "50.45"
                }
            },
            'impact_qualification': "Catastrophic",
            'effects': {
                'effects' : [
                    "User Data Loss",
                    "Data Breach or Compromise"
                    ]
            }
        },
        'categories': ['Unauthorized Access', 'Improper Usage'],
        'description': 'The Datacenter was broken into.',
        'related_indicators': {
            'indicators': [{
                'indicator': {
                    'description': 'An indicator containing a File observable with an associated hash',
                    'id': 'example:indicator-1ae45e9c-9b0b-11e3-ada0-28cfe912ced6',
                    'observable': {
                        'id': 'example:Observable-fdaa7cec-f8be-494d-b83f-575f6f018666',
                        'object': {
                            'id': 'example:File-ec52e6bc-2d7e-44e2-911b-468bb775a5c6',
                            'properties': {
                                'hashes': [
                                    {
                                        'simple_hash_value': u'4EC0027BEF4D7E1786A04D021FA8A67F',
                                        'type': u'MD5'
                                    }
                                ],
                                'xsi:type': 'FileObjectType'
                            }
                        }
                    },
                    'producer': {
                        'description': '',
                        'identity': {
                            'id': 'example:Identity-1ae603ab-9b0b-11e3-980e-28cfe912ced8',
                            'specification': {
                                'party_name': {
                                    'name_lines': [
                                        {'value': 'Foo'},
                                        {'value': 'Bar'}
                                    ],
                                    'person_names': [
                                        {'name_elements': [{'value': 'John Smith'}]},
                                        {'name_elements': [{'value': 'Jill Smith'}]}
                                    ]
                                }
                            },
                            'xsi:type': 'ciqIdentity:CIQIdentity3.0InstanceType'
                        },
                        'time': {'produced_time': '2014-02-21T10:16:14.947201'}
                    },
                    'title': 'File Hash Example',
                    'version': '2.1'
                }
            }],
            'scope': 'exclusive'
        },
        'leveraged_ttps': {
            'scope': "inclusive",
            'ttps': [
                {
                    'confidence': {'value': "High"},
                    'ttp': {'id': "example:TTP-1",
                            'version': "1.1"},
                }
            ],
        },
        'time': {
            'containment_achieved': '2005-02-21T10:25:10.894398',
            'first_data_exfiltration': '2002-02-21T10:25:10.894398',
            'first_malicious_action': '2000-02-21T10:25:10.894398',
            'incident_closed': '2008-02-21T10:25:10.894398',
            'incident_discovery': '2003-02-21T10:25:10.894398',
            'incident_opened': '2004-02-21T10:25:10.894398',
            'incident_reported': '2007-02-21T10:25:10.894398',
            'initial_compromise': '2001-02-21T10:25:10.894398',
            'restoration_achieved': '2006-02-21T10:25:10.894398'
        },
        'title': 'Datacenter Compromise',
        'version': '1.1',
        'victims': [
            {'name': 'John Smith'},
            {'id': 'example:Identity-1ae603ab-9b0b-11e3-980e-28cfe912ced6'}
        ],
        'reporter': {
            'description': "Mr. Evil's enemy",
            'identity': {
                'name': "Ms. Good",
            },
        },
        'responders': [{
            'description': "Mr. Evil's enemy",
            'identity': {
                'name': "Ms. Responder",
            },
        }],
        'coordinators': [{
            'description': "Mr. Evil's enemy",
            'identity': {
                'name': "Ms. Coordinator",
            },
        }],
        'external_ids': [
            {
                'value' : '478392-feb3ca-98a9ef-984392742',
                'source' : "some source"
            }
        ],
        'information_source': {
            'description': "Mr. Evil's enemy",
            'identity': {
                'name': "Ms. Good",
            },
        },
        'security_compromise': "Suspected"
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
        asset.set_Structured_Description(description.to_obj())

        assets.add_Affected_Asset(asset)
        incident.set_Affected_Assets(assets)

        s = StringIO()

        incident.export(s, 0, {'http://stix.mitre.org/Incident-1': 'incident'})
        xml = s.getvalue()
        self.assertTrue("A Description" in xml, "Description not exported")

if __name__ == "__main__":
    unittest.main()
