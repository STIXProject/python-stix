# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
from stix.utils import deprecated
from stix.common import InformationSource, StructuredTextList, Profiles
from stix.common.vocabs import VocabField, PackageIntent
from stix.data_marking import Marking
import stix.bindings.stix_core as stix_core_binding


class STIXHeader(stix.Entity):
    """The STIX Package Header.

    Args:
        handling: The data marking section of the Header.
        information_source: The :class:`.InformationSource` section of the
            Header.
        package_intents: **DEPRECATED**. A collection of :class:`.VocabString`
            defining the intent of the parent :class:`.STIXPackage`.
        description: **DEPRECATED**. A description of the intent or purpose
            of the parent :class:`.STIXPackage`.
        short_description: **DEPRECATED**. A short description of the intent
            or purpose of the parent :class:`.STIXPackage`.
        title: **DEPRECATED**. The title of the :class:`.STIXPackage`.

    Attributes:
        profiles: A collection of STIX Profiles the parent
            :class:`.STIXPackage` conforms to.
        title: **DEPRECATED**. The title of the parent :class:`.STIXPackage`.

    """
    _binding = stix_core_binding
    _binding_class = _binding.STIXHeaderType
    _namespace = 'http://stix.mitre.org/stix-1'

    title = fields.TypedField("Title", preset_hook=deprecated.field)
    package_intents = VocabField("Package_Intent", PackageIntent, multiple=True, preset_hook=deprecated.field)
    descriptions = fields.TypedField("Description", type_=StructuredTextList, preset_hook=deprecated.field)
    short_descriptions = fields.TypedField("Short_Description", type_=StructuredTextList, preset_hook=deprecated.field)
    handling = fields.TypedField("Handling", Marking)
    information_source = fields.TypedField("Information_Source", InformationSource)
    profiles = fields.TypedField("Profiles", Profiles)

    def __init__(self, package_intents=None, description=None, handling=None,
                 information_source=None, title=None, short_description=None):

        super(STIXHeader, self).__init__()

        self.package_intents = package_intents
        self.title = title
        self.description = StructuredTextList(description)
        self.short_description = StructuredTextList(short_description)
        self.handling = handling
        self.information_source = information_source
        self.profiles = None

    @property
    def description(self):
        """**DEPRECATED**. A single description about the contents or
        purpose of this object.

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
        self.descriptions = StructuredTextList(value)

    def add_description(self, description):
        """**DEPRECATED**. Adds a description to the ``descriptions``
        collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        deprecated.warn(description)
        self.descriptions.add(description)

    @property
    def short_description(self):
        """**DEPRECATED**. A single short description about the contents or
        purpose of this object.

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
        self.short_descriptions = StructuredTextList(value)

    def add_short_description(self, description):
        """**DEPRECATED**. Adds a description to the ``short_descriptions``
        collection.

        This is the same as calling "foo.short_descriptions.add(bar)".

        """
        deprecated.warn(description)
        self.short_descriptions.add(description)


    def add_package_intent(self, package_intent):
        """**DEPRECATED**. Adds :class:`.VocabString` object to the
        :attr:`package_intents` collection.

        If the input is not an instance of :class:`.VocabString`, an effort
        will be made to convert it into an instance of :class:`.PackageIntent`.

        """
        deprecated.warn(package_intent)
        self.package_intents.append(package_intent)

    def add_profile(self, profile):
        """Adds a profile to the STIX Header. A Profile is represented by a
        string URI.

        """
        self.profiles.append(profile)

