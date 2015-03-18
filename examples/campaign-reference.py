#!/usr/bin/env python
# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

"""
Demonstrates the methods for adding related Campaign references to an
Indicator object.
"""

from stix.core import STIXPackage
from stix.common import CampaignRef
from stix.campaign import Campaign
from stix.indicator import Indicator


def main():
    # Build Campaign instances
    camp1 = Campaign(title='Campaign 1')
    camp2 = Campaign(title='Campaign 2')

    # Build a CampaignRef object, setting the `idref` to the `id_` value of
    # our `camp2` Campaign object.
    campaign_ref = CampaignRef(idref=camp2.id_)

    # Build an Indicator object.
    i = Indicator()

    # Add CampaignRef object pointing to `camp2`.
    i.add_related_campaign(campaign_ref)

    # Add Campaign object, which gets promoted into an instance of
    # CampaignRef type internally. Only the `idref` is set.
    i.add_related_campaign(camp1)

    # Build our STIX Package and attach our Indicator and Campaign objects.
    package = STIXPackage()
    package.add_indicator(i)
    package.add_campaign(camp1)
    package.add_campaign(camp2)

    # Print!
    print package.to_xml()

if __name__ == "__main__":
    main()
