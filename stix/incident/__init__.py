# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# external
from mixbox import signals

# internal
import stix
import stix.bindings.incident as incident_binding
from stix.common import (
    vocabs, Identity, Statement, VocabString,InformationSource, Confidence
)
from stix.common.related import (
    GenericRelationshipList, RelatedIndicator, RelatedThreatActor, RelatedTTP,
    RelatedObservable, RelatedIncident, RelatedPackageRefs
)

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

    def __init__(self, id_=None, idref=None, timestamp=None, title=None, description=None, short_description=None):
        super(Incident, self).__init__(
            id_=id_,
            idref=idref,
            timestamp=timestamp,
            title=title,
            description=description,
            short_description=short_description
        )

        self.status = None
        self.time = None
        self.victims = None
        self.attributed_threat_actors = AttributedThreatActors()
        self.related_indicators = RelatedIndicators()
        self.related_observables = RelatedObservables()
        self.related_incidents = RelatedIncidents()
        self.related_packages = RelatedPackageRefs()
        self.affected_assets = None
        self.categories = None
        self.intended_effects = None
        self.leveraged_ttps = LeveragedTTPs()
        self.discovery_methods = None
        self.reporter = None
        self.responders = None
        self.coordinators = None
        self.external_ids = None
        self.impact_assessment = None
        self.security_compromise = None
        self.confidence = None
        self.coa_taken = None
        self.coa_requested = None
        self.history = History()
        self._contacts = None
        self._url = None


    @property
    def status(self):
        """A :class:`.VocabString` property. If set to a string, an attempt
        will be made to convert it to an instance of :class:`.IncidentStatus`.

        """
        return self._status
    
    @status.setter
    def status(self, value):
        self._set_vocab(vocabs.IncidentStatus, status=value)

    @property
    def time(self):
        """Time section of the Incident. This is a :class:`.time.Time` field.

        """
        return self._time

    @time.setter
    def time(self, value):
        self._set_var(Time, try_cast=False, time=value)

    @property
    def intended_effects(self):
        """The impact of this intended effects of this Incident. This is a
        collection of :class:`.Statement` objects and behaves like a
        ``MutableSequence`` type.

        If set to a string, an attempt will be made to convert it into a
        :class:`.Statement` object with its value set to an instance of
        :class:`.IntendedEffect`.

        """
        return self._intended_effects

    @intended_effects.setter
    def intended_effects(self, value):
        self._intended_effects = _IntendedEffects(value)

    def add_intended_effect(self, value):
        """Adds a :class:`.Statement` object to the :attr:`intended_effects`
        collection.

        If `value` is a string, an attempt will be made to convert it into an
        instance of :class:`.Statement`.

        """
        self.intended_effects.append(value)

    @property
    def victims(self):
        """A collection of victim :class:`.Identity` objects. This behaves like
        a ``MutableSequence`` type.

        """
        return self._victims

    @victims.setter
    def victims(self, value):
        self._victims = _Victims(value)

    def add_victim(self, victim):
        """Adds a :class:`.IdentityType` value to the :attr:`victims`
        collection.

        """
        self._victims.append(victim)

    @property
    def categories(self):
        """A collection of :class:`.VocabString` objects. This behaves
        like a ``MutableSequence`` type.

        """
        return self._categories

    @categories.setter
    def categories(self, value):
        self._categories = IncidentCategories(value)

    def add_category(self, category):
        """Adds a :class:`.VocabString` object to the :attr:`categories`
        collection.

        If `category` is a string, an attempt will be made to convert it into
        an instance of :class:`.IncidentCategory`.

        """
        self.categories.append(category)

    @property
    def affected_assets(self):
        """A collection of :class:`.AffectedAsset` objects. This behaves like
        a ``MutableSequence`` type.

        """
        return self._affected_assets
    
    @affected_assets.setter
    def affected_assets(self, value):
        self._affected_assets = AffectedAssets(value)
    
    def add_affected_asset(self, v):
        """Adds a :class:`.AffectedAsset` object to the :attr:`affected_assets`
        collection.

        """
        self.affected_assets.append(v)

    @property
    def discovery_methods(self):
        """A :class:`.VocabString` collection. This behaves like a
        ``MutableSequence`` type.

        """
        return self._discovery_methods

    @discovery_methods.setter
    def discovery_methods(self, value):
        self._discovery_methods = DiscoveryMethods(value)

    def add_discovery_method(self, value):
        """Adds a :class:`.VocabString` object to the :attr:`discovery_methods`
        collection.

        If `value` is a string, an attempt will be made to convert it to an
        instance of :class:`.DiscoveryMethod`.

        """
        self.discovery_methods.append(value)

    @property
    def reporter(self):
        """A :class:`.InformationSource` field.

        """
        return self._reporter

    @reporter.setter
    def reporter(self, value):
        self._set_var(InformationSource, try_cast=False, reporter=value)

    @property
    def responders(self):
        """A class of :class:`.InformationSource` objects which contain
        information about incident responders.

        This behaves like a ``MutableSequence`` type.

        """
        return self._responders

    @responders.setter
    def responders(self, value):
        self._responders = _InformationSources(value)

    def add_responder(self, value):
        """Adds a :class:`.InformationSource` object to the :attr:`responders`
        collection.

        """
        self.responders.append(value)

    @property
    def coordinators(self):
        """A class of :class:`.InformationSource` objects. This behaves like a
        ``MutableSequence`` type.

        """
        return self._coordinators

    @coordinators.setter
    def coordinators(self, value):
        self._coordinators = _InformationSources(value)

    def add_coordinator(self, value):
        """Adds a :class:`.InformationSource` object to the :attr:`coordinators`
        collection.

        """
        self.coordinators.append(value)

    @property
    def external_ids(self):
        return self._external_ids

    @external_ids.setter
    def external_ids(self, value):
        """A collection of :class:`.ExternalID` objects for capturing
        incident tracker identification information.

        """
        self._external_ids = _ExternalIDs(value)

    def add_external_id(self, value):
        """Adds a :class:`.ExternalID` object to the :attr:`external_ids`
        collection.

        """
        self.external_ids.append(value)

    @property
    def impact_assessment(self):
        """A class :class:`.ImpactAssessment` field.

        """
        return self._impact_assessment

    @impact_assessment.setter
    def impact_assessment(self, value):
        self._set_var(ImpactAssessment, try_cast=False, impact_assessment=value)

    @property
    def security_compromise(self):
        """A :class:`.VocabString` field.  If set to a string, an attempt will
        be made to convert it into an instance of :class:`.SecurityCompromise`.

        """
        return self._security_compromise

    @security_compromise.setter
    def security_compromise(self, value):
        self._set_vocab(vocabs.SecurityCompromise, security_compromise=value)

    @property
    def confidence(self):
        """A :class:`.Confidence` field.

        """
        return self._confidence
    
    @confidence.setter
    def confidence(self, value):
        self._set_var(Confidence, confidence=value)

    @property
    def coa_taken(self):
        """A collection of :class:`.COATaken` objects which characterize
        courses of action taken during the incident.

        This behaves like a ``MutableSequence`` type.

        """
        return self._coa_taken
    
    @coa_taken.setter
    def coa_taken(self, value):
        self._coa_taken = _COAsTaken(value)

    def add_coa_taken(self, value):
        """Adds a :class:`.COATaken` object to the :attr:`coas_taken`
        collection.

        """
        self.coa_taken.append(value)

    @property
    def coa_requested(self):
        """A collection of :class:`.COARequested` objects which characterize
        courses of action requested for response to this incident.

        This behaves like a ``MutableSequence`` type.

        """
        return self._coa_requested

    @coa_requested.setter
    def coa_requested(self, value):
        self._coa_requested = _COAsRequested(value)

    def add_coa_requested(self, value):
        """Adds a :class:`.COARequested` object to the :attr:`coas_requested`
        collection.

        """
        self.coa_requested.append(value)

    @property
    def related_indicators(self):
        """A collection of :class:`.RelatedIndicator` objects characterizing
        indicators related to this incident.

        """
        return self._related_indicators

    @related_indicators.setter
    def related_indicators(self, value):
        self._set_var(RelatedIndicators, related_indicators=value)

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

    @property
    def related_observables(self):
        return self._related_observables

    @related_observables.setter
    def related_observables(self, value):
        self._set_var(RelatedObservables, related_observables=value)

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

    @property
    def related_packages(self):
        return self._related_packages

    @related_packages.setter
    def related_packages(self, value):
        self._related_packages = RelatedPackageRefs(value)

    def add_related_package(self, value):
        self.related_packages.append(value)

    @property
    def contacts(self):
        return self._contacts

    @contacts.setter
    def contacts(self, contacts_list):
        self._contacts = _InformationSources(contacts_list)

    def add_contact(self, contact):
        if self._contacts is None:
            self._contacts = _InformationSources()
        self._contacts.append(contact)

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(Incident, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if self.time:
            return_obj.Time = self.time.to_obj(ns_info=ns_info)
        if self.victims:
            return_obj.Victim = self.victims.to_obj(ns_info=ns_info)
        if self.attributed_threat_actors:
            return_obj.Attributed_Threat_Actors = self.attributed_threat_actors.to_obj(ns_info=ns_info)
        if self.related_indicators:
            return_obj.Related_Indicators = self.related_indicators.to_obj(ns_info=ns_info)
        if self.related_observables:
            return_obj.Related_Observables = self.related_observables.to_obj(ns_info=ns_info)
        if self.related_incidents:
            return_obj.Related_Incidents = self.related_incidents.to_obj(ns_info=ns_info)
        if self.categories:
            return_obj.Categories = self.categories.to_obj(ns_info=ns_info)
        if self.intended_effects:
            return_obj.Intended_Effect = self.intended_effects.to_obj(ns_info=ns_info)
        if self.leveraged_ttps:
            return_obj.Leveraged_TTPs = self.leveraged_ttps.to_obj(ns_info=ns_info)
        if self.affected_assets:
            return_obj.Affected_Assets = self.affected_assets.to_obj(ns_info=ns_info)
        if self.discovery_methods:
            return_obj.Discovery_Method = self.discovery_methods.to_obj(ns_info=ns_info)
        if self.reporter:
            return_obj.Reporter = self.reporter.to_obj(ns_info=ns_info)
        if self.responders:
            return_obj.Responder = self.responders.to_obj(ns_info=ns_info)
        if self.coordinators:
            return_obj.Coordinator = self.coordinators.to_obj(ns_info=ns_info)
        if self.external_ids:
            return_obj.External_ID = self.external_ids.to_obj(ns_info=ns_info)
        if self.impact_assessment:
            return_obj.Impact_Assessment = self.impact_assessment.to_obj(ns_info=ns_info)
        if self.security_compromise:
            return_obj.Security_Compromise = self.security_compromise.to_obj(ns_info=ns_info)
        if self.confidence:
            return_obj.Confidence = self.confidence.to_obj(ns_info=ns_info)
        if self.coa_taken:
            return_obj.COA_Taken = self.coa_taken.to_obj(ns_info=ns_info)
        if self.coa_requested:
            return_obj.COA_Requested = self.coa_requested.to_obj(ns_info=ns_info)
        if self.status:
            return_obj.Status = self.status.to_obj(ns_info=ns_info)
        if self.history:
            return_obj.History = self.history.to_obj(ns_info=ns_info)
        if self.related_packages:
            return_obj.Related_Packages = self.related_packages.to_obj(ns_info=ns_info)
        if self.contacts:
            return_obj.Contact = self.contacts.to_obj(ns_info=ns_info)
        if self.url:
            return_obj.URL = self.url

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(Incident, cls).from_obj(obj, return_obj=return_obj)

        if isinstance(obj, cls._binding_class):
            return_obj.time = Time.from_obj(obj.Time)
            return_obj.victims = _Victims.from_obj(obj.Victim)
            return_obj.categories = IncidentCategories.from_obj(obj.Categories)
            return_obj.intended_effects = _IntendedEffects.from_obj(obj.Intended_Effect)
            return_obj.affected_assets = AffectedAssets.from_obj(obj.Affected_Assets)
            return_obj.discovery_methods = DiscoveryMethods.from_obj(obj.Discovery_Method)
            return_obj.coa_taken = _COAsTaken.from_obj(obj.COA_Taken)
            return_obj.coa_requested = _COAsRequested.from_obj(obj.COA_Requested)
            return_obj.confidence = Confidence.from_obj(obj.Confidence)
            return_obj.attributed_threat_actors = AttributedThreatActors.from_obj(obj.Attributed_Threat_Actors)
            return_obj.related_indicators = RelatedIndicators.from_obj(obj.Related_Indicators)
            return_obj.related_observables = RelatedObservables.from_obj(obj.Related_Observables)
            return_obj.leveraged_ttps = LeveragedTTPs.from_obj(obj.Leveraged_TTPs)
            return_obj.related_incidents = RelatedIncidents.from_obj(obj.Related_Incidents)
            return_obj.status = VocabString.from_obj(obj.Status)
            return_obj.history = History.from_obj(obj.History)
            return_obj.responders = _InformationSources.from_obj(obj.Responder)
            return_obj.coordinators = _InformationSources.from_obj(obj.Coordinator)
            return_obj.external_ids = _ExternalIDs.from_obj(obj.External_ID)
            return_obj.reporter = InformationSource.from_obj(obj.Reporter)
            return_obj.impact_assessment = ImpactAssessment.from_obj(obj.Impact_Assessment)
            return_obj.security_compromise = VocabString.from_obj(obj.Security_Compromise)
            return_obj.related_packages = RelatedPackageRefs.from_obj(obj.Related_Packages)
            return_obj.contacts = _InformationSources.from_obj(obj.Contact)
            return_obj.url = obj.URL

        signals.emit("Entity.created.from_obj", return_obj, obj)
        return return_obj

    def to_dict(self):
        return super(Incident, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(Incident, cls).from_dict(dict_repr, return_obj=return_obj)

        get = dict_repr.get
        return_obj.time = Time.from_dict(get('time'))
        return_obj.victims = _Victims.from_dict(get('victims'))
        return_obj.categories = IncidentCategories.from_dict(get('categories'))
        return_obj.attributed_threat_actors = AttributedThreatActors.from_dict(get('attributed_threat_actors'))
        return_obj.related_indicators = RelatedIndicators.from_dict(get('related_indicators'))
        return_obj.related_observables = RelatedObservables.from_dict(get('related_observables'))
        return_obj.related_incidents = RelatedIncidents.from_dict(get('related_incidents'))
        return_obj.intended_effects = _IntendedEffects.from_list(get('intended_effects'))
        return_obj.leveraged_ttps = LeveragedTTPs.from_dict(get('leveraged_ttps'))
        return_obj.affected_assets = AffectedAssets.from_dict(get('affected_assets'))
        return_obj.discovery_methods = DiscoveryMethods.from_dict(get('discovery_methods'))
        return_obj.reporter = InformationSource.from_dict(get('reporter'))
        return_obj.responders = _InformationSources.from_dict(get('responders'))
        return_obj.coordinators = _InformationSources.from_dict(get('coordinators'))
        return_obj.external_ids = _ExternalIDs.from_dict(get('external_ids'))
        return_obj.impact_assessment = ImpactAssessment.from_dict(get('impact_assessment'))
        return_obj.security_compromise = VocabString.from_dict(get('security_compromise'))
        return_obj.confidence = Confidence.from_dict(get('confidence'))
        return_obj.coa_taken = _COAsTaken.from_dict(get('coa_taken'))
        return_obj.coa_requested = _COAsRequested.from_dict(get('coa_requested'))
        return_obj.status = VocabString.from_dict(get('status'))
        return_obj.history = History.from_dict(get('history'))
        return_obj.related_packages = RelatedPackageRefs.from_dict(get('related_packages'))
        return_obj.contacts = _InformationSources.from_dict(get('contacts'))
        return_obj.url = get('url')

        return return_obj


class AttributedThreatActors(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.AttributedThreatActorsType
    _binding_var = "Threat_Actor"
    _contained_type = RelatedThreatActor
    _inner_name = "threat_actors"


class RelatedIndicators(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedIndicatorsType
    _binding_var = "Related_Indicator"
    _contained_type = RelatedIndicator
    _inner_name = "indicators"


class RelatedObservables(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedObservablesType
    _binding_var = "Related_Observable"
    _contained_type = RelatedObservable
    _inner_name = "observables"


class LeveragedTTPs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = _binding.LeveragedTTPsType
    _binding_var = "Leveraged_TTP"
    _contained_type = RelatedTTP
    _inner_name = "ttps"
    

class RelatedIncidents(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.RelatedIncidentsType
    _binding_var = "Related_Incident"
    _contained_type = RelatedIncident
    _inner_name = "incidents"


class IncidentCategories(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _contained_type = VocabString
    _binding = incident_binding
    _binding_class = _binding.CategoriesType
    _binding_var = "Category"
    _inner_name = "categories"
    _dict_as_list = True

    def _fix_value(self, value):
        return vocabs.IncidentCategory(value)


class AffectedAssets(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _contained_type = AffectedAsset
    _binding = incident_binding
    _binding_class = _binding.AffectedAssetsType
    _binding_var = "Affected_Asset"
    _inner_name = "affected_assets"
    _dict_as_list = True


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
