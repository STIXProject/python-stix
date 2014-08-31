# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import warnings
import collections
import inspect
import json
from StringIO import StringIO
from lxml import etree

class NamespaceInfo(object):
    def __init__(self):
        self.namespaces = {}
        self.input_namespaces = {}
        self.input_schemalocs = {}

    def update(self, ns_info):
        self.namespaces.update(ns_info.namespaces)
        self.input_namespaces.update(ns_info.input_namespaces)
        self.input_schemalocs.update(ns_info.input_schemalocs)

    def finalize(self, ns_dict=None, schemaloc_dict=None):
        from stix.utils import (get_id_namespace, get_id_namespace_alias,
                                DEFAULT_STIX_NAMESPACES, XML_NAMESPACES,
                                DEFAULT_STIX_SCHEMALOCATIONS)

        if not ns_dict:
            ns_dict = {}

        if not schemaloc_dict:
            schemaloc_dict = {}

        id_ns = get_id_namespace()
        id_ns_alias = get_id_namespace_alias()

        d_ns = {'http://www.w3.org/2001/XMLSchema-instance': 'xsi',
                'http://stix.mitre.org/stix-1': 'stix',
                'http://stix.mitre.org/common-1': 'stixCommon',
                'http://stix.mitre.org/default_vocabularies-1': 'stixVocabs',
                'http://cybox.mitre.org/cybox-2': 'cybox',
                'http://cybox.mitre.org/common-2': 'cyboxCommon',
                'http://cybox.mitre.org/default_vocabularies-2': 'cyboxVocabs',
                id_ns: id_ns_alias}

        for ns, alias in self.input_namespaces.iteritems():
            if ns not in DEFAULT_STIX_NAMESPACES:
                d_ns[ns] = alias

        for ns, alias in self.namespaces.iteritems():
            if alias:
                d_ns[ns] = alias
            else:
                default_alias = DEFAULT_STIX_NAMESPACES[ns]
                d_ns[ns] = default_alias

        d_ns.update(ns_dict)

        if all((d_ns.get('http://example.com/'),
               d_ns.get('http://example.com'))):
            del d_ns['http://example.com/']

        aliases = []
        for ns, alias in d_ns.iteritems():
            if alias not in aliases:
                aliases.append(alias)
            else:
                # TODO: Should we just throw an exception here?
                # The XML will be invalid if there is a duplicate ns alias
                warnings.warn("namespace alias '%s' mapped to '%s' and '%s'" %
                              (alias, ns, aliases[alias]))

        d_sl = dict(self.input_schemalocs.items())

        # Iterate over input/discovered namespaces for document and attempt
        # to map them to schemalocations. Warn if unable to map ns to schemaloc.
        for ns, _ in d_ns.iteritems():
            if ns in DEFAULT_STIX_SCHEMALOCATIONS:
                schemalocation = DEFAULT_STIX_SCHEMALOCATIONS[ns]
                d_sl[ns] = schemalocation
            else:
                if not ((ns == id_ns) or
                        (ns in schemaloc_dict) or
                        (ns in self.input_schemalocs) or
                        (ns in XML_NAMESPACES)):
                    warnings.warn("Unable to map namespace '%s' to "
                                  "schemaLocation" % ns)

        d_sl.update(schemaloc_dict)

        self.finalized_schemalocs = d_sl
        self.finalized_namespaces = d_ns


    def collect(self, entity):
        try:
            ns_alias, type_ = entity._XSI_TYPE.split(":")
            self.namespaces[entity._namespace] = ns_alias
        except:
            self.namespaces[entity._namespace] = None

        try:
            self.input_namespaces.update(entity.__input_namespaces__)
        except AttributeError:
            pass

        try:
            self.input_schemalocs.update(entity.__input_schemalocations__)
        except AttributeError:
            pass

    def __setitem__(self, key, value):
        self.namespaces[key] = value


