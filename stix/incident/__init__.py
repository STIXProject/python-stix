# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
from mixbox import fields

import stix
import stix.bindings.incident as incident_binding
from stix.common import vocabs
from stix.common import Statement, VocabString, InformationSource, Confidence
from stix.common.vocabs import VocabField
from stix.common.identity import Identity, IdentityFactory
from stix.common.related import (GenericRelationshipList, RelatedIndicator,
    RelatedThreatActor, RelatedTTP, RelatedObservable, RelatedIncident,
    RelatedPackageRefs)

# relative
from .affected_asset import AffectedAsset
from .property_affected import PropertyAffected  # noqa
from .time import Time
from .external_id import ExternalID
from .impact_assessment import ImpactAssessment
from .coa import COATaken, COARequested, COATime # noqa
from .history import History


class Incident(stix.BaseCoreComponent):
    """Implementation of the STIX Incident.

    Args:
        id_ (optional): An identifier. If ``None``, a value will be generated
            via ``mixbox.idgen.create_id()``. If set, this will unset the
            ``idref`` property.
        idref (optional): An identifier reference. If set this will unset the
            ``id_`` property.
        timestamp (optional): A timestamp value. Can be an instance of
            ``datetime.datetime`` or ``str``.
        description: A description of the purpose or intent of this object.
        short_description: A short description of the intent
            or purpose of this object.
        title: The title of this object.

    """
    _binding = incident_binding
    _binding_class = _binding.IncidentType
    _namespace = "http://stix.mitre.org/Incident-1"
    _version = "1.2"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1", "1.2")
    _ID_PREFIX = 'incident'

    status = fields.TypedField("Status", vocabs.IncidentStatus)
    time = fields.TypedField("Time", Time)
    victims = fields.TypedField("Victim", Identity, factory=IdentityFactory, multiple=True, key_name="victims")
    attributed_threat_actors = fields.TypedField("Attributed_Threat_Actors", type_="stix.incident.AttributedThreatActors")
    related_indicators = fields.TypedField("Related_Indicators", type_="stix.incident.RelatedIndicators")
    related_observables = fields.TypedField("Related_Observables", type_="stix.incident.RelatedObservables")
    related_incidents = fields.TypedField("Related_Incidents", type_="stix.incident.RelatedIncidents")
    related_packages = fields.TypedField("Related_Packages", RelatedPackageRefs)
    affected_assets = fields.TypedField("Affected_Assets", type_="stix.incident.AffectedAssets")
    categories = fields.TypedField("Categories", type_="stix.incident.IncidentCategories")
    intended_effects = fields.TypedField("Intended_Effect", Statement, multiple=True, key_name="intended_effects")
    leveraged_ttps = fields.TypedField("Leveraged_TTPs", type_="stix.incident.LeveragedTTPs")
    discovery_methods = fields.TypedField("Discovery_Method", vocabs.DiscoveryMethod, multiple=True, key_name="discovery_methods")
    reporter = fields.TypedField("Reporter", InformationSource)
    responders = fields.TypedField("Responder", InformationSource, multiple=True, key_name="responders")
    coordinators = fields.TypedField("Coordinator", InformationSource, multiple=True, key_name="coordinators")
    external_ids = fields.TypedField("External_ID", ExternalID, multiple=True, key_name="external_ids")
    impact_assessment = fields.TypedField("Impact_Assessment", ImpactAssessment)
    security_compromise = fields.TypedField("Security_Compromise", vocabs.SecurityCompromise)
    confidence = fields.TypedField("Confidence", Confidence)
    coa_taken = fields.TypedField("COA_Taken", COATaken, multiple=True)
    coa_requested = fields.TypedField("COA_Requested", COARequested, multiple=True)
    history = fields.TypedField("History", History)

    def __init__(self, id_=None, idref=None, timestamp=None, title=None, description=None, short_description=None):
        super(Incident, self).__init__(
            id_=id_,
            idref=idref,
            timestamp=timestamp,
            title=title,
            description=description,
            short_description=short_description
        )
    def add_intended_effect(self, value):
        """Adds a :class:`.Statement` object to the :attr:`intended_effects`
        collection.

        If `value` is a string, an attempt will be made to convert it into an
        instance of :class:`.Statement`.

        """
        self.intended_effects.append(value)


    def add_victim(self, victim):
        """Adds a :class:`.IdentityType` value to the :attr:`victims`
        collection.

        """
        self._victims.append(victim)

    def add_category(self, category):
        """Adds a :class:`.VocabString` object to the :attr:`categories`
        collection.

        If `category` is a string, an attempt will be made to convert it into
        an instance of :class:`.IncidentCategory`.

        """
        self.categories.append(category)
    
    def add_affected_asset(self, v):
        """Adds a :class:`.AffectedAsset` object to the :attr:`affected_assets`
        collection.

        """
        self.affected_assets.append(v)

    def add_discovery_method(self, value):
        """Adds a :class:`.VocabString` object to the :attr:`discovery_methods`
        collection.

        If `value` is a string, an attempt will be made to convert it to an
        instance of :class:`.DiscoveryMethod`.

        """
        self.discovery_methods.append(value)

    def add_responder(self, value):
        """Adds a :class:`.InformationSource` object to the :attr:`responders`
        collection.

        """
        self.responders.append(value)

    def add_coordinator(self, value):
        """Adds a :class:`.InformationSource` object to the :attr:`coordinators`
        collection.

        """
        self.coordinators.append(value)

    def add_external_id(self, value):
        """Adds a :class:`.ExternalID` object to the :attr:`external_ids`
        collection.

        """
        self.external_ids.append(value)

    def add_coa_taken(self, value):
        """Adds a :class:`.COATaken` object to the :attr:`coas_taken`
        collection.

        """
        self.coa_taken.append(value)

    def add_coa_requested(self, value):
        """Adds a :class:`.COARequested` object to the :attr:`coas_requested`
        collection.

        """
        self.coa_requested.append(value)

    def add_related_indicator(self, value):
        """Adds an Related Indicator to the :attr:`related_indicators` list
        property of this :class:`Incident`.

        The `indicator` parameter must be an instance of
        :class:`.RelatedIndicator` or :class:`Indicator`.

        If the `indicator` parameter is ``None``, no item wil be added to the
        ``related_indicators`` list property.

        Calling this method is the same as calling ``append()`` on the
        ``related_indicators`` property.

        See Also:
            The :class:`RelatedIndicators` documentation.

        Note:
            If the `indicator` parameter is not an instance of
            :class:`.RelatedIndicator` an attempt will be
            made to convert it to one.

        Args:
            indicator: An instance of :class:`Indicator` or
                :class:`.RelatedIndicator`.

        Raises:
            ValueError: If the `indicator` parameter cannot be converted into
                an instance of :class:`.RelatedIndicator`

        """
        self.related_indicators.append(value)

    def add_related_observable(self, value):
        """Adds a Related Observable to the ``related_observables`` list
        property of this :class:`Incident`.

        The `observable` parameter must be an instance of
        :class:`.RelatedObservable` or :class:`Observable`.

        If the `observable` parameter is ``None``, no item will be added to the
        ``related_observables`` list property.

        Calling this method is the same as calling ``append()`` on the
        ``related_observables`` property.

        See Also:
            The :class:`RelatedObservables` documentation.

        Note:
            If the `observable` parameter is not an instance of
            :class:`.RelatedObservable` an attempt will be
            made to convert it to one.

        Args:
            observable: An instance of :class:`Observable` or
                :class:`.RelatedObservable`.

        Raises:
            ValueError: If the `value` parameter cannot be converted into
                an instance of :class:`.RelatedObservable`

        """
        self.related_observables.append(value)

    def add_related_package(self, value):
        self.related_packages.append(value)

    # def to_obj(self, return_obj=None, ns_info=None):
    #     if not return_obj:
    #         return_obj = self._binding_class()
    # 
    #     super(Incident, self).to_obj(return_obj=return_obj, ns_info=ns_info)
    # 
    #     if self.time:
    #         return_obj.Time = self.time.to_obj(ns_info=ns_info)
    #     if self.victims:
    #         return_obj.Victim = self.victims.to_obj(ns_info=ns_info)
    #     if self.attributed_threat_actors:
    #         return_obj.Attributed_Threat_Actors = self.attributed_threat_actors.to_obj(ns_info=ns_info)
    #     if self.related_indicators:
    #         return_obj.Related_Indicators = self.related_indicators.to_obj(ns_info=ns_info)
    #     if self.related_observables:
    #         return_obj.Related_Observables = self.related_observables.to_obj(ns_info=ns_info)
    #     if self.related_incidents:
    #         return_obj.Related_Incidents = self.related_incidents.to_obj(ns_info=ns_info)
    #     if self.categories:
    #         return_obj.Categories = self.categories.to_obj(ns_info=ns_info)
    #     if self.intended_effects:
    #         return_obj.Intended_Effect = self.intended_effects.to_obj(ns_info=ns_info)
    #     if self.leveraged_ttps:
    #         return_obj.Leveraged_TTPs = self.leveraged_ttps.to_obj(ns_info=ns_info)
    #     if self.affected_assets:
    #         return_obj.Affected_Assets = self.affected_assets.to_obj(ns_info=ns_info)
    #     if self.discovery_methods:
    #         return_obj.Discovery_Method = self.discovery_methods.to_obj(ns_info=ns_info)
    #     if self.reporter:
    #         return_obj.Reporter = self.reporter.to_obj(ns_info=ns_info)
    #     if self.responders:
    #         return_obj.Responder = self.responders.to_obj(ns_info=ns_info)
    #     if self.coordinators:
    #         return_obj.Coordinator = self.coordinators.to_obj(ns_info=ns_info)
    #     if self.external_ids:
    #         return_obj.External_ID = self.external_ids.to_obj(ns_info=ns_info)
    #     if self.impact_assessment:
    #         return_obj.Impact_Assessment = self.impact_assessment.to_obj(ns_info=ns_info)
    #     if self.security_compromise:
    #         return_obj.Security_Compromise = self.security_compromise.to_obj(ns_info=ns_info)
    #     if self.confidence:
    #         return_obj.Confidence = self.confidence.to_obj(ns_info=ns_info)
    #     if self.coa_taken:
    #         return_obj.COA_Taken = self.coa_taken.to_obj(ns_info=ns_info)
    #     if self.coa_requested:
    #         return_obj.COA_Requested = self.coa_requested.to_obj(ns_info=ns_info)
    #     if self.status:
    #         return_obj.Status = self.status.to_obj(ns_info=ns_info)
    #     if self.history:
    #         return_obj.History = self.history.to_obj(ns_info=ns_info)
    #     if self.related_packages:
    #         return_obj.Related_Packages = self.related_packages.to_obj(ns_info=ns_info)
    #     if self.contacts:
    #         return_obj.Contact = self.contacts.to_obj(ns_info=ns_info)
    #     if self.url:
    #         return_obj.URL = self.url
    # 
    #     return return_obj
    # 
    # @classmethod
    # def from_obj(cls, obj, return_obj=None):
    #     if not obj:
    #         return None
    # 
    #     if not return_obj:
    #         return_obj = cls()
    # 
    #     super(Incident, cls).from_obj(obj, return_obj=return_obj)
    # 
    #     if isinstance(obj, cls._binding_class):
    #         return_obj.time = Time.from_obj(obj.Time)
    #         return_obj.victims = _Victims.from_obj(obj.Victim)
    #         return_obj.categories = IncidentCategories.from_obj(obj.Categories)
    #         return_obj.intended_effects = _IntendedEffects.from_obj(obj.Intended_Effect)
    #         return_obj.affected_assets = AffectedAssets.from_obj(obj.Affected_Assets)
    #         return_obj.discovery_methods = DiscoveryMethods.from_obj(obj.Discovery_Method)
    #         return_obj.coa_taken = _COAsTaken.from_obj(obj.COA_Taken)
    #         return_obj.coa_requested = _COAsRequested.from_obj(obj.COA_Requested)
    #         return_obj.confidence = Confidence.from_obj(obj.Confidence)
    #         return_obj.attributed_threat_actors = AttributedThreatActors.from_obj(obj.Attributed_Threat_Actors)
    #         return_obj.related_indicators = RelatedIndicators.from_obj(obj.Related_Indicators)
    #         return_obj.related_observables = RelatedObservables.from_obj(obj.Related_Observables)
    #         return_obj.leveraged_ttps = LeveragedTTPs.from_obj(obj.Leveraged_TTPs)
    #         return_obj.related_incidents = RelatedIncidents.from_obj(obj.Related_Incidents)
    #         return_obj.status = VocabString.from_obj(obj.Status)
    #         return_obj.history = History.from_obj(obj.History)
    #         return_obj.responders = _InformationSources.from_obj(obj.Responder)
    #         return_obj.coordinators = _InformationSources.from_obj(obj.Coordinator)
    #         return_obj.external_ids = _ExternalIDs.from_obj(obj.External_ID)
    #         return_obj.reporter = InformationSource.from_obj(obj.Reporter)
    #         return_obj.impact_assessment = ImpactAssessment.from_obj(obj.Impact_Assessment)
    #         return_obj.security_compromise = VocabString.from_obj(obj.Security_Compromise)
    #         return_obj.related_packages = RelatedPackageRefs.from_obj(obj.Related_Packages)
    #         return_obj.contacts = _InformationSources.from_obj(obj.Contact)
    #         return_obj.url = obj.URL
    # 
    #     return return_obj
    # 
    # def to_dict(self):
    #     return super(Incident, self).to_dict()
    # 
    # @classmethod
    # def from_dict(cls, dict_repr, return_obj=None):
    #     if not dict_repr:
    #         return None
    # 
    #     if not return_obj:
    #         return_obj = cls()
    # 
    #     super(Incident, cls).from_dict(dict_repr, return_obj=return_obj)
    # 
    #     get = dict_repr.get
    #     return_obj.time = Time.from_dict(get('time'))
    #     return_obj.victims = _Victims.from_dict(get('victims'))
    #     return_obj.categories = IncidentCategories.from_dict(get('categories'))
    #     return_obj.attributed_threat_actors = AttributedThreatActors.from_dict(get('attributed_threat_actors'))
    #     return_obj.related_indicators = RelatedIndicators.from_dict(get('related_indicators'))
    #     return_obj.related_observables = RelatedObservables.from_dict(get('related_observables'))
    #     return_obj.related_incidents = RelatedIncidents.from_dict(get('related_incidents'))
    #     return_obj.intended_effects = _IntendedEffects.from_list(get('intended_effects'))
    #     return_obj.leveraged_ttps = LeveragedTTPs.from_dict(get('leveraged_ttps'))
    #     return_obj.affected_assets = AffectedAssets.from_dict(get('affected_assets'))
    #     return_obj.discovery_methods = DiscoveryMethods.from_dict(get('discovery_methods'))
    #     return_obj.reporter = InformationSource.from_dict(get('reporter'))
    #     return_obj.responders = _InformationSources.from_dict(get('responders'))
    #     return_obj.coordinators = _InformationSources.from_dict(get('coordinators'))
    #     return_obj.external_ids = _ExternalIDs.from_dict(get('external_ids'))
    #     return_obj.impact_assessment = ImpactAssessment.from_dict(get('impact_assessment'))
    #     return_obj.security_compromise = VocabString.from_dict(get('security_compromise'))
    #     return_obj.confidence = Confidence.from_dict(get('confidence'))
    #     return_obj.coa_taken = _COAsTaken.from_dict(get('coa_taken'))
    #     return_obj.coa_requested = _COAsRequested.from_dict(get('coa_requested'))
    #     return_obj.status = VocabString.from_dict(get('status'))
    #     return_obj.history = History.from_dict(get('history'))
    #     return_obj.related_packages = RelatedPackageRefs.from_dict(get('related_packages'))
    #     return_obj.contacts = _InformationSources.from_dict(get('contacts'))
    #     return_obj.url = get('url')
    # 
    #     return return_obj

