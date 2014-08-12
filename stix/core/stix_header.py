# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.stix_core as stix_core_binding
from stix.common import InformationSource, StructuredText, VocabString
from stix.data_marking import Marking

from stix.common.vocabs import PackageIntent

class STIXHeader(stix.Entity):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'

    def __init__(self, package_intents=None, description=None, handling=None, information_source=None, title=None):
        self.package_intents = package_intents
        self.title = title
        self.description = description
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
        elif isinstance(value, list):
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

        return_obj.title = obj.get_Title()
        return_obj.description = StructuredText.from_obj(obj.get_Description())
        return_obj.handling = Marking.from_obj(obj.get_Handling())
        return_obj.information_source = InformationSource.from_obj(obj.get_Information_Source())

        if obj.get_Package_Intent():
            return_obj.package_intents = [VocabString.from_obj(x) for x in obj.get_Package_Intent()]
        if obj.get_Profiles():
            return_obj.profiles = obj.get_Profiles().get_Profile()

        return return_obj

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding.STIXHeaderType()

        if self.title:
            return_obj.set_Title(self.title)
        if self.package_intents:
            return_obj.set_Package_Intent([x.to_obj() for x in self.package_intents])
        if self.description:
            return_obj.set_Description(self.description.to_obj())
        if self.handling:
            return_obj.set_Handling(self.handling.to_obj())
        if self.information_source:
            return_obj.set_Information_Source(self.information_source.to_obj())
        if self.profiles:
            profiles_obj = stix_common_binding.ProfilesType(Profile=self.profiles)
            return_obj.set_Profiles(profiles_obj)

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
