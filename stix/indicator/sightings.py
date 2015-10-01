# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from mixbox import fields

import stix
import stix.utils as utils
from stix.common import (GenericRelationshipList, RelatedObservable,
    StructuredTextList, Confidence, InformationSource)
from stix.common.datetimewithprecision import validate_precision

import stix.bindings.indicator as indicator_binding
from stix.base import AttributeField, ElementField
from stix.common.structured_text import StructuredTextListField


class Sighting(stix.Entity):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.SightingType
    
    timestamp = fields.DateTimeField("timestamp")
    timestamp_precision = fields.TypedField("timestamp_precision", preset_hook=validate_precision)
    descriptions = StructuredTextListField("Description", StructuredTextList, key_name="description")
    source = ElementField("Source", InformationSource)
    reference = ElementField("Reference")
    confidence = ElementField("Confidence", Confidence)
    related_observables = ElementField("Related_Observables", type_="stix.indicator.sightings.RelatedObservables")
    
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
        return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        self.descriptions = StructuredTextList(value)

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".

        """
        self.descriptions.add(description)
    
    """
    def to_obj(self, return_obj=None, ns_info=None):
        super(Sighting, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()
        
        return_obj.timestamp = utils.dates.serialize_value(self.timestamp)
        return_obj.timestamp_precision = self.timestamp_precision
        return_obj.Reference = self.reference
        
        if self.source:
            return_obj.Source = self.source.to_obj(ns_info=ns_info)
        if self.confidence:
            return_obj.Confidence = self.confidence.to_obj(ns_info=ns_info)
        if self.descriptions:
            return_obj.Description = self.descriptions.to_obj(ns_info=ns_info)
        if self.related_observables:
            return_obj.Related_Observables = self.related_observables.to_obj(ns_info=ns_info)
        
        return return_obj

    def to_dict(self):
        return super(Sighting, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if return_obj is None:
            return_obj = cls()
        
        return_obj.timestamp = obj.timestamp
        return_obj.timestamp_precision = obj.timestamp_precision
        return_obj.source = InformationSource.from_obj(obj.Source)
        return_obj.reference = obj.Reference
        return_obj.confidence = Confidence.from_obj(obj.Confidence)
        return_obj.descriptions = StructuredTextList.from_obj(obj.Description)
        return_obj.related_observables = RelatedObservables.from_obj(obj.Related_Observables)
        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None
        if return_obj is None:
            return_obj = cls()

        return_obj.timestamp = d.get('timestamp')
        return_obj.timestamp_precision = d.get('timestamp_precision')
        return_obj.source = InformationSource.from_dict(d.get('source'))
        return_obj.reference = d.get('reference')
        return_obj.confidence = Confidence.from_dict(d.get('confidence'))
        return_obj.descriptions = StructuredTextList.from_dict(d.get('description'))
        return_obj.related_observables = RelatedObservables.from_dict(d.get('related_observables'))
        return return_obj
    """

class Sightings(stix.EntityList):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.SightingsType
    _contained_type = Sighting
    _binding_var = "Sighting"
    _inner_name = "sightings"
    
    sightings_count = AttributeField("sightings_count")
    
    def __init__(self, sightings_count=None, *args):
        super(Sightings, self).__init__(*args)
        self.sightings_count = sightings_count

    def __nonzero__(self):
        return super(Sightings, self).__nonzero__() or bool(self.sightings_count)

    """
    @property
    def sightings_count(self):
        return self._sightings_count

    @sightings_count.setter
    def sightings_count(self, value):
        self._set_var(int, sightings_count=value)
    """
    
    def to_obj(self, return_obj=None, ns_info=None):
        list_obj = super(Sightings, self).to_obj(return_obj=return_obj, ns_info=ns_info)
        list_obj.sightings_count = self.sightings_count
        return list_obj

    def to_dict(self):
        d = super(Sightings, self).to_dict()
        if self.sightings_count:
            d['sightings_count'] = self.sightings_count
        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if return_obj is None:
            return_obj = cls()

        super(Sightings, cls).from_obj(obj, return_obj=return_obj)
        return_obj.sightings_count = obj.sightings_count
        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if return_obj is None:
            return_obj = cls()

        super(Sightings, cls).from_dict(dict_repr, return_obj=return_obj)
        return_obj.sightings_count = dict_repr.get('sightings_count')
        return return_obj


class RelatedObservables(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.RelatedObservablesType
    _binding_var = "Related_Observable"
    _contained_type = RelatedObservable
    _inner_name = "observables"
