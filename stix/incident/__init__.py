# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.
from mixbox import fields

import stix
import stix.bindings.incident as incident_binding
from stix.common import vocabs
from stix.common import Statement, VocabString, InformationSource, Confidence
from stix.common.vocabs import VocabField
from stix.common.statement import StatementField
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

    status = vocabs.VocabField("Status", vocabs.IncidentStatus)
    time = fields.TypedField("Time", Time)
    victims = fields.TypedField("Victim", Identity, factory=IdentityFactory, multiple=True, key_name="victims")
    attributed_threat_actors = fields.TypedField("Attributed_Threat_Actors", type_="stix.incident.AttributedThreatActors")
    related_indicators = fields.TypedField("Related_Indicators", type_="stix.incident.RelatedIndicators")
    related_observables = fields.TypedField("Related_Observables", type_="stix.incident.RelatedObservables")
    related_incidents = fields.TypedField("Related_Incidents", type_="stix.incident.RelatedIncidents")
    related_packages = fields.TypedField("Related_Packages", RelatedPackageRefs)
    affected_assets = fields.TypedField("Affected_Assets", type_="stix.incident.AffectedAssets")
    categories = fields.TypedField("Categories", type_="stix.incident.IncidentCategories")
    intended_effects = StatementField("Intended_Effect", Statement, vocab_type=vocabs.IntendedEffect, multiple=True, key_name="intended_effects")
    leveraged_ttps = fields.TypedField("Leveraged_TTPs", type_="stix.incident.LeveragedTTPs")
    discovery_methods = vocabs.VocabField("Discovery_Method", vocabs.DiscoveryMethod, multiple=True, key_name="discovery_methods")
    reporter = fields.TypedField("Reporter", InformationSource)
    responders = fields.TypedField("Responder", InformationSource, multiple=True, key_name="responders")
    coordinators = fields.TypedField("Coordinator", InformationSource, multiple=True, key_name="coordinators")
    external_ids = fields.TypedField("External_ID", ExternalID, multiple=True, key_name="external_ids")
    impact_assessment = fields.TypedField("Impact_Assessment", ImpactAssessment)
    security_compromise = vocabs.VocabField("Security_Compromise", vocabs.SecurityCompromise)
    confidence = fields.TypedField("Confidence", Confidence)
    coa_taken = fields.TypedField("COA_Taken", COATaken, multiple=True)
    coa_requested = fields.TypedField("COA_Requested", COARequested, multiple=True)
    history = fields.TypedField("History", History)
    information_source = fields.TypedField("Information_Source", InformationSource)
    url = fields.TypedField("URL")
    contacts = fields.TypedField("Contact", InformationSource, multiple=True, key_name="contacts")

    def __init__(self, id_=None, idref=None, timestamp=None, title=None, description=None, short_description=None):
        super(Incident, self).__init__(
            id_=id_,
            idref=idref,
            timestamp=timestamp,
            title=title,
            description=description,
            short_description=short_description
        )
        self.related_indicators = RelatedIndicators()
        self.related_observables = RelatedObservables()
        self.related_incidents = RelatedIncidents()
        self.related_packages = RelatedPackageRefs()
        self.categories = IncidentCategories()
        self.affected_assets = AffectedAssets()
        self.leveraged_ttps = LeveragedTTPs()
        
    def add_intended_effect(self, value):
        """Adds a :class:`.Statement` object to the :attr:`intended_effects`
        collection.

        If `value` is a string, an attempt will be made to convert it into an
        instance of :class:`.Statement`.

        """
        self.intended_effects.append(value)

    def add_leveraged_ttps(self, ttp):
        """Adds a :class:`.RelatedTTP` value to the :attr:`leveraged_ttps`
        collection.

        """
        self.leveraged_ttps.append(ttp)

    def add_victim(self, victim):
        """Adds a :class:`.IdentityType` value to the :attr:`victims`
        collection.

        """
        self.victims.append(victim)

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

        If the `indicator` parameter is ``None``, no item will be added to the
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
        
    def add_related_incidents(self, value):
        self.related_incidents.append(value)

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
        name="Leveraged_TTP",
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
