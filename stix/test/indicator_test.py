# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.indicator import Indicator
from stix.test import EntityTestCase, round_trip, round_trip_dict

class IndicatorTest(EntityTestCase, unittest.TestCase):
    klass = Indicator
    _full_dict = {
        'id': 'example:test-1',
        # no idref because we can't have both an id and idref
    }

    _base_dict = {
        'version': '2.1.1',
        'negate': True,
        'title': 'File Hash Example',
        'description': 'An indicator containing a File observable with an associated hash',
        'short_description': "A short description",
        'timestamp': '2015-03-06T14:35:23.375304+00:00',
    }

    def test_base(self):
        self._test_partial_dict(self._base_dict)


    def test_negate(self):
        d = dict(self._base_dict.items())
        d['negate'] = False

        d2 = self.klass.from_dict(d).to_dict()
        self.assertTrue('negate' not in d2)


    def test_indicator_types(self):
        d = {
            'indicator_types': [
                {
                    'value': 'C2',
                    'xsi:type': 'stixVocabs:IndicatorTypeVocab-1.1'
                },
                {
                    'value': 'IP Watchlist',
                    'xsi:type': 'stixVocabs:IndicatorTypeVocab-1.1'
                }
            ]
        }

        self._test_partial_dict(d)

    def test_alternative_ids(self):
        d = {
            'alternative_id': [
                "test 1",
                "not a test 2"
            ],
        }

        self._test_partial_dict(d)

    def test_valid_time_positions(self):
        d =  {
            'valid_time_positions': [
                {
                    'start_time': {'value': '2013-08-22T01:23:45', 'precision':'minute'},
                    'end_time': {'value': '2013-09-22T01:34:56', 'precision':'minute'}
                },
                {
                    'start_time': {'value': '2014-08-22T01:23:45', 'precision':'minute'},
                    'end_time': {'value': '2014-09-22T01:34:56', 'precision':'minute'}
                }
            ]
        }

        self._test_partial_dict(d)

    def test_observable(self):
        d = {
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
            }
        }

        self._test_partial_dict(d)

    def test_composite_indicator_expression(self):
        d = {
            'composite_indicator_expression': {
                'operator': 'AND',
                'indicators': [
                    {'idref': 'example:foo-1'},
                    {'idref': 'example:foo-2'},
                ]
            }
        }

        self._test_partial_dict(d)

    def test_indicated_ttps(self):
        d = {
            'indicated_ttps': [
                {
                    'confidence': {
                        'value': {
                            'value': 'Medium',
                            'xsi:type': 'stixVocabs:HighMediumLowVocab-1.0'}
                    },
                    'ttp': {
                        'idref': 'example:TTP-1'
                    }
                },
                {
                    'confidence': {
                        'value': {
                            'value': 'Medium',
                            'xsi:type': 'stixVocabs:HighMediumLowVocab-1.0'}
                    },
                    'ttp': {
                        'idref': 'example:TTP-2'
                    }
                },
            ],
        }

        self._test_partial_dict(d)

    def test_related_campaigns(self):
        d = {
            'related_campaigns': {
                'scope': 'inclusive',
                'related_campaigns': [
                    {
                        'campaign': {
                            'idref': 'example:Campaign-2f193992-d1c9-45a4-9db6-edbe9f7109cb',
                            'names': ['foo', 'bar']
                        }
                    },
                    {
                        'campaign': {
                            'idref': 'example:Campaign-2f193992-d1c9-45a4-9db6-edbe9f7109cb',
                            'names': ['foo', 'bar']
                        }
                    }
                ]
            }
        }

        self._test_partial_dict(d)

    def test_producer(self):
        d = {
            'producer': {
                'description': 'A sample description',
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
                    'xsi:type': 'stix-ciqidentity:CIQIdentity3.0InstanceType'
                },
                'time': {'produced_time': '2014-02-21T10:16:14.947201'}
            }
        }

        self._test_partial_dict(d)

    def test_kill_chain_phases(self):
        d = {
            'kill_chain_phases': {
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
        }

        self._test_partial_dict(d)

    def test_test_mechanisms(self):
        d = {
            'test_mechanisms': [
                {
                    'id': 'example:testmechanism-1',
                    'efficacy': {
                        'timestamp': '2014-06-20T15:16:56.987966+00:00',
                        'value': {
                            'value': 'Low',
                            'xsi:type': 'stixVocabs:HighMediumLowVocab-1.0'
                        }
                    },
                    'producer': {
                        'identity': {
                          'id': 'example:Identity-a0740d84-9fcd-44af-9033-94e76a53201e',
                          'name': 'FOX IT'
                        },
                        'references': [
                          'http://blog.fox-it.com/2014/04/08/openssl-heartbleed-bug-live-blog/'
                        ]
                    },
                    'description': {
                        'value': 'Foo',
                        'structuring_format': 'Bar'
                    },
                    'type': "Test",
                    'specification': {
                        'value': "Test",
                        'encoded': False
                    },
                    'xsi:type': 'genericTM:GenericTestMechanismType'
                }
            ]
        }
        self._test_partial_dict(d)


    def test_likely_impact(self):
        d = {
            'likely_impact': {
                'timestamp': "2014-01-31T06:14:46",
                'timestamp_precision': 'day',
                'value': "Something strange is going on",
                'description': "An amazing source",
                'source': { 'description': "An amazing source",
                            'identity': {'name': "Spiderman",}
                           },
                'confidence': {
                    'value': {'value': "Low", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'},
                },
            }
        }
        self._test_partial_dict(d)

    def test_suggested_coas(self):
        d = {
            'suggested_coas': {
                'suggested_coas': [
                    {
                        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                        'information_source': {
                            'description': "Source of the relationship",
                        },
                        'relationship': "Associated",
                        'course_of_action': {
                            'id': 'example:bar-1',
                            'title': 'Test'
                        }
                    }
                ]
            }
        }

        self._test_partial_dict(d)

    def test_handling(self):
        d = {
            'handling': [
                {
                    'marking_structures': [
                        {
                            'marking_model_name': 'TLP',
                            'color': "WHITE",
                            'xsi:type': "tlpMarking:TLPMarkingStructureType",
                        }
                    ]
                }
            ]
        }
        self._test_partial_dict(d)

    def test_confidence(self):
        d = {
            'confidence': {
                'timestamp': "2014-01-31T06:14:46",
                'timestamp_precision': 'day',
                'value': {'value': "High", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'},
                'description': "An amazing source",
                'source': {
                    'description': "An amazing source",
                    'identity': {'name': "Spiderman",}
                }
            }
        }
        self._test_partial_dict(d)

    def test_sightings(self):
        d = {
            'sightings': {
                'sightings_count': 2,
                'sightings': [
                    {
                        'timestamp': "2014-01-31T06:14:46",
                        'timestamp_precision': 'day',
                        'source': {
                            'description': "An amazing source",
                            'identity': {'name': "Spiderman",}
                        },
                        'reference': 'foobar',
                        'confidence': {
                            'timestamp': "2014-01-31T06:14:46",
                            'timestamp_precision': 'day',
                            'value': {'value': "High", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'},
                            'description': "An amazing source",
                            'source': {
                                'description': "An amazing source",
                                'identity': {'name': "Spiderman",}
                            }
                        },
                        'description': "Test",
                        'related_observables': {
                            'observables': [
                                {
                                    'relationship': "Associated",
                                    'observable': {
                                        'id': 'example:bar-1',
                                        'title': 'Test'
                                    }
                                },
                                {
                                    'relationship': "Associated",
                                    'observable': {
                                        'id': 'example:bar-2',
                                        'title': 'Test'
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        }

        self._test_partial_dict(d)

    def test_related_indicators(self):
        d = {
            'related_indicators': {
                'related_indicators': [
                    {
                        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                        'information_source': {
                            'description': "Source of the relationship",
                        },
                        'relationship': "Associated",
                        'indicator': {
                            'id': 'example:bar-1',
                            'title': 'Test'
                        }
                    }
                ]
            }
        }

        self._test_partial_dict(d)

    def test_related_packages(self):
        d = {
            'related_packages': {
                'packages': [
                    {
                        'idref': "example:foo-1",
                        'timestamp': "2014-01-31T06:14:46",
                        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                        'information_source': {
                            'description': "Source of the relationship",
                        },
                        'relationship': "Associated"
                    },
                    {
                        'idref': "example:foo--2",
                        'timestamp': "2014-01-31T06:14:46",
                        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                        'information_source': {
                            'description': "Source of the relationship",
                        },
                        'relationship': "Associated"
                    }
                ]
            }
        }

        self._test_partial_dict(d)

if __name__ == "__main__":
    unittest.main()
