# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from os.path import abspath, dirname, join
from setuptools import setup, find_packages

INIT_FILE = join(dirname(abspath(__file__)), 'stix', '__init__.py')

def get_version():
    with open(INIT_FILE) as f:
        for line in f.readlines():
            if line.startswith("__version__"):
                version = line.split()[-1].strip('"')
                return version
        raise AttributeError("Package does not have a __version__")

with open('README.rst') as f:
    readme = f.read()

extras_require = {
    'docs': [
        'Sphinx==1.2.1',
        # TODO: remove when updating to Sphinx 1.3, since napoleon will be
        # included as sphinx.ext.napoleon
        'sphinxcontrib-napoleon==0.2.4',
    ],
    'test': [
        'nose==1.3.0',
        'tox==1.6.1',
        'maec>=4.1.0.10,<4.1.1.0'
    ],
}

setup(
    name="stix",
    version=get_version(),
    author="STIX Project, MITRE Corporation",
    author_email="stix@mitre.org",
    description="An API for parsing and generating STIX content.",
    long_description=readme,
    url="http://stix.mitre.org",
    packages=find_packages(),
    install_requires=['lxml>=2.3', 'python-dateutil', 'cybox>=2.1.0.9,<2.1.1.0'],
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
