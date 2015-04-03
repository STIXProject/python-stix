:mod:`stix.common.kill_chains` Module
=====================================

.. module:: stix.common.kill_chains

Classes
-------

.. autoclass:: KillChain
	:show-inheritance:
	:members:

.. autoclass:: KillChains
	:show-inheritance:
	:members:

.. autoclass:: KillChainPhase
	:show-inheritance:
	:members:

.. autoclass:: KillChainPhaseReference
	:show-inheritance:
	:members:

.. autoclass:: KillChainPhasesReference
	:show-inheritance:
	:members:

Lockheed Martin Kill Chain
--------------------------

There is a shortcuts for adding kill chain phases from the `Lockheed
Martin Cyber Kill Chain`__ to indicators:

.. code:: python

    from stix.common.kill_chains.lmco import PHASE_RECONNAISSANCE
    from stix.indicator import Indicator
    i = Indicator()
    i.add_kill_chain_phase(PHASE_RECONNAISSANCE)
    print i.to_xml(include_namespaces=False)

.. code:: xml

    <indicator:Indicator id="example:indicator-2bb1c0ea-7dd8-40fb-af64-7199f00719c1"
            timestamp="2015-03-17T19:14:22.797675+00:00" xsi:type='indicator:IndicatorType'>
        <indicator:Kill_Chain_Phases>
            <stixCommon:Kill_Chain_Phase phase_id="stix:TTP-af1016d6-a744-4ed7-ac91-00fe2272185a"/>
        </indicator:Kill_Chain_Phases>
    </indicator:Indicator>

__ http://www.lockheedmartin.com/us/what-we-do/information-technology/cyber-security/cyber-kill-chain.html
