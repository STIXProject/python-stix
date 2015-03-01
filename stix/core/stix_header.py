# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils as utils
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.stix_core as stix_core_binding
from stix.common import InformationSource, StructuredText, VocabString
from stix.data_marking import Marking

from stix.common.vocabs import PackageIntent

class STIXHeader(stix.Entity):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'

    def __init__(self, package_intents=None, description=None, handling=None,
        information_source=None, title=None, short_description=None):

        self.package_intents = package_intents
        self.title = title
        self.description = description
        self.short_description=short_description
        self.handling = handling
        self.information_source = information_source
        self.profiles = []

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        '''Sets the value of the description property.

        If the value is an instance of basestring, it will be coerced into an
        instance of StructuredText, with its 'text' property set to the input
        value.
        '''

        if value and isinstance(value, basestring):
            st = StructuredText()
            st.value = value
            self._description = st
        elif isinstance(value, StructuredText):
            self._description = value
        elif not value:
            self._description = None
        else:
            raise ValueError('value must be instance of StructuredText or basestring')

    @property
    def short_description(self):
        """The ``short_description`` property for this entity.

        Default Value: ``None``

        Note:
            If set to a value that is not an instance of
            :class:`stix.common.structured_text.StructuredText`, an attempt to
            will be made to convert the value into an instance of
            :class:`stix.common.structured_text.StructuredText`.

        Returns:
            An instance of
            :class:`stix.common.structured_text.StructuredText`

        """
        return self._short_description

    @short_description.setter
    def short_description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._short_description = value
            else:
                self._short_description = StructuredText(value=value)
        else:
            self._short_description = None


    @property
    def handling(self):
        return self._handling

    @handling.setter
    def handling(self, value):
        if value and not isinstance(value, Marking):
            raise ValueError('value must be instance of Marking')

        self._handling = value

    @property
    def package_intents(self):
        return self._package_intents

    @package_intents.setter
    def package_intents(self, value):
        self._package_intents = PackageIntents()
        if not value:
            return
        elif utils.is_sequence(value):
            for v in value:
                self.add_package_intent(v)
        else:
            self.add_package_intent(value)

    def add_package_intent(self, package_intent):
        if not package_intent:
            return
        elif isinstance(package_intent, VocabString):
            self.package_intents.append(package_intent)
        else:
            tmp_package_intent = PackageIntent(value=package_intent)
            self.package_intents.append(tmp_package_intent)

    @property
    def information_source(self):
        return self._information_source

    @information_source.setter
    def information_source(self, value):
        if value and not isinstance(value, InformationSource):
            raise ValueError('value must instance of InformationSource')

        self._information_source = value

    def add_profile(self, profile):
        """Adds a profile to the STIX Header. A Profile is represented by a string URI"""
        self.profiles.append(profile)

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.title = obj.Title
        return_obj.description = StructuredText.from_obj(obj.Description)
        return_obj.short_description = StructuredText.from_obj(obj.Short_Description)
        return_obj.handling = Marking.from_obj(obj.Handling)
        return_obj.information_source = InformationSource.from_obj(obj.Information_Source)

        if obj.Package_Intent:
            return_obj.package_intents = [VocabString.from_obj(x) for x in obj.Package_Intent]
        if obj.Profiles:
            return_obj.profiles = obj.Profiles.Profile

        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        super(STIXHeader, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding.STIXHeaderType()

        if self.title:
            return_obj.Title = self.title
        if self.package_intents:
            return_obj.Package_Intent = [x.to_obj(ns_info=ns_info) for x in self.package_intents]
        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.short_description:
            return_obj.Short_Description = self.short_description.to_obj(ns_info=ns_info)
        if self.handling:
            return_obj.Handling = self.handling.to_obj(ns_info=ns_info)
        if self.information_source:
            return_obj.Information_Source = self.information_source.to_obj(ns_info=ns_info)
        if self.profiles:
            profiles_obj = stix_common_binding.ProfilesType(Profile=self.profiles)
            return_obj.Profiles = profiles_obj

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.title = dict_repr.get('title')
        return_obj.package_intents = [VocabString.from_dict(x) for x in dict_repr.get('package_intents', [])]
        return_obj.description = StructuredText.from_dict(dict_repr.get('description'))
        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))
        return_obj.handling = Marking.from_dict(dict_repr.get('handling'))
        return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))
        return_obj.profiles = dict_repr.get('profiles')

        return return_obj

    def to_dict(self):
        d = {}
        if self.title:
            d['title'] = self.title
        if self.package_intents:
            d['package_intents'] = [x.to_dict() for x in self.package_intents]
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
        if self.handling:
            d['handling'] = self.handling.to_dict()
        if self.information_source:
            d['information_source'] = self.information_source.to_dict()
        if self.profiles:
            d['profiles'] = self.profiles

        return d


class PackageIntents(stix.EntityList):
    _namespace = "http://stix.mitre.org/stix-1"
    _contained_type = VocabString

    def _fix_value(self, value):
        return PackageIntent(value)