class Entity(object):
    """Base class for all classes in the STIX API."""
    _namespace = None
    _XSI_TYPE = None


    def to_obj(self, return_obj=None, ns_info=None):
        obj = self._to_obj(return_obj, ns_info)

        if ns_info:
            ns_info.collect(self)

        return obj


    def _to_obj(self, return_obj=None, ns_info=None):
        """Export an object as a binding object representation"""
        raise NotImplementedError()


    @classmethod
    def from_obj(cls, obj):
        """Create an object from a binding object"""
        raise NotImplementedError()


    def to_xml(self, include_namespaces=True, include_schemalocs=True,
               ns_dict=None, schemaloc_dict=None, pretty=True,
               auto_namespace=True):
        """Export an object as an XML String"""
        from stix.utils.nsparser import  NamespaceParser, DEFAULT_STIX_NAMESPACES
        parser = NamespaceParser()

        if auto_namespace:
            ns_info = NamespaceInfo()
        else:
            ns_info = None

        obj = self.to_obj(ns_info=ns_info)

        if (not auto_namespace) and (not ns_dict):
            raise Exception("Auto-namespacing was disabled but ns_dict "
                            "was empty or missing.")

        if auto_namespace:
            ns_info.finalize()
            obj_ns_dict = ns_info.finalized_namespaces
        else:
            ns_info = NamespaceInfo()
            ns_info.finalized_namespaces = ns_dict or {}
            ns_info.finalized_schemalocs = schemaloc_dict or {}
            obj_ns_dict = dict(ns_dict.items() + DEFAULT_STIX_NAMESPACES.items())

        namespace_def = ""
        if include_namespaces:
            namespace_def += ("\n\t" +
                              parser.get_xmlns_str(ns_info.finalized_namespaces))

        if include_schemalocs and include_namespaces:
            namespace_def += ("\n\t" +
                              parser.get_schemaloc_str(ns_info.finalized_schemalocs))

        if not pretty:
            namespace_def = namespace_def.replace('\n\t', ' ')

        s = StringIO()
        obj.export(s.write, 0, obj_ns_dict, pretty_print=pretty,
                             namespacedef_=namespace_def)
        return s.getvalue()

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_doc):
        try:
            d = json.load(json_doc)
        except AttributeError: # catch the read() error
            d = json.loads(json_doc)

        return cls.from_dict(d)

    def to_dict(self):
        d = {}
        for raw_key in self.__dict__.keys():
            raw_value = self.__dict__[raw_key]
            
            if raw_value:
                if isinstance(raw_value, Entity):
                    value = raw_value.to_dict()
                elif isinstance(raw_value, collections.MutableSequence):
                    value = []
                    for x in raw_value:
                        if isinstance(x, Entity):
                            value.append(x.to_dict())
                        else:
                            value.append(x)
                elif isinstance(raw_value, etree._ElementTree):
                    value = etree.tostring(raw_value)
                else:
                    value = raw_value
                
                if raw_key.startswith("_"):
                    key = raw_key[1:]
                elif raw_key.endswith("_"):
                    key = raw_key[:-1]
                else:
                    key = raw_key
            
                d[key] = value
        return d

    @classmethod
    def from_dict(cls, d, return_obj=None):
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

    def walk(self):
        from cybox import Entity as cyboxEntity
        from cybox.common import ObjectProperties

        yieldable = (Entity, cyboxEntity)
        skip = {ObjectProperties : '_parent'}

        def can_skip(obj, field):
            for klass, prop in skip.iteritems():
                if prop == field and isinstance(obj, klass):
                    return True
            return False

        def get_members(obj):
            for k, v in obj.__dict__.iteritems():
                if v and not can_skip(obj, k):
                    yield v

        visited = []
        def descend(obj):
            if id(obj) in visited:
                return
            visited.append(id(obj))

            for member in get_members(obj):
                if isinstance(member, yieldable):
                    yield member
                    for i in descend(member):
                        yield i

                if hasattr(member, "__getitem__"):
                    for i in member:
                        if isinstance(i, yieldable):
                            yield i
                            for d in descend(i):
                                yield d

            visited.remove(id(obj))
        # end descend()

        for node in descend(self):
            yield node

    def find(self, id_):
        for entity in self.walk():
            try:
                if entity.id_ == id_:
                    return entity
            except:
                pass

class EntityList(collections.MutableSequence, Entity):
    def __init__(self, *args):
        super(EntityList, self).__init__()
        self._inner = []

        for arg in args:
            if isinstance(arg, list):
                self.extend(arg)
            else:
                self.append(arg)

    def __nonzero__(self):
        return bool(self._inner)

    def __getitem__(self, key):
        return self._inner.__getitem__(key)

    def __setitem__(self, key, value):
        if not self._is_valid(value):
            value = self._fix_value(value)
        self._inner.__setitem__(key, value)

    def __delitem__(self, key):
        self._inner.__delitem__(key)

    def __len__(self):
        return len(self._inner)

    def insert(self, idx, value):
        if not value:
            return
        if not self._is_valid(value):
            value = self._fix_value(value)
        self._inner.insert(idx, value)

    def _is_valid(self, value):
        """Check if this is a valid object to add to the list."""
        # Subclasses can override this function, but if it becomes common, it's
        # probably better to use self._contained_type.istypeof(value)
        return isinstance(value, self._contained_type)

    def _fix_value(self, value):
        """Attempt to coerce value into the correct type.

        Subclasses can override this function.
        """
        try:
            new_value = self._contained_type(value)
        except:
            raise ValueError("Can't put '%s' (%s) into a %s" %
                (value, type(value), self.__class__))
        return new_value

    # The next four functions can be overridden, but otherwise define the
    # default behavior for EntityList subclasses which define the following
    # class-level members:
    # - _binding_class
    # - _binding_var
    # - _contained_type
    # - _inner_name

    def _to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            return_obj = self._binding_class()

        setattr(return_obj, self._binding_var, [x.to_obj(ns_info=ns_info) for x in self])

        return return_obj

    def to_dict(self):
        d = {}

        if self._inner:
            d[self._inner_name] = [h.to_dict() for h in self]

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None, contained_type=None,
                 binding_var=None):
        if not obj:
            return None

        if return_obj is None:
            return_obj = cls()
        if not contained_type:
            contained_type = cls._contained_type
        if not binding_var:
            binding_var = cls._binding_var

        for item in getattr(obj, binding_var):
            return_obj.append(contained_type.from_obj(item))

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None, contained_type=None,
                  inner_name=None):
        if not isinstance(dict_repr, dict):
            return None

        if return_obj is None:
            return_obj = cls()
        if not contained_type:
            contained_type = cls._contained_type
        if not inner_name:
            inner_name = cls._inner_name

        for item in dict_repr.get(inner_name, []):
            return_obj.append(contained_type.from_dict(item))

        return return_obj
    

