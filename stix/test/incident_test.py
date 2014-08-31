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
'attributed_threat_actors': {'scope': 'exclusive',
                             'threat_actors': [{'threat_actor': {'description': 'A Threat Actor Description',
                                                                  'id': 'example:threatactor-1',
                                                                  'sophistications': [{'value': {"value" : "Novice", 
                                                                                                 "xsi:type" : "stixVocabs:ThreatActorSophisticationVocab-1.0"}}],
                                                                  'title': 'A Threat Actor',
                                                                  'version': '1.1.test'}}]},
'categories': [{'value': 'Unauthorized Access',
                 'xsi:type': 'stixVocabs:IncidentCategoryVocab-1.0'},
                {'value': 'Improper Usage',
                 'xsi:type': 'stixVocabs:IncidentCategoryVocab-1.0'}],
'coa_taken': [{'course_of_action': {'timestamp': '2014-05-05T14:50:25.992383+00:00', 'version': '1.1', 'id': 'example:coa-74e50620-7536-4fcd-94db-a6889f75e098'}},
              {'course_of_action': {'timestamp': '2014-05-05T14:50:25.992384+00:00', 'version': '1.1', 'id': 'example:coa-74e50620-7536-4fcd-94db-a6889f75e099'}}],
'coordinators': [{'description': "Mr. Evil's enemy",
                   'identity': {'name': 'Ms. Coordinator'}}],
'description': 'The Datacenter was broken into.',
'external_ids': [{'source': 'some source',
                   'value': '478392-feb3ca-98a9ef-984392742'}],
'impact_assessment': {'direct_impact_summary': {'asset_losses': {'value': 'Minor',
                                                                  'xsi:type': 'stixVocabs:ImpactRatingVocab-1.0'},
                                                 'business_mission_disruption': {'value': 'Major',
                                                                                 'xsi:type': 'stixVocabs:ImpactRatingVocab-1.0'},
                                                 'response_and_recovery_costs': {'value': 'Moderate',
                                                                                 'xsi:type': 'stixVocabs:ImpactRatingVocab-1.0'}},
                       'effects': [{'value': 'User Data Loss',
                                                'xsi:type': 'stixVocabs:IncidentEffectVocab-1.0'},
                                               {'value': 'Data Breach or Compromise',
                                                'xsi:type': 'stixVocabs:IncidentEffectVocab-1.0'}],
                       'impact_qualification': {'value': 'Catastrophic',
                                                'xsi:type': 'stixVocabs:ImpactQualificationVocab-1.0'},
                       'indirect_impact_summary': {'brand_and_market_damage': {'value': 'No',
                                                                               'xsi:type': 'stixVocabs:SecurityCompromiseVocab-1.0'},
                                                   'increased_operating_costs': {'value': 'No',
                                                                                 'xsi:type': 'stixVocabs:SecurityCompromiseVocab-1.0'},
                                                   'legal_and_regulatory_costs': {'value': 'Unknown',
                                                                                  'xsi:type': 'stixVocabs:SecurityCompromiseVocab-1.0'},
                                                   'loss_of_competitive_advantage': {'value': 'Yes',
                                                                                     'xsi:type': 'stixVocabs:SecurityCompromiseVocab-1.0'}},
                       'total_loss_estimation': {'actual_total_loss_estimation': {'amount': '50.45',
                                                                                  'iso_currency_code': 'USD'},
                                                 'initial_reported_total_loss_estimation': {'amount': '99.99',
                                                                                            'iso_currency_code': 'USD'}}},
 'leveraged_ttps': {'scope': 'inclusive',
                    'ttps': [{'confidence': {'value': {'value': 'Medium',
                                                       'xsi:type': 'stixVocabs:HighMediumLowVocab-1.0'}},
                              'ttp': {'id': 'example:TTP-1',
                                      'version': '1.1.test'}}]},
 'related_indicators': {'indicators': [{'indicator': {'description': 'An indicator containing a File observable with an associated hash',
                                                      'id': 'example:indicator-1ae45e9c-9b0b-11e3-ada0-28cfe912ced6',
                                                      'observable': {'id': 'example:Observable-fdaa7cec-f8be-494d-b83f-575f6f018666',
                                                                     'object': {'id': 'example:File-ec52e6bc-2d7e-44e2-911b-468bb775a5c6',
                                                                                'properties': {'hashes': [{'simple_hash_value': u'4EC0027BEF4D7E1786A04D021FA8A67F',
                                                                                                           'type': u'MD5'}],
                                                                                               'xsi:type': 'FileObjectType'}}},
                                                      'producer': {'description': '',
                                                                   'identity': {'id': 'example:Identity-1ae603ab-9b0b-11e3-980e-28cfe912ced8',
                                                                                'specification': {'party_name': {'name_lines': [{'value': 'Foo'},
                                                                                                                                {'value': 'Bar'}],
                                                                                                                 'person_names': [{'name_elements': [{'value': 'John Smith'}]},
                                                                                                                                  {'name_elements': [{'value': 'Jill Smith'}]}]}},
                                                                                'xsi:type': 'ciqIdentity:CIQIdentity3.0InstanceType'},
                                                                   'time': {'produced_time': '2014-02-21T10:16:14.947201'}},
                                                      'title': 'File Hash Example',
                                                      'version': '2.1.1.test'}}],
                        'scope': 'exclusive'},
 'reporter': {'description': "Mr. Evil's enemy",
              'identity': {'name': 'Ms. Good'}},
 'responders': [{'description': "Mr. Evil's enemy",
                 'identity': {'name': 'Ms. Responder'}}],
 'time': {'containment_achieved': '2005-02-21T10:25:10.894398',
          'first_data_exfiltration': '2002-02-21T10:25:10.894398',
          'first_malicious_action': '2000-02-21T10:25:10.894398',
          'incident_closed': '2008-02-21T10:25:10.894398',
          'incident_discovery': '2003-02-21T10:25:10.894398',
          'incident_opened': '2004-02-21T10:25:10.894398',
          'incident_reported': '2007-02-21T10:25:10.894398',
          'initial_compromise': '2001-02-21T10:25:10.894398',
          'restoration_achieved': '2006-02-21T10:25:10.894398'},
 'title': 'Datacenter Compromise',
 'version': '1.1.test',
 'victims': [{'name': 'John Smith'},
             {'id': 'example:Identity-1ae603ab-9b0b-11e3-980e-28cfe912ced6'}],
 'information_source': {
              'description': "Mr. Evil's enemy",
              'identity': {
                  'name': "Ms. Good",
              },
          },
'security_compromise': {"value": "Suspected", "xsi:type":"stixVocabs:SecurityCompromiseVocab-1.0"},
'history': {'history_items':[{'journal_entry': {'value': 'hi',
                                                'author': 'Paul'}}]}
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
