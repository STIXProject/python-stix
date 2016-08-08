# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
import stix.bindings.report as report_binding
from stix.common import InformationSource, StructuredTextList
from stix.common.vocabs import VocabField, ReportIntent
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
    _binding_class = _binding.HeaderType
    _namespace = 'http://stix.mitre.org/Report-1'

    title = fields.TypedField("Title")
    descriptions = fields.TypedField("Description", type_=StructuredTextList)
    short_descriptions = fields.TypedField("Short_Description", type_=StructuredTextList)
    intents = VocabField("Intent", ReportIntent, multiple=True, key_name="intents")
    handling = fields.TypedField("Handling", Marking)
    information_source = fields.TypedField("Information_Source", InformationSource)

    def __init__(self, title=None, description=None, short_description=None,
                 handling=None, intents=None, information_source=None):

        super(Header, self).__init__()

        self.intents = intents
        self.title = title
        self.description = StructuredTextList(description)
        self.short_description = StructuredTextList(short_description)
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

    def add_intent(self, intent):
        """Adds :class:`.VocabString` object to the :attr:`intents`
        collection.

        If the input is not an instance of :class:`.VocabString`, an effort
        will be made to convert it into an instance of :class:`.ReportIntent`.

        """
        self.intents.append(intent)
