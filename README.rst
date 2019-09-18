python-stix
===========

A python library for parsing, manipulating, and generating `Structured Threat Information eXpression (STIX™) <https://stixproject.github.io/>`_ v1.2.0 content.

:Source: https://github.com/STIXProject/python-stix
:Documentation: https://stix.readthedocs.io/
:Information: https://stixproject.github.io/
:Download: https://pypi.python.org/pypi/stix/

|travis_badge| |landscape_io_badge| |version_badge|

.. |travis_badge| image:: https://api.travis-ci.org/STIXProject/python-stix.svg?branch=master
   :target: https://travis-ci.org/STIXProject/python-stix
   :alt: Build Status
.. |landscape_io_badge| image:: https://landscape.io/github/STIXProject/python-stix/master/landscape.svg
   :target: https://landscape.io/github/STIXProject/python-stix/master
   :alt: Code Health
.. |version_badge| image:: https://img.shields.io/pypi/v/stix.svg?maxAge=3600
   :target: https://pypi.python.org/pypi/stix/
   :alt: Version


Installation
------------

The python-stix library is hosted on `PyPI
<https://pypi.python.org/pypi/stix/>`_ and the most recent stable version can be
installed with `pip <https://pypi.python.org/pypi/pip>`_:

::

    $ pip install stix

The python-stix library can also be installed via the distutils setup.py script
included at the root directory:

::

    $ python setup.py install

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

Installation on Windows
~~~~~~~~~~~~~~~~~~~~~~~

Download the Lxml wheel for your version of Python from
http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml, then install it via "pip install
<filename>.whl". For example, to install it on 64-bit Windows running Python 2.7:

::

    $ pip install lxml-3.6.1-cp27-cp27m-win_amd64.whl
    $ pip install stix

Versioning
----------

Releases of the python-stix library will be given version numbers of the form
``major.minor.update.revision``, where ``major``, ``minor``, and ``update``
correspond to the STIX version being supported. The ``revision`` number is used
to indicate new versions of the python-stix library itself.


Layout
------

The python-stix package layout is as follows:

* ``stix/`` : root level package.

* ``examples/`` : example python scripts that leverage the python-stix library.

* ``stix/utils/`` : utility classes and modules used internally by the python-stix
  library.

* ``stix/bindings/`` : generateDS generated xml-to-python bindings (leveraged for
  parsing and output of STIX XML content).
  
* ``stix/campaign/`` : APIs for STIX Campaign constructs.

* ``stix/coa/`` : APIs for STIX Course Of Action constructs.

* ``stix/core/`` : APIs for core STIX constructs (e.g., STIX Header, STIX Package).

* ``stix/common/`` : APIs for common STIX constructs (e.g., Structured Text,
  Information Source).

* ``stix/exploit_target/`` : APIs for STIX Exploit Target constructs.

* ``stix/incident/`` : APIs for common Incident constructs.

* ``stix/indicator/`` : APIs for STIX Indicator constructs.

* ``stix/extensions/`` : APIs for STIX extensions (e.g., CIQ Identity).

* ``stix/report/``: APIs for STIX Report constructs.

* ``stix/threat_actor/`` : APIs for STIX Threat Actor constructs.

* ``stix/ttp/`` : APIs for STIX TTP constructs.

Please refer to examples for concrete examples of how to interact with the
python-stix library.
