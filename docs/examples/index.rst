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

    from stix.core import STIXPackage, STIXHeader
    from stix.utils import IDGenerator, set_id_method

    set_id_method(IDGenerator.METHOD_INT) # For testing and demonstration only!

    stix_package = STIXPackage()
    stix_header = STIXHeader()
    stix_header.description = "Getting Started!"
    stix_package.stix_header = stix_header

    print stix_package.to_xml()

Which outputs:

.. code-block:: xml

    <stix:STIX_Package id="example:Package-1" version="1.2" timestamp="2014-08-12T18:03:44.240457+00:00">
        <stix:STIX_Header>
            <stix:Description>Getting Started!</stix:Description>
        </stix:STIX_Header>
    </stix:STIX_Package>


Controlled Vocabularies: VocabString
------------------------------------

This section has moved! Head over to :doc:`/overview/controlled_vocabularies`
for the documentation.


ID Namespaces
-------------

This section has moved! Head over to :doc:`/overview/id_namespaces` for the
documentation.


