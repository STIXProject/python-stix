# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import functools

# mixbox
from mixbox import fields
from mixbox import typedlist

# cybox
from cybox.core import Observable

# internal
import stix
import stix.bindings.stix_common as common_binding
import stix.bindings.stix_core as core_binding
import stix.bindings.report as report_binding

# deprecation warnings
from stix.utils import deprecated

# relative
from .vocabs import VocabField
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
    """Base class for concrete GenericRelationshipList types.

    Note:
        Subclasses must supply exactly one multiple TypedField.
    """

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

    @classmethod
    def _dict_as_list(cls):
        return False


class _RelatedPackageList(typedlist.TypedList):
    def __init__(self, *args):
        super(_RelatedPackageList, self).__init__(type=RelatedPackageRef, *args)

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
        return super(_RelatedPackageList, self)._is_valid(value)


class RelatedPackageRefs(stix.EntityList):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.RelatedPackageRefsType

    package = fields.TypedField(
        name="Package_Reference",
        type_=RelatedPackageRef,
        multiple=True,
        key_name="packages",
        listfunc=_RelatedPackageList
    )

    @classmethod
    def _dict_as_list(cls):
        return False


class _BaseRelated(GenericRelationship):
    """A base class for related types.

    This class is not a real STIX type and should not be directly instantiated.

    Note:
        Subclasses must supply a TypedField named `item`!
    """

    item = None  # override in subclass.

    def __init__(self, item=None, confidence=None,
                 information_source=None, relationship=None):

        super(_BaseRelated, self).__init__(
            confidence,
            information_source,
            relationship
        )

        self.item = item


class RelatedCampaign(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedCampaignType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("Campaign", type_="stix.campaign.Campaign")


class RelatedCOA(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedCourseOfActionType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("Course_Of_Action", type_="stix.coa.CourseOfAction")


class RelatedExploitTarget(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedExploitTargetType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("Exploit_Target", type_="stix.exploit_target.ExploitTarget")


class RelatedIdentity(_BaseRelated):
    _namespace = 'http://stix.mitre.org/common-1'
    _binding = common_binding
    _binding_class = common_binding.RelatedIdentityType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("Identity", type_="stix.common.identity.Identity", factory="stix.common.identity.IdentityFactory")


class RelatedIncident(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedIncidentType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("Incident", type_="stix.incident.Incident")

class RelatedIndicator(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedIndicatorType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("Indicator", type_="stix.indicator.Indicator")


class RelatedObservable(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedObservableType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("Observable", type_=Observable)

class RelatedThreatActor(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedThreatActorType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("Threat_Actor", type_="stix.threat_actor.ThreatActor")


class RelatedTTP(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedTTPType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("TTP", type_="stix.ttp.TTP")


class RelatedPackage(_BaseRelated):
    _namespace = "http://stix.mitre.org/stix-1"
    _binding = core_binding
    _binding_class = core_binding.RelatedPackageType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("Package", type_="stix.core.STIXPackage", preset_hook=deprecated.field)


class RelatedReport(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = common_binding.RelatedReportType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("Report", type_="stix.report.Report")


class RelatedCampaignRef(_BaseRelated):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.RelatedCampaignReferenceType

    # _BaseRelated requires an "item" field.
    item = fields.TypedField("Campaign", type_="stix.common.CampaignRef")


class RelatedPackages(GenericRelationshipList):
    _namespace = 'http://stix.mitre.org/stix-1'
    _binding = core_binding
    _binding_class = core_binding.RelatedPackagesType

    related_package = fields.TypedField("Related_Package", RelatedPackage, multiple=True, key_name="related_packages")


class RelatedReports(GenericRelationshipList):
    _namespace = 'http://stix.mitre.org/Report-1'
    _binding = report_binding
    _binding_class = report_binding.RelatedReportsType

    related_report = fields.TypedField("Related_Report", RelatedReport, multiple=True, key_name="related_reports")
