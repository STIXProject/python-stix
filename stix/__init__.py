# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

__version__ = "1.0.1.0"

import json
from StringIO import StringIO
from stix.utils import NamespaceParser

class Entity(object):
    """Base class for all classes in the STIX API."""
    def to_obj(self, return_obj=None):
        """Export an object as a binding object representation"""
        pass

    def from_obj(self, obj):
        """Create an object from a binding object"""
        pass

    def to_xml(self):
        """Export an object as an XML String"""
        s = StringIO()
        # For now, just export all the namespaces
        import stix.bindings.stix_core as core_binding
        self.to_obj().export(s, 0,  core_binding.DEFAULT_XML_NS_MAP)
        return s.getvalue()

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_dict(dict_repr, return_obj=None):
        """Convert from dict representation to object representation."""
        return return_obj
