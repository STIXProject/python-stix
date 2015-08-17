# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding
from stix.base import AttributeField, ElementField

# relative
from .names import Names


class CampaignRef(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.CampaignReferenceType

    idref = AttributeField("idref")
    timestamp = AttributeField("timestamp") #preset_hook = lambda inst, value : if value is not None or not isinstance(value, datetime.datetime): inst.set_timestamp(utils.dates.parse_value(value))
    names = ElementField("Names", Names)

    def __init__(self, idref=None, timestamp=None, **kwargs):
        super(CampaignRef, self).__init__(**kwargs)
        self.idref = idref
        self.timestamp = timestamp
        self.names = None

    def add_name(self, name):
        self.names.append(name)
        
    #timestamp.setter
    #def timestamp(self, value):
    #    self._timestamp = utils.dates.parse_value(value)
        
"""
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
"""