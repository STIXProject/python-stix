# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.stix_core as stix_core_binding
from stix.common import InformationSource, StructuredText, VocabString
from stix.data_marking import Handling


class PackageIntent(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:PackageIntentVocab-1.0'


class STIXHeader(stix.Entity):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    
    def __init__(self, package_intent=None, description=None, handling=None, information_source=None, title=None):
        self.package_intent = package_intent
        self.title = title
        self.description = description
        self.handling = handling
        self.information_source = information_source

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

        if isinstance(value, basestring):
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
        if value and not isinstance(value, Handling):
            raise ValueError('value must be instance of Handling')

        self._handling = value

    @property
    def package_intent(self):
        return self._package_intent

    @package_intent.setter
    def package_intent(self, value):
        if value and not isinstance(value, PackageIntent):
            value = PackageIntent(value)

        self._package_intent = value

    @property
    def information_source(self):
        return self._information_source

    @information_source.setter
    def information_source(self, value):
        if value and not isinstance(value, InformationSource):
            raise ValueError('value must instance of InformationSource')

        self._information_source = value

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.title = obj.get_Title()
        return_obj.package_intent = PackageIntent.from_obj(obj.get_Package_Intent())
        return_obj.description = StructuredText.from_obj(obj.get_Description())
        return_obj.handling = Handling.from_obj(obj.get_Handling())
        return_obj.information_source = InformationSource.from_obj(obj.get_Information_Source())

        return return_obj

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding.STIXHeaderType()

        if self.title:
            return_obj.set_Title(self.title)

        if self.package_intent:
            return_obj.set_Package_Intent(self.package_intent.to_obj())

        if self.description:
            return_obj.set_Description(self.description.to_obj())

        if self.handling:
            return_obj.set_Handling(self.handling.to_obj())

        if self.information_source:
            return_obj.set_Information_Source(self.information_source.to_obj())

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.title = dict_repr.get('title')
        return_obj.package_intent = PackageIntent.from_dict(dict_repr.get('package_intent'))

        desc_dict = dict_repr.get('description')
        return_obj.description = StructuredText.from_dict(desc_dict)

        handling_dict = dict_repr.get('handling')
        return_obj.handling = Handling.from_dict(handling_dict)

        info_dict = dict_repr.get('information_source', None)
        return_obj.information_source = InformationSource.from_dict(info_dict)

        return return_obj

    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}

        if self.title:
            return_dict['title'] = self.title

        if self.package_intent:
            return_dict['package_intent'] = self.package_intent.to_dict()

        if self.description:
            return_dict['description'] = self.description.to_dict()

        if self.handling:
            return_dict['handling'] = self.handling.to_dict()

        if self.information_source:
            return_dict['information_source'] = self.information_source.to_dict()

        return return_dict
