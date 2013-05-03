# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
import stix.common
import stix.bindings.indicator as indicator_binding
from cybox.core import Observable, ObservableComposition
from cybox.common import Time

class Indicator(stix.Entity):
    TYPE_SOURCE_ORG = 0
    TYPE_SOURCE_PERSON = 1
    TYPES_SOURCE = (TYPE_SOURCE_ORG, TYPE_SOURCE_PERSON)
    
    def __init__(self, id_=None, producer=None, observables=None):
        self.id_ = id_ if id_ is not None else stix.utils.create_id()
        self.producer = producer if producer else stix.common.InformationSource()
        self.observables = observables
        self.name = None
        self.description = None
            
    @property
    def producer(self):
        return self._producer
    
    @producer.setter
    def producer(self, value):
        if value and not isinstance(value, stix.common.InformationSource):
            raise ValueError('value must be instance of InformationSource')
        
        self._producer = value
    
    @property
    def observables(self):
        return self._observables
    
    @observables.setter
    def observables(self, valuelist):
        self._observables = [] # initialize the variable
        
        if valuelist:
            for value in valuelist:
                self.add_observable(value)
    
    def add_source(self, type_, name):
        '''
        Adds a source to this indicator. 
        
        Keyword arguments:
        type_ -- the type_ of source (Indicator.TYPE_SOURCE_ORG, Indicator.TYPE_SOURCE_PERSON)
        name -- the name of the source
        '''
        if type_ not in self.TYPES_SOURCE:
            raise ValueError('type_ not known')
        
        if type_ == self.TYPE_SOURCE_ORG:
            org_name_element = stix.common.OrganisationNameElement(value=name)
            org_name = stix.common.OrganisationName()
            org_name.add_organisation_name_element(org_name_element)
            self.producer.identity.party_name.add_organisation_name(org_name)
        
        if type_ == self.TYPE_SOURCE_PERSON:
            person_name_element = stix.common.PersonNameElement(value=name)
            person_name = stix.common.PersonName()
            person_name.add_name_element(person_name_element)
            self.producer.identity.party_name.add_person_name(person_name)
    
    def get_sources(self):
        '''
        Returns a dictionary of source information, effectively returning
        self.producer.identity.party_name.to_dict()
       '''
        try:
            return_dict = self.producer.identity.party_name.to_dict()
        except:
            return_dict = {}
        
        return return_dict
            
    def set_produced_time(self, produced_time):
        '''The produced date variable must be in ISO 8601 format'''
        if not self.producer.time:
            self.producer.time = Time
            
        self.producer.time.produced_time = produced_time
    
    def get_produced_time(self):
        if self.producer and self.producer.time:
            return self.producer.time.produced_time
        else:
            return None    
    
    def set_received_time(self, received_time):
        '''Set the time when this indicator was received'''
        if not self.producer.time:
            self.producer.time = Time()

        self.producer.time.received_time = received_time
    
    def get_received_time(self):
        '''Return the time when this indicator was received'''
        if self.producer and self.producer.time:
            return self.producer.time.received_time
        else:
            return None
    
        
    def add_observable(self, observable):
        ''' Adds an observable to the Indicator. If the number of observables associated with this indicator 
            is greater than one, the indicator will nest all of its observables under a parent observable
            composition, with an logical operator of 'OR'. If this is not ideal, an separate indicator
            should be made for each observable'''
        
        if not isinstance(observable, Observable):
            raise ValueError('observable must be instance of Observable')
        
        self.observables.append(observable)
    
    def _merge_observables(self, observables, operator='AND'):
        observable_composition = ObservableComposition()
        observable_composition.operator = operator
        
        for observable_ in observables:
            observable_composition.add(observable_)
        
        root_observable = Observable()
        root_observable.observable_composition = observable_composition
        
        return root_observable
    
    def add_object(self, object_):
        ''' The object paramter is wrapped in an observable and attached to the indicator. The object must be a 
            cybox.core.DefinedObject instance'''
        
        observable = Observable(object_)
        self.add_observable(observable)
    
    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = indicator_binding.IndicatorType()
        
        if self.id_:
            return_obj.set_id(self.id_)
        
        '''most of this does not work because of the state of the cybox api development'''
        if self.observables:
            if len(self.observables) > 1:
                root_observable = self._merge_observables(self.observables)
            else:
                root_observable = self.observables[0]
            
            return_obj.set_Observable(root_observable)

        return_obj.set_Producer(self.producer.to_obj())
    
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):        
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        return_obj.id_ = obj.get_id()
        
        if obj.get_Producer():
            return_obj.producer = stix.common.InformationSource.from_obj(obj.get_Producer())
        
        if obj.get_Observables() and obj.get_Observables().get_Observable():
            observable_obj = obj.get_Observables().get_Observable()
            observable = Observable.from_obj(observable_obj)
            return_obj.observables.append(observable)
        
        return return_obj
    
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        if self.id_:
            return_dict['id'] = self.id_
        
        if self.observables:
            if len(self.observables) == 1:
                return_dict['observable'] = self.observables[0].to_dict()
            else:
                composite_observable = self._merge_observables(self.observables)
                return_dict['observable'] = composite_observable.to_dict()
        
        if self.producer:
            return_dict['producer'] = self.producer.to_dict()
        
        return return_dict
        
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        return_obj.id_ = dict_repr.get('id', None)
        
        observable_dict = dict_repr.get('observable', )
        producer_dict = dict_repr.get('producer', None)
        
        if observable_dict:
            return_obj.add_observable(Observable.from_dict(observable_dict))
            
        if producer_dict:
            return_obj.producer = stix.common.InformationSource.from_dict(producer_dict)
        
        return return_obj
    
    
    
    
