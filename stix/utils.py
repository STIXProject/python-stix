# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import uuid


class InvalidMethodError(ValueError):
    def __init__(self, method):
        ValueError.__init__(self, "invalid method: %s" % method)


class IDGenerator(object):
    """Utility class for generating STIX ids"""
    METHOD_UUID = 1
    METHOD_INT = 2

    METHODS = (METHOD_UUID, METHOD_INT,)

    def __init__(self, namespace="stix", method=METHOD_UUID):
        self.namespace = namespace
        self.method = method
        self.next_int = 1

    @property
    def namespace(self):
        return self._namespace

    @namespace.setter
    def namespace(self, value):
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
            id_ = str(uuid.uuid1())
        elif self.method == IDGenerator.METHOD_INT:
            id_ = self.next_int
            self.next_int += 1
        else:
            raise InvalidMethodError()

        return "%s:%s-%s" % (self.namespace, prefix, id_)



# Singleton instance within this module. It is lazily instantiated, so simply
# importing the utils module will not create the object.
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


def set_id_namespace(namespace):
    """ Set the namespace for the module-level ID Generator"""
    _get_generator().namespace = namespace


def set_id_method(method):
    """ Set the method for the module-level ID Generator"""
    _get_generator().method = method


def create_id(prefix=None):
    """ Create an ID using the module-level ID Generator"""
    if not prefix:
        return _get_generator().create_id()
    else:
        return _get_generator().create_id(prefix)
