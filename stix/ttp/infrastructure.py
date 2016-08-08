# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# mixbox
from mixbox import fields

# cybox
from cybox.core import Observables

# internal
import stix
from stix.common import StructuredTextList, VocabString
from stix.common.vocabs import AttackerInfrastructureType
import stix.bindings.ttp as ttp_binding
from mixbox import fields, entities

class Infrastructure(stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.InfrastructureType
    _namespace = "http://stix.mitre.org/TTP-1"
    
    
    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    title = fields.TypedField("Title")
    descriptions = fields.TypedField("Description", StructuredTextList)
    short_descriptions = fields.TypedField("Short_Description", StructuredTextList)
    types = fields.TypedField("Type", VocabString, multiple=True, key_name="types")
    observable_characterization = fields.TypedField("Observable_Characterization", Observables)
    
    
    def __init__(self, id_=None, idref=None, title=None, description=None, short_description=None):
        super(Infrastructure, self).__init__()
        self.id_ = id_
        self.idref = idref
        self.title = title
        self.description = StructuredTextList(description)
        self.short_description = StructuredTextList(short_description)


    @property
    def description(self):
        """A single description about the contents or purpose of this object.

        Default Value: ``None``

        Note:
            If this object has more than one description set, this will return
            the description with the lowest ordinality value.

        Returns:
            An instance of :class:`.StructuredText`
        """
        if self.descriptions is None:
            self.descriptions = StructuredTextList()
        return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        self.descriptions = StructuredTextList(value)

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".
        """
        self.descriptions.add(description)

    @property
    def short_description(self):
        """A single short description about the contents or purpose of this
        object.

        Default Value: ``None``

        Note:
            If this object has more than one short description set, this will
            return the description with the lowest ordinality value.

        Returns:
            An instance of :class:`.StructuredText`
        """
        if self.short_descriptions is None:
            self.short_descriptions = StructuredTextList()
        return next(iter(self.short_descriptions), None)

    @short_description.setter
    def short_description(self, value):
        self.short_descriptions = value

    def add_short_description(self, description):
        """Adds a description to the ``short_descriptions`` collection.

        This is the same as calling "foo.short_descriptions.add(bar)".
        """
        self.short_descriptions.add(description)

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
