:mod:`stix.incident` Module
===========================

.. module:: stix.incident

Overview
--------

The :mod:`stix.incident` module implements :class:`.Incident`.

Incidents are discrete instances of Indicators affecting an organization along
with information discovered or decided during an incident response investigation.


Documentation Resources
~~~~~~~~~~~~~~~~~~~~~~~

* `Incident Data Model <https://stixproject.github.io/data-model/1.2/incident/IncidentType/>`_

Classes
-------

.. autoclass:: Incident
    :show-inheritance:
    :members: add_affected_asset, add_category, add_coa_requested, add_coa_taken,
        add_coordinator, add_description, add_discovery_method, add_external_id,
        add_intended_effect, add_related_indicator, add_related_observable,
        add_related_package, add_responder, add_short_description, add_victim,
        affected_assets, categories, coa_requested, coa_taken, confidence,
        coordinators, description, descriptions, discovery_methods, external_ids,
        find, handling, id_, idref, impact_assessment, information_source,
        intended_effects, related_indicators, related_observables, related_packages,
        reporter, responders, security_compromise, short_description,
        short_descriptions, status, time, timestamp, title, to_dict, to_json,
        to_obj, version, victims, walk

.. autoclass:: AttributedThreatActors
    :show-inheritance:
    :members:

.. autoclass:: LeveragedTTPs
    :show-inheritance:
    :members:

.. autoclass:: RelatedIndicators
    :show-inheritance:
    :members:

.. autoclass:: RelatedObservables
    :show-inheritance:
    :members:

.. autoclass:: RelatedIncidents
    :show-inheritance:
    :members:
