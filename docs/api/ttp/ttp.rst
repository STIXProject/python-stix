:mod:`stix.ttp` Module
======================

.. module:: stix.ttp

Overview
--------

The :mod:`stix.ttp` module implements :class:`.TTP`.

TTPs are representations of the behavior or modus operandi of cyber adversaries.


Documentation Resources
~~~~~~~~~~~~~~~~~~~~~~~

* `TTP Data Model <https://stixproject.github.io/data-model/1.2/ttp/TTPType/>`_

Classes
-------

.. autoclass:: TTP
    :show-inheritance:
    :members: add_description, add_intended_effect, add_kill_chain_phase,
        add_related_package, add_short_description, behavior, description,
        descriptions, exploit_targets, find, handling, id_, idref, information_source,
        intended_effects, kill_chain_phases, related_packages, related_ttps,
        resources, short_description, short_descriptions, timestamp, title,
        to_dict, to_json, to_obj, version, victim_targeting, walk
