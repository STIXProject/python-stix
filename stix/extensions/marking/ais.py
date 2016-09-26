import stix
import stix_ais.bindings.ais as ais_binding
from stix.common import InformationSource
from stix.data_marking import Marking, MarkingStructure


class AISHandling(Marking):
    _binding = ais_binding
    _binding_class = _binding.AISHandling
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'
    _XSI_TYPE = "AIS:AISHandling"

    def __init__(self, marking=None):
        super(AISHandling, self).__init__()
        self.marking = marking

    def to_obj(self, return_obj=None, ns_info=None):
        super(AISHandling, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        Marking.to_obj(self, return_obj=return_obj, ns_info=ns_info)
        if self.marking:
            return_obj.Marking = self.marking.to_obj(ns_info=ns_info)

        return return_obj

    def to_dict(self):
        d = {}

        if self._XSI_TYPE:
            d['xsi:type'] = self._XSI_TYPE

        if self.marking:
            d['marking'] = self.marking.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()

        Marking.from_obj(obj, return_obj=return_obj)
        return_obj.marking = MarkingSpecificationType.from_obj(obj.Marking)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        Marking.from_dict(d, return_obj)
        return_obj.marking = d.get('marking')

        return return_obj


class MarkingSpecificationType(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.MarkingSpecificationType
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'

    def __init__(self, controlled_structure='//node() | //@*', marking_structure=None, information_source=None):
        super(MarkingSpecificationType, self).__init__()
        self.controlled_structure = controlled_structure
        self.marking_structure = marking_structure
        self.information_source = information_source

    def to_obj(self, return_obj=None, ns_info=None):
        super(MarkingSpecificationType, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        if self.controlled_structure:
            return_obj.Controlled_Structure = self.controlled_structure
        if self.marking_structure:
            return_obj.Marking_Structure = self.marking_structure.to_obj(ns_info=ns_info)
        if self.information_source:
            return_obj.Information_Source = self.information_source.to_obj(ns_info=ns_info)

        return return_obj

    def to_dict(self):
        d = {}

        if self.controlled_structure:
            d['controlled_structure'] = self.controlled_structure
        if self.marking_structure:
            d['marking_structure'] = self.marking_structure.to_dict()
        if self.information_source:
            d['information_source'] = self.information_source.to_dict()

        return d

    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None

        if not return_obj:
            return_obj = cls()
        return_obj.controlled_structure = obj.Controlled_Structure
        return_obj.marking_structure = AISMarkingStructure.from_obj(obj.Marking_Structure)
        return_obj.information_source = InformationSource.from_obj(obj.Information_Source)

        return return_obj

    @classmethod
    def from_dict(cls, d, return_obj=None):
        if not d:
            return None

        if not return_obj:
            return_obj = cls()

        return_obj.controlled_structure = d.get('controlled_structure')
        return_obj.marking_structure = d.get('marking_structure')
        return_obj.information_source = d.get('information_source')

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

        MarkingStructure.from_dict(d, return_obj)
        return_obj.is_proprietary = d.get('is_proprietary')
        return_obj.not_proprietary = d.get('not_proprietary')

        return return_obj


class IsProprietary(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.IsProprietary
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'

    def __init__(self, cisa_proprietary='true', ais_consent=None, tlp_marking=None):
        super(IsProprietary, self).__init__()
        self.cisa_proprietary = cisa_proprietary
        self.ais_consent = ais_consent
        self.tlp_marking = tlp_marking

    def to_obj(self, return_obj=None, ns_info=None):
        super(IsProprietary, self).to_obj(return_obj=return_obj, ns_info=ns_info)

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
        return_obj.ais_consent = d.get('ais_consent')
        return_obj.tlp_marking = d.get('tlp_marking')

        return return_obj


class NotProprietary(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.NotProprietary
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'

    def __init__(self, cisa_proprietary='false', ais_consent=None, tlp_marking=None):
        super(NotProprietary, self).__init__()
        self.cisa_proprietary = cisa_proprietary
        self.ais_consent = ais_consent
        self.tlp_marking = tlp_marking

    def to_obj(self, return_obj=None, ns_info=None):
        super(NotProprietary, self).to_obj(return_obj=return_obj, ns_info=ns_info)

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
        return_obj.ais_consent = d.get('ais_consent')
        return_obj.tlp_marking = d.get('tlp_marking')

        return return_obj


class AISConsentType(stix.Entity):
    _binding = ais_binding
    _binding_class = _binding.AISConsentType
    _namespace = 'http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2'

    def __init__(self, consent=None):
        self.consent = consent

    def to_obj(self, return_obj=None, ns_info=None):
        super(AISConsentType, self).to_obj(return_obj=return_obj, ns_info=ns_info)

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

    def __init__(self, color=None):
        self.color = color

    def to_obj(self, return_obj=None, ns_info=None):
        super(TLPMarkingType, self).to_obj(return_obj=return_obj, ns_info=ns_info)

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


# Register extension
stix.data_marking.add_extension(AISMarkingStructure)
