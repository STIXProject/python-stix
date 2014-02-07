# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

__version__ = "1.0.1.0"

import json
from StringIO import StringIO


class Entity(object):
    """Base class for all classes in the STIX API."""
    def to_obj(self, return_obj=None):
        """Export an object as a binding object representation"""
        pass

    def from_obj(self, obj):
        """Create an object from a binding object"""
        pass

    def to_xml(self, ns_dict=None):
        """Export an object as an XML String"""
        if not ns_dict: ns_dict = {}
        
        s = StringIO()
        
        # do this here so we don't cause problems with distutils setup.py
        import cybox.utils.nsparser as cybox_nsparser
        import stix.utils.nsparser as nsparser
        import stix.utils.idgen as idgen
        import stix.bindings.stix_core as core_binding
        
        xml_ns_dict = {'http://www.w3.org/1999/xlink': 'xlink',
                       'http://www.w3.org/2000/09/xmldsig#': 'ds',
                       'http://www.w3.org/2001/XMLSchema': 'xs',
                       'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
                       idgen.get_id_namespace() : idgen.get_id_namespace_alias()}
        
        all_ns_dict = dict(xml_ns_dict)
        
        ns_set = nsparser.NamespaceParser().get_namespaces(self)
        for ns in ns_set:
            if ns in ns_dict:
                all_ns_dict[ns] = ns_dict[ns]
            elif ns.startswith("http://cybox.mitre.org"):
                for cybox_ns_tup in cybox_nsparser.NS_LIST:
                    if ns == cybox_ns_tup[0]:
                        all_ns_dict[ns] = cybox_ns_tup[1]
            else:
                all_ns_dict[ns] = nsparser.DEFAULT_STIX_NS_TO_PREFIX[ns]
        
        self.to_obj().export(s, 0, all_ns_dict)
        return s.getvalue()

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_dict(dict_repr, return_obj=None):
        """Convert from dict representation to object representation."""
        return return_obj
