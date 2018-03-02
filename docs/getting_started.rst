Getting Started
===============

This page gives an introduction to **python-stix** and how to use it.  

.. note:: 

	This page is being actively worked on; feedback is always welcome.

Prerequisites
-------------

The python-stix library provides an API for creating or processing STIX content. As such, it is a developer tool that can be leveraged by those who know Python 2.7/3.3+ and are familiar with object-oriented programming practices, Python package layouts, and are comfortable with the installation of Python libraries. To contribute code to the python-stix repository, users must be familiar with `git`_ and `GitHub pull request`_ methodologies. Understanding XML, XML Schema, and the STIX language is also incredibly helpful when using python-stix in an application.

.. _git: http://git-scm.com/documentation
.. _GitHub pull request: https://help.github.com/articles/using-pull-requests

Your First STIX Application
---------------------------

Once you have installed python-stix, you can begin writing Python applications that consume or create STIX content!

.. note::

	The *python-stix* library provides **bindings** and **APIs**, both of which can be used to parse and write STIX XML files. For in-depth description of the *APIs, bindings, and the differences between the two*, please refer to :doc:`api_vs_bindings/index`

Creating a STIX Package
***********************

.. code-block:: python
	
	from stix.core import STIXPackage                      # Import the STIX Package API
	from stix.report import Report                         # Import the STIX Report API
	from stix.report.header import Header                  # Import the STIX Report Header API

	stix_package = STIXPackage()                           # Create an instance of STIXPackage
	stix_report = Report()                                 # Create a Report instance
	stix_report.header = Header()                          # Create a header for the report
	stix_report.header.description = "Getting Started!"    # Set the description
	stix_package.add(stix_report)                          # Add the report to our STIX Package

	print(stix_package.to_xml())                           # Print the XML for this STIX Package
	
Parsing STIX XML
****************

.. code-block:: python

	from stix.core import STIXPackage        # Import the STIX Package API

	fn = 'stix_content.xml'                  # The STIX content filename
	stix_package = STIXPackage.from_xml(fn)  # Parse using the from_xml() method
	
Examples
--------

The python-stix GitHub repository contains several example scripts that help illustrate the capabilities of the APIs. These examples can be found `here`_. 
Accompanying walkthrough `slides`_ are available.
These scripts are simple command line utilities that can be executed by passing the name of the script to a Python interpreter.

.. _slides: http://tiny.cc/pystixpreso

.. _here: https://github.com/STIXProject/python-stix/tree/master/examples

.. code-block:: python

	Example:
	$ python ex_01.py
	
.. note::

	You must install python-stix before running these example scripts.
