# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from __future__ import absolute_import

import stix
import stix.bindings.stix_common as common_binding

from .confidence import Confidence
from .information_source import InformationSource
from .vocabs import VocabString


class Relationship(VocabString):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding


class GenericRelationship(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.GenericRelationshipType

    def __init__(self, confidence=None, information_source=None, relationship=None):
        self.confidence = confidence
        self.information_source = information_source
        self.relationship = relationship

    @property
    def confidence(self):
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        if value:
            if isinstance(value, Confidence):
                self._confidence = value
            else:
                self._confidence = Confidence(value=value)
        else:
            self._confidence = None

    @property
    def information_source(self):
        return self._information_source

    @information_source.setter
    def information_source(self, value):
        if value and not isinstance(value, InformationSource):
            raise ValueError('value must be instance of InformationSource')

        self._information_source = value

    @property
    def relationship(self):
        return self._relationship

    @relationship.setter
    def relationship(self, value):
        if value:
            if isinstance(value, Relationship):
                self._relationship = value
            else:
                self._relationship = Relationship(value=value)
        else:
            self._relationship = None

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.confidence = Confidence.from_obj(obj.get_Confidence())
        return_obj.information_source = InformationSource.from_obj(obj.get_Information_Source())
        return_obj.relationship = Relationship.from_obj(obj.get_Relationship())

        return return_obj

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        if self.confidence:
            return_obj.set_Confidence(self.confidence.to_obj())
        if self.information_source:
            return_obj.set_Information_Source(self.information_source.to_obj())
        if self.relationship:
            return_obj.set_Relationship(self.relationship.to_obj())

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.confidence = Confidence.from_dict(dict_repr.get('confidence'))
        return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))
        return_obj.relationship = Relationship.from_dict(dict_repr.get('relationship'))

        return return_obj

    def to_dict(self,):
        d = {}
        if self.confidence:
            d['confidence'] = self.confidence.to_dict()
        if self.information_source:
            d['information_source'] = self.information_source.to_dict()
        if self.relationship:
            d['relationship'] = self.relationship.to_dict()

        return d


class RelatedPackageRef(GenericRelationship):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedPackageRefType

    def __init__(self, **kwargs):
        super(RelatedPackageRef, self).__init__(**kwargs)
        self.idref = None
        self.timestamp = None

    def to_obj(self):
        return_obj = super(RelatedPackageRef, self).to_obj()

        if self.idref:
            return_obj.set_idref(self.idref)
        if self.timestamp:
            return_obj.set_timestamp(self.timestamp)

        return return_obj

    def to_dict(self):
        d = super(RelatedPackageRef, self).to_dict()

        if self.idref:
            d['idref'] = self.idref
        if self.timestamp:
            d['timestamp'] = self.timestamp

        return d

    @classmethod
    def from_obj(cls, obj):
        return_obj = cls()

        super(RelatedPackageRef, cls).from_obj(obj, return_obj)

        return_obj.idref = obj.get_idref()
        return_obj.timestamp = obj.get_timestamp()

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(RelatedPackageRef, cls).from_dict(dict_repr, return_obj)

        return_obj.idref = dict_repr.get("idref")
        return_obj.timestamp = dict_repr.get("timestamp")

        return return_obj


class GenericRelationshipList(stix.EntityList):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.GenericRelationshipListType

    def __init__(self, scope=None, *args):
        super(GenericRelationshipList, self).__init__()
        self.scope = scope

    def __nonzero__(self):
        return super(GenericRelationshipList, self).__nonzero__() \
                or bool(self.scope)

    def to_obj(self):
        list_obj = super(GenericRelationshipList, self).to_obj()
        list_obj.set_scope(self.scope)
        return list_obj

    def to_dict(self):
        d = super(GenericRelationshipList, self).to_dict()
        if self.scope:
            d['scope'] = self.scope
        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if return_obj is None:
            return_obj = cls()

        super(GenericRelationshipList, cls).from_obj(obj,
                return_obj=return_obj,
                contained_type=cls._contained_type,
                binding_var=cls._binding_var)

        return_obj.scope = obj.get_scope()

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not isinstance(dict_repr, dict):
            return None

        if return_obj is None:
            return_obj = cls()

        super(GenericRelationshipList, cls).from_dict(dict_repr,
                return_obj=return_obj,
                contained_type=cls._contained_type,
                inner_name=cls._inner_name)

        return_obj.scope = dict_repr.get('scope')

        return return_obj


class RelatedPackageRefs(stix.EntityList):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.RelatedPackageRefsType
    _binding_var = "Package_Reference"
    _contained_type = RelatedPackageRef
    _inner_name = "packages"


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


class RelatedCampaign(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedCampaignType
    # _base_type is set in common/__init__.py
    _inner_var = "Campaign"

class RelatedCOA(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedCourseOfActionType
    # _base_type is set in common/__init__.py
    _inner_var = "Course_Of_Action"

class RelatedIdentity(_BaseRelated):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.RelatedIdentityType
    # _base_type is set in common/__init__.py
    _inner_var = "Identity"


class RelatedIncident(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedIncidentType
    # _base_type is set in common/__init__.py
    _inner_var = "Incident"


class RelatedIndicator(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedIndicatorType
    # _base_type is set in common/__init__.py
    _inner_var = "Indicator"


class RelatedObservable(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedObservableType
    # _base_type is set in common/__init__.py
    _inner_var = "Observable"


class RelatedThreatActor(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedThreatActorType
    # _base_type is set in common/__init__.py
    _inner_var = "Threat_Actor"


class RelatedTTP(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedTTPType
    # _base_type is set in common/__init__.py
    _inner_var = "TTP"
