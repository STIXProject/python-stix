:mod:`stix.threat_actor` Module
==================================

.. module:: stix.threat_actor

Overview
--------

The :mod:`stix.threat_actor` module implements :class:`.ThreatActor`.

ThreatActors are characterizations of malicious actors (or adversaries)
representing a cyber attack threat including presumed intent and historically
observed behavior.


Documentation Resources
~~~~~~~~~~~~~~~~~~~~~~~

* `Threat Actor Data Model <https://stixproject.github.io/data-model/1.2/ta/ThreatActorType/>`_


Classes
-------

.. autoclass:: ThreatActor
    :show-inheritance:
    :members: add_description, add_intended_effect, add_motivation,
        add_planning_and_operational_support, add_short_description,
        add_sophistication, add_type, description, descriptions, find, id_,
        identity, idref, information_source, intended_effects, motivations,
        planning_and_operational_supports, short_description, short_descriptions,
        sophistications, timestamp, title, to_dict, to_json, to_obj, types,
        version, walk

.. autoclass:: AssociatedActors
    :show-inheritance:
    :members:

.. autoclass:: AssociatedCampaigns
    :show-inheritance:
    :members:

.. autoclass:: ObservedTTPs
    :show-inheritance:
    :members:
