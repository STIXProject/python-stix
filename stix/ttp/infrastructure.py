# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# mixbox
from mixbox import fields

# cybox
from cybox.core import Observables

# internal
import stix
from stix.common import StructuredText, VocabString
from stix.common.vocabs import AttackerInfrastructureType
import stix.bindings.ttp as ttp_binding


class Infrastructure(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.InfrastructureType
    _namespace = "http://stix.mitre.org/TTP-1"

    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    title = fields.TypedField("Title")
    description = fields.TypedField("Description", StructuredText)
    short_description = fields.TypedField("Short_Description", StructuredText)
    types = fields.TypedField("Type", VocabString, multiple=True, key_name="types")
    observable_characterization = fields.TypedField("Observable_Characterization", Observables)

    def __init__(self, id_=None, idref=None, title=None, description=None,
                 short_description=None):

        super(Infrastructure, self).__init__()

        self.id_ = id_
        self.idref = idref
        self.title = title
        self.description = description
        self.short_description = short_description

    def add_type(self, type_):
        self.types.append(type_)


class InfraStructureTypes(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _contained_type = VocabString

    @classmethod
    def _dict_as_list(cls):
        return True

    def _fix_value(self, value):
        return AttackerInfrastructureType(value)
