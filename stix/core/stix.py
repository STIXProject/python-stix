'''
Created on Mar 5, 2013

@author: BWORRELL
'''

import stix
from stix.utils import IDGenerator as stix_id_generator
from stix.indicator import Indicator


class STIX(stix.Entity):
    '''
    classdocs
    '''

    def __init__(self, id=None, idref=None, indicators=[]):
        '''
        Constructor
        '''
        self.id_ = id if id else stix_id_generator().create_id() 
        self.idref_ = idref
        self.indicators=[]
    
    
    @property
    def indicators(self):
        return self._indicators
    
    @indicators.setter
    def indicators(self, value):
        if value:
            raise ValueError('do not set indicators. call add_indicator() instead')    
    
    def add_indicator(self, indicator):
        if not isinstance(indicator, Indicator):
            raise ValueError('indicator must be instance of stix.indicator.Indicator')
    
        self.indicators.append(indicator)
        
        
    def to_obj(self, return_obj=None):
        pass
    
    
    def to_dict(self):
        pass
    
        
    @classmethod
    def from_obj(cls, obj):
        pass
    
    
    @classmethod
    def from_dict(cls, dict_repr):
        pass
    