# Copyright (c) 2016, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix.bindings.extensions.marking.ais as ais_binding
import stix.data_marking
from stix.data_marking import MarkingStructure


class AISConsentType(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.AISConsentType
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'
    _ALLOWED_VALUES = ('EVERYONE', 'USG', 'NONE')

    def __init__(self, consent=None):
        self.consent = consent

    @property
    def consent(self):
        return self._consent

    @consent.setter
    def consent(self, value):
        if value is not None and value not in self._ALLOWED_VALUES:
            msg = "consent should be one of: %s. Received %s"
            raise ValueError(msg % (self._ALLOWED_VALUES, value))
        else:
            self._consent = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(AISConsentType, self).to_obj(return_obj=return_obj,
                                           ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.consent:
            return_obj.consent = self.consent

        return return_obj

    def to_dict(self):
        return super(AISConsentType, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.consent = obj.consent

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.consent = d.get('consent')

        return return_obj


class TLPMarkingType(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.TLPMarkingType
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'
    _ALLOWED_VALUES = ('WHITE', 'GREEN', 'AMBER')

    def __init__(self, color=None):
        self.color = color

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if value is not None and value not in self._ALLOWED_VALUES:
            msg = "color should be one of: %s. Received %s"
            raise ValueError(msg % (self._ALLOWED_VALUES, value))
        else:
            self._color = value

    def to_obj(self, return_obj=None, ns_info=None):
        super(TLPMarkingType, self).to_obj(return_obj=return_obj,
                                           ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        return_obj.color = self.color

        return return_obj

    def to_dict(self):
        return super(TLPMarkingType, self).to_dict()

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.color = obj.color

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.color = d.get('color')

        return return_obj


class NotProprietary(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.NotProprietary
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'

    def __init__(self, cisa_proprietary='false', ais_consent=None,
                 tlp_marking=None):
        super(NotProprietary, self).__init__()
        self.cisa_proprietary = cisa_proprietary
        self.ais_consent = ais_consent
        self.tlp_marking = tlp_marking

    @property
    def ais_consent(self):
        return self._ais_consent

    @ais_consent.setter
    def ais_consent(self, value):
        if isinstance(value, AISConsentType):
            self._ais_consent = value
        else:
            self._set_var(AISConsentType, try_cast=False, ais_consent=value)

    @property
    def tlp_marking(self):
        return self._tlp_marking

    @tlp_marking.setter
    def tlp_marking(self, value):
        if isinstance(value, TLPMarkingType):
            self._tlp_marking = value
        else:
            self._set_var(TLPMarkingType, try_cast=False, tlp_marking=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(NotProprietary, self).to_obj(return_obj=return_obj,
                                           ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.cisa_proprietary:
            return_obj.CISA_Proprietary = self.cisa_proprietary
        if self.ais_consent:
            return_obj.AISConsent = self.ais_consent.to_obj(ns_info=ns_info)
        if self.tlp_marking:
            return_obj.TLPMarking = self.tlp_marking.to_obj(ns_info=ns_info)

        return return_obj

    def to_dict(self):
        d = {}

        if self.cisa_proprietary:
            d['cisa_proprietary'] = self.cisa_proprietary
        if self.ais_consent:
            d['ais_consent'] = self.ais_consent.to_dict()
        if self.tlp_marking:
            d['tlp_marking'] = self.tlp_marking.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.cisa_proprietary = obj.CISA_Proprietary
        return_obj.ais_consent = AISConsentType.from_obj(obj.AISConsent)
        return_obj.tlp_marking = TLPMarkingType.from_obj(obj.TLPMarking)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.cisa_proprietary = d.get('cisa_proprietary')
        return_obj.ais_consent = AISConsentType.from_dict(d.get('ais_consent'))
        return_obj.tlp_marking = TLPMarkingType.from_dict(d.get('tlp_marking'))

        return return_obj


class IsProprietary(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.IsProprietary
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'

    def __init__(self, cisa_proprietary='true', ais_consent=None,
                 tlp_marking=None):
        super(IsProprietary, self).__init__()
        self.cisa_proprietary = cisa_proprietary
        self.ais_consent = ais_consent
        self.tlp_marking = tlp_marking

    def to_obj(self, return_obj=None, ns_info=None):
        super(IsProprietary, self).to_obj(return_obj=return_obj,
                                          ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.cisa_proprietary:
            return_obj.CISA_Proprietary = self.cisa_proprietary
        if self.ais_consent:
            return_obj.AISConsent = self.ais_consent.to_obj(ns_info=ns_info)
        if self.tlp_marking:
            return_obj.TLPMarking = self.tlp_marking.to_obj(ns_info=ns_info)

        return return_obj

    def to_dict(self):
        d = {}

        if self.cisa_proprietary:
            d['cisa_proprietary'] = self.cisa_proprietary
        if self.ais_consent:
            d['ais_consent'] = self.ais_consent.to_dict()
        if self.tlp_marking:
            d['tlp_marking'] = self.tlp_marking.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.cisa_proprietary = obj.CISA_Proprietary
        return_obj.ais_consent = AISConsentType.from_obj(obj.AISConsent)
        return_obj.tlp_marking = TLPMarkingType.from_obj(obj.TLPMarking)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.cisa_proprietary = d.get('cisa_proprietary')
        return_obj.ais_consent = AISConsentType.from_dict(d.get('ais_consent'))
        return_obj.tlp_marking = TLPMarkingType.from_dict(d.get('tlp_marking'))

        return return_obj


class AISMarkingStructure(MarkingStructure):
    _binding = ais_binding
    _binding_class = _binding.AISMarkingStructure
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'
    _XSI_TYPE = "AIS:AISMarkingStructure"

    def __init__(self, is_proprietary=None, not_proprietary=None):
        super(AISMarkingStructure, self).__init__()
        self.is_proprietary = is_proprietary
        self.not_proprietary = not_proprietary

    @property
    def not_proprietary(self):
        return self._not_proprietary

    @not_proprietary.setter
    def not_proprietary(self, value):
        if isinstance(value, NotProprietary):
            self._not_proprietary = value
        else:
            self._set_var(NotProprietary, try_cast=False, not_proprietary=value)

    @property
    def is_proprietary(self):
        return self._is_proprietary

    @is_proprietary.setter
    def is_proprietary(self, value):
        if isinstance(value, IsProprietary):
            self._is_proprietary = value
        else:
            self._set_var(IsProprietary, try_cast=False, is_proprietary=value)

    def to_obj(self, return_obj=None, ns_info=None):
        super(AISMarkingStructure, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        MarkingStructure.to_obj(self, return_obj=return_obj, ns_info=ns_info)
        if self.is_proprietary:
            return_obj.Is_Proprietary = self.is_proprietary.to_obj(ns_info=ns_info)
        if self.not_proprietary:
            return_obj.Not_Proprietary = self.not_proprietary.to_obj(ns_info=ns_info)

        return return_obj

    def to_dict(self):
        d = MarkingStructure.to_dict(self)

        if self.is_proprietary:
            d['is_proprietary'] = self.is_proprietary.to_dict()

        if self.not_proprietary:
            d['not_proprietary'] = self.not_proprietary.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        MarkingStructure.from_obj(obj, return_obj=return_obj)
        return_obj.is_proprietary = IsProprietary.from_obj(obj.Is_Proprietary)
        return_obj.not_proprietary = NotProprietary.from_obj(obj.Not_Proprietary)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        MarkingStructure.from_dict(d, return_obj=return_obj)
        return_obj.is_proprietary = IsProprietary.from_dict(d.get('is_proprietary'))
        return_obj.not_proprietary = NotProprietary.from_dict(d.get('not_proprietary'))

        return return_obj


NAMESPACES = {
    'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2': 'AIS'
}

SCHEMALOCATIONS = {
    'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2': 'http://www.us-cert.gov/sites/default/files/STIX_Namespace/AIS_Bundle_Marking_1.1.1_v1.0.xsd'
}


def _update_namespaces():
    # Update the python-stix namespace dictionary
    import stix.utils.nsparser as nsparser

    # Register the extension namespaces
    nsparser.DEFAULT_EXT_TO_PREFIX.update(NAMESPACES)

    # Update the default dict
    nsparser.DEFAULT_STIX_NAMESPACES.update(NAMESPACES)


def _update_schemalocations():
    # Update the python-stix schemalocation dictionary
    import stix.utils.nsparser as nsparser

    # Register the extension schemalocations
    nsparser.EXT_NS_TO_SCHEMALOCATION.update(SCHEMALOCATIONS)

    # Update the default dict
    nsparser.DEFAULT_STIX_SCHEMALOCATIONS.update(SCHEMALOCATIONS)


# Register extension
stix.data_marking.add_extension(AISMarkingStructure)
_update_namespaces()
_update_schemalocations()
