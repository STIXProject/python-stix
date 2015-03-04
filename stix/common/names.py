# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.bindings.stix_common as common_binding

# relative
from .vocabs import VocabString


class Names(stix.EntityList):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.NamesType
    _contained_type = VocabString
    _binding_var = 'Name'
    _inner_name = 'names'
    _dict_as_list = True
