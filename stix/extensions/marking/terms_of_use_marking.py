# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
from stix.data_marking import MarkingStructure
import stix.bindings.extensions.marking.terms_of_use_marking as tou_marking_binding


@stix.register_extension
class TermsOfUseMarkingStructure(MarkingStructure):
    _binding = tou_marking_binding
    _binding_class = tou_marking_binding.TermsOfUseMarkingStructureType
    _namespace = 'http://data-marking.mitre.org/extensions/MarkingStructure#Terms_Of_Use-1'
    _XSI_TYPE = "TOUMarking:TermsOfUseMarkingStructureType"

    terms_of_use = fields.TypedField("Terms_Of_Use")

    def __init__(self, terms_of_use=None):
        super(TermsOfUseMarkingStructure, self).__init__()
        self.terms_of_use = terms_of_use
