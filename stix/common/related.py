# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
from mixbox import fields

# internal
import stix
import stix.utils as utils
import stix.bindings.stix_common as common_binding
import stix.bindings.stix_core as core_binding
import stix.bindings.report as report_binding

from stix.base import AttributeField

# deprecation warnings
from stix.utils.deprecated import idref_deprecated, deprecated

# relative
from .vocabs import VocabString, VocabField
from .information_source import InformationSource
from .confidence import Confidence


ALLOWED_SCOPE = ('inclusive', 'exclusive')


def validate_scope(instance, value):
    if not value:
        return
    elif value in ALLOWED_SCOPE:
        return
    else:
        msg = "Scope must be one of {0}. Received '{1}'"
        msg = msg.format(ALLOWED_SCOPE, value)
        raise ValueError(msg)


class GenericRelationship(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.GenericRelationshipType

    confidence = fields.TypedField("Confidence", Confidence)
    information_source = fields.TypedField("Information_Source", InformationSource)
    relationship = VocabField("Relationship")

    def __init__(self, confidence=None, information_source=None, relationship=None):
        super(GenericRelationship, self).__init__()

        self.confidence = confidence
        self.information_source = information_source
        self.relationship = relationship

    # @property
    # def confidence(self):
    #     return self._confidence
    #
    # @confidence.setter
    # def confidence(self, value):
    #     self._set_var(Confidence, confidence=value)
    #
    # @property
    # def information_source(self):
    #     return self._information_source
    #
    # @information_source.setter
    # def information_source(self, value):
    #     self._set_var(InformationSource, try_cast=False, information_source=value)
    #
    # @property
    # def relationship(self):
    #     return self._relationship
    #
    # @relationship.setter
    # def relationship(self, value):
    #     self._set_vocab(relationship=value)
    #
    # @classmethod
    # def from_obj(cls, obj, return_obj=None):
    #     if not obj:
    #         return None
    #
    #     if not return_obj:
    #         return_obj = cls()
    #
    #     return_obj.confidence = Confidence.from_obj(obj.Confidence)
    #     return_obj.information_source = InformationSource.from_obj(obj.Information_Source)
    #     return_obj.relationship = VocabString.from_obj(obj.Relationship)
    #
    #     return return_obj
    #
    # def to_obj(self, return_obj=None, ns_info=None):
    #     super(GenericRelationship, self).to_obj(return_obj=return_obj, ns_info=ns_info)
    #
    #     if not return_obj:
    #         return_obj = self._binding_class()
    #
    #     if self.confidence:
    #         return_obj.Confidence = self.confidence.to_obj(ns_info=ns_info)
    #     if self.information_source:
    #         return_obj.Information_Source = self.information_source.to_obj(ns_info=ns_info)
    #     if self.relationship:
    #         return_obj.Relationship = self.relationship.to_obj(ns_info=ns_info)
    #
    #     return return_obj
    #
    # @classmethod
    # def from_dict(cls, dict_repr, return_obj=None):
    #     if not dict_repr:
    #         return None
    #
    #     if not return_obj:
    #         return_obj = cls()
    #
    #     #print "DICT", dict_repr
    #
    #     return_obj.confidence = Confidence.from_dict(dict_repr.get('confidence'))
    #     return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))
    #     return_obj.relationship = VocabString.from_dict(dict_repr.get('relationship'))
    #
    #     return return_obj
    #
    # def to_dict(self,):
    #     d = {}
    #     if self.confidence:
    #         d['confidence'] = self.confidence.to_dict()
    #     if self.information_source:
    #         d['information_source'] = self.information_source.to_dict()
    #     if self.relationship:
    #         d['relationship'] = self.relationship.to_dict()
    #
    #     return d


class RelatedPackageRef(GenericRelationship):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedPackageRefType

    idref = fields.IdrefField("idref")
    timestamp = fields.DateTimeField("timestamp")

    def __init__(self, idref=None, timestamp=None, confidence=None,
                 information_source=None, relationship=None):

        super(RelatedPackageRef, self).__init__(
            confidence=confidence,
            information_source=information_source,
            relationship=relationship
        )

        self.idref = idref
        self.timestamp = timestamp

    # def to_obj(self, return_obj=None, ns_info=None):
    #     if not return_obj:
    #         return_obj = self._binding_class()
    #
    #     return_obj = super(RelatedPackageRef, self).to_obj(return_obj=return_obj, ns_info=ns_info)
    #
    #     if self.idref:
    #         return_obj.idref = self.idref
    #     if self.timestamp:
    #         return_obj.timestamp = self.timestamp
    #
    #     return return_obj
    #
    # @property
    # def timestamp(self):
    #     return self._timestamp
    #
    # @timestamp.setter
    # def timestamp(self, value):
    #     self._timestamp = utils.dates.parse_value(value)
    #
    # def to_dict(self):
    #     d = super(RelatedPackageRef, self).to_dict()
    #
    #     if self.idref:
    #         d['idref'] = self.idref
    #     if self.timestamp:
    #         d['timestamp'] = utils.dates.serialize_value(self.timestamp)
    #
    #     return d
    #
    # @classmethod
    # def from_obj(cls, obj, return_obj=None):
    #     if not obj:
    #         return None
    #
    #     if not return_obj:
    #         return_obj = cls()
    #
    #     super(RelatedPackageRef, cls).from_obj(obj, return_obj)
    #
    #     return_obj.idref = obj.idref
    #     return_obj.timestamp = obj.timestamp
    #
    #     return return_obj
    #
    # @classmethod
    # def from_dict(cls, dict_repr, return_obj=None):
    #     if not dict_repr:
    #         return None
    #
    #     if not return_obj:
    #         return_obj = cls()
    #
    #     super(RelatedPackageRef, cls).from_dict(dict_repr, return_obj)
    #
    #     return_obj.idref = dict_repr.get("idref")
    #     return_obj.timestamp = dict_repr.get("timestamp")
    #
    #     return return_obj

class GenericRelationshipEntity(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.GenericRelationshipListType
    
    _ALLOWED_SCOPE = ('inclusive', 'exclusive')
    
    scope = AttributeField("scope")
    
    def __init__(self, scope=None, *args):

        super(GenericRelationshipEntity, self).__init__(*args)
        self.scope = scope
    
    def __nonzero__(self):
        return (
            super(GenericRelationshipList, self).__nonzero__() or
            bool(self.scope)
        )


class GenericRelationshipList(stix.EntityList):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.GenericRelationshipListType

    scope = fields.TypedField("scope", preset_hook=validate_scope)

    def __init__(self, scope=None, *args):
        super(GenericRelationshipList, self).__init__(*args)
        self.scope = scope

    def __nonzero__(self):
        return (
            super(GenericRelationshipList, self).__nonzero__() or
            bool(self.scope)
        )

    # def to_obj(self, return_obj=None, ns_info=None):
    #     list_obj = super(GenericRelationshipList, self).to_obj(
    #         return_obj=return_obj,
    #         ns_info=ns_info
    #     )
    #
    #     list_obj.scope = self.scope
    #     return list_obj
    #
    # @classmethod
    # def from_obj(cls, obj, return_obj=None):
    #     if not obj:
    #         return None
    #
    #     if return_obj is None:
    #         return_obj = cls()
    #
    #     super(GenericRelationshipList, cls).from_obj(
    #         obj,
    #         return_obj=return_obj,
    #         contained_type=cls._contained_type,
    #         binding_var=cls._binding_var
    #     )
    #
    #     return_obj.scope = obj.scope
    #
    #     return return_obj
    #
    # @classmethod
    # def from_dict(cls, dict_repr, return_obj=None):
    #     if not dict_repr:
    #         return None
    #
    #     if return_obj is None:
    #         return_obj = cls()
    #
    #     super(GenericRelationshipList, cls).from_dict(
    #         dict_repr,
    #         return_obj=return_obj,
    #         contained_type=cls._contained_type,
    #         inner_name=cls._inner_name
    #     )
    #
    #     return_obj.scope = dict_repr.get('scope')
    #
    #     return return_obj


class RelatedPackages(GenericRelationshipList):
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding = core_binding
    _binding_class = core_binding.RelatedPackagesType
    _binding_var = "Related_Package"
    # _contained_type is patched in common/__init__.py
    _inner_name = "related_packages"


class RelatedReports(GenericRelationshipList):
    _namespace = 'http://stix.mitre.org/Report-1'
    _binding = report_binding
    _binding_class = report_binding.RelatedReportsType
    _binding_var = "Related_Report"
    # _contained_type is patched in common/__init__.py
    _inner_name = "related_reports"


class RelatedPackageRefs(stix.EntityList):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.RelatedPackageRefsType
    _binding_var = "Package_Reference"
    _contained_type = RelatedPackageRef
    _inner_name = "packages"

    def _fix_value(self, value):
        from stix.core import STIXPackage

        if isinstance(value, STIXPackage) and value.id_:
            return RelatedPackageRef(idref=value.id_, timestamp=value.timestamp)

        fmt = ("Cannot add type '{0}' to RelatedPackageRefs collection. "
               "Expected RelatedPackageRef or STIXPackage")
        error = fmt.format(type(value))
        raise TypeError(error)

    def _is_valid(self, value):
        deprecated(value)
        return stix.EntityList._is_valid(self, value)


class _BaseRelated(GenericRelationship):
    """A base class for related types.

    This class is not a real STIX type and should not be directly instantiated.
    """
    # Subclasses should define
    # - _base_type
    # - _inner_var (This is the name of the contained XML element, and the
    #               lowercase version is used for the key name in the
    #               dictionary representation).

    _base_type = None
    _inner_var = None

    def __init__(self, item=None, confidence=None,
                 information_source=None, relationship=None):

        super(_BaseRelated, self).__init__(
            confidence,
            information_source,
            relationship
        )
        self.item = item

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, value):
        self._set_item(value)

    def _set_item(self, value):
        if value and not isinstance(value, self._base_type):
            error = "Value must be instance of %s" % self._base_type.__name__
            raise ValueError(error)

        self._item = value

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(_BaseRelated, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if self.item:
            setattr(return_obj, self._inner_var, self.item.to_obj(ns_info=ns_info))

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


class RelatedExploitTarget(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedExploitTargetType
    # _base_type is set in common/__init__.py
    _inner_var = "Exploit_Target"


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


class RelatedPackage(_BaseRelated):
    _namespace = "http://stix.mitre.org/stix-1"
    _binding = core_binding
    _binding_class = core_binding.RelatedPackageType
    # _base_type is set in common/__init__.py
    _inner_var = "Package"

    @_BaseRelated.item.setter
    def item(self, value):
        idref_deprecated(value)
        _BaseRelated.item.fset(self, value)

class RelatedReport(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedReportType
    # _base_type is set in common/__init__.py
    _inner_var = "Report"


class RelatedCampaignRef(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.RelatedCampaignReferenceType
    # _base_type is set in common/__init__.py
    _inner_var = "Campaign"
