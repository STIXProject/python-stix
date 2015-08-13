# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

# builtin
import json
import collections
import itertools
import StringIO
from mixbox import fields, entities

# internal
from . import bindings, utils

def _override(*args, **kwargs):
    raise NotImplementedError()


class AttributeField(fields.TypedField):
    pass

class ElementField(fields.TypedField):
    pass

class IdField(AttributeField):
    pass

class Entity(object):
    """Base class for all classes in the STIX API."""
    _namespace = None
    _XSI_TYPE = None

    def __init__(self):
        self._fields = {}

    def _collect_ns_info(self, ns_info=None):
        if not ns_info:
            return
        ns_info.collect(self)

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
        name, item = kwargs.iteritems().next()
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

    @classmethod
    def _get_vars(cls):
        import inspect
        var_list = []
        for (name, obj) in inspect.getmembers(cls, inspect.isdatadescriptor):
            #print name + " " + str(type(obj)) + " " + str(obj.__class__)
            if isinstance(obj, fields.TypedField):
                var_list.append(obj)

        return var_list

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
        item  = kwargs.itervalues().next()

        if isinstance(item, VocabString):
            self._set_var(VocabString, **kwargs)
        else:
            self._set_var(klass, **kwargs)

    @classmethod
    def istypeof(cls, obj):
        """Check if `cls` is the type of `obj`

        In the normal case, as implemented here, a simple isinstance check is
        used. However, there are more complex checks possible. For instance,
        EmailAddress.istypeof(obj) checks if obj is an Address object with
        a category of Address.CAT_EMAIL
        """
        return isinstance(obj, cls)

    def to_obj(self, return_obj=None, ns_info=None):
        """Convert to a GenerateDS binding object.

        Subclasses can override this function.

        Returns:
            An instance of this Entity's ``_binding_class`` with properties
            set from this Entity.
        """
        
        def _objectify(value, return_obj, ns_info):
            """Make `value` suitable for a binding object.
        
            If `value` is an Entity, call to_obj() on it. Otherwise, return it
            unmodified.
            """
            try:
                #print "objifying", value.to_obj
                return value.to_obj(return_obj=return_obj, ns_info=ns_info)
            except AttributeError:
                if type(value) == dict:
                    print "dict doesn't have to_obj", return_obj, value
                return value
        
        self._collect_ns_info(ns_info)

        entity_obj = self._binding_class()
        #print "entity", entity_obj, self

        vars = {}
        for klass in self.__class__.__mro__:
            if klass is Entity:
                break
            vars.update(klass.__dict__.iteritems())
            
        #print "vars", vars
        #print "self", self.__dict__

        for name, field in vars.iteritems():
            if isinstance(field, fields.TypedField):
                #print name, field.__class__, field.attr_name
                val = getattr(self, field.attr_name)

                if field.multiple:
                    if val:
                        val = [_objectify(x, return_obj, ns_info) for x in val]
                    else:
                        val = []
                else:
                    #print "objectifying", val
                    val = _objectify(val, return_obj, ns_info)
                    #print "objectified", val

                #print "setting on binding", field.name, val
                setattr(entity_obj, field.name, val)

        self._finalize_obj(entity_obj)
        return entity_obj

    def _finalize_obj(self, entity_obj):
        """Subclasses can define additional items in the binding object.

        `entity_obj` should be modified in place.
        """
        pass

    @classmethod
    def from_obj(cls, cls_obj=None, return_obj=None):
        """Create an object from a binding object"""
        if not cls_obj:
            return None

        if return_obj is None:
            entity = cls()
        else:
            entity = return_obj

        for field in cls._get_vars():
            val = getattr(cls_obj, field.name)
            if field.type_:
                if field.multiple and val is not None:
                    val = [field.type_.from_obj(x) for x in val]
                else:
                    val = field.type_.from_obj(val)
            setattr(entity, field.attr_name, val)

        return entity

    def to_xml(self, include_namespaces=True, include_schemalocs=False,
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

        from .utils import nsparser
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
            obj_ns_dict = ns_info.binding_namespaces
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
            An implementation of :class:`.Entity` (e.g.,
            :class:`.STIXPackage`).

        """
        try:
            d = json.load(json_doc)
        except AttributeError:  # catch the read() error
            d = json.loads(json_doc)

        return cls.from_dict(d)

    def to_dict(self):
        """Converts a STIX :class:`Entity` implementation into a Python
        dictionary. This may be overridden by derived classes.

        Returns:
            Python dict with keys set from this Entity.
        """
        def _dictify(value):
            """Make `value` suitable for a dictionary.
        
            If `value` is an Entity, call to_dict() on it. Otherwise, return it
            unmodified.
            """
            try:
                return value.to_dict()
            except:
                return value
        
        entity_dict = { }
        vars = { }
        for klass in self.__class__.__mro__:
            if klass is Entity:
                break
            vars.update(klass.__dict__.iteritems())

        hasAnyTypedField = False
        for name, field in vars.iteritems():
            if isinstance(field, fields.TypedField):
                hasAnyTypedField = True
                
                val = getattr(self, field.attr_name)

                if field.multiple:
                    if val:
                        val = [_dictify(x) for x in val]
                    else:
                        val = []
                else:
                    val = _dictify(val)

                # Only add non-None objects or non-empty lists
                if val is not None and val != []:
                    entity_dict[field.key_name] = val

        # doesn't quite work, possibly because of inherited TypedFields?
        #if not hasAnyTypedField:
        #    return utils.to_dict(self)

        self._finalize_dict(entity_dict)

        return entity_dict
    
    def _finalize_dict(self, entity_dict):
        """Subclasses can define additional items in the dictionary.

        `entity_dict` should be modified in place.
        """
        pass

    @classmethod
    def from_dict(cls, cls_dict=None, return_obj=None):
        """Convert from dict representation to object representation."""
        if cls_dict is None:
            return None

        if return_obj is None:
            entity = cls()
        else:
            entity = return_obj

        # Shortcut if an actual dict is not provided:
        if not isinstance(cls_dict, dict):
            value = cls_dict
            # Call the class's constructor
            try:
                return cls(value)
            except TypeError:
                raise TypeError("Could not instantiate a %s from a %s: %s" %
                                (cls, type(value), value))

        for field in cls._get_vars():
            val = cls_dict.get(field.key_name)
            if field.type_:
                if issubclass(field.type_, EntityList):
                    val = field.type_.from_list(val)
                elif field.multiple:
                    if val is not None:
                        val = [field.type_.from_dict(x) for x in val]
                    else:
                        val = []
                else:
                    val = field.type_.from_dict(val)
            else:
                if field.multiple and not val:
                    val = []
            setattr(entity, field.attr_name, val)

        return entity
            
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
            error = "Can't put '{0}' ({1}) into a {2}. Expected a {3} object."
            error = error.format(
                value,                  # Input value
                type(value),            # Type of input value
                type(self),             # Type of collection
                self._contained_type    # Expected type of input value
            )
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

        objlist = [x.to_obj(ns_info=ns_info) for x in self]
        setattr(return_obj, self._binding_var, objlist)

        return return_obj

    def to_list(self):
        return [h.to_dict() for h in self]

    def to_dict(self):
        if self._dict_as_list:
            return self.to_list()

        d = utils.to_dict(self, skip=('inner',))

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
        from stix.common.related import GenericRelationshipList

        if not utils.is_sequence(list_repr):
            return None

        if return_obj is None:
            return_obj = cls()
        if not contained_type:
            contained_type = cls._contained_type

        #print list_repr.__class__, isinstance(list_repr, GenericRelationshipList)

        # GenericRelationshipList is not actually a list; it's dict with a list member
        if issubclass(cls, GenericRelationshipList):
            return cls.from_dict(list_repr, return_obj)

        try:
            list_repr = list_repr[getattr(cls, '_inner_name')]
        except:
            pass
        

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
        if not obj_list:
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

class BaseCoreComponent(Entity):
    _ALL_VERSIONS = ()
    _ID_PREFIX = None

    title = ElementField("Title")
    id_ = IdField("id")
    idref = IdField("idref")
    version = AttributeField("version")
    timestamp = AttributeField("timestamp")
    information_source = ElementField("Information_Source")
    descriptions = None
    short_descriptions = None
    handling = ElementField("Handling")

    @classmethod
    def initClassFields(cls):
        import data_marking
        import common
        from stix.common.structured_text import StructuredTextList, StructuredTextListField
        cls.handling.type_ = data_marking.Marking
        cls.information_source.type_ = common.InformationSource
        cls.descriptions = StructuredTextListField("Description", StructuredTextList, key_name="description")
        cls.short_descriptions = StructuredTextListField("Short_Description", StructuredTextList, key_name="short_description")

    def __init__(self, id_=None, idref=None, timestamp=None, title=None,
                 description=None, short_description=None):
        super(BaseCoreComponent, self).__init__()
        self.id_ = id_ or utils.create_id(self._ID_PREFIX)
        self.idref = idref
        self.title = title
        self.description = description
        self.short_description = short_description
        self.version = None
        self.information_source = None
        self.handling = None

        if timestamp:
            self.timestamp = timestamp
        else:
            self.timestamp = utils.dates.now() if not idref else None

    # TODO: add this as a callback_hook to version TypedField
    def check_version(self, value):
        if not value:
            self._version = None
        else:
            utils.check_version(self._ALL_VERSIONS, value)
            self._version = value

    @property
    def timestamp(self):
        """The timestam property declares the time of creation and is
        automatically set in ``__init__()``.

        This property can accept ``datetime.datetime`` or ``str`` values.
        If an ``str`` value is supplied, a best-effort attempt is made to
        parse it into an instance of ``datetime.datetime``.

        Default Value: A ``datetime.dateime`` instance with a value of the
        date/time when ``__init__()`` was called.

        Note:
            If an ``idref`` is set during ``__init__()``, the value of
            ``timestamp`` will not automatically generated and instead default
            to the ``timestamp`` parameter, which has a default value of
            ``None``.

        Returns:
            An instance of ``datetime.datetime``.

        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        self._timestamp = utils.dates.parse_value(value)

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
        from stix.common.structured_text import StructuredTextList
        self.descriptions = StructuredTextList(value)

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
        from stix.common.structured_text import StructuredTextList
        self.short_descriptions = StructuredTextList(value)

    def add_short_description(self, description):
        """Adds a description to the ``short_descriptions`` collection.

        This is the same as calling "foo.short_descriptions.add(bar)".

        """
        self.short_descriptions.add(description)

"""
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        from stix.common import StructuredTextList, InformationSource
        from stix.data_marking import Marking

        if not return_obj:
            raise ValueError("Must provide a return_obj argument")

        if not obj:
            raise ValueError("Must provide an obj argument")

        return_obj.id_ = obj.id
        return_obj.idref = obj.idref
        return_obj.timestamp = obj.timestamp

        # These may not be found on the input obj if it isn't a full
        # type definition (e.g., used as a reference)
        return_obj.version = getattr(obj, 'version', None)
        return_obj.title = getattr(obj, 'Title', None)
        return_obj.descriptions = \
            StructuredTextList.from_obj(getattr(obj, 'Description', None))
        return_obj.short_descriptions = \
            StructuredTextList.from_obj(getattr(obj, 'Short_Description', None))
        return_obj.information_source = \
            InformationSource.from_obj(getattr(obj, 'Information_Source', None))
        return_obj.handling = \
            Marking.from_obj(getattr(obj, 'Handling', None))

        return return_obj

    def to_obj(self, return_obj=None, ns_info=None):
        if not return_obj:
            raise ValueError("Must provide a return_obj argument")

        super(BaseCoreComponent, self).to_obj(
            return_obj=return_obj,
            ns_info=ns_info
        )

        return_obj.id = self.id_
        return_obj.idref = self.idref
        return_obj.version = self.version
        return_obj.Title = self.title

        if self.timestamp:
            return_obj.timestamp = utils.dates.serialize_value(self.timestamp)
        if self.descriptions:
            return_obj.Description = self.descriptions.to_obj(ns_info=ns_info)
        if self.short_descriptions:
            return_obj.Short_Description = self.short_descriptions.to_obj(ns_info=ns_info)
        if self.information_source:
            return_obj.Information_Source = self.information_source.to_obj(ns_info=ns_info)
        if self.handling:
            return_obj.Handling = self.handling.to_obj(ns_info=ns_info)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        from stix.common import StructuredTextList, InformationSource
        from stix.data_marking import Marking

        if not return_obj:
            raise ValueError("Must provide a return_obj argument")

        get = d.get
        return_obj.id_ = get('id')
        return_obj.idref = get('idref')
        return_obj.timestamp = get('timestamp')
        return_obj.version = get('version')
        return_obj.title = get('title')
        return_obj.descriptions = \
            StructuredTextList.from_dict(get('description'))
        return_obj.short_descriptions = \
            StructuredTextList.from_dict(get('short_description'))
        return_obj.information_source = \
            InformationSource.from_dict(get('information_source'))
        return_obj.handling = \
            Marking.from_dict(get('handling'))

        return return_obj

    def to_dict(self):
        return super(BaseCoreComponent, self).to_dict()
"""
