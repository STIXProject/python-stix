# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from datetime import datetime

import dateutil
from dateutil.tz import tzutc
from datetime import datetime

import stix
import stix.bindings.campaign as campaign_binding
from stix.common import (Activity, Confidence, InformationSource, Statement,
        StructuredText, VocabString)
from stix.common.related import (GenericRelationshipList, RelatedCampaign,
        RelatedIncident, RelatedIndicator, RelatedPackageRefs,
        RelatedThreatActor, RelatedTTP)
from stix.data_marking import Marking
import stix.utils
from stix.utils import dates
from stix.common.vocabs import CampaignStatus, IntendedEffect


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


class AttributionList(stix.EntityList):
    # NOT AN ACTUAL STIX CLASS. DO NOT CALL `.to_obj()`
    # ON THIS DIRECTLY! THIS IS BEING USED FOR CASTING
    # PURPOSES ONLY.
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = None
    _binding_class = None
    _binding_var = None
    _contained_type = Attribution
    _inner_name = None

    def _fix_value(self, value):
        try:
            new_value = self._contained_type(None, value)
        except:
            raise ValueError("Can't put '%s' (%s) into a %s" %
                (value, type(value), self.__class__))
        return new_value


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


class Campaign(stix.Entity):
    _binding = campaign_binding
    _binding_class = _binding.CampaignType
    _namespace = "http://stix.mitre.org/Campaign-1"
    _version = "1.1.1"

    def __init__(self, id_=None, idref=None, timestamp=None, title=None, description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("Campaign")
        self.idref = idref
        self.version = None # self._version
        self.title = title
        self.description = description
        self.short_description = short_description
        self.names = None
        self.intended_effects = None
        self.status = None
        self.related_ttps = RelatedTTPs()
        self.related_incidents = RelatedIncidents()
        self.related_indicators = RelatedIndicators()
        self.attribution = AttributionList()
        self.associated_campaigns = AssociatedCampaigns()
        self.confidence = None
        self.activity = []
        self.information_source = None
        self.handling = None
        self.related_packages = RelatedPackageRefs()

        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = datetime.now(tzutc()) if not idref else None

    @property
    def id_(self):
        return self._id
    
    @id_.setter
    def id_(self, value):
        if not value:
            self._id = None
        else:
            self._id = value
            self.idref = None
    
    @property
    def version(self):
        return self._version
    
    @version.setter
    def version(self, value):
        if not value:
            self._version = None
        else:
            if value != Campaign._version:
                self._version = value
            else:
                self._version = None
    
    @property
    def idref(self):
        return self._idref
    
    @idref.setter
    def idref(self, value):
        if not value:
            self._idref = None
        else:
            self._idref = value
            self.id_ = None # unset id_ if idref is present
    
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = dates.parse_value(value)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

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

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, value):
        if value:
            if isinstance(value, StructuredText):
                self._short_description = value
            else:
                self._short_description = StructuredText(value=value)
        else:
            self._short_description = None

    @property
    def intended_effects(self):
        return self._intended_effects
    
    @intended_effects.setter
    def intended_effects(self, value):
        self._intended_effects = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_intended_effect(v)
        else:
            self.add_intended_effect(value)
    
    def add_intended_effect(self, value):
        if not value:
            return
        elif isinstance(value, Statement):
            self.intended_effects.append(value)
        else:
            intended_effect = IntendedEffect(value)
            self.intended_effects.append(Statement(value=intended_effect))

    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, value):
        if not value:
            self._status = None
        elif isinstance(value, VocabString):
            self._status = value
        else:
            self._status = CampaignStatus(value)

    @property
    def attribution(self):
        return self._attribution

    @attribution.setter
    def attribution(self, value):
        self._attribution = AttributionList()
        if not value:
            return
        elif isinstance(value, AttributionList):
            self._attribution = value
        elif hasattr(value, '__getitem__'):
            self._attribution = AttributionList(*value)
        else:
            self._attribution.append(value) # may raise a ValueError


    def to_obj(self, return_obj=None, ns_info=None):
        super(Campaign, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.id = self.id_
        return_obj.idref = self.idref
        if self.timestamp:
            return_obj.timestamp = self.timestamp.isoformat()
        return_obj.version = self.version
        return_obj.Title = self.title
        if self.description:
            return_obj.Description = self.description.to_obj(ns_info=ns_info)
        if self.short_description:
            return_obj.Short_Description = self.short_description.to_obj(ns_info=ns_info)
        if self.names:
            return_obj.Names = self.names.to_obj(ns_info=ns_info)
        if self.intended_effects:
            return_obj.Intended_Effect = [x.to_obj(ns_info=ns_info) for x in self.intended_effects]
        if self.status:
            return_obj.Status = self.status.to_obj(ns_info=ns_info)
        if self.related_ttps:
            return_obj.Related_TTPs = self.related_ttps.to_obj(ns_info=ns_info)
        if self.related_incidents:
            return_obj.Related_Incidents = self.related_incidents.to_obj(ns_info=ns_info)
        if self.related_indicators:
            return_obj.Related_Indicators = self.related_indicators.to_obj(ns_info=ns_info)
        if self.attribution:
            return_obj.Attribution = [x.to_obj(ns_info=ns_info) for x in self.attribution]
        if self.associated_campaigns:
            return_obj.Associated_Campaigns = self.associated_campaigns.to_obj(ns_info=ns_info)
        if self.confidence:
            return_obj.Confidence = self.confidence.to_obj(ns_info=ns_info)
        if self.activity:
            return_obj.Activity = [x.to_obj(ns_info=ns_info) for x in self.activity]
        if self.information_source:
            return_obj.Information_Source = self.information_source.to_obj(ns_info=ns_info)
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

        return_obj.id_ = obj.id
        return_obj.idref = obj.idref
        return_obj.timestamp = obj.timestamp
        
        if isinstance(obj, cls._binding_class):
            return_obj.version = obj.version or cls._version
            return_obj.title = obj.Title
            return_obj.description = StructuredText.from_obj(obj.Description)
            return_obj.short_description = \
                    StructuredText.from_obj(obj.Short_Description)
            return_obj.names = Names.from_obj(obj.Names)
            return_obj.intended_effects = \
                    [Statement.from_obj(x) for x in obj.Intended_Effect]
            return_obj.status = VocabString.from_obj(obj.Status)
            return_obj.related_ttps = RelatedTTPs.from_obj(obj.Related_TTPs)
            return_obj.related_incidents = \
                    RelatedIncidents.from_obj(obj.Related_Incidents)
            return_obj.related_indicators = \
                    RelatedIndicators.from_obj(obj.Related_Indicators)
            return_obj.attribution = \
                    [Attribution.from_obj(x) for x in obj.Attribution]
            return_obj.associated_campaigns = \
                    AssociatedCampaigns.from_obj(obj.Associated_Campaigns)
            return_obj.confidence = Confidence.from_obj(obj.Confidence)
            return_obj.activity = \
                    [Activity.from_obj(x) for x in obj.Activity]
            return_obj.information_source = \
                    InformationSource.from_obj(obj.Information_Source)
            return_obj.handling = Marking.from_obj(obj.Handling)
            return_obj.related_packages = \
                    RelatedPackageRefs.from_obj(obj.Related_Packages)

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
        if self.intended_effects:
            d['intended_effects'] = [x.to_dict() for x in self.intended_effects]
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
        if self.activity:
            d['activity'] = [x.to_dict() for x in self.activity]
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
        return_obj.intended_effects = \
                [Statement.from_dict(x) for x in dict_repr.get('intended_effects', [])]
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
        return_obj.activity = \
                [Activity.from_dict(x) for x in dict_repr.get('activity', [])]
        return_obj.information_source = \
                InformationSource.from_dict(dict_repr.get('information_source'))
        return_obj.handling = Marking.from_dict(dict_repr.get('handling'))
        return_obj.related_packages = \
                RelatedPackageRefs.from_dict(dict_repr.get('related_packages'))

        return return_obj

