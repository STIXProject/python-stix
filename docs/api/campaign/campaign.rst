:mod:`stix.campaign` Module
==================================

.. module:: stix.campaign

Overview
--------

The :mod:`stix.campaign` module implements :class:`.Campaign`.

Campaigns are instances of ThreatActors pursuing an intent, as observed through
sets of Incidents and/or TTP, potentially across organizations.


Documentation Resources
~~~~~~~~~~~~~~~~~~~~~~~

* `Campaign Data Model <http://stixproject.github.io/data-model/1.2/campaign/CampaignType/>`_

Classes
-------

.. autoclass:: Campaign
    :show-inheritance:
    :members: activity, add_activity, add_description, add_intended_effect,
        add_short_description, attribution, description, descriptions, find, id_,
        idref, information_source, intended_effects, short_description,
        short_descriptions, status, timestamp, title, to_dict, to_json, to_obj,
        version, walk

.. autoclass:: AssociatedCampaigns
    :show-inheritance:
    :members:

.. autoclass:: Attribution
    :show-inheritance:
    :members:

.. autoclass:: Names
    :show-inheritance:
    :members:

.. autoclass:: RelatedIncidents
    :show-inheritance:
    :members:

.. autoclass:: RelatedIndicators
    :show-inheritance:
    :members:

.. autoclass:: RelatedTTPs
    :show-inheritance:
    :members:
