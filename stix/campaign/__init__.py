# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from functools import partial

from mixbox import fields

import stix
from stix.common import Activity, Confidence, Statement
from stix.common.statement import StatementField
from stix.common.related import (GenericRelationshipList, RelatedCampaign,
    RelatedIncident, RelatedIndicator, RelatedPackageRefs, RelatedThreatActor,
    RelatedTTP)
from stix.common import vocabs
from stix.common.vocabs import VocabField, CampaignStatus
import stix.bindings.campaign as campaign_binding
from stix.common.structured_text import StructuredTextList
from stix.common.information_source import InformationSource
from stix.utils.deprecated import DeprecatedList


class AssociatedCampaigns(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.AssociatedCampaignsType

    campaign = fields.TypedField("Associated_Campaign", RelatedCampaign, multiple=True, key_name="campaigns")


class Attribution(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.AttributionType

    threat_actor = fields.TypedField("Attributed_Threat_Actor", RelatedThreatActor, multiple=True, key_name="threat_actors")


class RelatedIncidents(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.RelatedIncidentsType

    incident = fields.TypedField("Related_Incident", RelatedIncident, multiple=True, key_name="incidents")


class RelatedIndicators(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.RelatedIndicatorsType

    indicator = fields.TypedField(
        name="Related_Indicator",
        type_=RelatedIndicator,
        multiple=True,
        key_name="indicators",
        listfunc=partial(DeprecatedList, type=RelatedIndicator)
    )


class RelatedTTPs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Campaign-1"
    _binding = campaign_binding
    _binding_class = campaign_binding.RelatedTTPsType

    ttp = fields.TypedField("Related_TTP", RelatedTTP, multiple=True, key_name="ttps")


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
    status = VocabField("Status", CampaignStatus)
    intended_effects = StatementField("Intended_Effect", Statement, vocab_type=vocabs.IntendedEffect, multiple=True, key_name="intended_effects")
    names = fields.TypedField("Names", Names)
    related_incidents = fields.TypedField("Related_Incidents", RelatedIncidents)
    related_indicators = fields.TypedField("Related_Indicators", RelatedIndicators)
    related_packages = fields.TypedField("Related_Packages", RelatedPackageRefs)
    related_ttps = fields.TypedField("Related_TTPs", RelatedTTPs)
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
        self.descriptions = StructuredTextList(value)

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        self.descriptions.add(description)
