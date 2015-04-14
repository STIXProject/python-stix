# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding

# relative
from .names import Names


class CampaignRef(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.CampaignReferenceType

    def __init__(self, idref=None, timestamp=None, **kwargs):
        super(CampaignRef, self).__init__(**kwargs)
        self.idref = idref
        self.timestamp = timestamp
        self.names = None

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = utils.dates.parse_value(value)

    @property
    def names(self):
        return self._names

    @names.setter
    def names(self, value):
        self._names = Names(value)

    def add_name(self, name):
        self.names.append(name)

    def to_obj(self, return_obj=None, ns_info=None):

        if not return_obj:
            return_obj = self._binding_class()

        return_obj = super(CampaignRef, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        return_obj.idref = self.idref
        return_obj.timestamp = utils.serialize_value(self.timestamp)

        if self.names:
            return_obj.Names = self.names.to_obj()

        return return_obj

    def to_dict(self):
        return super(CampaignRef, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.idref = obj.idref
        return_obj.timestamp = obj.timestamp
        return_obj.names = Names.from_obj(obj.Names)

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        get = dict_repr.get
        return_obj.idref = get("idref")
        return_obj.timestamp = get("timestamp")
        return_obj.names = Names.from_dict(get("names"))

        return return_obj
