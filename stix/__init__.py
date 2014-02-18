# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

__version__ = "1.0.1.1"

import json
from StringIO import StringIO


class Entity(object):
    """Base class for all classes in the STIX API."""

    def to_obj(self, return_obj=None):
        """Export an object as a binding object representation"""
        raise NotImplementedError()
    
    @classmethod
    def from_obj(cls, obj):
        """Create an object from a binding object"""
        raise NotImplementedError()

    def _get_namespaces(self, ns_dict):
        import stix.utils.nsparser as nsparser
        import cybox.utils.nsparser as cybox_nsparser
        import stix.utils.idgen as idgen
        
        if not ns_dict: ns_dict = {}
        xml_ns_dict = {'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
                       'http://stix.mitre.org/stix-1': 'stix',
                       'http://stix.mitre.org/common-1': 'stixCommon',
                       'http://stix.mitre.org/default_vocabularies-1': 'stixVocabs',
                       idgen.get_id_namespace() : idgen.get_id_namespace_alias()}
        
        namespace_parser = nsparser.NamespaceParser()
        all_ns_dict = dict(xml_ns_dict)
        ns_set = namespace_parser.get_namespaces(self)
        
        for ns in ns_set:
            if ns in ns_dict:
                all_ns_dict[ns] = ns_dict[ns]
            elif ns.startswith("http://cybox.mitre.org"):
                for cybox_ns_tup in cybox_nsparser.NS_LIST:
                    if ns == cybox_ns_tup[0]:
                        all_ns_dict[ns] = cybox_ns_tup[1]
            elif ns in nsparser.DEFAULT_EXT_TO_PREFIX:
                all_ns_dict[ns] = nsparser.DEFAULT_EXT_TO_PREFIX[ns]
            else:
                all_ns_dict[ns] = nsparser.DEFAULT_STIX_NS_TO_PREFIX[ns]
        
        return all_ns_dict
    
    def _get_schema_locations(self):
        import stix.utils.nsparser as nsparser
        schemaloc_dict = nsparser.NamespaceParser().get_namespace_schemalocation_dict(self)
        return schemaloc_dict
        
    def to_xml(self, include_namespaces=True, ns_dict=None, pretty=True):
        """Export an object as an XML String""" 
        s = StringIO()
        namespace_def = ""
        
        import stix.utils.nsparser as nsparser
        if include_namespaces:
            if not ns_dict: ns_dict = {}
            all_ns_dict = self._get_namespaces(ns_dict)
            schemaloc_dict = self._get_schema_locations()
            namespace_def = nsparser.NamespaceParser().get_namespace_def_str(all_ns_dict, schemaloc_dict)
        else:
            all_ns_dict = dict(nsparser.DEFAULT_STIX_NS_TO_PREFIX.items() + nsparser.DEFAULT_EXT_TO_PREFIX.items())
            
        if not pretty:
            namespace_def = namespace_def.replace('\n\t', ' ')
        
        self.to_obj().export(s, 0, all_ns_dict, pretty_print=pretty, namespacedef_=namespace_def)
        return s.getvalue()

    def to_json(self):
        return json.dumps(self.to_dict())

    def to_dict(self, return_dict=None):
        raise NotImplementedError()

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        """Convert from dict representation to object representation. This should be overriden by a subclass"""
        raise NotImplementedError()

    @classmethod
    def object_from_dict(cls, entity_dict):
        """Convert from dict representation to object representation."""
        return cls.from_dict(entity_dict).to_obj()

    @classmethod
    def dict_from_object(cls, entity_obj):
        """Convert from object representation to dict representation."""
        return cls.from_obj(entity_obj).to_dict()
\
