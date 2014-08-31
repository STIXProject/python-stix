# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
from stix.test import EntityTestCase
from stix.extensions.identity.ciq_identity_3_0 import CIQIdentity3_0Instance


class CIQIdentity3_0InstanceTests(EntityTestCase, unittest.TestCase):
    klass = CIQIdentity3_0Instance
    _full_dict = {'id': 'example:ciqidentity-1',
                  'name': 'John Smith',
                  'roles': ['Programmer', 'Analyst'],
                  'specification': {'party_name': {'name_lines': [{'value': 'Foo'},
                                                                  {'value': 'Bar'}],
                                    'organisation_names': [{'name_elements': [{'element_type': 'FullName',
                                                                               'value': 'Foo Inc.'}],
                                                            'subdivision_names': [{'type': 'Department',
                                                                                   'value': 'InfoSec'}]}],
                                    'person_names': [{'name_elements': [{'value': 'John Smith'}]},
                                                     {'name_elements': [{'value': 'Jill Smith'}]}]}},
                  'xsi:type': 'ciqIdentity:CIQIdentity3.0InstanceType'}


if __name__ == "__main__":
    unittest.main()
