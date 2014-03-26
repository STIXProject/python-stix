# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.utils
from stix.utils import dates
from stix.common import (Identity, InformationSource, StructuredText, VocabString, 
                         Confidence, RelatedTTP)
import stix.extensions.identity as ext_identity
import stix.bindings.indicator as indicator_binding
from .test_mechanism import _BaseTestMechanism
from .sightings import Sightings
from stix.common.related import GenericRelationshipList, RelatedCOA
from cybox.core import Observable, ObservableComposition
from cybox.common import Time

class IndicatorType(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:IndicatorTypeVocab-1.0'

class SuggestedCOAs(GenericRelationshipList):
    _namespace = "http://stix.mitre.org/Indicator-2"
    _binding = indicator_binding
    _binding_class = indicator_binding.SuggestedCOAsType
    _binding_var = "Suggested_COA"
    _contained_type = RelatedCOA
    _inner_name = "suggested_coas"

    def __init__(self, suggested_coas=None, scope=None):
        if suggested_coas is None:
            suggested_coas = []
        super(SuggestedCOAs, self).__init__(*suggested_coas, scope=scope)

class Indicator(stix.Entity):
    _binding = indicator_binding
    _binding_class = indicator_binding.IndicatorType
    _namespace = 'http://stix.mitre.org/Indicator-2'
    _version = "2.1"

    def __init__(self, id_=None, idref=None, timestamp=None, title=None, description=None, short_description=None):
        self.id_ = id_ or stix.utils.create_id("indicator")
        self.idref = idref
        self.timestamp = timestamp
        self.version = self._version
        self.producer = None
        self.observables = None
        self.title = title
        self.description = description
        self.short_description = short_description
        self.indicator_types = None
        self.confidence = None
        self.indicated_ttps = None
        self.test_mechanisms = None
        self.alternative_id = None
        self.suggested_coas = SuggestedCOAs()
        self.sightings = Sightings()
        self.composite_indicator_expression = None
    
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
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, value):
        if value and not isinstance(value, InformationSource):
            raise ValueError('value must be instance of InformationSource')

        self._producer = value

    @property
    def observable(self):
        if self.observables:
            return self.observables[0]
        else:
            return None
    
    @observable.setter
    def observable(self, observable):
        self._observables = []
        self.add_observable(observable)

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
    def alternative_id(self):
        return self._alternative_id

    @alternative_id.setter
    def alternative_id(self, value):
        self._alternative_id = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_alternative_id(v)
        else:
            self.add_alternative_id(value)

    def add_alternative_id(self, value):
        if not value:
            return
        else:
            self.alternative_id.append(value)

    @property
    def indicator_types(self):
        return self._indicator_types

    @indicator_types.setter
    def indicator_types(self, value):
        self._indicator_types = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_indicator_type(v)
        else:
            self.add_indicator_type(value)

    def add_indicator_type(self, value):
        if not value:
            return
        elif isinstance(value, IndicatorType):
            self.indicator_types.append(value)
        else:
            tmp_indicator_type = IndicatorType(value=value)
            self.indicator_types.append(tmp_indicator_type)
            
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
            self._confidence = Confidence(value=value)

    @property
    def indicated_ttps(self):
        return self._indicated_ttps
    
    @indicated_ttps.setter
    def indicated_ttps(self, value):
        self._indicated_ttps = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_indicated_ttp(v)
        else:
            self.add_indicated_ttp(value)
            
    def add_indicated_ttp(self, v):
        if not v:
            return
        elif isinstance(v, RelatedTTP):
            self.indicated_ttps.append(v)
        else:
            self.indicated_ttps.append(RelatedTTP(v))
        
    @property
    def test_mechanisms(self):
        return self._test_mechanisms
    
    @test_mechanisms.setter
    def test_mechanisms(self, value):
        self._test_mechanisms = []
        if not value:
            return
        elif isinstance(value, list):
            for v in value:
                self.add_test_mechanism(v)
        else:
            self.add_test_mechanism(value)
            
    def add_test_mechanism(self, tm):
        if not tm:
            return
        elif isinstance(tm, _BaseTestMechanism):
            self.test_mechanisms.append(tm)
        else:
            raise ValueError('Cannot add type %s to test_mechanisms list' % type(tm))

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

        if isinstance(observable, Observable):
            self.observables.append(observable)
        else:
            # try to cast it to an Observable type
            self.observables.append(Observable(observable))

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
            return_obj = self._binding_class()

        return_obj.set_id(self.id_)
        return_obj.set_idref(self.idref)
        return_obj.set_timestamp(dates.serialize_value(self.timestamp))
        return_obj.set_Title(self.title)
        
        if self.version:
            return_obj.set_version(self._version)
        if self.description:
            return_obj.set_Description(self.description.to_obj())
        if self.short_description:
            return_obj.set_Short_Description(self.short_description.to_obj())
        if self.confidence:
            return_obj.set_Confidence(self.confidence.to_obj())
        if self.indicator_types:
            for indicator_type in self.indicator_types:
                tmp_indicator_type = indicator_type.to_obj()
                return_obj.add_Type(tmp_indicator_type)
        if self.indicated_ttps:
            return_obj.set_Indicated_TTP([x.to_obj() for x in self.indicated_ttps])
        if self.observables:
            if len(self.observables) > 1:
                root_observable = self._merge_observables(self.observables)
            else:
                root_observable = self.observables[0]
            return_obj.set_Observable(root_observable.to_obj())
        if self.producer:
            return_obj.set_Producer(self.producer.to_obj())
        if self.test_mechanisms:
            tms_obj = self._binding.TestMechanismsType()
            tms_obj.set_Test_Mechanism([x.to_obj() for x in self.test_mechanisms])
            return_obj.set_Test_Mechanisms(tms_obj)
        if self.alternative_id:
            return_obj.set_Alternative_ID(self.alternative_id)
        if self.suggested_coas:
            return_obj.set_Suggested_COAs(self.suggested_coas.to_obj())
        if self.sightings:
            return_obj.set_Sightings(self.sightings.to_obj())
        if self.composite_indicator_expression:
            return_obj.set_Composite_Indicator_Expression(self.composite_indicator_expression.to_obj())

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):        
        if not obj:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_              = obj.get_id()
        return_obj.idref            = obj.get_idref()
        return_obj.timestamp        = obj.get_timestamp()
        
        if isinstance(obj, cls._binding_class):
            return_obj.title            = obj.get_Title()
            return_obj.description      = StructuredText.from_obj(obj.get_Description())
            return_obj.short_description = StructuredText.from_obj(obj.get_Short_Description())
            return_obj.producer         = InformationSource.from_obj(obj.get_Producer())
            return_obj.confidence       = Confidence.from_obj(obj.get_Confidence())
            return_obj.sightings        = Sightings.from_obj(obj.get_Sightings())
            return_obj.composite_indicator_expression = CompositeIndicatorExpression.from_obj(obj.get_Composite_Indicator_Expression())
            
            if obj.get_version():
                return_obj.version = obj.get_version()
            if obj.get_Type():
                for indicator_type in obj.get_Type():
                    return_obj.add_indicator_type(IndicatorType.from_obj(indicator_type)) 
            if obj.get_Observable():
                observable_obj = obj.get_Observable()
                observable = Observable.from_obj(observable_obj)
                return_obj.observables.append(observable)
            if obj.get_Indicated_TTP():
                return_obj.indicated_ttps = [RelatedTTP.from_obj(x) for x in obj.get_Indicated_TTP()]
            if obj.get_Test_Mechanisms():
                return_obj.test_mechanisms = [_BaseTestMechanism.from_obj(x) for x in obj.get_Test_Mechanisms().get_Test_Mechanism()]
            if obj.get_Suggested_COAs():
                return_obj.suggested_coas = SuggestedCOAs.from_obj(obj.get_Suggested_COAs())
            if obj.get_Alternative_ID():
                return_obj.alternative_id = obj.get_Alternative_ID()

        
        return return_obj

    def to_dict(self):
        d = {}
        if self.id_:
            d['id'] = self.id_
        if self.idref:
            d['idref'] = self.idref
        if self.timestamp:
            d['timestamp'] = dates.serialize_value(self.timestamp)
        if self.version:
            d['version'] = self.version
        if self.observables:
            if len(self.observables) == 1:
                d['observable'] = self.observables[0].to_dict()
            else:
                composite_observable = self._merge_observables(self.observables)
                d['observable'] = composite_observable.to_dict()
        if self.producer:
            d['producer'] = self.producer.to_dict()
        if self.title:
            d['title'] = self.title
        if self.description:
            d['description'] = self.description.to_dict()
        if self.short_description:
            d['short_description'] = self.short_description.to_dict()
        if self.indicator_types:
            d['indicator_types'] = [x.to_dict() for x in self.indicator_types]
        if self.confidence:
            d['confidence'] = self.confidence.to_dict()
        if self.indicated_ttps:
            d['indicated_ttps'] = [x.to_dict() for x in self.indicated_ttps]
        if self.test_mechanisms:
            d['test_mechanisms'] = [x.to_dict() for x in self.test_mechanisms]
        if self.alternative_id:
            d['alternative_id'] = self.alternative_id
        if self.suggested_coas:
            d['suggested_coas'] = self.suggested_coas.to_dict()
        if self.sightings:
            d['sightings'] = self.sightings.to_dict()
        if self.composite_indicator_expression:
            d['composite_indicator_expression'] = self.composite_indicator_expression.to_dict()
        
        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if not return_obj:
            return_obj = cls()

        return_obj.id_       = dict_repr.get('id')
        return_obj.idref     = dict_repr.get('idref')
        return_obj.timestamp = dict_repr.get('timestamp')
        return_obj.title     = dict_repr.get('title')
        return_obj.version   = dict_repr.get('version', cls._version)
        observable_dict      = dict_repr.get('observable')
        producer_dict        = dict_repr.get('producer')
        description_dict     = dict_repr.get('description')
        indicator_type_list  = dict_repr.get('indicator_types')
        confidence_dict      = dict_repr.get('confidence')
        alternative_id_dict  = dict_repr.get('alternative_id')

        return_obj.short_description = StructuredText.from_dict(dict_repr.get('short_description'))
        return_obj.indicated_ttps = [RelatedTTP.from_dict(x) for x in dict_repr.get('indicated_ttps', [])]
        return_obj.test_mechanisms = [_BaseTestMechanism.from_dict(x) for x in dict_repr.get('test_mechanisms', [])]
        return_obj.suggested_coas = SuggestedCOAs.from_dict(dict_repr.get('suggested_coas'))
        return_obj.sightings = Sightings.from_dict(dict_repr.get('sightings'))
        return_obj.composite_indicator_expression = CompositeIndicatorExpression.from_dict(dict_repr.get('composite_indicator_expression'))
        
        if observable_dict:
            return_obj.add_observable(Observable.from_dict(observable_dict))
        if producer_dict:
            return_obj.producer = InformationSource.from_dict(producer_dict)
        if description_dict:
            return_obj.description = StructuredText.from_dict(description_dict)
        if indicator_type_list:
            for indicator_type_dict in indicator_type_list:
                return_obj.add_indicator_type(IndicatorType.from_dict(indicator_type_dict))
        if confidence_dict:
            return_obj.confidence = Confidence.from_dict(confidence_dict)
        if alternative_id_dict:
            return_obj.alternative_id = alternative_id_dict
        
        return return_obj

