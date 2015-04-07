# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import unittest
import StringIO

import lxml

from stix import utils
from stix.test import EntityTestCase
from stix.extensions.test_mechanism.open_ioc_2010_test_mechanism import OpenIOCTestMechanism


class OpenIOCTestMechanismTests(EntityTestCase, unittest.TestCase):
    klass = OpenIOCTestMechanism
    _full_dict = {
        'id': 'example:testmechanism-a1475567-50f7-4dae-b0d0-47c7ea8e79e1',
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
        'xsi:type': 'stix-openioc:OpenIOC2010TestMechanismType'
    }


class OpenIOCEtreeTests(unittest.TestCase):
    DESCRIPTION = "Finds Zeus variants, twexts, sdra64, ntos"
    XML = (
        """
        <stix-openioc:ioc
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xmlns:xsd="http://www.w3.org/2001/XMLSchema"
            xmlns:mandiant-openioc="http://schemas.mandiant.com/2010/ioc"
            xmlns="http://schemas.mandiant.com/2010/ioc"
            xmlns:stix-openioc="http://stix.mitre.org/extensions/TestMechanism#OpenIOC2010-1"
            id="mandiant:6d2a1b03-b216-4cd8-9a9e-8827af6ebf93" last-modified="2011-10-28T19:28:20">
            <short_description>Zeus</short_description>
              <description>{0}</description>
              <keywords/>
              <authored_by>Mandiant</authored_by>
              <authored_date>0001-01-01T00:00:00</authored_date>
              <links/>
              <definition>
                <Indicator operator="OR" id="9c8df971-32a8-4ede-8a3a-c5cb2c1439c6">
                  <Indicator operator="AND" id="0781258f-6960-4da5-97a0-ec35fb403cac">
                    <IndicatorItem id="50455b63-35bf-4efa-9f06-aeba2980f80a" condition="contains">
                      <Context document="ProcessItem" search="ProcessItem/name" type="mir"/>
                      <Content type="string">winlogon.exe</Content>
                    </IndicatorItem>
                    <IndicatorItem id="b05d9b40-0528-461f-9721-e31d5651abdc" condition="contains">
                      <Context document="ProcessItem" search="ProcessItem/HandleList/Handle/Type" type="mir"/>
                      <Content type="string">File</Content>
                    </IndicatorItem>
                    <Indicator operator="OR" id="67505775-6577-43b2-bccd-74603223180a">
                      <IndicatorItem id="c5ae706f-c032-4da7-8acd-4523f1dae9f6" condition="contains">
                        <Context document="ProcessItem" search="ProcessItem/HandleList/Handle/Name" type="mir"/>
                        <Content type="string">system32\sdra64.exe</Content>
                      </IndicatorItem>
                      <IndicatorItem id="25ff12a7-665b-4e45-8b0f-6e5ca7b95801" condition="contains">
                        <Context document="ProcessItem" search="ProcessItem/HandleList/Handle/Name" type="mir"/>
                        <Content type="string">system32\twain_32\user.ds</Content>
                      </IndicatorItem>
                      <IndicatorItem id="fea11706-9ebe-469b-b30a-4047cfb7436b" condition="contains">
                        <Context document="ProcessItem" search="ProcessItem/HandleList/Handle/Type" type="mir"/>
                        <Content type="string">\WINDOWS\system32\twext.exe</Content>
                      </IndicatorItem>
                      <IndicatorItem id="94ac992c-8d6d-441f-bfc4-5235f9b09af8" condition="contains">
                        <Context document="ProcessItem" search="ProcessItem/HandleList/Handle/Name" type="mir"/>
                        <Content type="string">system32\twain32\local.ds</Content>
                      </IndicatorItem>
                      <IndicatorItem id="bc12f44e-7d93-47ea-9cc9-86a2beeaa04c" condition="contains">
                        <Context document="ProcessItem" search="ProcessItem/HandleList/Handle/Name" type="mir"/>
                        <Content type="string">system32\twext.exe</Content>
                      </IndicatorItem>
                      <IndicatorItem id="1c3f8902-d4e2-443a-a407-15be3951bef9" condition="contains">
                        <Context document="ProcessItem" search="ProcessItem/HandleList/Handle/Name" type="mir"/>
                        <Content type="string">system32\lowsec\user.ds</Content>
                      </IndicatorItem>
                      <IndicatorItem id="7fab12d1-67ed-4149-b46a-ec50fc622bee" condition="contains">
                        <Context document="ProcessItem" search="ProcessItem/HandleList/Handle/Name" type="mir"/>
                        <Content type="string">system32\lowsec\local.ds</Content>
                      </IndicatorItem>
                    </Indicator>
                  </Indicator>
                  <Indicator operator="AND" id="9f7a5703-8a26-45cf-b801-1c13f0f15d40">
                    <IndicatorItem id="cf77d82f-0ac9-4c81-af0b-d634f71525b5" condition="contains">
                      <Context document="ProcessItem" search="ProcessItem/HandleList/Handle/Type" type="mir"/>
                      <Content type="string">Mutant</Content>
                    </IndicatorItem>
                    <Indicator operator="OR" id="83f72cf7-6399-4620-b735-d08ce23ba517">
                      <IndicatorItem id="a1250d55-cd63-46cd-9436-e1741f5f42c7" condition="contains">
                        <Context document="ProcessItem" search="ProcessItem/HandleList/Handle/Name" type="mir"/>
                        <Content type="string">__SYSTEM__</Content>
                      </IndicatorItem>
                      <IndicatorItem id="e033b865-95ba-44ab-baa5-3b1e8e5f348c" condition="contains">
                        <Context document="ProcessItem" search="ProcessItem/HandleList/Handle/Name" type="mir"/>
                        <Content type="string">_AVIRA_</Content>
                      </IndicatorItem>
                    </Indicator>
                  </Indicator>
                </Indicator>
              </definition>
        </stix-openioc:ioc>
        """.format(DESCRIPTION)
    )

    def setUp(self):
        utils.set_id_namespace({"http://schemas.mandiant.com/2010/ioc": "mandiant-openioc"})

    def tearDown(self):
        utils.set_id_namespace(utils.EXAMPLE_NAMESPACE)

    def _test_xml(self, obj):
        xml = obj.to_xml()
        parser = utils.parser.get_xml_parser()
        tree = lxml.etree.parse(StringIO.StringIO(xml), parser=parser)
        root = tree.getroot()

        xpath = "//openioc:description"
        nodes = root.xpath(xpath, namespaces={'openioc': 'http://schemas.mandiant.com/2010/ioc'})

        self.assertTrue(nodes is not None)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, self.DESCRIPTION)

    def test_etree(self):
        parser = utils.parser.get_xml_parser()
        tree = lxml.etree.parse(StringIO.StringIO(self.XML), parser=parser)

        ext = OpenIOCTestMechanism()
        ext.ioc = tree
        self._test_xml(ext)

    def test_etree_dict(self):
        parser = utils.parser.get_xml_parser()
        tree = lxml.etree.parse(StringIO.StringIO(self.XML), parser=parser)
        ext = OpenIOCTestMechanism()
        ext.ioc = tree

        d = ext.to_dict()
        ext2 = OpenIOCTestMechanism.from_dict(d)
        self._test_xml(ext2)

if __name__ == "__main__":
    unittest.main()

