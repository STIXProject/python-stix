# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from . import KillChain, KillChainPhase


PHASE_RECONNAISSANCE = KillChainPhase(
    phase_id="stix:TTP-af1016d6-a744-4ed7-ac91-00fe2272185a",
    name="Reconnaissance",
    ordinality="1"
)

PHASE_WEAPONIZE = KillChainPhase(
    phase_id="stix:TTP-445b4827-3cca-42bd-8421-f2e947133c16",
    name="Weaponization",
    ordinality="2"
)

PHASE_DELIVERY  = KillChainPhase(
    phase_id="stix:TTP-79a0e041-9d5f-49bb-ada4-8322622b162d",
    name="Delivery",
    ordinality="3"
)

PHASE_EXPLOITATION = KillChainPhase(
    phase_id="stix:TTP-f706e4e7-53d8-44ef-967f-81535c9db7d0",
    name="Exploitation",
    ordinality="4"
)

PHASE_INSTALLATION  = KillChainPhase(
    phase_id="stix:TTP-e1e4e3f7-be3b-4b39-b80a-a593cfd99a4f",
    name="Installation",
    ordinality="5"
)

PHASE_COMMAND_AND_CONTROL = KillChainPhase(
    phase_id="stix:TTP-d6dc32b9-2538-4951-8733-3cb9ef1daae2",
    name="Command and Control",
    ordinality="6"

)

PHASE_ACTIONS_AND_OBJECTIVES  = KillChainPhase(
    phase_id="stix:TTP-786ca8f9-2d9a-4213-b38e-399af4a2e5d6",
    name="Actions on Objectives",
    ordinality="7"
)

LMCO_KILL_CHAIN_PHASES = (
    PHASE_RECONNAISSANCE, PHASE_WEAPONIZE, PHASE_DELIVERY,
    PHASE_EXPLOITATION, PHASE_INSTALLATION, PHASE_COMMAND_AND_CONTROL,
    PHASE_ACTIONS_AND_OBJECTIVES
)

LMCO_KILL_CHAIN = KillChain(
    id_="stix:TTP-af3e707f-2fb9-49e5-8c37-14026ca0a5ff",
    name="LM Cyber Kill Chain",
    definer="LMCO",
    reference="http://www.lockheedmartin.com/content/dam/lockheed/data/corporate/documents/LM-White-Paper-Intel-Driven-Defense.pdf"
)

LMCO_KILL_CHAIN.kill_chain_phases.extend(LMCO_KILL_CHAIN_PHASES)
