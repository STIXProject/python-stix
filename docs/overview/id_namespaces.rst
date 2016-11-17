ID Namespaces
=============

By default, **python-stix** sets the default ID namespace to
``http://example.com`` with an alias of ``example``. This results in STIX
id declarations that look like
``id="example:Package-2813128d-f45e-41f7-b10a-20a5656e3785"``.

To change this, use the :meth:`stix.utils.idgen.set_id_namespace` method which takes
a dictionary as a parameter.

.. code-block:: python

    from stix.core import STIXPackage
    from mixbox.idgen import set_id_namespace
    from mixbox.namespaces import Namespace

    NAMESPACE = Namespace("http://MY-NAMESPACE.com", "myNS")
    set_id_namespace(NAMESPACE) # new ids will be prefixed by "myNS"

    stix_package = STIXPackage() # id will be created automatically
    print stix_package.to_xml()

Which outputs:

.. code-block:: xml

    <stix:STIX_Package
        xmlns:ds="http://www.w3.org/2000/09/xmldsig#"
        xmlns:myNS="http://MY-NAMESPACE.com"
        xmlns:stix="http://docs.oasis-open.org/cti/ns/stix/core-1"
        xmlns:xs="http://www.w3.org/2001/XMLSchema"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xlink="http://www.w3.org/1999/xlink"
        id="myNS:Package-b2039368-9476-4a5b-8c1d-0ef5d1b37e06" version="1.2.1"/>

Success! The ``xmlns:myNS="http://MY-NAMESPACE.com"`` matches our ``NAMESPACE``
dictionary and the ``id`` attribute includes the ``myNS`` namespace alias.

Working With CybOX
~~~~~~~~~~~~~~~~~~
When setting the ID namespace in **python-stix**, the ID namespace will also be
set in **python-cybox**.
