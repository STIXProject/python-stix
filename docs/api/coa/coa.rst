:mod:`stix.coa` Module
======================

.. module:: stix.coa

Overview
--------

The :mod:`stix.coa` module implements :class:`.CourseOfAction`.

CoursesOfAction are specific measures to be taken to address threat whether
they are corrective or preventative to address ExploitTargets, or responsive to
counter or mitigate the potential impacts of Incidents


Documentation Resources
~~~~~~~~~~~~~~~~~~~~~~~

* `Course Of Action Data Model <http://stixproject.github.io/data-model/1.2/coa/CourseOfActionType/>`_


Classes
-------

.. autoclass:: CourseOfAction
    :show-inheritance:
    :members: add_description, add_short_description, cost, description,
        descriptions, efficacy, find, handling, id_, idref, impact,
        information_source, objective, short_description, short_descriptions,
        stage, structured_coa, timestamp, title, to_dict, to_json, to_obj, type_,
        version, walk

.. autoclass:: RelatedCOAs
    :show-inheritance:
    :members:
