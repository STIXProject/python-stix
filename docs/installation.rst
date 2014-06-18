.. _installation:

Installation
============

The installation of python-stix can be accomplished through a few different workflows.

Recommended Installation
------------------------

Use pypi_ and pip_:

.. code-block:: bash

    $ pip install stix

You might also want to consider using a virtualenv_.
Please refer to the `pip installation instructions`_ for details regarding the installation of pip.

.. _pypi: https://pypi.python.org/pypi/stix/
.. _pip: http://pip.readthedocs.org/
.. _pip installation instructions: http://www.pip-installer.org/en/latest/installing.html
.. _virtualenv: http://virtualenv.readthedocs.org/


Dependencies
------------

The python-stix library relies on some non-standard Python libraries for the processing of STIX content. Revisions of python-stix may depend on particular versions of dependencies to function correctly. These versions are detailed within the distutils setup.py installation script.

The following libraries are required to use python-stix:

* lxml_ - A Pythonic binding for the C libraries **libxml2** and
  **libxslt**.
* python-cybox_ - A library for consuming and producing CybOX content.
* python-dateutil_ - A library for parsing datetime information.

Each of these can be installed with ``pip`` or by manually downloading packages
from PyPI. On Windows, you will probably have the most luck using `pre-compiled
binaries`_ for ``lxml``. On Ubuntu (12.04 or 14.04), you should make sure the
following packages are installed before attempting to compile ``lxml`` from
source:

* libxml2-dev
* libxslt1-dev
* zlib1g-dev

.. warning::

   Users have encountered errors with versions of libxml2 (a dependency of
   lxml) prior to version 2.9.1.  The default version of libxml2 provided on
   Ubuntu 12.04 is currently 2.7.8.  Users are encouraged to upgrade libxml2
   manually if they have any issues.  Ubuntu 14.04 provides libxml2 version
   2.9.1.

.. _lxml: http://lxml.de/
.. _python-dateutil: http://labix.org/python-dateutil
.. _python-cybox: https://github.com/CybOXProject/python-cybox
.. _pre-compiled binaries: http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml


Manual Installation
-------------------

If you are unable to use pip, you can also install python-stix with setuptools_.
If you don't already have setuptools installed, please install it before
continuing.

1. Download and install the dependencies_ above. Although setuptools will
   generally install dependencies automatically, installing the dependencies
   manually beforehand helps distinguish errors in dependency installation from
   errors in stix installation. Make sure you check to ensure the
   versions you install are compatible with the version of stix you plan
   to install.

2. Download the desired version of stix from PyPI_ or the GitHub releases_
   page. The steps below assume you are using the |release| release.

3. Extract the downloaded file. This will leave you with a directory named
   stix-|release|.

.. parsed-literal::
    $ tar -zxf stix-|release|.tar.gz
    $ ls
    stix-|release| stix-|release|.tar.gz

OR

.. parsed-literal::
    $ unzip stix-|release|.zip
    $ ls
    stix-|release| stix-|release|.zip

4. Run the installation script.

.. parsed-literal::
    $ cd stix-|release|
    $ python setup.py install

5. Test the installation.

.. parsed-literal::
    $ python
    Python 2.7.6 (default, Mar 22 2014, 22:59:56)
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import stix
    >>>

If you don't see an ``ImportError``, the installation was successful.

.. _setuptools: https://pypi.python.org/pypi/setuptools/
.. _PyPI: https://pypi.python.org/pypi/stix/
.. _releases: https://github.com/STIXProject/python-stix/releases


Further Information
-------------------

If you're new to installing Python packages, you can learn more at the `Python
Packaging User Guide`_, specifically the `Installing Python Packages`_ section.

.. _Python Packaging User Guide: http://python-packaging-user-guide.readthedocs.org/
.. _Installing Python Packages: http://python-packaging-user-guide.readthedocs.org/en/latest/tutorial.html#installing-python-packages
