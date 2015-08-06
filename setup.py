#!/usr/bin/env python

# Copyright (c) 2015 - The MITRE Corporation
# For license information, see the LICENSE.txt file

from os.path import abspath, dirname, join


from setuptools import setup, find_packages

BASE_DIR = dirname(abspath(__file__))
VERSION_FILE = join(BASE_DIR, 'stix', 'version.py')

def get_version():
    with open(VERSION_FILE) as f:
        for line in f.readlines():
            if line.startswith("__version__"):
                version = line.split()[-1].strip('"')
                return version
        raise AttributeError("Package does not have a __version__")


with open('README.rst') as f:
    readme = f.read()

extras_require = {
    'docs': [
        'Sphinx==1.3.1',
        'sphinx_rtd_theme==0.1.8',
    ],
    'test': [
        'nose==1.3.0',
        'tox==1.6.1',
        'maec>=4.1.0.13.dev1,<4.1.1.0',
    ],
}


install_requires = [
    'lxml>=2.3',
    'python-dateutil',
    'cybox>=2.1.0.13.dev0,<2.1.1.0',
    'mixbox>=0.0.10',
]


setup(
    name="stix",
    version=get_version(),
    author="STIX Project, MITRE Corporation",
    author_email="stix@mitre.org",
    description="An API for parsing and generating STIX content.",
    long_description=readme,
    url="http://stix.mitre.org",
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
