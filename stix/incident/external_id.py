# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding


class ExternalID(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding  = incident_binding
    _binding_class = incident_binding.ExternalIDType

    def __init__(self, value=None, source=None):
        super(ExternalID, self).__init__()
        self.value = value
        self.source = source

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, value):
        self._source = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(ExternalID, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        obj = self._binding_class()
        obj.valueOf_ = self.value
        obj.source = self.source
        return obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.value = obj.valueOf_
        return_obj.source = obj.source
        return return_obj

    def to_dict(self):    
        d  = {}
        d['value'] = self.value
        d['source'] = self.source
        return d

    @classmethod
    def from_dict(cls, dict_, return_obj=None):
        if not dict_:
            return None

        if not return_obj:
            return_obj = cls()

        if not isinstance(dict_, dict):
            return_obj.value = dict_
        else:
            return_obj.source = dict_.get('source')
            return_obj.value = dict_.get('value')

        return return_obj
