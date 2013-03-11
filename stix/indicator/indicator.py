import stix
import stix.common
from stix.utils import IDGenerator as stix_id_generator
import stix.bindings.stix_indicator_1_1 as stix_indicator_binding
from cybox.core import Observable,ObservableComposition
from cybox.common import Time


class Indicator(stix.Entity):
    TYPE_SOURCE_ORG = 0
    TYPE_SOURCE_PERSON = 1
    TYPES_SOURCE = (SOURCE_ORG, SOURCE_PERSON)
    
    def __init__(self, id=None, producer=stix.common.InformationSource(), observables=[]):
        self._id = id if id is not None else stix_id_generator().create_id()
        self.producer = producer
        self.observables = []
        
        for observable in observables:
            self.add_observable(observable)
            
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
    def observables(self, value):
        raise ValueError('do not set observables directly; call add_observable()')
    
    def add_source(self, type, name):
        '''
        Adds a source to this indicator. 
        
        Keyword arguments:
        type -- the type of source (Indicator.TYPE_SOURCE_ORG, Indicator.TYPE_SOURCE_PERSON)
        name -- the name of the source
        '''
        if type not in TYPES_SOURCE:
            raise ValueError('type not known')
        
        if type == TYPE_SOURCE_ORG:
            org_name_element = stix.common.OrganisationNameElement(org_name)
            org_name = stix.common.OrganisationName()
            org_name.add_organisation_name_element(org_name_element)
            self.producer.identity.party_name.add_organisation_name(org_name)
        
        if type == TYPE_SOURCE_PERSON:
            person_name_element = stix.common.PersonNameElement(person_name)
            person_name = stix.common.PersonName()
            person_name.add_name_element(person_name_element)
            self.producer.identity.party_name.add_person_name(person_name)
    
    def get_sources(self):
        '''
        Returns a dictionary of source information.
        dict = {
                'people' : list of person names (stix.common.identity.PersonName)
                'orgs' : list of organisation names (stix.common.identity.OrganisationName)
                'unknown' : list of names where the type is unknown (stix.common.identity.NameLine)
                }
        '''
        
        list_people = []
        list_orgs = []
        list_names = []
        
        # get the source people
        try:
            party_name = self.producer.identity.party_name
            list_people.extend(party_name.person_names)
        except: 
            pass
       
        # get the source_organizations
        try:
            party_name = self.producer.identity.party_name
            list_orgs.extend(party_name.organisation_names)
        except:
            pass
        
        # get the namelines
        try:
            part_name = self.producer.identity.party_name
            list_names.extend(party_name.name_lines)
        except:
            pass
        
        return {'people' : list_people, 'orgs' : list_orgs, 'unknown' : list_names}
            
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
    
    def add_object(self, object):
        ''' The object paramter is wrapped in an observable and attached to the indicator. The object must be a 
            cybox.core.DefinedObject instance'''
        
        observable = Observable(stateful_measure=object)
        self.add_observable(observable)
    
    def to_obj(self, return_obj=stix_indicator_binding.IndicatorType()):
        '''most of this does not work because of the state of the cybox api development'''
        if self.observables:
            if len(self.observables) > 1:
                root_observable = self._merge_observables(self.observables)
                return_obj.set_Observable(root_observable.to_obj())
            else:
                root_observable = self.observables[0]
                return_obj.set_Observable(root_observable.to_obj())

        return_obj.set_Producer(self.producer.to_obj())
    
        return return_obj
    
    @staticmethod
    def from_obj(obj, return_obj=Indicator()):        
        if obj.get_Producer():
            return_obj.producer = stix.common.InformationSource.from_obj(indicator_obj.get_Producer())
        
        if obj.get_Observables() and indicator_obj.get_Observables().get_Observable():
            observable_obj = indicator_obj.get_Observables().get_Observable()
            observable = Observable.from_obj(observable_obj)
            return_obj.observables.append(observable)
        
        return return_obj
    
    def to_dict(self, return_dict={}):
        if self.observables:
            if len(observables) == 1:
                return_dict['observables'] = self.observables[0].to_dict()
            else:
                composite_observable = self._merge_observables(self.observables)
                return_dict['observables'] = composite_observable.to_dict()
        
        if self.producer:
            return_dict['producer'] = self.producer.to_dict()
        
        return return_dict
        
    
    @staticmethod
    def from_dict(dict_repr, return_obj=Indicator()):
        observable_dict = dict_repr.get('observables', None)
        producer_dict = dict_repr.get('producer', None)
        
        if observable_dict:
            return_obj.add_observable(Observable.from_dict(observable_dict))
            
        if producer_dict:
            return_obj.producer = stix.common.InformationSource.from_dict(producer_dict)
        
        return return_obj
    
    
    
    