class CompositeIndicatorExpression(stix.EntityList):
    _binding = indicator_binding
    _binding_class = indicator_binding.CompositeIndicatorExpressionType
    _namespace = 'http://stix.mitre.org/Indicator-2'
    _contained_type = Indicator
    _binding_var = "Indicator"
    _inner_name = "indicators"
    
    OP_AND = "AND"
    OP_OR = "OR"
    OPERATORS = (OP_AND, OP_OR)
    
    def __init__(self, operator="OR", *args):
        super(CompositeIndicatorExpression, self).__init__(*args)
        self.operator = operator

    @property
    def operator(self):
        return self._operator
    
    @operator.setter
    def operator(self, value):
        if not value:
            raise ValueError("operator must not be None or empty")
        elif value not in self.OPERATORS:
            raise ValueError("operator must be one of: %s" % ",".join(self.OPERATORS))
        else:
            self._operator = value
            
    def __nonzero__(self):
        return super(CompositeIndicatorExpression, self).__nonzero__()

    def to_obj(self):
        list_obj = super(CompositeIndicatorExpression, self).to_obj()
        list_obj.set_operator(self.operator)
        return list_obj

    def to_dict(self):
        d = super(CompositeIndicatorExpression, self).to_dict()
        if self.operator:
            d['operator'] = self.operator
        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        if return_obj is None:
            return_obj = cls()

        super(CompositeIndicatorExpression, cls).from_obj(obj, return_obj=return_obj)
        return_obj.operator = obj.get_operator()
        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        if return_obj is None:
            return_obj = cls()

        super(CompositeIndicatorExpression, cls).from_dict(dict_repr, return_obj=return_obj)
        return_obj.operator = dict_repr.get('operator')
        return return_obj
    
