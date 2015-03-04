# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# builtin
import json
import collections
import itertools
import StringIO

# external
import lxml.etree

# internal
from . import bindings, utils


def _override(*args, **kwargs):
    raise NotImplementedError()


class Entity(object):
    """Base class for all classes in the STIX API."""
    _namespace = None
    _XSI_TYPE = None


    def _collect_ns_info(self, ns_info=None):
        if not ns_info:
            return
        ns_info.collect(self)


    def to_obj(self, return_obj=None, ns_info=None):
        """Converts an `Entity` into a binding object.

        Note:
            This needs to be overridden by derived classes.

        """
        self._collect_ns_info(ns_info)
        return return_obj


    @classmethod
    def from_obj(cls, obj, return_obj=None):
        """Create an object from a binding object"""
        raise NotImplementedError()


    def to_xml(self, include_namespaces=True, include_schemalocs=True,
               ns_dict=None, schemaloc_dict=None, pretty=True,
               auto_namespace=True, encoding='utf-8'):
        """Serializes a :class:`Entity` instance to an XML string.

        The default character encoding is ``utf-8`` and can be set via the
        `encoding` parameter. If `encoding` is ``None``, a unicode string
        is returned.

        Args:
            auto_namespace: Automatically discover and export XML namespaces
                for a STIX :class:`Entity` instance.
            include_namespaces: Export namespace definitions in the output
                XML. Default is ``True``.
            include_schemalocs: Export ``xsi:schemaLocation`` attribute
                in the output document. This will attempt to associate
                namespaces declared in the STIX document with schema locations.
                If a namespace cannot be resolved to a schemaLocation, a
                Python warning will be raised. Schemalocations will only be
                exported if `include_namespaces` is also ``True``.
            ns_dict: Dictionary of XML definitions (namespace is key, alias is
                value) to include in the exported document. This must be
                passed in if `auto_namespace` is ``False``.
            schemaloc_dict: Dictionary of XML ``namespace: schema location``
                mappings to include in the exported document. These will
                only be included if `auto_namespace` is ``False``.
            pretty: Pretty-print the XML.
            encoding: The output character encoding. Default is ``utf-8``. If
                `encoding` is set to ``None``, a unicode string is returned.

        Returns:
            An XML string for this
            :class:`Entity` instance. Default character encoding is ``utf-8``.

        """

        nsparser = utils.nsparser
        parser = nsparser.NamespaceParser()

        if auto_namespace:
            ns_info = nsparser.NamespaceInfo()
        else:
            ns_info = None

        obj = self.to_obj(ns_info=ns_info)

        if (not auto_namespace) and (not ns_dict):
            raise Exception(
                "Auto-namespacing was disabled but ns_dict was empty "
                "or missing."
            )

        if auto_namespace:
            ns_info.finalize(ns_dict=ns_dict, schemaloc_dict=schemaloc_dict)
            obj_ns_dict = ns_info.finalized_namespaces
        else:
            ns_info = nsparser.NamespaceInfo()
            ns_info.finalized_namespaces = ns_dict or {}
            ns_info.finalized_schemalocs = schemaloc_dict or {}
            obj_ns_dict = dict(
                itertools.chain(
                    ns_dict.iteritems(),
                    nsparser.DEFAULT_STIX_NAMESPACES.iteritems()
                )
            )

        namespace_def = ""
        if include_namespaces:
            xmlns = parser.get_xmlns_str(ns_info.finalized_namespaces)
            namespace_def += ("\n\t" + xmlns)

        if include_schemalocs and include_namespaces:
            schemaloc = parser.get_schemaloc_str(ns_info.finalized_schemalocs)
            namespace_def += ("\n\t" + schemaloc)

        if not pretty:
            namespace_def = namespace_def.replace('\n\t', ' ')

        with bindings.save_encoding(encoding):
            sio = StringIO.StringIO()
            obj.export(
                sio.write,                    # output buffer
                0,                            # output level
                obj_ns_dict,                  # namespace dictionary
                pretty_print=pretty,          # pretty printing
                namespacedef_=namespace_def   # namespace/schemaloc def string
            )

        # Ensure that the StringIO buffer is unicode
        s = unicode(sio.getvalue())

        if encoding:
            return s.encode(encoding)

        return s

    def to_json(self):
        return json.dumps(self.to_dict())


    @classmethod
    def from_json(cls, json_doc):
        """Parses the JSON document `json_doc` and returns a STIX
        :class:`Entity` implementation instance.

        Arguments:
            json_doc: Input JSON representation of a STIX entity. This can be
                a readable object or a JSON string.

        Returns:
            An implementation of :class:`.Entity` (e.g., :class:`.STIXPackage`).

        """
        try:
            d = json.load(json_doc)
        except AttributeError: # catch the read() error
            d = json.loads(json_doc)

        return cls.from_dict(d)

    def to_dict(self, skip=()):
        """Converts a STIX :class:`Entity` implementation into a Python
        dictionary. This may be overridden by derived classes.

        """
        def dict_iter(items):
            return [x.to_dict() if utils.is_dictable(x) else x for x in items]

        d = {}

        for name, field in utils.iter_vars(self):
            key = utils.key_name(name)

            if key in skip:
                continue

            if utils.is_dictable(field):
                d[key] = field.to_dict()
            elif utils.is_timestamp(field):
                d[key] = utils.dates.serialize_value(field)
            elif utils.is_etree(field):
                d[key] = lxml.etree.tostring(field)
            elif utils.is_sequence(field):
                d[key] = dict_iter(field)
            else:
                d[key] = field

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
        return utils.walk.iterwalk(self)

    def find(self, id_):
        """Searches the children of a :class:`Entity` implementation for an
        object with an ``id_`` property that matches `id_`.

        """
        if not id_:
            return

        for entity in self.walk():
            if id_ == getattr(entity, "id_", None):
                return entity


