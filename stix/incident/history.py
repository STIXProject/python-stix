# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# internal
import stix
import stix.utils as utils
import stix.bindings.incident as incident_binding
from stix.common.datetimewithprecision import DATETIME_PRECISION_VALUES

# relative
from .coa import COATaken

from mixbox import fields, entities

def validate_precision(instance, value):
    if value and (value not in DATETIME_PRECISION_VALUES):
        error = "time_precision must be one of {0}. Received '{1}'"
        error = error.format(DATETIME_PRECISION_VALUES, value)
        raise ValueError(error)

class JournalEntry(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.JournalEntryType
    
    value = fields.TypedField("valueOf_", key_name="value")
    author = fields.TypedField("author")
    time = fields.TypedField("time")     #TDOO: utils.dates.parse_value(value)
    time_precision = fields.TypedField("time_precision", preset_hook=validate_precision)
    
    def __init__(self, value=None):
        super(JournalEntry, self).__init__()
        self.value = value
        self.time_precision = 'second'


class HistoryItem(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.HistoryItemType
    
    action_entry = fields.TypedField("Action_Entry", COATaken)
    journal_entry = fields.TypedField("Journal_Entry", JournalEntry)
    
    def __init__(self):
        super(HistoryItem, self).__init__()


class History(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.HistoryType

    history_items = fields.TypedField("History_Item", HistoryItem, multiple=True, key_name="history_items")
    
    @classmethod
    def _dict_as_list(cls):
        return False
    