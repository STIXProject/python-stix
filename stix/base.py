# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# stdlib
import json
import collections
import itertools
from sys import version_info

# mixbox
from mixbox import idgen
from mixbox import entities
from mixbox import fields
from mixbox import binding_utils
from mixbox import namespaces
from mixbox.vendor.six import StringIO, iteritems, itervalues, text_type, binary_type

# internal
from . import utils

def _override(*args, **kwargs):
    raise NotImplementedError()


class Entity(entities.Entity):
    """Base class for all classes in the STIX API."""
    _namespace = None
    _XSI_TYPE = None

    def _set_var(self, klass, try_cast=True, arg=None, **kwargs):
        """Sets an instance property value.

        * If the input value is ``None``, the property is set to ``None``.
        * If the input value is an instance of `klass`, the property is set
          the input value.
        * If the input value is not an instance of `klass` and `try_cast` is
          ``True``, an attempt will be made to cast the input value to an
          instance of `klass`.

        Args:
            klass: The expected input value class.
            try_cast: If ``True`` attempt to cast the input value to `klass`
                if it is not an instance of `klass`.
            arg: The __init__ parameter name to use when casting the input
                value to `klass`. E.g., StructuredText(value=input), the `arg`
                is `value`. If ``None``, it is assumed that the first
                __init__ parameter will accept the value.
            **kwargs: The field name and value. The field name is the key
                and the field value is the value.

        """
        name, item = next(iteritems(kwargs))
        attr = utils.private_name(name)  # 'title' => '_title'

        if item is None:
            setattr(self, attr, None)
        elif isinstance(item, klass):
            setattr(self, attr, item)
        elif try_cast:
            promoted = utils.cast_var(item, klass, arg=arg)
            setattr(self, attr, promoted)
        else:
            error = "'{0}' expects an instance of {1}. Received: {2}."
            error = error.format(name, klass, type(item))
            raise TypeError(error)

    def _set_vocab(self, klass=None, **kwargs):
        """Sets a controlled vocabulary property value.

        * If the input value is ``None``, the property is set to ``None``.
        * If the input value is an instance of ``VocabString``, the property
          is set to the input value.
        * If the input value is not an instance of ``VocabString``, an attempt
          will be made to cast the input to an instance of `klass`. If `klass`
          is ``None``, ``VocabString`` will be used.

        Args:
            klass: The VocabString impl to cast the input value to. If ``None``
                ``VocabString`` will be assumed.
            **kwargs: The field name, value pair. The field name is the key
                and the field value is the value.

        """
        from stix.common import VocabString

        klass = klass or VocabString
        item  = next(itervalues(kwargs))

        if isinstance(item, VocabString):
            self._set_var(VocabString, **kwargs)
        else:
            self._set_var(klass, **kwargs)

    def to_xml(self, include_namespaces=True, include_schemalocs=False,
               ns_dict=None, schemaloc_dict=None, pretty=True,
               auto_namespace=True, encoding='utf-8'):
        """Serializes a :class:`Entity` instance to an XML string.

        The default character encoding is ``utf-8`` and can be set via the
        `encoding` parameter. If `encoding` is ``None``, a string (unicode in
        Python 2, str in Python 3) is returned.

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
                `encoding` is set to ``None``, a string (unicode in Python 2,
                str in Python 3) is returned.

        Returns:
            An XML string for this
            :class:`Entity` instance. Default character encoding is ``utf-8``.

        """

        from mixbox.entities import NamespaceCollector

        if (not auto_namespace) and (not ns_dict):
            raise Exception(
                "Auto-namespacing was disabled but ns_dict was empty "
                "or missing."
            )

        ns_info = NamespaceCollector()

        obj = self.to_obj(ns_info=ns_info if auto_namespace else None)

        ns_info.finalize(ns_dict=ns_dict, schemaloc_dict=schemaloc_dict)

        if auto_namespace:
            obj_ns_dict = ns_info.binding_namespaces
        else:
            obj_ns_dict = dict(
                itertools.chain(
                    iteritems(ns_info.binding_namespaces),
                    iteritems(namespaces.get_full_ns_map())
                )
            )

        namespace_def = ""
        if include_namespaces:
            delim = "\n\t" if pretty else " "
            xmlns = ns_info.get_xmlns_string(delim)
            namespace_def += (delim + xmlns)
            if include_schemalocs:
                schemaloc = ns_info.get_schema_location_string(delim)
                namespace_def += (delim + schemaloc)

        with binding_utils.save_encoding(encoding):
            sio = StringIO()
            obj.export(
                sio.write,                    # output buffer
                0,                            # output level
                obj_ns_dict,                  # namespace dictionary
                pretty_print=pretty,          # pretty printing
                namespacedef_=namespace_def   # namespace/schemaloc def string
            )

        # Ensure that the StringIO buffer is unicode
        s = text_type(sio.getvalue())

        if encoding:
            return s.encode(encoding)

        return s

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


class EntityList(entities.EntityList, Entity):
    def to_xml(self, *args, **kwargs):
        return Entity.to_xml(self, *args, **kwargs)


