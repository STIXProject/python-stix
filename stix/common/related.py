# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.stix_common as common_binding

from .generic_relationship import GenericRelationship
# Additional imports below to avoid circular imports


class _BaseRelated(GenericRelationship):
    """A base class for related types.

    This class is not a real STIX type and should not be directly instantiated.
    """
    # Subclasses should define
    # - _base_type
    # - _inner_var (This is the name of the contained XML element, and the
    #               lowercase version is used for the key name in the
    #               dictionary representation).

    def __init__(self, item=None, confidence=None,
                       information_source=None, relationship=None):
        super(_BaseRelated, self).__init__(confidence, information_source,
                                           relationship)
        self.item = item

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        if value and not isinstance(value, self._base_type):
            raise ValueError("Value must be instance of %s" %
                             self._base_type.__name__)

        self._item = value

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(_BaseRelated, self).to_obj(return_obj=return_obj)

        if self.item:
            setattr(return_obj, self._inner_var, self.item.to_obj())

        return return_obj

    def to_dict(self):
        d = super(_BaseRelated, self).to_dict()
        if self.item:
            d[self._inner_var.lower()] = self.item.to_dict()
        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(_BaseRelated, cls).from_obj(obj, return_obj)

        contained_item = getattr(obj, cls._inner_var)
        return_obj.item = cls._base_type.from_obj(contained_item)

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(_BaseRelated, cls).from_dict(dict_repr, return_obj)

        contained_item = dict_repr.get(cls._inner_var.lower())
        return_obj.item = cls._base_type.from_dict(contained_item)

        return return_obj


class RelatedThreatActor(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.RelatedThreatActorType
    # _base_type is set below
    _inner_var = "Threat_Actor"


class RelatedIndicator(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.RelatedIndicatorType
    # _base_type is set below
    _inner_var = "Indicator"


class RelatedTTP(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.RelatedTTPType
    # _base_type is set below
    _inner_var = "TTP"


# Avoid circular imports
from stix.threat_actor import ThreatActor
from stix.indicator import Indicator
from stix.ttp import TTP

# Patch the above types with the correct _bsae_types
RelatedThreatActor._base_type = ThreatActor
RelatedIndicator._base_type = Indicator
RelatedTTP._base_type = TTP
