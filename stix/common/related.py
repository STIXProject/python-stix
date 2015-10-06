# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
from mixbox import fields

# internal
import stix
import stix.bindings.stix_common as common_binding
import stix.bindings.stix_core as core_binding
import stix.bindings.report as report_binding

# deprecation warnings
from stix.utils import deprecated

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


class GenericRelationshipEntity(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.GenericRelationshipListType
    
    _ALLOWED_SCOPE = ('inclusive', 'exclusive')
    
    scope = fields.TypedField("scope")
    
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
        return (super(GenericRelationshipList, self).__nonzero__() or
                bool(self.scope))


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
        deprecated.warn(value)
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

    def to_obj(self, ns_info=None):
        obj = super(_BaseRelated, self).to_obj(ns_info=ns_info)

        if self.item:
            setattr(obj, self._inner_var, self.item.to_obj(ns_info=ns_info))

        return obj

    def to_dict(self):
        d = super(_BaseRelated, self).to_dict()

        if self.item:
            d[self._inner_var.lower()] = self.item.to_dict()

        return d

    @classmethod
    def from_obj(cls, cls_obj):
        if not cls_obj:
            return None

        obj = super(_BaseRelated, cls).from_obj(cls_obj)
        contained_item = getattr(cls_obj, cls._inner_var)
        obj.item = cls._base_type.from_obj(contained_item)

        return obj

    @classmethod
    def from_dict(cls, cls_dict):
        if not cls_dict:
            return None

        obj = super(_BaseRelated, cls).from_dict(cls_dict)
        contained_item = cls_dict.get(cls._inner_var.lower())
        obj.item = cls._base_type.from_dict(contained_item)

        return obj


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
        deprecated.idref(value)
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
