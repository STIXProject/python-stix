# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
from stix.data_marking import MarkingStructure
import stix.bindings.extensions.marking.simple_marking as simple_marking_binding


@stix.register_extension
class SimpleMarkingStructure(MarkingStructure):
    _binding = simple_marking_binding
    _binding_class = simple_marking_binding.SimpleMarkingStructureType
    _namespace = 'http://data-marking.mitre.org/extensions/MarkingStructure#Simple-1'
    _XSI_TYPE = "simpleMarking:SimpleMarkingStructureType"

    statement = fields.TypedField("Statement")

    def __init__(self, statement=None):
        super(SimpleMarkingStructure, self).__init__()
        self.statement = statement
