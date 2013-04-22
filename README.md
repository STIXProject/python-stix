# python-stix

A python library for parsing, manipulating, and generating STIX content. The `python-stix` library
utilizes the STIX v1.0 bindings, is under heavy development and should be considered **PRE-ALPHA**.

For more information about STIX, see http://stix.mitre.org.


## Installation

The `python-stix` package depends on the `lxml` XML parsing library and the 
`python-cybox` CybOX library.

To build `lxml` on Ubuntu, you will need the following packages from the
Ubuntu package repository:

* python-dev
* libxml2-dev
* libxslt1-dev

Once the dependencies have been built, you can install `lxml` via pip:

<code>
$ pip install lxml
</code>

Note, on Windows it is recommended to download a pre-compiled distribution of `lxml`.

For more information about installing `lxml`, see
http://lxml.de/installation.html

The CybOX library can be found at its GitHub repositories:
CybOX: https://github.com/CybOXProject/python-cybox

To install, download or clone the repositories into their own folders. Once cloned or downloaded,
the setuptools script, setup.py can be run to install CybOX. To install, run the following 
commands from within the project directories:

<code>
$ python setup.py install
</code>

For more information about CybOX, see http://cybox.mitre.org
