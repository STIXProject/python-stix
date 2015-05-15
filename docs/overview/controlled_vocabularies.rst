Controlled Vocabularies
=======================

Many fields in STIX leverage the ``stixCommon:ControlledVocabularyStringType``,
which acts as a base type for controlled vocabulary implementations. The STIX
language defines a set of default controlled vocabularies which are  found in
the ``stix_default_vocabs.xsd`` XML Schema file.

The **python-stix** library contains a :mod:`stix.common.vocabs` module, which
defines the :class:`.VocabString` class implementation of the schema
``ControlledVocabularyStringType`` as well as :class:`.VocabString`
implementations which correspond to default controlled vocabularies.

For example, the ``stix_default_vocabularies.xsd`` schema defines a controlled
vocabulary for STIX Package Intents: ``PackageIntentVocab-1.0``. The
:mod:`.stix.common.vocabs` module contains an analogous :class:`.PackageIntent`
class, which acts as a derivation of :class:`.VocabString`.

Each :class:`.VocabString` implementation contains:

* A static list of class-level term attributes, each beginning with ``TERM_`
  (e.g., ``TERM_INDICATORS``)

* A tuple containing all allowed vocabulary terms: ``_ALLOWED_VALUES``, which is
  use for input validation. This is generated via the :meth:`.vocabs.register_vocab`
  class decorator.

* Methods found on :class:`stix.Entity`, such as ``to_xml()``, ``to_dict()``,
  ``from_dict()``, etc.


Interacting With VocabString Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The following sections define ways of interacting with VocabString fields.

Default Vocabulary Terms
########################

The STIX Language often suggested a default controlled vocabulary type for a
given controlled vocabulary field. Each controlled vocabulary contains an
enumeration of allowed terms.

Each :class:`.VocabString` implementation found in the :mod:`stix.common.vocabs`
module contains static class-level attributes for each vocabulary term. When
setting controlled vocabulary field values, it is recommended that users take
advantage of these class-level attributes.

The following demonstrates setting the ``Package_Intent`` field with a default
vocabulary term. Note that the :attr:`.STIXHeader.package_intents` property returns
a list. As such, we use the ``append()`` method to add terms. Other STIX
controlled vocabulary fields may only allow one value rather than a list of
values.

.. code-block:: python

    from stix.core import STIXHeader
    from stix.common.vocabs import PackageIntent

    header = STIXHeader()
    header.package_intents.append(PackageIntent.TERM_INDICATORS)

    print header.to_xml()

Which outputs:

.. code-block:: xml

    <stix:STIXHeaderType>
        <stix:Package_Intent xsi:type="stixVocabs:PackageIntentVocab-1.0">Indicators</stix:Package_Intent>
    </stix:STIXHeaderType>

Non-Default Vocabulary Terms
############################

Though it is suggested, STIX content authors are not required to use the default
controlled vocabulary for a given field. As such, **python-stix** allows users
to pass in non-default values for controlled vocabulary fields.

To set a controlled vocabulary to a non-default vocabulary term, pass a
:class:`.VocabString` instance into a controlled vocabulary field.

A raw :class:`.VocabString` field will contain no ``xsi:type`` information or
``_ALLOWED_VALUES`` members, which removes the input and schema validation
requirements.

.. code-block:: python

    from stix.core import STIXHeader
    from stix.common.vocabs import VocabString, PackageIntent

    header = STIXHeader()
    non_default_term = VocabString("NON-DEFAULT VOCABULARY TERM")
    header.package_intents.append(non_default_term)

    print header.to_xml()

Which outputs:

.. code-block:: xml

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
        version="1.2"
        xml:lang="English">
        <xs:import namespace="http://stix.mitre.org/common-1" schemaLocation="http://stix.mitre.org/XMLSchema/common/1.2/stix_common.xsd"/>
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
        version="1.2">
        <stix:STIX_Header>
            <stix:Package_Intent xsi:type="customVocabs:CustomVocab-1.0">FOO</stix:Package_Intent>
        </stix:STIX_Header>
    </stix:STIX_Package>

Python Code
"""""""""""

To parse content which uses custom controlled vocabularies, Python developers
don't have to do anything special--you just call :meth:`.STIXPackage.from_xml()` on
the input and all the namespaces, ``xsi:types``, etc. are attached to each
instance of :class:`.VocabString`. When serializing the document, the input namespaces
and ``xsi:type`` attributes are retained!

However, to `create` new content which utilizes a schema defined and enforced
custom controlled vocabulary, developers must create a :class:`.VocabString`
implementation which mirrors the schema definition.

For our ``CustomVocab-1.0`` schema type, the Python would look like this:

.. code-block:: python

    from stix.common import vocabs

    # Create a custom vocabulary type
    @vocabs.register_vocab
    class CustomVocab(vocabs.VocabString):
        _namespace = 'http://customvocabs.com/vocabs-1'
        _XSI_TYPE = 'customVocabs:CustomVocab-1.0'

        # Valid terms
        TERM_FOO = 'FOO'
        TERM_BAR = 'BAR'

As you can see, we can express a lot of the same information found in the
XML Schema definition, but in Python!

* ``_namespace``: The ``targetNamespace`` for our custom vocabulary

* ``_XSI_TYPE``: The ``xsi:type`` attribute value to write out for instances
  of this vocabulary.

* ``TERM_FOO|BAR``: Allowable terms for the vocabulary. These terms are
  collected for input validation.

.. note::

    The ``@register_vocab`` class decorator registers the class and its
    ``xsi:type`` as a :class:`.VocabString` implementation so **python-stix** will
    know to build instances of ``CustomVocab`` when parsed content contains
    ``CustomVocab-1.0`` content.

    This also inspects the class attributes for any that begin with
    ``TERM_`` and collects their values for the purpose of input validation.

.. warning::

    Before **python-stix** 1.2.0.0, users registered custom :class:`.VocabString`
    implementations via the :meth:`stix.common.vocabs.add_vocab` method. This
    method still exists but is considered **DEPRECATED** in favor of the
    :meth:`stix.common.vocabs.register_vocab` class decorator.

.. code-block:: python

    # builtin
    from StringIO import StringIO

    # python-stix modules
    from stix.core import STIXPackage
    from stix.common.vocabs import VocabString, register_vocab

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
        version="1.2">
        <stix:STIX_Header>
            <stix:Package_Intent xsi:type="customVocabs:CustomVocab-1.0">FOO</stix:Package_Intent>
        </stix:STIX_Header>
    </stix:STIX_Package>
    """

    # Create a VocabString class for our CustomVocab-1.0 vocabulary which
    @register_vocab
    class CustomVocab(VocabString):
        _namespace = 'http://customvocabs.com/vocabs-1'
        _XSI_TYPE  = 'customVocabs:CustomVocab-1.0'
        TERM_FOO   = 'FOO'
        TERM_BAR   = 'BAR'

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

