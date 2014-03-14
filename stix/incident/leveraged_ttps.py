# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix.bindings.incident as incident_binding
from stix.common.related import GenericRelationshipList, RelatedTTP


class LeveragedTTPs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.LeveragedTTPsType
    _binding_var = "Leveraged_TTP"
    _contained_type = RelatedTTP
    _inner_name = "ttps"

    def __init__(self, leveraged_ttps=None, scope=None):
        if leveraged_ttps is None:
            leveraged_ttps = []
        super(LeveragedTTPs, self).__init__(*leveraged_ttps, scope=scope)
