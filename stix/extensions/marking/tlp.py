# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
from mixbox import fields

import stix
from stix.data_marking import MarkingStructure
import stix.bindings.extensions.marking.tlp as tlp_binding


@stix.register_extension
class TLPMarkingStructure(MarkingStructure):
    _binding = tlp_binding
    _binding_class = tlp_binding.TLPMarkingStructureType
    _namespace = 'http://data-marking.mitre.org/extensions/MarkingStructure#TLP-1'
    _XSI_TYPE = "tlpMarking:TLPMarkingStructureType"

    color = fields.TypedField("color")

    def __init__(self, color=None):
        super(TLPMarkingStructure, self).__init__()
        self.color = color
