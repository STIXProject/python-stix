import unittest

from cybox.test import EntityTestCase

from stix.core import STIXPackage


class STIXPackageTests(EntityTestCase, unittest.TestCase):
    klass = STIXPackage
    _full_dict = {
        'stix_header': {
            'title': "A Title",
            'description': "A really, really long description",
        },
        'ttps': {
            'ttps': [
            {
                'title': "Foo",
                'version': "1.1"
            },
            ]
        },
        'exploit_targets': [
        {
            'id': 'example:ExploitTarget-1',
            'version': '1.1',
            'title': "ExploitTarget1",
            'description': "This is a long description about an ExploitTarget",
            'short_description': "an ExploitTarget",
            'information_source': {
                'description': "Mr. Evil's enemy",
                'identity': {
                    'name': "Ms. Good",
                },
            },
            'handling': [
            {
                'marking_structure': [{
                    'marking_model_name': 'TLP',
                    'color': "RED",
                    'xsi:type': "tlpMarking:TLPMarkingStructureType",
                }]
            }
            ]
        }
        ],
        'campaigns': [
            {
                    'id': "example:Campaign-341",
                    'idref': 'example:Campaign-344',
                    'timestamp': "2014-01-31T06:14:46",
                    'version': '1.1',
                    'title': 'Purple Elephant',
                    'description': 'A pretty novice set of actors.',
                    'short_description': 'novices',
                    'names': {
                        'names': ["Dancing Hippos", "Crazy Squirrels"],
                    },
                    'intended_effect': [
                        {
                            'timestamp': "2014-03-11T06:24:26",
                            'value': "Doing bad stuff",
                        },
                        {
                            'timestamp': "2014-03-21T06:24:26",
                            'value': "Doing really bad stuff",
                        }
                    ],
                    'status': "Ongoing",
                    'related_ttps': {
                        'scope': "exclusive",
                        'ttps': [
                            {
                                'confidence': {'value': "High"},
                                'ttp': {'title': "Stealth", 'version': "1.1"},
                            }
                        ]
                    },
                    'related_incidents': {
                        'scope': "inclusive",
                        'incidents': [
                            {
                                'confidence': {'value': "Low"},
                                'incident': {'idref': "example:Incident-2",
                                             'version': "1.1"},
                            }
                        ]
                    },
                    'related_indicators': {
                        'scope': "inclusive",
                        'indicators': [
                            {
                                'confidence': {'value': "Low"},
                                'indicator': {'idref': "example:Indicator-77",
                                              'version': "2.1"},
                            }
                        ]
                    },
                    'attribution': [{
                        'scope': "inclusive",
                        'threat_actors': [
                            {
                                'confidence': {'value': "Low"},
                                'threat_actor': {'title': "Campaign Actor #1",
                                                 'version': "1.1"},
                            },
                            {
                                'threat_actor': {'idref': "example:ThreatActor-111",
                                                 'version': "1.1"},
                            },
                        ],
                    }],
                    'associated_campaigns': {
                        'scope': "inclusive",
                        'campaigns': [
                            {
                                'confidence': {'value': "High"},
                                'information_source': {'description': "Threat Feed"},
                                'campaign': {'title': "Baby Elephant", 'version': "1.1"},
                            }
                        ],
                    },
                    'confidence': {"value": "Low"},
                    'activity': [
                            {
                                'date_time': "2012-01-01T08:45:31",
                                'description': "The first bad thing"
                            },
                            {
                                'date_time': "2012-01-02T08:45:31",
                                'description': "Another bad thing"
                            },
                    ],
                    'information_source': {
                        'description': "A former member of the campaign.",
                        'identity': {
                            'name': "Mr. D. Fector",
                        },
                    },
                    'handling': [
                        {
                            'marking_structure': [{
                                'marking_model_name': 'TLP',
                                'color': "RED",
                                'xsi:type': "tlpMarking:TLPMarkingStructureType",
                            }]
                        }
                    ],
                    'related_packages': {
                        'packages': [
                            {'idref': "example:Package-AB", 'relationship': "Parent"},
                            {'idref': "example:Package-CD", 'relationship': "Child"}
                        ]
                    }
                }
        ],
        'courses_of_action': [
        {
            'id': 'example:coa-1',
            'idref': 'example:coa-2',
            'version': '1.1',
            'timestamp': "2014-03-20T04:35:12",
            'title': "COA1",
            'description': "This is a long description about a course of action",
            'short_description': "a COA",
            'stage': "Remedy",
            'type': "Redirection",
            'cost': {
                'value': "100"
            },
            'efficacy': {
                'value': "Half"
            },
            'impact': {
                'value': "Large"
            },
            'information_source': {
                'description': "Mr. Evil's enemy",
                'identity': {
                    'name': "Ms. Good",
                },
            },
            'handling': [
            {
                'marking_structure': [{
                    'marking_model_name': 'TLP',
                    'color': "GREEN",
                    'xsi:type': "tlpMarking:TLPMarkingStructureType",
                }]
            }
            ]
        }
        ],
        'version': "1.1"
    }


if __name__ == "__main__":
    unittest.main()
