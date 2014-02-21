# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix.utils.parser import EntityParser
from stix_header import STIXHeader
from stix.indicator import Indicator
from stix.incident import Incident
from cybox.core import Observables

import stix.bindings.stix_core as stix_core_binding
import cybox.bindings.cybox_core as cybox_core_binding

from StringIO import StringIO

class STIXPackage(stix.Entity):
    _binding = stix_core_binding
    _namespace = 'http://stix.mitre.org/stix-1'
    _version = "1.1"

    def __init__(self, id_=None, idref_=None, stix_header=None, indicators=None, observables=None, incidents=None):
        self.id_ = id_ or stix.utils.create_id("Package")
        self.idref_ = idref_
        self.version = self._version
        self.indicators = indicators
        self.observables = observables
        self.incidents = incidents
        self.stix_header = stix_header

    @property
    def stix_header(self):
        return self._stix_header

    @stix_header.setter
    def stix_header(self, value):
        if value and not isinstance(value, STIXHeader):
            raise ValueError('value must be instance of STIXHeader')

        self._stix_header = value

    @property
    def indicators(self):
        return self._indicators

    @indicators.setter
    def indicators(self, value):
        self._indicators = []

        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_indicator(v)
        else:
            self.add_indicator(value)

    @property
    def observables(self):
        return self._observables

    @observables.setter
    def observables(self, value):
        if value and not isinstance(value, Observables):
            raise ValueError('value must be instance of cybox.core.Observables')

        self._observables = value

    @property
    def incidents(self):
        return self._incidents
    
    @incidents.setter
    def incidents(self, value):
        self._incidents = []
        
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_incident(v)
        else:
            self.add_incident(value)
    
    def add_incident(self, incident):
        if not incident:
            return
        elif isinstance(incident, Incident):
            self.incidents.append(incident)
        else:
            raise ValueError('Cannot add %s to incident list' % type(incident))

    def add_indicator(self, indicator):
        if not indicator:
            return
        elif isinstance(indicator, Indicator):
            self.indicators.append(indicator)
        else:
            raise ValueError('indicator must be instance of stix.indicator.Indicator')

    def add_observable(self, observable):
        if not self.observables:
            self.observables = Observables(observable)
        else:
            self.observables.add(observable)

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding.STIXType()

        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref_)
        return_obj.set_version(self.version)

        if self.stix_header:
            return_obj.set_STIX_Header(self.stix_header.to_obj())

        if self.indicators:
            indicators_obj = stix_core_binding.IndicatorsType()
            indicators_obj.set_Indicator([x.to_obj() for x in self.indicators])
            return_obj.set_Indicators(indicators_obj)

        if self.observables:
            return_obj.set_Observables(self.observables.to_obj())

        if self.incidents:
            incidents_obj = stix_core_binding.IncidentsType()
            incidents_obj.set_Incident([x.to_obj() for x in self.incidents])
            return_obj.set_Incidents(incidents_obj)
            
        return return_obj

    def to_dict(self, d=None):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.version:    
            d['version'] = self.version
        if self.idref_:
            d['idref'] = self.idref_
        if self.stix_header:
            d['stix_header'] = self.stix_header.to_dict()
        if self.indicators:
            d['indicators'] = [x.to_dict() for x in self.indicators]
        if self.observables:
            d['observables'] = self.observables.to_dict()
        if self.incidents:
            d['incidents'] = [x.to_dict() for x in self.incidents]

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = obj.get_id()
        return_obj.idref_ = obj.get_idref()
        return_obj.stix_header = STIXHeader.from_obj(obj.get_STIX_Header())

        if obj.get_version():
            return_obj.version = obj.get_version()
        if obj.get_Indicators():
            return_obj.indicators = [Indicator.from_obj(x) for x in obj.get_Indicators().get_Indicator()]
        if obj.get_Observables():
            return_obj.observables = Observables.from_obj(obj.get_Observables())
        if obj.get_Incidents():
            return_obj.incidents = [Incident.from_obj(x) for x in obj.get_Incidents().get_Incident()]
        
        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not return_obj:
            return_obj = cls()

        return_obj.id_ = dict_repr.get('id', None)
        return_obj.idref_ = dict_repr.get('idref', None)
        return_obj.version = dict_repr.get('version', cls._version)
        header_dict = dict_repr.get('stix_header', None)
        return_obj.stix_header = STIXHeader.from_dict(header_dict)
        return_obj.indicators = [Indicator.from_dict(x) for x in dict_repr.get('indicators', [])]
        return_obj.observables = Observables.from_dict(dict_repr.get('observables'))
        return_obj.incidents = [Incident.from_dict(x) for x in dict_repr.get('incidents', [])]

        return return_obj

    @classmethod
    def from_xml(cls, xml_file):
        parser = EntityParser()
        return parser.parse_xml(xml_file)