class TypedCollection(object):
    """Abstract base class for non-STIX collections of entities.

    See also:
        TypedList

    """
    _contained_type = _override

    def __init__(self, *args):
        self._inner = []
        self._initialize_inner(*args)

    def _initialize_inner(self, *args):
        """Must be overridden by subclass.

        """
        raise NotImplementedError()

    def __len__(self):
        return len(self._inner)

    def __nonzero__(self):
        return bool(self._inner)

    def _is_valid(self, value):
        """Check if this is a valid object to add to the list."""
        # Subclasses can override this function, but if it becomes common,
        # it's probably better to use self._contained_type.istypeof(value)
        return isinstance(value, self._contained_type)

    def _fix_value(self, value):
        """Attempt to coerce value into the correct type.

        Subclasses can override this function.
        """
        try:
            new_value = self._contained_type(value)
        except Exception:
            error = "Can't put '{0}' ({1}) into a {2}. Expected a {3} object."
            error = error.format(
                value,                  # Input value
                type(value),            # Type of input value
                type(self),             # Type of collection
                self._contained_type    # Expected type of input value
            )
            raise ValueError(error)

        return new_value

    def to_obj(self, ns_info=None):
        #print "TypedCollection to_obj called"
        return [x.to_obj(ns_info=ns_info) for x in self]

    def to_list(self):
        return [h.to_dict() for h in self]

    @classmethod
    def from_obj(cls, obj_list, contained_type=None):
        if obj_list is None:
            return None

        if not contained_type:
            contained_type = cls._contained_type

        if not utils.is_sequence(obj_list):
            obj_list = [obj_list]

        items = (contained_type.from_obj(x) for x in obj_list)
        return cls(items)

    @classmethod
    def from_list(cls, list_repr, contained_type=None):

        if not list_repr:
            return cls()

        if isinstance(list_repr, dict) or not utils.is_sequence(list_repr):
            list_repr = [list_repr]

        if not contained_type:
            contained_type = cls._contained_type

        items = (contained_type.from_dict(x) for x in list_repr)
        return cls(items)

    from_dict = from_list
    to_dict = to_list

    @classmethod
    def object_from_dict(cls, entity_dict):
        """Convert from dict representation to object representation."""
        return cls.from_dict(entity_dict).to_obj()

    @classmethod
    def dict_from_object(cls, entity_obj):
        """Convert from object representation to dict representation."""
        return cls.from_obj(entity_obj).to_dict()
    
    @classmethod
    def istypeof(cls, obj):
        """Check if `cls` is the type of `obj`

        In the normal case, as implemented here, a simple isinstance check is
        used. However, there are more complex checks possible. For instance,
        EmailAddress.istypeof(obj) checks if obj is an Address object with
        a category of Address.CAT_EMAIL
        """
        return isinstance(obj, cls)


class TypedList(TypedCollection, collections.MutableSequence):
    def __init__(self, *args):
        TypedCollection.__init__(self, *args)

    def _initialize_inner(self, *args):
        # Check if it was initialized with args=None
        if not any(args):
            return

        for arg in args:
            if utils.is_sequence(arg):
                self.extend(arg)
            else:
                self.append(arg)

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


def _validate_version(instance, value):
    if value:
        utils.check_version(instance._ALL_VERSIONS, value)


class BaseCoreComponent(Entity):
    _ALL_VERSIONS = ()
    _ID_PREFIX = None

    title = fields.TypedField("Title")
    id_ = fields.IdField("id")
    idref = fields.IdrefField("idref")
    descriptions = fields.TypedField("Description", type_="stix.common.StructuredTextList", )
    short_descriptions = fields.TypedField("Short_Description", type_="stix.common.StructuredTextList")
    version = fields.TypedField("version", preset_hook=_validate_version)
    timestamp = fields.DateTimeField("timestamp")
    handling = fields.TypedField("Handling", type_="stix.data_marking.Marking")


    def __init__(self, id_=None, idref=None, timestamp=None, title=None,
                 description=None, short_description=None):
        from stix.common import StructuredTextList

        super(BaseCoreComponent, self).__init__()

        self.id_ = id_ or idgen.create_id(self._ID_PREFIX)
        self.idref = idref
        self.title = title
        self.descriptions = StructuredTextList(description)
        self.short_descriptions = StructuredTextList(short_description)

        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = utils.dates.now() if not idref else None

    @property
    def description(self):
        """A single description about the contents or purpose of this object.

        Default Value: ``None``

        Note:
            If this object has more than one description set, this will return
            the description with the lowest ordinality value.

        Returns:
            An instance of :class:`.StructuredText`
        """
        return next(iter(self.descriptions), None)

    @description.setter
    def description(self, value):
        self.descriptions = value

    def add_description(self, description):
        """Adds a description to the ``descriptions`` collection.

        This is the same as calling "foo.descriptions.add(bar)".
        """
        self.descriptions.add(description)

    @property
    def short_description(self):
        """A single short description about the contents or purpose of this
        object.

        Default Value: ``None``

        Note:
            If this object has more than one short description set, this will
            return the description with the lowest ordinality value.

        Returns:
            An instance of :class:`.StructuredText`
        """
        return next(iter(self.short_descriptions), None)

    @short_description.setter
    def short_description(self, value):
        self.short_descriptions = value

    def add_short_description(self, description):
        """Adds a description to the ``short_descriptions`` collection.

        This is the same as calling "foo.short_descriptions.add(bar)".
        """
        self.short_descriptions.add(description)