class AttributedThreatActors(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.AttributedThreatActorsType

    threat_actor = fields.TypedField(
        name="Threat_Actor",
        type_=RelatedThreatActor,
        multiple=True,
        key_name="threat_actors"
    )


class RelatedIndicators(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedIndicatorsType

    indicator = fields.TypedField(
        name="Related_Indicator",
        type_=RelatedIndicator,
        multiple=True,
        key_name="indicators"
    )


class RelatedObservables(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedObservablesType

    observable = fields.TypedField(
        name="Related_Observable",
        type_=RelatedObservable,
        multiple=True,
        key_name="observables"
    )


class LeveragedTTPs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.LeveragedTTPsType

    ttp = fields.TypedField(
        name="Leverated_TTP",
        type_=RelatedTTP,
        multiple=True,
        key_name="ttps"
    )
    

class RelatedIncidents(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedIncidentsType

    incident = fields.TypedField(
        name="Related_Incident",
        type_=RelatedIncident,
        multiple=True,
        key_name="incidents"
    )


class IncidentCategories(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.CategoriesType

    category = VocabField(
        name="Category",
        type_=vocabs.IncidentCategory,
        multiple=True,
        key_name="categories"
    )


class AffectedAssets(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.AffectedAssetsType

    affected_asset = fields.TypedField(
        name="Affected_Asset",
        type_=AffectedAsset,
        multiple=True,
        key_name="affected_assets"
    )


# NOT ACTUAL STIX TYPES!

class DiscoveryMethods(stix.TypedList):
    _contained_type = VocabString

    def _fix_value(self, value):
        return vocabs.DiscoveryMethod(value)


class _COAsTaken(stix.TypedList):
    _contained_type = COATaken


class _COAsRequested(stix.TypedList):
    _contained_type = COARequested


class _ExternalIDs(stix.TypedList):
    _contained_type = ExternalID


class _InformationSources(stix.TypedList):
    _contained_type = InformationSource


class _Victims(stix.TypedList):
    _contained_type = Identity

    def _fix_value(self, value):
        return Identity(name=value)


class _IntendedEffects(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        return Statement(value=vocabs.IntendedEffect(value))
