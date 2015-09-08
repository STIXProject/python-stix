# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import signals
from mixbox.cache import Cached
from cybox.core import Observables

# internal
import stix
from stix.common import StructuredTextList, VocabString
from stix.common.vocabs import AttackerInfrastructureType
import stix.bindings.ttp as ttp_binding


class Infrastructure(Cached, stix.Entity):
    _binding = ttp_binding
    _binding_class = _binding.InfrastructureType
    _namespace = "http://stix.mitre.org/TTP-1"

    def __init__(self, id_=None, idref=None, title=None, description=None, short_description=None):
        self.id_ = id_
        self.idref = idref
        self.title = title
        self.description = description
        self.short_description = short_description
        self.types = None
        self.observable_characterization = None

    @property
    def id_(self):
        """The ``id_`` property serves as an identifier.

        Default Value: ``None``

        Note:
            Both the ``id_`` and ``idref`` properties cannot be set at the
            same time. **Setting one will unset the other!**

        Returns:
            A string id.

        """
        return self._id

    @id_.setter
    def id_(self, value):
        if not value:
            self._id = None
        else:
            self._id = value
            self.idref = None

    @property
    def idref(self):
        """The ``idref`` property must be set to the ``id_`` value of another
        object instance of the same type. An idref does not need to resolve to
        a local object instance.

        Default Value: ``None``.

        Note:
            Both the ``id_`` and ``idref`` properties cannot be set at the
            same time. **Setting one will unset the other!**

        Returns:
            The value of the ``idref`` property

        """
        return self._idref

    @idref.setter
    def idref(self, value):
        if not value:
            self._idref = None
        else:
            self._idref = value
            self.id_ = None  # unset id_ if idref is present

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def description(self):
        """A single description about the contents or purpose of this object.

        Default Value: ``None``

        Note:
            If this object has more than one description set, this will return
            the description with the lowest ordinality value.

        Returns:
            An instance of
            :class:`.StructuredText`

        """
        return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        self.descriptions = value

    @property
    def descriptions(self):
        """A :class:`.StructuredTextList` object, containing descriptions about
        the purpose or intent of this object.

        This is typically used for the purpose of providing multiple
        descriptions with different classificaton markings.

        Iterating over this object will yield its contents sorted by their
        ``ordinality`` value.

        Default Value: Empty :class:`.StructuredTextList` object.

        Note:
            IF this is set to a value that is not an instance of
            :class:`.StructuredText`, an effort will ne made to convert it.
            If this is set to an iterable, any values contained that are not
            an instance of :class:`.StructuredText` will be be converted.

        Returns:
            An instance of
            :class:`.StructuredTextList`

        """
        return self._description

    @descriptions.setter
    def descriptions(self, value):
        self._description = StructuredTextList(value)

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
        return next(iter(self.short_descriptions), None)

    @short_description.setter
    def short_description(self, value):
        self.short_descriptions = value

    @property
    def short_descriptions(self):
        """A :class:`.StructuredTextList` object, containing short descriptions
        about the purpose or intent of this object.

        This is typically used for the purpose of providing multiple
        short descriptions with different classificaton markings.

        Iterating over this object will yield its contents sorted by their
        ``ordinality`` value.

        Default Value: Empty :class:`.StructuredTextList` object.

        Note:
            IF this is set to a value that is not an instance of
            :class:`.StructuredText`, an effort will ne made to convert it.
            If this is set to an iterable, any values contained that are not
            an instance of :class:`.StructuredText` will be be converted.

        Returns:
            An instance of :class:`.StructuredTextList`

        """
        return self._short_description

    @short_descriptions.setter
    def short_descriptions(self, value):
        self._short_description = StructuredTextList(value)

    def add_short_description(self, description):
        """Adds a description to the ``short_descriptions`` collection.

        This is the same as calling "foo.short_descriptions.add(bar)".

        """
        self.short_descriptions.add(description)

    @property
    def types(self):
        return self._types

    @types.setter
    def types(self, value):
        self._types = InfraStructureTypes(value)

    def add_type(self, type_):
        self.types.append(type_)

    @property
    def observable_characterization(self):
        return self._observable_characterization

    @observable_characterization.setter
    def observable_characterization(self, value):
        self._set_var(Observables, observable_characterization=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(Infrastructure, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.Title = self.title

        if self.description:
            return_obj.Description = self.descriptions.to_obj(ns_info=ns_info)
        if self.short_description:
            return_obj.Short_Description = self.short_descriptions.to_obj(ns_info=ns_info)
        if self.types:
            return_obj.Type = [x.to_obj(ns_info=ns_info) for x in self.types]
        if self.observable_characterization:
            return_obj.Observable_Characterization = self.observable_characterization.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.id
        return_obj.title = obj.Title
        return_obj.descriptions = StructuredTextList.from_obj(obj.Description)
        return_obj.short_descriptions = StructuredTextList.from_obj(obj.Short_Description)
        return_obj.observable_characterization = Observables.from_obj(obj.Observable_Characterization)

        if obj.Type:
            return_obj.types = [VocabString.from_obj(x) for x in obj.Type]

        signals.emit("Entity.created.from_obj", return_obj, obj)
        return return_obj

    def to_dict(self):
        return super(Infrastructure, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = dict_repr.get('id')
        return_obj.title = dict_repr.get('title')
        return_obj.descriptions = StructuredTextList.from_dict(dict_repr.get('description'))
        return_obj.short_descriptions = StructuredTextList.from_dict(dict_repr.get('short_description'))
        return_obj.types = [VocabString.from_dict(x) for x in dict_repr.get('types', [])]
        return_obj.observable_characterization = Observables.from_dict(dict_repr.get('observable_characterization'))

        return return_obj


class InfraStructureTypes(stix.EntityList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _contained_type = VocabString
    _dict_as_list = True

    def _fix_value(self, value):
        return AttackerInfrastructureType(value)
