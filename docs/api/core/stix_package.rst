:mod:`stix.core.stix_package` Module
====================================

.. module:: stix.core.stix_package

Overview
--------

The :mod:`stix.core.stix_package` module implements :class:`.STIXPackage`.

STIXType defines a bundle of information characterized in the Structured Threat
Information eXpression (STIX) language.


Documentation Resources
~~~~~~~~~~~~~~~~~~~~~~~

* `STIX Package Data Model <https://stixproject.github.io/data-model/1.2/stix/STIXType/>`_


Classes
-------

.. autoclass:: STIXPackage
    :show-inheritance:
    :members: add_course_of_action, add_related_package, add_incident,
        stix_header, add_indicator, add, version, indicators, exploit_targets,
        id_, add_exploit_target, add_report, timestamp, add_threat_actor,
        campaigns, add_observable, to_obj, related_packages, idref,
        courses_of_action, reports, ttps, incidents, to_dict, observables,
        add_ttp, threat_actors, add_campaign, walk, to_obj, to_xml, find,
        to_json, to_dict, from_xml


.. autoclass:: RelatedPackages
    :show-inheritance:
    :members:
