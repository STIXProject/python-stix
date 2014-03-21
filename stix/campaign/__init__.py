# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from datetime import datetime

import dateutil

import stix
import stix.bindings.campaign as campaign_binding
from stix.common import (Confidence, InformationSource, Statement,
        StructuredText, VocabString)
from stix.common.related import (GenericRelationshipList, RelatedCampaign,
        RelatedIncident, RelatedIndicator, RelatedPackageRefs,
        RelatedThreatActor, RelatedTTP)
from stix.data_marking import Marking
import stix.utils


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


class Name(VocabString):
    pass


class Names(stix.EntityList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.NamesType
    _binding_var = "Name"
    _contained_type = Name
    _inner_name = "names"


class Campaign(stix.Entity):
    _binding = campaign_binding
    _binding_class = _binding.CampaignType
    _namespace = "http://stix.mitre.org/Campaign-1"
    _version = "1.1"

    def __init__(self, id_=None, title=None, description=None):
        self.id_ = id_ or stix.utils.create_id("Campaign")
        self.idref = None
        self.timestamp = None
        self.version = self._version
        self.title = title
        self.description = description
        self.short_description = None
        self.names = None
        self.intended_effect = []
        self.status = None
        self.related_ttps = RelatedTTPs()
        self.related_incidents = RelatedIncidents()
        self.related_indicators = RelatedIndicators()
        self.attribution = []
        self.associated_campaigns = AssociatedCampaigns()
        self.confidence = None
        # self.activity = None
        self.information_source = None
        self.handling = None
        self.related_packages = RelatedPackageRefs()

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if not value:
            self._timestamp = None
        elif isinstance(value, datetime):
            self._timestamp = value
        else:
            self._timestamp = dateutil.parser.parse(value)

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._description = value
            else:
                self._description = StructuredText(value=value)
        else:
            self._description = None

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref)
        if self.timestamp:
            return_obj.set_timestamp(self.timestamp.isoformat())
        return_obj.set_version(self.version)
        return_obj.set_Title(self.title)
        if self.description:
            return_obj.set_Description(self.description.to_obj())
        if self.short_description:
            return_obj.set_Short_Description(self.short_description.to_obj())
        if self.names:
            return_obj.set_Names(self.names.to_obj())
        if self.intended_effect:
            return_obj.set_Intended_Effect([x.to_obj() for x in self.intended_effect])
        if self.status:
            return_obj.set_Status(self.status.to_obj())
        if self.related_ttps:
            return_obj.set_Related_TTPs(self.related_ttps.to_obj())
        if self.related_incidents:
            return_obj.set_Related_Incidents(self.related_incidents.to_obj())
        if self.related_indicators:
            return_obj.set_Related_Indicators(self.related_indicators.to_obj())
        if self.attribution:
            return_obj.set_Attribution([x.to_obj() for x in self.attribution])
        if self.associated_campaigns:
            return_obj.set_Associated_Campaigns(self.associated_campaigns.to_obj())
        if self.confidence:
            return_obj.set_Confidence(self.confidence.to_obj())

        if self.information_source:
            return_obj.set_Information_Source(self.information_source.to_obj())
        if self.handling:
            return_obj.set_Handling(self.handling.to_obj())
        if self.related_packages:
            return_obj.set_Related_Packages(self.related_packages.to_obj())

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.get_id()
        return_obj.idref = obj.get_idref()
        return_obj.timestamp = obj.get_timestamp()
        return_obj.version = obj.get_version() or cls._version
        return_obj.title = obj.get_Title()
        return_obj.description = StructuredText.from_obj(obj.get_Description())
        return_obj.short_description = \
                StructuredText.from_obj(obj.get_Short_Description())
        return_obj.names = Names.from_obj(obj.get_Names())
        return_obj.intended_effect = \
                [Statement.from_obj(x) for x in obj.get_Intended_Effect()]
        return_obj.status = VocabString.from_obj(obj.get_Status())
        return_obj.related_ttps = RelatedTTPs.from_obj(obj.get_Related_TTPs())
        return_obj.related_incidents = \
                RelatedIncidents.from_obj(obj.get_Related_Incidents())
        return_obj.related_indicators = \
                RelatedIndicators.from_obj(obj.get_Related_Indicators())
        return_obj.attribution = \
                [Attribution.from_obj(x) for x in obj.get_Attribution()]
        return_obj.associated_campaigns = \
                AssociatedCampaigns.from_obj(obj.get_Associated_Campaigns())
        return_obj.confidence = Confidence.from_obj(obj.get_Confidence())

        return_obj.information_source = \
                InformationSource.from_obj(obj.get_Information_Source())
        return_obj.handling = Marking.from_obj(obj.get_Handling())
        return_obj.related_packages = \
                RelatedPackageRefs.from_obj(obj.get_Related_Packages())

        return return_obj

    def to_dict(self):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.idref:
            d['idref'] = self.idref
        if self.timestamp:
            d['timestamp'] = self.timestamp.isoformat()
        if self.version:
            d['version'] = self.version or self._version
        if self.title:
            d['title'] = self.title
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
        if self.names:
            d['names'] = self.names.to_dict()
        if self.intended_effect:
            d['intended_effect'] = [x.to_dict() for x in self.intended_effect]
        if self.status:
            d['status'] = self.status.to_dict()
        if self.related_ttps:
            d['related_ttps'] = self.related_ttps.to_dict()
        if self.related_incidents:
            d['related_incidents'] = self.related_incidents.to_dict()
        if self.related_indicators:
            d['related_indicators'] = self.related_indicators.to_dict()
        if self.attribution:
            d['attribution'] = [x.to_dict() for x in self.attribution]
        if self.associated_campaigns:
            d['associated_campaigns'] = self.associated_campaigns.to_dict()
        if self.confidence:
            d['confidence'] = self.confidence.to_dict()

        if self.information_source:
            d['information_source'] = self.information_source.to_dict()
        if self.handling:
            d['handling'] = self.handling.to_dict()
        if self.related_packages:
            d['related_packages'] = self.related_packages.to_dict()

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.id_ = dict_repr.get('id')
        return_obj.idref = dict_repr.get('idref')
        return_obj.timestamp = dict_repr.get('timestamp')
        return_obj.version = dict_repr.get('version', cls._version)
        return_obj.title = dict_repr.get('title')
        return_obj.description = \
                StructuredText.from_dict(dict_repr.get('description'))
        return_obj.short_description = \
                StructuredText.from_dict(dict_repr.get('short_description'))
        return_obj.names = Names.from_dict(dict_repr.get('names'))
        return_obj.intended_effect = \
                [Statement.from_dict(x) for x in dict_repr.get('intended_effect', [])]
        return_obj.status = VocabString.from_dict(dict_repr.get('status'))
        return_obj.related_ttps = \
                RelatedTTPs.from_dict(dict_repr.get('related_ttps'))
        return_obj.related_incidents = \
                RelatedIncidents.from_dict(dict_repr.get('related_incidents'))
        return_obj.related_indicators = \
                RelatedIndicators.from_dict(dict_repr.get('related_indicators'))
        return_obj.attribution = \
                [Attribution.from_dict(x) for x in
                        dict_repr.get('attribution', [])]
        return_obj.associated_campaigns = \
                AssociatedCampaigns.from_dict(dict_repr.get('associated_campaigns'))
        return_obj.confidence = \
                Confidence.from_dict(dict_repr.get('confidence'))

        return_obj.information_source = \
                InformationSource.from_dict(dict_repr.get('information_source'))
        return_obj.handling = Marking.from_dict(dict_repr.get('handling'))
        return_obj.related_packages = \
                RelatedPackageRefs.from_dict(dict_repr.get('related_packages'))

        return return_obj

