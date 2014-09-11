# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix.utils import dates
from stix.common import (GenericRelationshipList, RelatedObservable, StructuredText,
                         Confidence, InformationSource)
import stix.bindings.indicator as indicator_binding
from datetime import datetime
from dateutil.tz import tzutc

class Sighting(stix.Entity):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.SightingType
    
    def __init__(self, timestamp=None, timestamp_precision=None, description=None):
        self.timestamp = timestamp or datetime.now(tzutc())
        self.timestamp_precision = timestamp_precision
        self.description = description
        self.source = None
        self.reference = None
        self.confidence = None
        self.related_observables = RelatedObservables()
        
    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = dates.parse_value(value)
    
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, value):
        if not value:
            self._description = None
        elif isinstance(value, StructuredText):
            self._description = value
        else:
            self._description = StructuredText(value)
            
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        if value is None:
            self._source = None
        elif isinstance(value, InformationSource):
            self._source = value
        else:
            raise ValueError("source must be of type InformationSource")
          
    
    @property
    def confidence(self):
        return self._confidence
    
    @confidence.setter
    def confidence(self, value):
        if not value:
            self._confidence = None
        elif isinstance(value, Confidence):
            self._confidence = value
        else:
            self._confidence = Confidence(value)
    
    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        if not return_obj:
            return_obj = self._binding_class()
        
        return_obj.set_timestamp(dates.serialize_value(self.timestamp))
        return_obj.set_timestamp_precision(self.timestamp_precision)
        return_obj.set_Reference(self.reference)
        
        if self.source:
            return_obj.set_Source(self.source.to_obj(ns_info=ns_info))
        if self.confidence:
            return_obj.set_Confidence(self.confidence.to_obj(ns_info=ns_info))
        if self.description:
            return_obj.set_Description(self.description.to_obj(ns_info=ns_info))
        if self.related_observables:
            return_obj.set_Related_Observables(self.related_observables.to_obj(ns_info=ns_info))
        
        return return_obj

    def to_dict(self):
        d = {}
        if self.timestamp:
            d['timestamp'] = dates.serialize_value(self.timestamp)
        if self.timestamp_precision:
            d['timestamp_precision'] = str(self.timestamp_precision)
        if self.source:
            d['source'] = self.source.to_dict()
        if self.reference:
            d['reference'] = str(self.reference)
        if self.confidence:
            d['confidence'] = self.confidence.to_dict()
        if self.description:
            d['description'] = self.description.to_dict()
        if self.related_observables:
            d['related_observables'] = self.related_observables.to_dict()
         
        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if return_obj is None:
            return_obj = cls()
        
        return_obj.timestamp = obj.get_timestamp()
        return_obj.timestamp_precision = obj.get_timestamp_precision()
        return_obj.source = InformationSource.from_obj(obj.get_Source())
        return_obj.refernce = obj.get_Reference()
        return_obj.confidence = Confidence.from_obj(obj.get_Confidence())
        return_obj.description = StructuredText.from_obj(obj.get_Description())
        return_obj.related_observables = RelatedObservables.from_obj(obj.get_Related_Observables())
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
        return_obj.description = StructuredText.from_dict(d.get('description'))
        return_obj.related_observables = RelatedObservables.from_dict(d.get('related_observables'))
        return return_obj

class Sightings(stix.EntityList):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = _binding.SightingsType
    _contained_type = Sighting
    _binding_var = "Sighting"
    _inner_name = "sightings"
    
    def __init__(self, sightings_count=None, *args):
        super(Sightings, self).__init__(*args)
        self.sightings_count = sightings_count

    def __nonzero__(self):
        return super(Sightings, self).__nonzero__() or bool(self.sightings_count)

    def to_obj(self, return_obj=None, ns_info=None):
        self._collect_ns_info(ns_info)

        list_obj = super(Sightings, self).to_obj(ns_info=ns_info)
        list_obj.set_sightings_count(self.sightings_count)
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
        return_obj.sightings_count = obj.get_sightings_count()
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
