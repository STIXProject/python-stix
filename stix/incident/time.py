# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import dateutil
import stix.bindings.incident as incident_binding
from datetime import datetime

class Time(stix.Entity):
    _binding = incident_binding
    _namespace = "http://stix.mitre.org/Incident-1"
    
    def __init__(self):
        self.first_malicious_action = None
        self.initial_compromise = None
        self.first_data_exfiltration = None
        self.incident_discovery = None
        self.incident_opened = None
        self.containment_achieved  = None
        self.restoration_achieved = None
        self.incident_reported = None`
        self.incident_closed = None
    
    def _parse_value(self, value):
        if not value:
            return None
        elif isinstance(value, datetime):
            return value
        return dateutil.parser.parse(value)
    
    @property
    def first_malicious_action(self):
        return self._first_malicious_action
    
    @first_malicious_action.setter
    def first_malicious_action(self, value):
        self._first_malicious_action = self._parse_value(value)
        
    @property
    def initial_compromise(self):
        return self._initial_compromise
    
    @initial_compromise.setter
    def initial_compromise(self, value):
        self._initial_compromise = self._parse_value(value)
        
    @property
    def first_data_exfiltration(self):
        return self._first_data_exfiltration
    
    @first_data_exfiltration.setter
    def first_data_exfiltration(self, value):
        self._first_data_exfiltration = self._parse_value(value)
        
    @property
    def incident_discovery(self):
        return self._incident_discovery
    
    @incident_discovery.setter
    def incident_discovery(self, value):
        self._incident_discovery = self._parse_value(value)
        
    @property
    def incident_opened(self):
        return self._incident_opened
    
    @incident_opened.setter
    def incident_opened(self, value):
        self._incident_opened = self._parse_value(value)
        
    @property
    def containment_achieved(self):
        return self._containment_achieved
    
    @containment_achieved.setter
    def containment_achieved(self, value):
        self._first_malicious_action = self._parse_value(value)
        
    @property
    def restoration_achieved(self):
        return self._restoration_achieved
    
    @restoration_achieved.setter
    def restoration_achieved(self, value):
        self._restoration_achieved = self._parse_value(value)
        
    @property
    def incident_reported(self):
        return self._incident_reported
    
    @incident_reported.setter
    def incident_reported(self, value):
        self._incident_reported = self._parse_value(value)
        
    @property
    def incident_closed(self):
        return self._incident_closed
    
    @incident_closed.setter
    def incident_closed(self, value):
        self._incident_closed = self._parse_value(value)
        
    
    def to_obj(self, return_obj=None):
        pass
    
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not return_obj:
            return None
        
        if not return_obj:
            return_obj = cls()
            
        return_obj.first_malicious_action = None
        return_obj.initial_compromise = None
        return_obj.first_data_exfiltration = None
        return_obj.incident_discovery = None
        return_obj.incident_opened = None
        return_obj.containment_achieved  = None
        return_obj.restoration_achieved = None
        return_obj.incident_reported = None
        return_obj.incident_closed = None
