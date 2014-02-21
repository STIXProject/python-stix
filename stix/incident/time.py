# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import dateutil
import stix.bindings.incident as incident_binding
from stix.common import DateTimeWithPrecision
from datetime import datetime


class Time(stix.Entity):
    _binding = incident_binding
    _binding_class = _binding.TimeType
    _namespace = "http://stix.mitre.org/Incident-1"

    def __init__(self):
        self.first_malicious_action = None
        self.initial_compromise = None
        self.first_data_exfiltration = None
        self.incident_discovery = None
        self.incident_opened = None
        self.containment_achieved  = None
        self.restoration_achieved = None
        self.incident_reported = None
        self.incident_closed = None

    @property
    def first_malicious_action(self):
        return self._first_malicious_action

    @first_malicious_action.setter
    def first_malicious_action(self, value):
        if value:
            if isinstance(value, DateTimeWithPrecision):
                self._first_malicious_action = value
            else:
                self._first_malicious_action = DateTimeWithPrecision(value=value)
        else:
            self._first_malicious_action = None

    @property
    def initial_compromise(self):
        return self._initial_compromise

    @initial_compromise.setter
    def initial_compromise(self, value):
        if value:
            if isinstance(value, DateTimeWithPrecision):
                self._initial_compromise = value
            else:
                self._initial_compromise = DateTimeWithPrecision(value=value)
        else:
            self._initial_compromise = None

    @property
    def first_data_exfiltration(self):
        return self._first_data_exfiltration

    @first_data_exfiltration.setter
    def first_data_exfiltration(self, value):
        if value:
            if isinstance(value, DateTimeWithPrecision):
                self._first_data_exfiltration = value
            else:
                self._first_data_exfiltration = DateTimeWithPrecision(value=value)
        else:
            self._first_data_exfiltration = None

    @property
    def incident_discovery(self):
        return self._incident_discovery

    @incident_discovery.setter
    def incident_discovery(self, value):
        if value:
            if isinstance(value, DateTimeWithPrecision):
                self._incident_discovery = value
            else:
                self._incident_discovery = DateTimeWithPrecision(value=value)
        else:
            self._incident_discovery = None

    @property
    def incident_opened(self):
        return self._incident_opened

    @incident_opened.setter
    def incident_opened(self, value):
        if value:
            if isinstance(value, DateTimeWithPrecision):
                self._incident_opened = value
            else:
                self._incident_opened = DateTimeWithPrecision(value=value)
        else:
            self._incident_opened = None

    @property
    def containment_achieved(self):
        return self._containment_achieved

    @containment_achieved.setter
    def containment_achieved(self, value):
        if value:
            if isinstance(value, DateTimeWithPrecision):
                self._containment_achieved = value
            else:
                self._containment_achieved = DateTimeWithPrecision(value=value)
        else:
            self._containment_achieved = None

    @property
    def restoration_achieved(self):
        return self._restoration_achieved

    @restoration_achieved.setter
    def restoration_achieved(self, value):
        if value:
            if isinstance(value, DateTimeWithPrecision):
                self._restoration_achieved = value
            else:
                self._restoration_achieved = DateTimeWithPrecision(value=value)
        else:
            self._restoration_achieved = None

    @property
    def incident_reported(self):
        return self._incident_reported

    @incident_reported.setter
    def incident_reported(self, value):
        if value:
            if isinstance(value, DateTimeWithPrecision):
                self._incident_reported = value
            else:
                self._incident_reported = DateTimeWithPrecision(value=value)
        else:
            self._incident_reported = None

    @property
    def incident_closed(self):
        return self._incident_closed

    @incident_closed.setter
    def incident_closed(self, value):
        if value:
            if isinstance(value, DateTimeWithPrecision):
                self._incident_closed = value
            else:
                self._incident_closed = DateTimeWithPrecision(value=value)
        else:
            self._incident_closed = None


    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        if self.first_malicious_action:
            return_obj.set_First_Malicious_Action(self.first_malicious_action.to_obj())
        if self.initial_compromise:
            return_obj.set_Initial_Compromise(self.initial_compromise.to_obj())
        if self.first_data_exfiltration:
            return_obj.set_First_Data_Exfiltration(self.first_data_exfiltration.to_obj())
        if self._incident_discovery:
            return_obj.set_Incident_Discovery(self.incident_discovery.to_obj())
        if self.incident_opened:
            return_obj.set_Incident_Opened(self.incident_opened.to_obj())
        if self.containment_achieved:
            return_obj.set_Containment_Achieved(self.containment_achieved.to_obj())
        if self.restoration_achieved:
            return_obj.set_Restoration_Achieved(self.restoration_achieved.to_obj())
        if self.incident_reported:
            return_obj.set_Incident_Reported(self.incident_reported.to_obj())
        if self.incident_closed:
            return_obj.set_Incident_Closed(self.incident_closed.to_obj())

        return return_obj

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.first_malicious_action = DateTimeWithPrecision.from_obj(obj.get_First_Malicious_Action())
        return_obj.initial_compromise = DateTimeWithPrecision.from_obj(obj.get_Initial_Compromise())
        return_obj.first_data_exfiltration = DateTimeWithPrecision.from_obj(obj.get_First_Data_Exfiltration())
        return_obj.incident_discovery = DateTimeWithPrecision.from_obj(obj.get_Incident_Discovery())
        return_obj.incident_opened = DateTimeWithPrecision.from_obj(obj.get_Incident_Opened())
        return_obj.containment_achieved  = DateTimeWithPrecision.from_obj(obj.get_Containment_Achieved())
        return_obj.restoration_achieved = DateTimeWithPrecision.from_obj(obj.get_Restoration_Achieved())
        return_obj.incident_reported = DateTimeWithPrecision.from_obj(obj.get_Incident_Reported())
        return_obj.incident_closed = DateTimeWithPrecision.from_obj(obj.get_Incident_Closed())

        return return_obj

    def to_dict(self):
        d = {}
        if self.first_malicious_action:
            d['first_malicious_action'] = self.first_malicious_action.to_dict()
        if self.initial_compromise:
            d['initial_compromise'] = self.initial_compromise.to_dict()
        if self.first_data_exfiltration:
            d['first_data_exfiltration'] = self.first_data_exfiltration.to_dict()
        if self.incident_discovery:
            d['incident_discovery'] = self.incident_discovery.to_dict()
        if self.incident_opened:
            d['incident_opened'] = self.incident_opened.to_dict()
        if self.containment_achieved:
            d['containment_achieved'] = self.containment_achieved.to_dict()
        if self.restoration_achieved:
            d['restoration_achieved'] = self.restoration_achieved.to_dict()
        if self.incident_reported:
            d['incident_reported'] = self.incident_reported.to_dict()
        if self.incident_closed:
            d['incident_closed'] = self.incident_closed.to_dict()

        return d

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.first_malicious_action = DateTimeWithPrecision.from_dict(dict_repr.get('first_malicious_action'))
        return_obj.initial_compromise = DateTimeWithPrecision.from_dict(dict_repr.get('initial_compromise'))
        return_obj.first_data_exfiltration = DateTimeWithPrecision.from_dict(dict_repr.get('first_data_exfiltration'))
        return_obj.incident_discovery = DateTimeWithPrecision.from_dict(dict_repr.get('incident_discovery'))
        return_obj.incident_opened = DateTimeWithPrecision.from_dict(dict_repr.get('incident_opened'))
        return_obj.containment_achieved = DateTimeWithPrecision.from_dict(dict_repr.get('containment_achieved'))
        return_obj.restoration_achieved = DateTimeWithPrecision.from_dict(dict_repr.get('restoration_achieved'))
        return_obj.incident_reported = DateTimeWithPrecision.from_dict(dict_repr.get('incident_reported'))
        return_obj.incident_closed = DateTimeWithPrecision.from_dict(dict_repr.get('incident_closed'))

        return return_obj

