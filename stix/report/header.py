# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import signals

# internal
import stix
import stix.bindings.report as report_binding
from stix.common import InformationSource, StructuredTextList, VocabString
from stix.common.vocabs import ReportIntent
from stix.data_marking import Marking


class Header(stix.Entity):
    """The Report Header.

    Args:
        handling: The data marking section of the Header.
        information_source: The :class:`.InformationSource` section of the
            Header.
        intents: A collection of :class:`.VocabString` defining the intent
            of the parent :class:`.Report`.
        description: A description of the intent or purpose of the parent
            :class:`.Report`.
        short_description: A short description of the intent or purpose of
            the parent :class:`.Report`.
        title: The title of the :class:`.Report`.

    Attributes:
        title: The title of the parent :class:`.Report`.

    """
    _binding = report_binding
    _namespace = 'http://stix.mitre.org/Report-1'

    def __init__(self, title=None, description=None, short_description=None,
                 handling=None, intents=None, information_source=None):

        self.intents = intents
        self.title = title
        self.description = description
        self.short_description = short_description
        self.handling = handling
        self.information_source = information_source

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
    def handling(self):
        """The :class:`.Marking` section of this Header. This section contains
        data marking information.

        """
        return self._handling

    @handling.setter
    def handling(self, value):
        self._set_var(Marking, try_cast=False, handling=value)

    @property
    def intents(self):
        """A collection of :class:`.VocabString` controlled vocabulary
        objects.

        """
        return self._intents

    @intents.setter
    def intents(self, value):
        self._intents = _ReportIntents(value)

    def add_intent(self, intent):
        """Adds :class:`.VocabString` object to the :attr:`intents`
        collection.

        If the input is not an instance of :class:`.VocabString`, an effort
        will be made to convert it into an instance of :class:`.ReportIntent`.

        """
        self.intents.append(intent)

    @property
    def information_source(self):
        """The :class:`.InformationSource` section of the Header.

        """
        return self._information_source

    @information_source.setter
    def information_source(self, value):
        self._set_var(InformationSource, try_cast=False, information_source=value)

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.title = obj.Title
        return_obj.descriptions = StructuredTextList.from_obj(obj.Description)
        return_obj.short_descriptions = StructuredTextList.from_obj(obj.Short_Description)
        return_obj.handling = Marking.from_obj(obj.Handling)
        return_obj.information_source = InformationSource.from_obj(obj.Information_Source)
        return_obj.intents = _ReportIntents.from_obj(obj.Intent)

        signals.emit("Entity.created.from_obj", return_obj, obj)
        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        super(Header, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding.HeaderType()

        if self.title:
            return_obj.Title = self.title
        if self.intents:
            return_obj.Intent = self.intents.to_obj(ns_info=ns_info)
        if self.descriptions:
            return_obj.Description = self.descriptions.to_obj(ns_info=ns_info)
        if self.short_descriptions:
            return_obj.Short_Description = self.short_descriptions.to_obj(ns_info=ns_info)
        if self.handling:
            return_obj.Handling = self.handling.to_obj(ns_info=ns_info)
        if self.information_source:
            return_obj.Information_Source = self.information_source.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        get = dict_repr.get

        return_obj.title = get('title')
        return_obj.intents = _ReportIntents.from_list(get('intents'))
        return_obj.descriptions = StructuredTextList.from_dict(get('description'))
        return_obj.short_descriptions = StructuredTextList.from_dict(get('short_description'))
        return_obj.handling = Marking.from_dict(get('handling'))
        return_obj.information_source = InformationSource.from_dict(get('information_source'))

        return return_obj

    def to_dict(self):
        return super(Header, self).to_dict()


# NOT AN ACTUAL STIX TYPE!
class _ReportIntents(stix.TypedList):
    _contained_type = VocabString

    def _fix_value(self, value):
        return ReportIntent(value)
