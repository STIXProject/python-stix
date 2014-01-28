# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

import stix.bindings.incident as incident_binding


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


class IncidentTest(unittest.TestCase):

    def test_parse_category(self):
        incident = incident_binding.parseString(INCIDENT_CATEGORIES)
        self.assertTrue(incident is not None)
        self.assertEqual(2, len(incident.Categories.Category))

        categories = incident.Categories.Category
        self.assertEqual('Foo', categories[0].valueOf_)
        self.assertEqual('Bar', categories[1].valueOf_)

if __name__ == "__main__":
    unittest.main()
