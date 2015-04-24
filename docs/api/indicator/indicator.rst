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
    :members: to_obj, from_obj, to_dict, from_dict, producer, observable,
        observables, add_observable, alternative_id, add_alternative_id,
        valid_time_positions, add_valid_time_position, indicator_types,
        add_indicator_type, confidence, add_indicated_ttp,
        add_test_mechanism, add_related_indicator


.. autoclass:: CompositeIndicatorExpression
    :show-inheritance:
    :members: to_obj, from_obj, to_dict, from_dict


.. autoclass:: RelatedIndicators
    :show-inheritance:
    :members: to_obj, from_obj, to_dict, from_dict


.. autoclass:: RelatedCampaignRefs
    :show-inheritance:
    :members: to_obj, from_obj, to_dict, from_dict


.. autoclass:: SuggestedCOAs
    :show-inheritance:
    :members: to_obj, from_obj, to_dict, from_dict


.. autoclass:: IndicatorTypes
    :show-inheritance:
    :members: to_obj, from_obj, to_dict, from_dict
