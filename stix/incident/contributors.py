# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from cybox.common import Contributor

# internal
import stix
import stix.utils
import stix.bindings.incident as incident_binding


class Contributors(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.ContributorsType
    _contained_type = Contributor
    _binding_var = "Contributor"
    _inner_name = "contributors"
