# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix.bindings.ttp as ttp_binding
from stix.common.related import GenericRelationshipList, RelatedTTP


class RelatedTTPs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _binding = ttp_binding
    _binding_class = _binding.RelatedTTPsType
    _binding_var = "Related_TTP"
    _contained_type = RelatedTTP
    _inner_name = "ttps"

    def __init__(self, related_ttps=None, scope=None):
        if related_ttps is None:
            related_ttps = []
        super(RelatedTTPs, self).__init__(*related_ttps, scope=scope)

