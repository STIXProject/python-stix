# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

__version__ = "1.1.0.2"

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
        namespace_parser = nsparser.NamespaceParser()
        all_ns_dict = namespace_parser.get_namespaces(self, ns_dict=ns_dict)        
        return all_ns_dict

    def _get_schema_locations(self, ns_dict=None):
        import stix.utils.nsparser as nsparser
        schemaloc_dict = nsparser.NamespaceParser().get_namespace_schemalocation_dict(self, ns_dict=ns_dict)
        return schemaloc_dict

    def to_xml(self, include_namespaces=True, ns_dict=None, pretty=True):
        """Export an object as an XML String""" 
        s = StringIO()
        namespace_def = ""

        import stix.utils.nsparser as nsparser
        if include_namespaces:
            if not ns_dict: ns_dict = {}
            all_ns_dict = self._get_namespaces(ns_dict)
            schemaloc_dict = self._get_schema_locations(all_ns_dict)
            namespace_def = nsparser.NamespaceParser().get_namespace_def_str(all_ns_dict, schemaloc_dict)
        else:
            all_ns_dict = dict(nsparser.DEFAULT_STIX_NS_TO_PREFIX.items() + nsparser.DEFAULT_EXT_TO_PREFIX.items())

        if not pretty:
            namespace_def = namespace_def.replace('\n\t', ' ')

        self.to_obj().export(s, 0, all_ns_dict, pretty_print=pretty, namespacedef_=namespace_def)
        return s.getvalue()

    def to_json(self):
        return json.dumps(self.to_dict())

    def from_json(self, json_doc):
        try:
            d = json.load(json_doc)
        except AttributeError: # catch the read() error
            d = json.loads(json_doc)
            
        return self.from_dict(d)

    def to_dict(self):
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

