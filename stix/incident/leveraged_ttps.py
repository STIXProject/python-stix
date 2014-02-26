# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.incident as incident_binding
from stix.common.generic_relationship import GenericRelationshipList
from stix.common.related import RelatedTTP
from stix.ttp import TTP

class LeveragedTTPs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.LeveragedTTPsType

    def __init__(self, leveraged_ttps=None, scope=None):
        super(LeveragedTTPs, self).__init__(scope=scope)
        self.leveraged_ttps = None

    @property
    def leveraged_ttps(self):
        return self._leveraged_ttps

    @leveraged_ttps.setter
    def leveraged_ttps(self, value):
        self._leveraged_ttps = []

        if isinstance(value, list):
            for v in value:
                self.add_leveraged_ttp(v)
        else:
            self.add_leveraged_ttp(value)

    def add_leveraged_ttp(self, ttp):
        if not ttp:
            return
        if isinstance(ttp, RelatedTTP):
            self.leveraged_ttps.append(ttp)
        elif isinstance(ttp, TTP):
            self.leveraged_ttps.append(RelatedTTP(ttp=ttp))
        else:
            raise ValueError("Cannot add %s to leveraged_ttps list" % type(ttp))

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(LeveragedTTPs, self).to_obj(return_obj)
        return_obj.set_Leveraged_TTP([x.to_obj() for x in self.leveraged_ttps])
        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(LeveragedTTPs, cls).from_obj(obj, return_obj)

        if obj.get_Leveraged_TTP():
            return_obj.leveraged_ttps = [RelatedTTP.from_obj(x) for x in obj.get_Leveraged_TTP()]

        return return_obj

    def to_dict(self):
        d = super(LeveragedTTPs, self).to_dict()
        if self.leveraged_ttps:
            d['leveraged_ttps'] = [x.to_dict() for x in self.leveraged_ttps]

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(LeveragedTTPs, cls).from_dict(dict_repr, return_obj)
        return_obj.leveraged_ttps = [RelatedTTP.from_dict(x) for x in dict_repr.get('leveraged_ttps', [])]
        return return_obj

        