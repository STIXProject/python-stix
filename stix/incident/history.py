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
    
#     def to_obj(self, return_obj=None, ns_info=None):
#         super(JournalEntry, self).to_obj(return_obj=return_obj, ns_info=ns_info)
# 
#         if not return_obj:
#             return_obj = self._binding_class()
#         
#         return_obj.valueOf_ = self.value
#         return_obj.author = self.author
#         return_obj.time = utils.dates.serialize_value(self.time)
#         return_obj.time_precision = self.time_precision
#         
#         return return_obj
#     
#     @classmethod
#     def from_obj(cls, obj, return_obj=None):
#         if not obj:
#             return None
#         
#         if not return_obj:
#             return_obj = cls()
#             
#         return_obj.value = obj.valueOf_
#         return_obj.author = obj.author
#         return_obj.time = obj.time
#         return_obj.time_precision = obj.time_precision
#         
#         return return_obj
#         
#     def to_dict(self):
#         return super(JournalEntry, self).to_dict()
# 
#     @classmethod
#     def from_dict(cls, d, return_obj=None):
#         if not d:
#             return None
#         
#         if not return_obj:
#             return_obj = cls()
#             
#         return_obj.value = d.get('value')
#         return_obj.author = d.get('author')
#         return_obj.time = d.get('time')
#         return_obj.time_precision = d.get('time_precision')
#         
#         return return_obj


class HistoryItem(stix.Entity):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.HistoryItemType
    
    action_entry = fields.TypedField("Action_Entry", COATaken)
    journal_entry = fields.TypedField("Journal_Entry", JournalEntry)
    
    def __init__(self):
        super(HistoryItem, self).__init__()
            
#     def to_obj(self, return_obj=None, ns_info=None):
#         super(HistoryItem, self).to_obj(return_obj=return_obj, ns_info=ns_info)
# 
#         if not return_obj:
#             return_obj = self._binding_class()
#             
#         if self.action_entry:
#             return_obj.Action_Entry = self.action_entry.to_obj(ns_info=ns_info)
#         if self.journal_entry:
#             return_obj.Journal_Entry = self.journal_entry.to_obj(ns_info=ns_info)
#         
#         return return_obj
#     
#     @classmethod
#     def from_obj(cls, obj, return_obj=None):
#         if not obj:
#             return None
#         
#         if not return_obj:
#             return_obj = cls()
#             
#         return_obj.action_entry = COATaken.from_obj(obj.Action_Entry)
#         return_obj.journal_entry = JournalEntry.from_obj(obj.Journal_Entry)
#         
#         return return_obj
#             
#     def to_dict(self):
#         return super(HistoryItem, self).to_dict()
#     
#     @classmethod
#     def from_dict(cls, d, return_obj=None):
#         if not d:
#             return None
#         
#         if not return_obj:
#             return_obj = cls()
#             
#         return_obj.action_entry = COATaken.from_dict(d.get('action_entry'))
#         return_obj.journal_entry = JournalEntry.from_dict(d.get('journal_entry'))
#         
#         return return_obj


class History(stix.EntityList):
    _namespace = "http://stix.mitre.org/Incident-1"
    _binding = incident_binding
    _binding_class = incident_binding.HistoryType

    history_items = fields.TypedField("History_Item", HistoryItem, multiple=True, key_name="history_items")
    