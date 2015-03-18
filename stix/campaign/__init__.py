# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
from stix.common import Activity, Confidence, Statement, VocabString
from stix.common.related import (
    GenericRelationshipList, RelatedCampaign, RelatedIncident, RelatedIndicator,
    RelatedPackageRefs, RelatedThreatActor, RelatedTTP
)
from stix.common import vocabs
from stix.data_marking import Marking
import stix.bindings.campaign as campaign_binding


class AssociatedCampaigns(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.AssociatedCampaignsType
    _binding_var = "Associated_Campaign"
    _contained_type = RelatedCampaign
    _inner_name = "campaigns"


class Attribution(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.AttributionType
    _binding_var = "Attributed_Threat_Actor"
    _contained_type = RelatedThreatActor
    _inner_name = "threat_actors"


class RelatedIncidents(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.RelatedIncidentsType
    _binding_var = "Related_Incident"
    _contained_type = RelatedIncident
    _inner_name = "incidents"


class RelatedIndicators(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.RelatedIndicatorsType
    _binding_var = "Related_Indicator"
    _contained_type = RelatedIndicator
    _inner_name = "indicators"


class RelatedTTPs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.RelatedTTPsType
    _binding_var = "Related_TTP"
    _contained_type = RelatedTTP
    _inner_name = "ttps"


class Names(stix.EntityList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.NamesType
    _binding_var = "Name"
    _contained_type = VocabString
    _inner_name = "names"


class Campaign(stix.BaseCoreComponent):
    _binding = campaign_binding
    _binding_class = _binding.CampaignType
    _namespace = "http://stix.mitre.org/Campaign-1"
    _version = "1.1.1"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1")
    _ID_PREFIX = 'campaign'

    def __init__(self, id_=None, idref=None, timestamp=None, title=None,
                 description=None, short_description=None):

        super(Campaign, self).__init__(
            id_=id_,
            idref=idref,
            timestamp=timestamp,
            title=title,
            description=description,
            short_description=short_description
        )

        self.names = None
        self.intended_effects = _IntendedEffects()
        self.status = None
        self.related_ttps = RelatedTTPs()
        self.related_incidents = RelatedIncidents()
        self.related_indicators = RelatedIndicators()
        self.attribution = _AttributionList()
        self.associated_campaigns = AssociatedCampaigns()
        self.confidence = None
        self.activity = _Activities()
        self.handling = None
        self.related_packages = RelatedPackageRefs()

    @property
    def intended_effects(self):
        return self._intended_effects

    @intended_effects.setter
    def intended_effects(self, value):
        self._intended_effects = _IntendedEffects(value)

    def add_intended_effect(self, value):
        self.intended_effects.append(value)

    @property
    def activity(self):
        return self._activity

    @activity.setter
    def activity(self, value):
        self._activity = _Activities(value)

    def add_activity(self, value):
        self.activity.append(value)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._set_vocab(vocabs.CampaignStatus, status=value)

    @property
    def attribution(self):
        return self._attribution

    @attribution.setter
    def attribution(self, value):
        self._attribution = _AttributionList(value)

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        super(Campaign, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if self.names:
            return_obj.Names = self.names.to_obj(ns_info=ns_info)
        if self.intended_effects:
            return_obj.Intended_Effect = self.intended_effects.to_obj(ns_info=ns_info)
        if self.status:
            return_obj.Status = self.status.to_obj(ns_info=ns_info)
        if self.related_ttps:
            return_obj.Related_TTPs = self.related_ttps.to_obj(ns_info=ns_info)
        if self.related_incidents:
            return_obj.Related_Incidents = self.related_incidents.to_obj(ns_info=ns_info)
        if self.related_indicators:
            return_obj.Related_Indicators = self.related_indicators.to_obj(ns_info=ns_info)
        if self.attribution:
            return_obj.Attribution = self.attribution.to_obj(ns_info=ns_info)
        if self.associated_campaigns:
            return_obj.Associated_Campaigns = self.associated_campaigns.to_obj(ns_info=ns_info)
        if self.confidence:
            return_obj.Confidence = self.confidence.to_obj(ns_info=ns_info)
        if self.activity:
            return_obj.Activity = self.activity.to_obj(ns_info=ns_info)
        if self.handling:
            return_obj.Handling = self.handling.to_obj(ns_info=ns_info)
        if self.related_packages:
            return_obj.Related_Packages = self.related_packages.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        super(Campaign, cls).from_obj(obj, return_obj=return_obj)

        if isinstance(obj, cls._binding_class):
            return_obj.names = Names.from_obj(obj.Names)
            return_obj.intended_effects = \
                _IntendedEffects.from_obj(obj.Intended_Effect)
            return_obj.status = VocabString.from_obj(obj.Status)
            return_obj.related_ttps = RelatedTTPs.from_obj(obj.Related_TTPs)
            return_obj.related_incidents = \
                RelatedIncidents.from_obj(obj.Related_Incidents)
            return_obj.related_indicators = \
                RelatedIndicators.from_obj(obj.Related_Indicators)
            return_obj.attribution = _AttributionList.from_obj(obj.Attribution)
            return_obj.associated_campaigns = \
                AssociatedCampaigns.from_obj(obj.Associated_Campaigns)
            return_obj.confidence = Confidence.from_obj(obj.Confidence)
            return_obj.activity = _Activities.from_obj(obj.Activity)
            return_obj.handling = Marking.from_obj(obj.Handling)
            return_obj.related_packages = \
                RelatedPackageRefs.from_obj(obj.Related_Packages)

        return return_obj

    def to_dict(self):
        return super(Campaign, self).to_dict()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        super(Campaign, cls).from_dict(dict_repr, return_obj=return_obj)

        get = dict_repr.get  # PEP 8 line lengths
        return_obj.names = Names.from_dict(get('names'))
        return_obj.intended_effects = \
            _IntendedEffects.from_dict(get('intended_effects'))
        return_obj.status = VocabString.from_dict(get('status'))
        return_obj.related_ttps = \
            RelatedTTPs.from_dict(get('related_ttps'))
        return_obj.related_incidents = \
            RelatedIncidents.from_dict(get('related_incidents'))
        return_obj.related_indicators = \
            RelatedIndicators.from_dict(get('related_indicators'))
        return_obj.attribution = _AttributionList.from_list(get('attribution'))
        return_obj.associated_campaigns = \
            AssociatedCampaigns.from_dict(get('associated_campaigns'))
        return_obj.confidence = \
            Confidence.from_dict(get('confidence'))
        return_obj.activity = _Activities.from_dict(get('activity'))
        return_obj.handling = Marking.from_dict(get('handling'))
        return_obj.related_packages = \
            RelatedPackageRefs.from_dict(get('related_packages'))

        return return_obj


# Not Actual STIX Types!
class _AttributionList(stix.TypedList):
    _contained_type = Attribution


class _Activities(stix.TypedList):
    _contained_type = Activity


class _IntendedEffects(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        intended_effect = vocabs.IntendedEffect(value)
        return Statement(value=intended_effect)
