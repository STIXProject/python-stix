# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
from stix.utils import deprecated
from stix.common import Activity, Confidence, Statement, VocabString
from stix.common.related import (GenericRelationshipList, RelatedCampaign,
    RelatedIncident, RelatedIndicator, RelatedPackageRefs, RelatedThreatActor,
    RelatedTTP)
from stix.common import vocabs
from stix.common.vocabs import VocabField
import stix.bindings.campaign as campaign_binding
from stix.common.structured_text import StructuredTextList
from stix.common.information_source import InformationSource


class AssociatedCampaigns(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.AssociatedCampaignsType

    campaign = fields.TypedField("Associated_Campaign", RelatedCampaign, multiple=True, key_name="campaigns")

    @classmethod
    def _dict_as_list(cls):
        return False


class Attribution(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.AttributionType

    threat_actor = fields.TypedField("Attributed_Threat_Actor", RelatedThreatActor, multiple=True, key_name="threat_actors")

    @classmethod
    def _dict_as_list(cls):
        return False


class RelatedIncidents(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.RelatedIncidentsType

    incident = fields.TypedField("Related_Incident", RelatedIncident, multiple=True, key_name="incidents")

    @classmethod
    def _dict_as_list(cls):
        return False


class RelatedIndicators(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.RelatedIndicatorsType

    indicator = fields.TypedField("Related_Indicator", RelatedIndicator, multiple=True, key_name="indicators")


    def _is_valid(self, value):
        deprecated.warn(value)
        return super(RelatedIndicators, self)._is_valid(value)


class RelatedTTPs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.RelatedTTPsType

    ttp = fields.TypedField("Related_TTP", RelatedTTP, multiple=True, key_name="ttps")

    @classmethod
    def _dict_as_list(cls):
        return False


class Names(stix.EntityList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.NamesType

    name = VocabField("Name", multiple=True, key_name="names")

    @classmethod
    def _dict_as_list(cls):
        return False


class Campaign(stix.BaseCoreComponent):
    """Implementation of the STIX Campaign.

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
    _binding = campaign_binding
    _binding_class = _binding.CampaignType
    _namespace = "http://stix.mitre.org/Campaign-1"
    _version = "1.2"
    _ALL_VERSIONS = ("1.0", "1.0.1", "1.1", "1.1.1", "1.2")
    _ID_PREFIX = 'campaign'

    descriptions = fields.TypedField("Description", StructuredTextList)
    activity = fields.TypedField("Activity", Activity, multiple=True)
    associated_campaigns = fields.TypedField("Associated_Campaigns", AssociatedCampaigns)
    attribution = fields.TypedField("Attribution", Attribution, multiple=True)
    confidence = fields.TypedField("Confidence", Confidence)
    # references = fields.TypedField("Reference", multiple=True)
    status = fields.TypedField("Status", VocabString)
    intended_effects = fields.TypedField("Intended_Effect", Statement, multiple=True, key_name="intended_effects")
    names = fields.TypedField("Names", Names)
    related_incidents = fields.TypedField("Related_Incidents", RelatedIncidents)
    related_indicators = fields.TypedField("Related_Indicators", RelatedIndicators)
    related_packages = fields.TypedField("Related_Packages", RelatedPackageRefs)
    information_source = fields.TypedField("Information_Source", InformationSource)

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

        self.related_ttps = RelatedTTPs()
        self.related_incidents = RelatedIncidents()
        self.related_indicators = RelatedIndicators()
        self.related_packages = RelatedPackageRefs()


    def add_intended_effect(self, value):
        self.intended_effects.append(value)

    def add_activity(self, value):
        """Adds an :class:`.Activity` object to the :attr:`activity`
        collection.

        """
        self.activity.append(value)

    @property
    def description(self):
        """A single description about the contents or purpose of this object.

        Default Value: ``None``

        Note:
            If this object has more than one description set, this will return
            the description with the lowest ordinality value.

        Returns:
            An instance of :class:`.StructuredText`

        """
        return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        from stix.common.structured_text import StructuredTextList
        self.descriptions = StructuredTextList(value)

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        self.descriptions.add(description)

    #@property
    #def status(self):
    #    """The status of the Campaign. This is a :class:`VocabString` field.

    #    If set to a string, an attempt will be made to convert it to a
    #    :class:`.CampaignStatus` object.

    #    """
    #    return self._status

    #@status.setter
    #def status(self, value):
    #    self._set_vocab(vocabs.CampaignStatus, status=value)



"""    def to_obj(self, return_obj=None, ns_info=None):
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
        return_obj.related_packages = \
            RelatedPackageRefs.from_dict(get('related_packages'))

        return return_obj
"""

# Not Actual STIX Types!
#class _Activities(stix.TypedList):
#    _contained_type = Activity


class _IntendedEffects(stix.TypedList):
    _contained_type = Statement

    def _fix_value(self, value):
        intended_effect = vocabs.IntendedEffect(value)
        return Statement(value=intended_effect)
