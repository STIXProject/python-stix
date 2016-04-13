# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import fields

# internal
import stix
import stix.bindings.stix_common as common_binding

# relative
from .vocabs import VocabField


class Names(stix.EntityList):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = _binding.NamesType

    name = VocabField("Name", multiple=True)
