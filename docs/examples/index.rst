Examples
========

This page includes some basic examples of creating and parsing STIX content.

There are a couple things we do in these examples for purposes of demonstration
that shouldn't be done in production code:

* In some examples, we use ``set_id_method(IDGenerator.METHOD_INT)`` to make
  IDs for STIX constructs easier to read and cross-reference within the XML
  document. In production code, you should omit this statement, which causes
  random UUIDs to be created instead, or create explicit IDs yourself for STIX
  constructs.

See the `STIX Idioms <http://stixproject.github.io/documentation/idioms/>`_
documentation for more great examples of how to use **python-stix**.


Creating a STIX Package
-----------------------

.. code-block:: python

    from stix.core import STIXPackage
    from stix.report import Report
    from stix.report.header import Header
    from stix.utils import IDGenerator, set_id_method

    set_id_method(IDGenerator.METHOD_INT) # For testing and demonstration only!

    stix_package = STIXPackage()
    stix_report = Report()
    stix_report.header = Header()
    stix_report.header.description = "Getting Started!"
    stix_package.add(stix_report)

    print(stix_package.to_xml())

Which outputs:

.. code-block:: xml

    <stix:STIX_Package
            xmlns:cybox="http://docs.oasis-open.org/cti/ns/cybox/core-2"
            xmlns:cyboxCommon="http://docs.oasis-open.org/cti/ns/cybox/common-2"
            xmlns:cyboxVocabs="http://docs.oasis-open.org/cti/ns/cybox/vocabularies-2"
            xmlns:example="http://example.com"
            xmlns:report="http://docs.oasis-open.org/cti/ns/stix/report-1"
            xmlns:stix="http://docs.oasis-open.org/cti/ns/stix/core-1"
            xmlns:stixCommon="http://docs.oasis-open.org/cti/ns/stix/common-1"
            xmlns:stixVocabs="http://docs.oasis-open.org/cti/ns/stix/vocabularies-1"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="example:Package-1" version="1.2.1">
        <stix:Reports>
            <stix:Report timestamp="2016-07-15T15:27:43.847000+00:00" id="example:Report-2" xsi:type='report:ReportType' version="1.0">
                <report:Header>
                    <report:Description>Getting Started!</report:Description>
                </report:Header>
            </stix:Report>
        </stix:Reports>
    </stix:STIX_Package>


Controlled Vocabularies: VocabString
------------------------------------

This section has moved! Head over to :doc:`/overview/controlled_vocabularies`
for the documentation.


ID Namespaces
-------------

This section has moved! Head over to :doc:`/overview/id_namespaces` for the
documentation.


