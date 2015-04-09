:mod:`stix.indicator.indicator` Module
======================================

.. module:: stix.indicator.indicator

Overview
--------
The :mod:`stix.indicator.indicator` module implements ``IndicatorType`` STIX
Language construct. The ``IndicatorType`` characterizes a cyber threat indicator
made up of a pattern identifying certain observable conditions as well as
contextual information about the patterns meaning, how and when it should be
acted on, etc.

Documentation Resources
~~~~~~~~~~~~~~~~~~~~~~~

* `Indicator Data Model <http://stixproject.github.io/data-model/1.1.1/indicator/IndicatorType/>`_
* `Indicator Idioms <http://stixproject.github.io/documentation/idioms/#Indicator>`_


Classes
-------

.. autoclass:: Indicator
    :show-inheritance:
    :members:

.. autoclass:: CompositeIndicatorExpression
    :show-inheritance:
    :members:

.. autoclass:: RelatedIndicators
    :show-inheritance:
    :members:

.. autoclass:: SuggestedCOAs
    :show-inheritance:
    :members:

.. autoclass:: IndicatorTypes
    :show-inheritance:
    :members:
