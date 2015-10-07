# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.bindings.stix_common as common_binding

# relative
from .vocabs import VocabString, VocabFactory


class Names(stix.EntityList):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = _binding.NamesType
    _contained_type = VocabString
    _entity_factory = VocabFactory
    _binding_var = 'Name'
