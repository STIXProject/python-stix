import collections

import stix
import stix.bindings.stix_common as common_binding

from .confidence import Confidence
from .information_source import InformationSource
from .vocabs import VocabString
from stix.bindings import stix_common


class Relationship(VocabString):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding

class GenericRelationship(stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding

    def __init__(self, confidence=None, information_source=None, relationship=None):
        self.confidence = confidence
        self.information_source = information_source
        self.relationship = relationship

    @property
    def confidence(self):
        return self._confidence

    @confidence.setter
    def confidence(self, value):
        if value:
            if isinstance(value, Confidence):
                self._confidence = value
            else:
                self._confidence = Confidence(value=value)
        else:
            self._confidence = None

    @property
    def information_source(self):
        return self._information_source

    @information_source.setter
    def information_source(self, value):
        if value and not isinstance(value, InformationSource):
            raise ValueError('value must be instance of InformationSource')

        self._information_source = value

    @property
    def relationship(self):
        return self._relationship

    @relationship.setter
    def relationship(self, value):
        if value:
            if isinstance(value, Relationship):
                self._relationship = value
            else:
                self._relationship = Relationship(value=value)
        else:
            self._relationship = None

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.confidence = Confidence.from_obj(obj.get_Confidence())
        return_obj.information_source = InformationSource.from_obj(obj.get_Information_Source())
        return_obj.relationship = Relationship.from_obj(obj.get_Relationship())

        return return_obj

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding.GenericRelationshipType()

        if self.confidence:    
            return_obj.set_Confidence(self.confidence.to_obj())

        if self.information_source:
            return_obj.set_Information_Source(self.information_source.to_obj())

        if self.relationship:
            return_obj.set_Relationship(self.relationship.to_obj())

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.confidence = Confidence.from_dict(dict_repr.get('confidence'))
        return_obj.information_source = InformationSource.from_dict(dict_repr.get('information_source'))
        return_obj.relationship = Relationship.from_dict(dict_repr.get('relationship'))

        return return_obj

    def to_dict(self,):
        d = {}
        if self.confidence:
            d['confidence'] = self.confidence.to_dict()
        if self.information_source:
            d['information_source'] = self.information_source.to_dict()
        if self.relationship:
            d['relationship'] = self.relationship.to_dict()

        return d



class GenericRelationshipList(collections.MutableSequence, stix.Entity):
    _namespace = "http://stix.mitre.org/common-1"
    _binding = common_binding
    _binding_class = _binding.GenericRelationshipListType

    def __init__(self, scope=None, *args):
        super(GenericRelationshipList, self).__init__()
        self._inner = []
        self.scope = scope

        for arg in args:
            if isinstance(arg, list):
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

    def to_obj(self):
        list_obj = self._binding_class()

        setattr(list_obj, self._binding_var, [x.to_obj() for x in self])
        if self.scope:
            list_obj.set_scope(self.scope)

        return list_obj

    def to_dict(self):
        d = {}

        d[self._inner_name] = [h.to_dict() for h in self]
        if self.scope:
            d['scope'] = self.scope

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        for item in getattr(obj, cls._binding_var):
            return_obj.append(cls._contained_type.from_obj(item))

        return_obj.scope = obj.get_scope()

        return return_obj

    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not isinstance(dict_repr, dict):
            return None

        if not return_obj:
            return_obj = cls()

        for item in dict_repr.get(cls._inner_name, []):
            return_obj.append(cls._contained_type.from_dict(item))

        return_obj.scope = dict_repr.get('scope')

        return return_obj
