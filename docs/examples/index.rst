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
documentation for more great examples of how to use **python-stix**.


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
By default, **python-stix** sets the default ID namespace to
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

Working With CybOX
~~~~~~~~~~~~~~~~~~
If you are creating CybOX entities such as ``Observables``, you'll want to set
the ID namespace for ``python-cybox`` as well.

Note that **python-stix** and ``python-cybox`` treat namespaces slightly
differently (for now anyway). Where **python-stix** uses Python dictionaries,
``python-cybox`` uses the ``cybox.utils.Namespace`` class to represent a
namespace.

.. testcode::

    from cybox.utils import set_id_namespace, Namespace
    from cybox.core import Observable

    NAMESPACE = Namespace("http://MY-NAMESPACE.com", "myNS")
    set_id_namespace(NAMESPACE)

    obs = Observable()
    print obs.to_xml()

Which outputs:

.. testoutput::

    <cybox:ObservableType
        xmlns:myNS="http://MY-NAMESPACE.com"
        xmlns:cybox="http://cybox.mitre.org/cybox-2"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://cybox.mitre.org/cybox-2 http://cybox.mitre.org/XMLSchema/core/2.1/cybox_core.xsd"
        id="myNS:Observable-7e6191d3-25e9-4283-a80c-867e175224ae">
    </cybox:ObservableType>

Success (again)! The ``xmlns:myNS="http://MY-NAMESPACE.com"`` matches our
``Namespace`` object and the ``id`` attribute includes the ``myNS`` namespace
alias.


Controlled Vocabularies: VocabString
------------------------------------
Many fields in STIX leverage the ``stixCommon:ControlledVocabularyStringType``,
which acts as a base type for controlled vocabulary implementations. The STIX
language defines a set of default controlled vocabularies which are  found in
the ``stix_default_vocabs.xsd`` XML Schema file.

The **python-stix** library contains a ``stix.common.vocabs`` module, which
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
controlled vocabulary for a given field. As such, **python-stix** allows users
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


Working With Custom Controlled Vocabularies
###########################################

STIX allows content authors and developers to extend the
``ControlledVocabularyStringType`` schema type for the definition of new
controlled vocabularies. The **python-stix** library allows developers to
create and register Python types which mirror the custom XML Schema vocabulary
types.

XSD Example
"""""""""""

The following XML Schema example shows the definition of a a new custom
controlled vocabulary schema type. Instances of this schema type could be
used wherever a ``ControlledVocabularyStringType`` instance is expected
(e.g., the ``STIX_Header/Package_Intent`` field).

.. code-block:: xml

    Filename: customVocabs.xsd

    <xs:schema
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xmlns:customVocabs="http://customvocabs.com/vocabs-1"
        xmlns:stixVocabs="http://stix.mitre.org/default_vocabularies-1"
        xmlns:stixCommon="http://stix.mitre.org/common-1"
        targetNamespace="http://customvocabs.com/vocabs-1"
        elementFormDefault="qualified"
        version="1.1.1"
        xml:lang="English">
        <xs:import namespace="http://stix.mitre.org/common-1" schemaLocation="http://stix.mitre.org/XMLSchema/common/1.1.1/stix_common.xsd"/>
        <xs:complexType name="CustomVocab-1.0">
            <xs:simpleContent>
                <xs:restriction base="stixCommon:ControlledVocabularyStringType">
                    <xs:simpleType>
                        <xs:union memberTypes="customVocabs:CustomEnum-1.0"/>
                    </xs:simpleType>
                    <xs:attribute name="vocab_name" type="xs:string" use="optional" fixed="Test Vocab"/>
                    <xs:attribute name="vocab_reference" type="xs:anyURI" use="optional" fixed="http://example.com/TestVocab"/>
                </xs:restriction>
            </xs:simpleContent>
        </xs:complexType>
        <xs:simpleType name="CustomEnum-1.0">
            <xs:restriction base="xs:string">
                <xs:enumeration value="FOO"/>
                <xs:enumeration value="BAR"/>
            </xs:restriction>
        </xs:simpleType>
    </xs:schema>

XML Instance Sample
"""""""""""""""""""

The following STIX XML instance document shows a potential use of this field.
Note the ``xsi:type=customVocabs:CustomVocab-1.0`` on the ``Package_Intent``
field.

.. code-block:: xml

    Filename: customVocabs.xml

    <stix:STIX_Package
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:stixExample="http://stix.mitre.org/example"
        xmlns:stix="http://stix.mitre.org/stix-1"
        xmlns:customVocabs="http://customvocabs.com/vocabs-1"
        xsi:schemaLocation="
        http://stix.mitre.org/stix-1 /path/to/stix_core.xsd
        http://customvocabs.com/vocabs-1 /path/to/customVocabs.xsd"
        id="stixExample:STIXPackage-33fe3b22-0201-47cf-85d0-97c02164528d"
        timestamp="2014-05-08T09:00:00.000000Z"
        version="1.1.1">
        <stix:STIX_Header>
            <stix:Package_Intent xsi:type="customVocabs:CustomVocab-1.0">FOO</stix:Package_Intent>
        </stix:STIX_Header>
    </stix:STIX_Package>

Python Code
"""""""""""

