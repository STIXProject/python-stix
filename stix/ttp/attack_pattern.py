# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
from stix.common import StructuredText

# bindings
import stix.bindings.ttp as ttp_binding

from mixbox import fields


class AttackPattern(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.AttackPatternType
    _namespace = "http://stix.mitre.org/TTP-1"

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    title = fields.TypedField("Title")
    capec_id = fields.TypedField("capec_id")
    description = fields.TypedField("Description", type_="stix.common.StructuredText")
    short_description = fields.TypedField("Short_Description", type_="stix.common.StructuredText")

    def __init__(self, id_=None, idref=None, title=None, description=None, short_description=None):
        super(AttackPattern, self).__init__()

        self.id_ = id_
        self.idref = idref
        self.title = title
        self.description = description
        self.short_description = short_description
