python-stix
===========

A python library for parsing, manipulating, and generating STIX v1.1.1 content.

:Source: https://github.com/STIXProject/python-stix
:Documentation: http://stix.readthedocs.org
:Information: http://stix.mitre.org

|travis badge| |landscape.io badge| |version badge| |downloads badge|

.. |travis badge| image:: https://api.travis-ci.org/STIXProject/python-stix.png?branch=master
   :target: https://travis-ci.org/STIXProject/python-stix
   :alt: Build Status
.. |landscape.io badge| image:: https://landscape.io/github/STIXProject/python-stix/master/landscape.png
   :target: https://landscape.io/github/STIXProject/python-stix/master
   :alt: Code Health
.. |version badge| image:: https://pypip.in/v/stix/badge.png
   :target: https://pypi.python.org/pypi/stix/
.. |downloads badge| image:: https://pypip.in/d/stix/badge.png
   :target: https://pypi.python.org/pypi/stix/


Installation
------------

The python-stix library can be installed via the distutils setup.py script
included at the root directory:

    $ python setup.py install

The python-stix library is also hosted on `PyPI
<https://pypi.python.org/pypi/stix/>`_ and can be installed with `pip
<https://pypi.python.org/pypi/pip>`_:

    $ pip install stix

Dependencies
------------

The python-stix library depends on the presence of certain packages/libraries
to function. Please refer to their installation documentation for installation
instructions.

-  `python-cybox <https://github.com/CybOXProject/python-cybox>`_
-  `lxml <http://lxml.de/>`_

Installation on Ubuntu 14.04 (and older)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ sudo apt-get install python-dev python-pip libxml2-dev libxslt-dev zlib1g-dev
    $ sudo pip install stix

Versioning
----------

Releases of the python-stix library will be given version numbers of the form
``major.minor.update.revision``, where ``major``, ``minor``, and ``update``
correspond to the STIX version being supported. The ``revision`` number is used
to indicate new versions of the python-stix library itself.


Layout
------

The python-stix package layout is as follows:

* ``stix/`` : root level package

* ``examples/`` : example python scripts that leverage the python-stix library

* ``stix/utils/`` : utility classes and modules used internally by the python-stix
  library

* ``stix/bindings/`` : generateDS generated xml-to-python bindings (leveraged for
  parsing and output of STIX XML content)
  
* ``stix/campaign/`` : APIs for STIX Campaign constructs

* ``stix/coa/`` : APIs for STIX Course Of Action constructs

* ``stix/core/`` : APIs for core STIX constructs (e.g., STIX Header, STIX Package)

* ``stix/common/`` : APIs for common STIX constructs (e.g., Structured Text,
  Information Source)

* ``stix/exploit_target/`` : APIs for STIX Exploit Target constructs

* ``stix/incident/`` : APIs for common Incident constructs

* ``stix/indicator/`` : APIs for STIX Indicator constructs

* ``stix/extensions/`` : APIs for STIX extensions (e.g., CIQ Identity)

* ``stix/threat_actor/`` : APIs for STIX Threat Actor constructs

* ``stix/ttp/`` : APIs for STIX TTP constructs

Please refer to examples for concrete examples of how to interact with the
python-stix library
