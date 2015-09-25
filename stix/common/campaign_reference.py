# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox.fields import DateTimeField

# internal
import stix
import stix.bindings.stix_common as common_binding
from stix.base import AttributeField, ElementField

# relative
from .names import Names


class CampaignRef(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.CampaignReferenceType

    idref = AttributeField("idref")
    timestamp = DateTimeField("timestamp")
    names = ElementField("Names", Names)

    def __init__(self, idref=None, timestamp=None):
        super(CampaignRef, self).__init__()
        
        self.idref = idref
        self.timestamp = timestamp
        self.names = None

    def add_name(self, name):
        self.names.append(name)