To parse content which uses custom controlled vocabularies, Python developers
don't have to do anything special--you just call ``STIXPackage.from_xml()`` on
the input and all the namespaces, ``xsi:types``, etc. are attached to each
instance of ``VocabString``. When serializing the document, the input namespaces
and ``xsi:type`` attributes are retained!

However, to `create` new content which utilizes a schema defined and enforced
custom controlled vocabulary, developers must create a :class:`.VocabString`
implementation which mirrors the schema definition.

For our ``CustomVocab-1.0`` schema type, the Python would look like this:

.. code-block:: python

    from stix.common import vocabs

    # Create a custom vocabulary type
    class CustomVocab(vocabs.VocabString):
        _namespace = 'http://customvocabs.com/vocabs-1'
        _XSI_TYPE = 'customVocabs:CustomVocab-1.0'
        _ALLOWED_VALUES = ('FOO', 'BAR')

    # Register the type as a VocabString
    vocabs.add_vocab(CustomVocab)

As you can see, we can express a lot of the same information found in the
XML Schema definition, just with a lot less typing!

* ``_namespace``: The ``targetNamespace`` for our custom vocabulary

* ``_XSI_TYPE``: The ``xsi:type`` attribute value to write out for instances
        of this vocabulary.
* ``_ALLOWED_VALUES``: A ``tuple`` of allowable values for this vocabulary.

.. note::

    The call to ``add_vocab()`` registers the class and its ``xsi:type`` as a
    ``VocabString`` implementation so **python-stix** will know to build
    instances of ``CustomVocab`` when parsed content contains
    ``CustomVocab-1.0`` content. You must call ``add_vocab()`` to register
    your class prior to parsing content if you want the parser to build
    instances of your custom vocabulary class!

.. code-block:: python

    # builtin
    from StringIO import StringIO

    # python-stix modules
    from stix.core import STIXPackage
    from stix.common import vocabs

    XML = \
    """
    <stix:STIX_Package
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:stix="http://stix.mitre.org/stix-1"
        xmlns:customVocabs="http://customvocabs.com/vocabs-1"
        xmlns:example="http://example.com/"
        xsi:schemaLocation="
        http://stix.mitre.org/stix-1 /path/to/stix_core.xsd
        http://customvocabs.com/vocabs-1 /path/to/customVocabs.xsd"
        id="example:STIXPackage-33fe3b22-0201-47cf-85d0-97c02164528d"
        timestamp="2014-05-08T09:00:00.000000Z"
        version="1.1.1">
        <stix:STIX_Header>
            <stix:Package_Intent xsi:type="customVocabs:CustomVocab-1.0">FOO</stix:Package_Intent>
        </stix:STIX_Header>
    </stix:STIX_Package>
    """

    # Create a VocabString class for our CustomVocab-1.0 vocabulary which
    class CustomVocab(vocabs.VocabString):
        _namespace = 'http://customvocabs.com/vocabs-1'
        _XSI_TYPE = 'customVocabs:CustomVocab-1.0'
        _ALLOWED_VALUES = ('FOO', 'BAR')

    # Register our Custom Vocabulary class so parsing builds instances of
    # CustomVocab
    vocabs.add_vocab(CustomVocab)

    # Parse the input document
    sio = StringIO(XML)
    package = STIXPackage.from_xml(sio)

    # Retrieve the first (and only) Package_Intent entry
    package_intent = package.stix_header.package_intents[0]

    # Print information about the input Package_Intent
    print type(package_intent), package_intent.xsi_type, package_intent

    # Add another Package Intent
    bar = CustomVocab('BAR')
    package.stix_header.add_package_intent(bar)

    # This will include the 'BAR' CustomVocab entry
    print package.to_xml()