class EntityList(collections.MutableSequence, Entity):
    _binding_class = _override
    _binding_var = None
    _contained_type = _override
    _inner_name = None
    _dict_as_list = False

    def __init__(self, *args):
        super(EntityList, self).__init__()
        self._inner = []

        if not any(args):
            return

        for arg in args:
            if utils.is_sequence(arg):
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
            error = "Can't put '{0}' ({1}) into a {2}. Expected {3} instance."
            error = error.format(value, type(value), type(self), type(self._contained_type))
            raise ValueError(error)

        return new_value

    # The next four functions can be overridden, but otherwise define the
    # default behavior for EntityList subclasses which define the following
    # class-level members:
    # - _binding_class
    # - _binding_var
    # - _contained_type
    # - _inner_name

    def to_obj(self, return_obj=None, ns_info=None):
        super(EntityList, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        setattr(return_obj, self._binding_var, [x.to_obj(ns_info=ns_info) for x in self])

        return return_obj

    def to_list(self):
        return [h.to_dict() for h in self]

    def to_dict(self):
        if self._dict_as_list:
            return self.to_list()

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
    def from_list(cls, list_repr, return_obj=None, contained_type=None):

        if not utils.is_sequence(list_repr):
            return None

        if return_obj is None:
            return_obj = cls()
        if not contained_type:
            contained_type = cls._contained_type

        return_obj.extend(contained_type.from_dict(x) for x in list_repr)
        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None, contained_type=None,
                  inner_name=None):

        if cls._dict_as_list:
            return cls.from_list(
                dict_repr,
                return_obj=return_obj,
                contained_type=contained_type,
            )


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


class TypedList(collections.MutableSequence):
    _contained_type = _override

    def __init__(self, *args):
        self._inner = []

        # Check if it was initialized with args=None
        if not any(args):
            return

        for arg in args:
            if utils.is_sequence(arg):
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
            error = "Can't put '{0}' ({1}) into a {2}. Expected {3} instance."
            error = error.format(value, type(value), type(self), type(self._contained_type))
            raise ValueError(error)

        return new_value

    def to_obj(self, ns_info=None):
        return [x.to_obj(ns_info=ns_info) for x in self]

    def to_list(self):
        return [h.to_dict() for h in self]

    to_dict = to_list

    @classmethod
    def from_obj(cls, obj_list, contained_type=None):

        if not obj_list:
            return None

        return_obj = cls()

        if not contained_type:
            contained_type = cls._contained_type

        if not utils.is_sequence(obj_list):
            obj_list = [obj_list]

        return_obj.extend(contained_type.from_obj(x) for x in obj_list)
        return return_obj

    @classmethod
    def from_list(cls, list_repr, contained_type=None):


        if not utils.is_sequence(list_repr):
            return None

        return_obj = cls()

        if not contained_type:
            contained_type = cls._contained_type

        return_obj.extend(contained_type.from_dict(x) for x in list_repr)
        return return_obj

    from_dict = from_list