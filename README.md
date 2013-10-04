# python-stix [![Build Status](https://travis-ci.org/STIXProject/python-stix.png?branch=master)](https://travis-ci.org/STIXProject/python-stix)

A python library for parsing, manipulating, and generating STIX content. The `python-stix` library
utilizes the STIX v1.0.1 bindings, is under heavy development.

For more information about STIX, see http://stix.mitre.org.

## Installation
The python-stix library can be installed via the distutils setup.py script included at
the root directory:

<code>
python setup.py install
</code>

The python-stix library is also hosted at [PyPI](https://pypi.python.org/pypi/stix/) and can be
installed via [pip](https://pypi.python.org/pypi/pip)*:

<code>
pip install stix
</code>

## Dependencies
The python-stix library depends on the presence of certain packages/libraries to function.
Please refer to their installation documentation for installation instructions.
* [python-cybox](https://github.com/CybOXProject/python-cybox)
* [lxml](http://lxml.de/)

## Versioning
Releases of the python-stix library will be given `major.minor.revision`
version numbers, where `major` and `minor` correspond to the STIX version
being supported. The `revision` number is used to indicate new versions of
the Python library itself.

## Layout
The python-stix package layout is as follows:
* stix/ : root level package
* examples/ : example python scripts that leverage the python-stix library
* stix/utils.py : utility methods used internally by the python-stix library
* stix/bindings/ : generateDS generated xml-to-python bindings (leveraged for parsing and output of STIX XML content)
* stix/core/ : APIs for core STIX constructs (e.g., STIX Header, STIX Package)
* stix/common/ : APIs for common STIX constructs (e.g., Structured Text, Information Source)
* stix/indicator/ : APIs for STIX Indicator constructs
* stix/extensions/ : APIs for STIX extensions (e.g.CIQ Identity)

Please refer to examples for concrete examples of how to interact with the python-stix library
