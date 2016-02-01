# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
from stix import utils
from stix.common import (GenericRelationshipList, RelatedObservable,
    StructuredTextList, Confidence, InformationSource)
from stix.common.datetimewithprecision import validate_precision

import stix.bindings.indicator as indicator_binding


class Sighting(stix.Entity):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.SightingType
    
    timestamp = fields.DateTimeField("timestamp")
    timestamp_precision = fields.TypedField("timestamp_precision", preset_hook=validate_precision)
    descriptions = fields.TypedField("Description", StructuredTextList)
    source = fields.TypedField("Source", InformationSource)
    reference = fields.TypedField("Reference")
    confidence = fields.TypedField("Confidence", Confidence)
    related_observables = fields.TypedField("Related_Observables", type_="stix.indicator.sightings.RelatedObservables")
    
    def __init__(self, timestamp=None, timestamp_precision=None, description=None):
        super(Sighting, self).__init__()

        self.timestamp = timestamp or utils.dates.now()
        self.timestamp_precision = timestamp_precision
        self.descriptions = description
        self.source = None
        self.reference = None
        self.confidence = None

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
        return next(iter(self.descriptions or []), None)

    @description.setter
    def description(self, value):
        self.descriptions = StructuredTextList(value)

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        self.descriptions.add(description)


class Sightings(stix.EntityList):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.SightingsType

    sightings_count = fields.TypedField("sightings_count")
    sighting = fields.TypedField("Sighting", Sighting, multiple=True, key_name="sightings")

    def __init__(self, sightings_count=None, *args):
        super(Sightings, self).__init__(*args)
        self.sightings_count = sightings_count

    def __nonzero__(self):
        return super(Sightings, self).__nonzero__() or (self.sightings_count is not None)


class RelatedObservables(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.RelatedObservablesType

    observable = fields.TypedField(
        name="Related_Observable",
        type_=RelatedObservable,
        multiple=True,
        key_name="observables"
    )
