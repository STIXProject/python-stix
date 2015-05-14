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
    :members: add_alternative_id, add_description, add_indicated_ttp,
        add_indicator_type, add_kill_chain_phase, add_object, add_observable,
        add_related_campaign, add_related_indicator, add_related_package,
        add_short_description, add_test_mechanism, add_valid_time_position,
        alternative_id, confidence, description, descriptions, find,
        get_produced_time, get_received_time, handling, id_, idref,
        indicated_ttps, indicator_types, information_source, kill_chain_phases,
        likely_impact, negate, observable, observable_composition_operator,
        observables, producer, related_campaigns, related_indicators,
        related_packages, set_produced_time, set_producer_identity,
        set_received_time, short_description, short_descriptions,
        test_mechanisms, timestamp, title, to_dict, to_json, to_obj, to_xml,
        valid_time_positions, version, walk


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
