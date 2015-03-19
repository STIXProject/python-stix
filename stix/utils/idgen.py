# Copyright (c) 2015, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import uuid
import contextlib
import cybox.utils


#: Default "example" namespace used for identifiers when no other namespace is
#: defined.
EXAMPLE_NAMESPACE = {'http://example.com': 'example'}


class InvalidMethodError(ValueError):
    def __init__(self, method):
        ValueError.__init__(self, "invalid method: %s" % method)


class IDGenerator(object):
    """Utility class for generating STIX ids"""
    METHOD_UUID = 1
    METHOD_INT = 2

    METHODS = (METHOD_UUID, METHOD_INT,)

    def __init__(self, namespace=None, method=METHOD_UUID):
        self.namespace = namespace or EXAMPLE_NAMESPACE
        self.method = method
        self.next_int = 1

    @property
    def namespace(self):
        return self._namespace

    @namespace.setter
    def namespace(self, value):
        if not isinstance(value, dict):
            raise ValueError("Must be a dictionary: ex {'http://example.com' : 'example'}")

        if len(value) != 1:
            raise ValueError("Provided dictionary must have at most one entry")

        self._namespace = value

    @property
    def method(self):
        return self._method

    @method.setter
    def method(self, value):
        if value not in IDGenerator.METHODS:
            raise InvalidMethodError("invalid method: %s" % value)
        self._method = value

    def create_id(self, prefix="guid"):
        """Create an ID.

        Note that if `prefix` is not provided, it will be `quid`, even if the
        `method` is `METHOD_INT`.
        """
        if self.method == IDGenerator.METHOD_UUID:
            id_ = str(uuid.uuid4())
        elif self.method == IDGenerator.METHOD_INT:
            id_ = self.next_int
            self.next_int += 1
        else:
            raise InvalidMethodError(self.method)

        ns_prefix = self.namespace.itervalues().next()
        return "%s:%s-%s" % (ns_prefix, prefix, id_)


#: Singleton instance within this module. It is lazily instantiated, so simply
#: importing the utils module will not create the object.
__generator = None


def _get_generator():
    """Return the `stix.utils` module's generator object.

    Only under rare circumstances should this function be called by external
    code. More likely, external code should initialize its own IDGenerator or
    use the `set_id_namespace`, `set_id_method`, or `create_id` functions of
    the `stix.utils` module.
    """
    global __generator
    if not __generator:
        __generator = IDGenerator()
    return __generator


def _set_cybox_namespace(namespace):
    uri = namespace.iterkeys().next()
    prefix = namespace.itervalues().next()

    ns = cybox.utils.Namespace(uri, prefix)
    cybox.utils.set_id_namespace(ns)


def set_id_namespace(namespace):
    """ Set the namespace for the module-level ID Generator"""
    _get_generator().namespace = namespace
    _set_cybox_namespace(namespace)


def set_id_method(method):
    """ Set the method for the module-level ID Generator"""
    _get_generator().method = method


def get_id_namespace():
    """Return the namespace associated with generated ids"""
    return _get_generator().namespace.iterkeys().next()


def get_id_namespace_alias():
    """Returns the namespace alias assoicated with generated ids"""
    return _get_generator().namespace.itervalues().next()


def create_id(prefix=None):
    """ Create an ID using the module-level ID Generator"""
    if not prefix:
        return _get_generator().create_id()
    else:
        return _get_generator().create_id(prefix)


@contextlib.contextmanager
def temp_id_namespace(namespace):
    try:
        saved_id_namespace = {get_id_namespace(): get_id_namespace_alias()}
        set_id_namespace(namespace)
        yield
    finally:
        set_id_namespace(saved_id_namespace)
