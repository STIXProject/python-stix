# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix.common import Identity, InformationSource, StructuredText, VocabString
import stix.extensions.identity as ext_identity
import stix.bindings.indicator as indicator_binding
from cybox.core import Observable, ObservableComposition
from cybox.common import Time

    
class IndicatorType(VocabString):
    _XSI_TYPE = 'stixVocabs:IndicatorTypeVocab-1.0'


class Indicator(stix.Entity):
    def __init__(self, id_=None, title=None, description=None, indicator_type=None, producer=None, observables=None):
        self.id_ = id_ if id_ is not None else stix.utils.create_id()
        self.producer = producer
        self.observables = observables
        self.title = title
        self.description = description
        self.indicator_type = indicator_type
        
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
    def producer(self):
        return self._producer
    
    @producer.setter
    def producer(self, value):
        if value and not isinstance(value, InformationSource):
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
  
    @property
    def indicator_type(self):
        return self._indicator_type

    @indicator_type.setter
    def indicator_type(self, value):
        if value and not isinstance(value, IndicatorType):
            value = IndicatorType(value)

        self._indicator_type = value
  
  
    def set_producer_identity(self, identity):
        '''
        Sets the name of the producer of this indicator.
        The identity param can be a string (name) or an Identity
        instance.
        '''
        if not self.producer:
            self.producer = InformationSource()
        
        if isinstance(identity, Identity):
            self.producer.identity = identity
        else:
            if not self.producer.identity:
                self.producer.identity = Identity()
            
            self.producer.identity.name = identity # assume it's a string
            
  
            
    def set_produced_time(self, produced_time):
        '''The produced date variable must be in ISO 8601 format'''
        if not self.producer.time:
            self.producer.time = Time()
            
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
        
        if self.description:
            return_obj.set_Description(self.description.to_obj())
        
        if self.indicator_type:
            return_obj.set_Type(self.indicator_type.to_obj())
        
        return_obj.set_Title(self.title)

        if self.observables:
            if len(self.observables) > 1:
                root_observable = self._merge_observables(self.observables)
            else:
                root_observable = self.observables[0]
            
            return_obj.set_Observable(root_observable.to_obj())

        if self.producer:
            return_obj.set_Producer(self.producer.to_obj())
    
        return return_obj
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):        
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        return_obj.id_              = obj.get_id()
        return_obj.title            = obj.get_Title()
        return_obj.description      = StructuredText.from_obj(obj.get_Description())
        return_obj.producer         = InformationSource.from_obj(obj.get_Producer())
        return_obj.indicator_type   = IndicatorType.from_obj(obj.get_Type()) 
        
        if obj.get_Observable():
            observable_obj = obj.get_Observable()
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
            
        if self.title:
            return_dict['title'] = self.title
            
        if self.description:
            return_dict['description'] = self.description.to_dict()
        
        if self.indicator_type:
            return_dict['indicator_type'] = self.indicator_type.to_dict()
        
        return return_dict
        
    
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        return_obj.id_      = dict_repr.get('id')
        return_obj.title    = dict_repr.get('title')
        observable_dict     = dict_repr.get('observable')
        producer_dict       = dict_repr.get('producer')
        description_dict    = dict_repr.get('description')
        indicator_type_dict = dict_repr.get('indicator_type')
        
        if observable_dict:
            return_obj.add_observable(Observable.from_dict(observable_dict))
            
        if producer_dict:
            return_obj.producer = InformationSource.from_dict(producer_dict)
        
        if description_dict:
            return_obj.description = StructuredText.from_dict(description_dict)
        
        if indicator_type_dict:
            return_obj.indicator_type = IndicatorType.from_dict(indicator_type_dict)
        
        return return_obj
    
    

    
