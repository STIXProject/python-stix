# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
from stix.common import InformationSource, StructuredText, Profiles
from stix.common.vocabs import VocabField, PackageIntent
from stix.data_marking import Marking
import stix.bindings.stix_core as stix_core_binding


class STIXHeader(stix.Entity):
    """The STIX Package Header.

    Args:
        handling: The data marking section of the Header.
        information_source: The :class:`.InformationSource` section of the
            Header.
        package_intents: A collection of :class:`.VocabString`
            defining the intent of the parent :class:`.STIXPackage`.
        description: A description of the intent or purpose
            of the parent :class:`.STIXPackage`.
        short_description: A short description of the intent
            or purpose of the parent :class:`.STIXPackage`.
        title: The title of the :class:`.STIXPackage`.

    Attributes:
        profiles: A collection of STIX Profiles the parent
            :class:`.STIXPackage` conforms to.
        title: The title of the parent :class:`.STIXPackage`.

    """
    _binding = stix_core_binding
    _binding_class = _binding.STIXHeaderType
    _namespace = 'http://stix.mitre.org/stix-1'

    title = fields.TypedField("Title")
    package_intents = VocabField("Package_Intent", PackageIntent, multiple=True)
    description = fields.TypedField("Description", StructuredText)
    short_description = fields.TypedField("Short_Description", StructuredText)
    handling = fields.TypedField("Handling", Marking)
    information_source = fields.TypedField("Information_Source", InformationSource)
    profiles = fields.TypedField("Profiles", Profiles)

    def __init__(self, package_intents=None, description=None, handling=None,
                 information_source=None, title=None, short_description=None):

        super(STIXHeader, self).__init__()

        self.package_intents = package_intents
        self.title = title
        self.description = description
        self.short_description = short_description
        self.handling = handling
        self.information_source = information_source
        self.profiles = None

    def add_package_intent(self, package_intent):
        self.package_intents.append(package_intent)

    def add_profile(self, profile):
        """Adds a profile to the STIX Header. A Profile is represented by a
        string URI.

        """
        self.profiles.append(profile)
