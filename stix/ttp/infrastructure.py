# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# mixbox
from mixbox import fields
from mixbox.cache import Cached

# cybox
from cybox.core import Observables

# internal
import stix
from stix.common import StructuredTextList, VocabString
from stix.common.vocabs import AttackerInfrastructureType
import stix.bindings.ttp as ttp_binding
from mixbox import fields, entities

class Infrastructure(Cached, entities.Entity):
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
        self.description = description
        self.short_description = short_description


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
        return next(iter(self.descriptions or []), None)

    @description.setter
    def description(self, value):
        self.descriptions = value

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
        return next(iter(self.short_descriptions or []), None)

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

#     def to_obj(self, return_obj=None, ns_info=None):
#         super(Infrastructure, self).to_obj(return_obj=return_obj, ns_info=ns_info)
# 
#         if not return_obj:
#             return_obj = self._binding_class()
# 
#         return_obj.id = self.id_
#         return_obj.Title = self.title
# 
#         if self.description:
#             return_obj.Description = self.descriptions.to_obj(ns_info=ns_info)
#         if self.short_description:
#             return_obj.Short_Description = self.short_descriptions.to_obj(ns_info=ns_info)
#         if self.types:
#             return_obj.Type = [x.to_obj(ns_info=ns_info) for x in self.types]
#         if self.observable_characterization:
#             return_obj.Observable_Characterization = self.observable_characterization.to_obj(ns_info=ns_info)
# 
#         return return_obj
# 
#     @classmethod
#     def from_obj(cls, obj, return_obj=None):
#         if not obj:
#             return None
#         if not return_obj:
#             return_obj = cls()
# 
#         return_obj.id_ = obj.id
#         return_obj.title = obj.Title
#         return_obj.descriptions = StructuredTextList.from_obj(obj.Description)
#         return_obj.short_descriptions = StructuredTextList.from_obj(obj.Short_Description)
#         return_obj.observable_characterization = Observables.from_obj(obj.Observable_Characterization)
# 
#         if obj.Type:
#             return_obj.types = [VocabString.from_obj(x) for x in obj.Type]
# 
#         return return_obj
# 
#     def to_dict(self):
#         return super(Infrastructure, self).to_dict()
# 
#     @classmethod
#     def from_dict(cls, dict_repr, return_obj=None):
#         if not dict_repr:
#             return None
#         if not return_obj:
#             return_obj = cls()
# 
#         return_obj.id_ = dict_repr.get('id')
#         return_obj.title = dict_repr.get('title')
#         return_obj.descriptions = StructuredTextList.from_dict(dict_repr.get('description'))
#         return_obj.short_descriptions = StructuredTextList.from_dict(dict_repr.get('short_description'))
#         return_obj.types = [VocabString.from_dict(x) for x in dict_repr.get('types', [])]
#         return_obj.observable_characterization = Observables.from_dict(dict_repr.get('observable_characterization'))
# 
#         return return_obj

class InfraStructureTypes(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _contained_type = VocabString
    _dict_as_list = True

    def _fix_value(self, value):
        return AttackerInfrastructureType(value)
