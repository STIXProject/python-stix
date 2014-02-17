# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

from . import VocabString, StructuredText, HighMediumLow

class Statement(object):
    def __init__(self, value=None, description=None, source=None):
        self.value = value
        self.description = description
        self.source = source
        self.confidence = None
        
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if isinstance(value, HighMediumLow):
            self._value = value
        else:
            self._value = HighMediumLow(value=value)
    
    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, value):
        if isinstance(value, VocabString):
            self._source = value
        else:
            self._source = VocabString(value=value)
    
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
    def confidence(self):
        return self._confidence
    
    @confidence.setter
    def confidence(self, value):
        if value:
            raise NotImplementedError()
        
