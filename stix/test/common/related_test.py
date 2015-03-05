# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest

from stix.test import EntityTestCase

from stix.common.related import (
    RelatedCampaign, RelatedCampaignRef, RelatedIdentity, RelatedCOA,
    RelatedPackage, RelatedPackageRef, RelatedExploitTarget, RelatedIncident,
    RelatedIndicator, RelatedObservable, RelatedThreatActor, RelatedTTP,
    RelatedPackageRefs, RelatedPackages
)

class RelatedPackageRefsTests(EntityTestCase, unittest.TestCase):
    klass = RelatedPackageRefs
    _full_dict = {
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



class RelatedPackageRefTests(EntityTestCase, unittest.TestCase):
    klass = RelatedPackageRef
    _full_dict = {
        'idref': "example:Campaign-133",
        'timestamp': "2014-01-31T06:14:46",
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Source of the relationship",
        },
        'relationship': "Associated",
    }


class RelatedCampaignTests(EntityTestCase, unittest.TestCase):
    klass = RelatedCampaign
    _full_dict = {
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Source of the relationship",
        },
        'relationship': "Associated",
        'campaign': {
            'id': 'example:bar-1',
            'title': 'Test'
        }
    }


class RelatedIndicatorTests(EntityTestCase, unittest.TestCase):
    klass = RelatedIndicator
    _full_dict = {
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


class RelatedIncidentTests(EntityTestCase, unittest.TestCase):
    klass = RelatedIncident
    _full_dict = {
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Source of the relationship",
        },
        'relationship': "Associated",
        'incident': {
            'id': 'example:bar-1',
            'title': 'Test'
        }
    }


class RelatedExploitTargetTests(EntityTestCase, unittest.TestCase):
    klass = RelatedExploitTarget
    _full_dict = {
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Source of the relationship",
        },
        'relationship': "Associated",
        'exploit_target': {
            'id': 'example:bar-1',
            'title': 'Test'
        }
    }


class RelatedThreatActorTests(EntityTestCase, unittest.TestCase):
    klass = RelatedThreatActor
    _full_dict = {
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Source of the relationship",
        },
        'relationship': "Associated",
        'threat_actor': {
            'id': 'example:bar-1',
            'title': 'Test'
        }
    }

class RelatedCOATests(EntityTestCase, unittest.TestCase):
    klass = RelatedCOA
    _full_dict = {
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

class RelatedTTPTests(EntityTestCase, unittest.TestCase):
    klass = RelatedTTP
    _full_dict = {
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Source of the relationship",
        },
        'relationship': "Associated",
        'ttp': {
            'id': 'example:bar-1',
            'title': 'Test'
        }
    }

class RelatedIdentityTests(EntityTestCase, unittest.TestCase):
    klass = RelatedIdentity
    _full_dict = {
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Source of the relationship",
        },
        'relationship': "Associated",
        'identity': {
            'id': 'example:bar-1',
            'name': 'Test'
        }
    }

class RelatedObservableTests(EntityTestCase, unittest.TestCase):
    klass = RelatedObservable
    _full_dict = {
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Source of the relationship",
        },
        'relationship': "Associated",
        'observable': {
            'id': 'example:bar-1',
            'title': 'Test'
        }
    }

class RelatedPackageTests(EntityTestCase, unittest.TestCase):
    klass = RelatedPackage
    _full_dict = {
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Source of the relationship",
        },
        'relationship': "Associated",
        'package': {
            'id': 'example:bar-1',
            'version': '1.1.1',
            'stix_header': {
                'title': 'Test'
            }
        }
    }

class RelatedPackagesTests(EntityTestCase, unittest.TestCase):
    klass = RelatedPackages
    _full_dict = {
        'scope': 'inclusive',
        'related_packages': [
            {
                'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                'information_source': {
                    'description': "Source of the relationship",
                },
                'relationship': "Associated",
                'package': {
                    'id': 'example:bar-1',
                    'version': '1.1.1',
                    'stix_header': {
                        'title': 'Test'
                    }
                }
            },
            {
                'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
                'information_source': {
                    'description': "Source of the relationship",
                },
                'relationship': "Associated",
                'package': {
                    'id': 'example:bar-2',
                    'version': '1.1.1',
                    'stix_header': {
                        'title': 'Test'
                    }
                }
            }
        ]
    }

class RelatedCampaignRefTests(EntityTestCase, unittest.TestCase):
    klass = RelatedCampaignRef
    _full_dict = {
        'confidence': {'value': {'value': "Medium", 'xsi:type':'stixVocabs:HighMediumLowVocab-1.0'}},
        'information_source': {
            'description': "Source of the relationship",
        },
        'relationship': "Associated",
        'campaign': {
            'idref': "example:foo-1",
            'timestamp': "2014-01-31T06:14:46",
            'names': ["foo", "bar"]
        }
    }


if __name__ == "__main__":
    unittest.main()
