# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.ttp as ttp_binding
from stix.common.generic_relationship import GenericRelationshipList
from stix.common.related import RelatedTTP
from stix.ttp import TTP

class RelatedTTPs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/TTP-1"
    _binding = ttp_binding
    _binding_class = _binding.RelatedTTPsType

    def __init__(self, related_ttps=None, scope=None):
        super(RelatedTTPs, self).__init__(scope=scope)
        self.related_ttps = None

    @property
    def related_ttps(self):
        return self._related_ttps

    @related_ttps.setter
    def related_ttps(self, value):
        self._related_ttps = []

        if isinstance(value, list):
            for v in value:
                self.add_related_ttp(v)
        else:
            self.add_related_ttp(value)

    def add_related_ttp(self, ttp):
        if not ttp:
            return
        if isinstance(ttp, RelatedTTP):
            self.related_ttps.append(ttp)
        elif isinstance(ttp, TTP):
            self.related_ttps.append(RelatedTTP(ttp=ttp))
        else:
            raise ValueError("Cannot add %s to related_ttps list" % type(ttp))

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(RelatedTTPs, self).to_obj(return_obj)
        return_obj.set_Related_TTP([x.to_obj() for x in self.related_ttps])
        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(RelatedTTPs, cls).from_obj(obj, return_obj)

        if obj.get_Related_TTP():
            return_obj.related_ttps = [RelatedTTP.from_obj(x) for x in obj.get_Related_TTP()]

        return return_obj

    def to_dict(self):
        d = super(RelatedTTPs, self).to_dict()
        if self.related_ttps:
            d['related_ttps'] = [x.to_dict() for x in self.related_ttps]

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        super(RelatedTTPs, cls).from_dict(dict_repr, return_obj)
        return_obj.related_ttps = [RelatedTTP.from_dict(x) for x in dict_repr.get('related_ttps', [])]
        return return_obj
