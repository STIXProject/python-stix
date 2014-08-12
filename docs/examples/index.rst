Examples
========

This page includes some basic examples of creating and parsing STIX content.

There are a couple things we do in these examples for purposes of demonstration
that shouldn't be done in production code:

* When calling ``to_xml()``, we use ``include_namespaces=False``. This is to
  make the example output easier to read, but means the resulting output
  cannot be successfully parsed. The XML parser doesn't know what namespaces
  to use if they aren't included. In production code, you should explicitly
  set ``include_namespaces`` to ``True`` or omit it entirely (``True`` is the
  default).

* In some examples, we use ``set_id_method(IDGenerator.METHOD_INT)`` to make
  IDs for STIX constructs easier to read and cross-reference within the XML
  document. In production code, you should omit this statement, which causes
  random UUIDs to be created instead, or create explicit IDs yourself for STIX
  constructs.

See the `STIX Idioms <http://stixproject.github.io/documentation/idioms/>`_
documentation for more great examples of how to use ``python-stix``.


Creating a STIX Package
-----------------------
.. testcode::

    from stix.core import STIXPackage, STIXHeader
    from stix.utils import IDGenerator, set_id_method

    set_id_method(IDGenerator.METHOD_INT) # For testing and demonstration only!

    stix_package = STIXPackage()
    stix_header = STIXHeader()
    stix_header.description = "Getting Started!"
    stix_package.stix_header = stix_header

    print stix_package.to_xml(include_namespaces=False)

Which outputs:

.. testoutput::

    <stix:STIX_Package id="example:Package-1" version="1.1.1" timestamp="2014-08-12T18:03:44.240457+00:00">
        <stix:STIX_Header>
            <stix:Description>Getting Started!</stix:Description>
        </stix:STIX_Header>
    </stix:STIX_Package>


ID Namespaces
-------------
By default, ``python-stix`` sets the default ID namespace to
``http://example.com`` with an alias of ``example``. This results in STIX
id declarations that look like
``id="example:Package-2813128d-f45e-41f7-b10a-20a5656e3785"``.

To change this, use the ``stix.utils.set_id_namespace()`` method which takes
a dictionary as a parameter.

.. testcode::

    from stix.core import STIXPackage
    from stix.utils import set_id_namespace

    NAMESPACE = {"http://MY-NAMESPACE.com" : "myNS"}
    set_id_namespace(NAMESPACE) # new ids will be prefixed by "myNS"

    stix_package = STIXPackage() # id will be created automatically
    print stix_package.to_xml()

Which outputs:

.. testoutput::

    <stix:STIX_Package
        xmlns:myNS="http://MY-NAMESPACE.com"
        xmlns:stixCommon="http://stix.mitre.org/common-1"
        xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
        xmlns:stix="http://stix.mitre.org/stix-1"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="
        http://stix.mitre.org/common-1 http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd
        http://stix.mitre.org/default_vocabularies-1 http://stix.mitre.org/XMLSchema/default_vocabularies/1.1.1/stix_default_vocabularies.xsd
        http://stix.mitre.org/stix-1 http://stix.mitre.org/XMLSchema/core/1.1.1/stix_core.xsd"
        id="myNS:Package-b2039368-9476-4a5b-8c1d-0ef5d1b37e06" version="1.1.1" timestamp="2014-08-12T18:15:33.603457+00:00"/>

Success! The ``xmlns:myNS="http://MY-NAMESPACE.com"`` matches our ``NAMESPACE``
dictionary and the ``id`` attribute includes the ``myNS`` namespace alias.

Controlled Vocabularies: VocabString
------------------------------------
Many fields in STIX leverage the ``stixCommon:ControlledVocabularyStringType``,
which acts as a base type for controlled vocabulary implementations. The STIX
language defines a set of default controlled vocabularies which are  found in
the ``stix_default_vocabs.xsd`` XML Schema file.

The ``python-stix`` library contains a ``stix.common.vocabs`` module, which
defines the ``VocabString`` class implementation of the schema
``ControlledVocabularyStringType`` as well as ``VocabString`` implementations
which correspond to default controlled vocabularies.

For example, the ``stix_default_vocabularies.xsd`` schema defines a controlled
vocabulary for STIX Package Intents: ``PackageIntentVocab-1.0``. The
``stix.common.vocabs`` module contains an analogous ``PackageIntent`` class,
which acts as a derivation of ``VocabString``.

Each ``VocabString`` implementation contains:

* A static list of class-level term attributes, each beginning with ``TERM_`
  (e.g., ``TERM_INDICATORS``)

* A tuple containing all allowed vocabulary terms: ``ALLOWED_VALUES``, which is
  use for input validation

* Methods found on ``stix.Entity``, such as ``to_xml()``, ``to_dict()``,
  ``from_dict()``, etc.


Interacting With VocabString Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The following sections define ways of interacting with VocabString fields.

Default Vocabulary Terms
########################
The STIX Language often suggested a default controlled vocabulary type for a
given controlled vocabulary field. Each controlled vocabulary contains an
enumeration of allowed terms.

Each ``VocabString`` implementation found in the ``stix.common.vocabs`` module
contains static class-level attributes for each vocabulary term. When setting
controlled vocabulary field values, it is recommended that users take advantage
of these class-level attributes.

The following demonstrates setting the ``Package_Intent`` field with a default
vocabulary term. Note that the ``STIXHeader.package_intents`` property returns
a list. As such, we use the ``append()`` method to add terms. Other STIX
controlled vocabulary fields may only allow one value rather than a list of
values.

.. testcode::

    from stix.core import STIXHeader
    from stix.common.vocabs import PackageIntent

    header = STIXHeader()
    header.package_intents.append(PackageIntent.TERM_INDICATORS)

    print header.to_xml(include_namespaces=False)

Which outputs:

.. testoutput::

    <stix:STIXHeaderType>
        <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators</stix:Package_Intent>
    </stix:STIXHeaderType>

Non-Default Vocabulary Terms
############################
Though it is suggested, STIX content authors are not required to use the default
controlled vocabulary for a given field. As such, ``python-stix`` allows users
to pass in non-default values for controlled vocabulary fields.

To set a controlled vocabulary to a non-default vocabulary term, pass a
``VocabString`` instance into a controlled vocabulary field.

A raw ``VocabString`` field will contain no ``xsi:type`` information or
``ALLOWED_VALUES`` members, which removes the input and schema validation
requirements.

.. testcode::

    from stix.core import STIXHeader
    from stix.common.vocabs import VocabString, PackageIntent

    header = STIXHeader()
    non_default_term = VocabString("NON-DEFAULT VOCABULARY TERM")
    header.package_intents.append(non_default_term)

    print header.to_xml(include_namespaces=False)

Which outputs:

.. testoutput::

    <stix:STIXHeaderType>
        <stix:Package_Intent>NON-DEFAULT VOCABULARY TERM</stix:Package_Intent>
    </stix:STIXHeaderType>

Notice that the ``<stix:Package_Intent>`` field does not have an ``xsi:type``
attribute. As such, this field can contain any string value and is not bound
by a controlled vocabulary enumeration of terms.