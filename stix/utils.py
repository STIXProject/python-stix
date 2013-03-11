import uuid

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

