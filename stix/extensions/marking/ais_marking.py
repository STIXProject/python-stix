import stix.bindings.extensions.marking.ais_marking as ais_marking_binding
import stix.data_marking
from stix.data_marking import MarkingStructure

CONSENT_EVERYONE = 'EVERYONE'
CONSENT_USG = 'USG'
CONSENT_NONE = 'NONE'

TLP_WHITE = 'WHITE'
TLP_GREEN = 'GREEN'
TLP_AMBER = 'AMBER'
# There is no TLP RED in the DHS AIS Consent Markings

PROPRIETARY_FALSE = False
PROPRIETARY_TRUE = True

CONSENT_TUPLE = (CONSENT_NONE, CONSENT_USG, CONSENT_EVERYONE)
TLP_TUPLE = (TLP_WHITE, TLP_GREEN, TLP_AMBER)
PROPRIETARY_TUPLE = (PROPRIETARY_FALSE, PROPRIETARY_TRUE)


class AISMarkingStructure(MarkingStructure):
    _binding = ais_marking_binding
    _binding_class = ais_marking_binding.AISMarkingStructure
    _namespace = "http://www.us-cert.gov/STIXMarkingStructure#AISConsentMarking-2"
    _XSI_TYPE = "AIS:AISMarkingStructure"

    def __init__(self, cisa_proprietary=PROPRIETARY_FALSE, tlp_color=TLP_GREEN, consent=CONSENT_EVERYONE):
        super(AISMarkingStructure, self).__init__()
        self.cisa_proprietary = cisa_proprietary
        self.tlp_color = tlp_color
        self.consent = consent

    def to_obj(self, return_obj=None, ns_info=None):
        super(AISMarkingStructure, self).to_obj(return_obj=return_obj, ns_info=ns_info)

        if not return_obj:
            return_obj = self._binding_class()

        MarkingStructure.to_obj(self, return_obj=return_obj, ns_info=ns_info)
        # print dir(return_obj)

        consent = ais_marking_binding.AISConsentType(consent=self.consent)
        marking = ais_marking_binding.TLPMarkingType(color=self.tlp_color)

        if self.cisa_proprietary:
            p = ais_marking_binding.IsProprietary(CISA_Proprietary=self.cisa_proprietary,
                                                  AISConsent=consent,
                                                  TLPMarking=marking)
            return_obj.set_Is_Proprietary(p)
        else:
            p = ais_marking_binding.NotProprietary(CISA_Proprietary=self.cisa_proprietary,
                                                   AISConsent=consent,
                                                   TLPMarking=marking)
            return_obj.set_Not_Proprietary(p)

        return return_obj

    def to_dict(self):
        d = super(AISMarkingStructure, self).to_dict()

        d['cisa_proprietary'] = self.cisa_proprietary
        d['consent'] = self.consent
        d['tlp_color'] = self.tlp_color

        return d

    @staticmethod
    def from_obj(obj):
        if not obj:
            return None

        m = AISMarkingStructure()
        MarkingStructure.from_obj(obj, m)

        proprietary = obj.get_Is_Proprietary() or obj.get_Not_Proprietary()

        m.cisa_proprietary = proprietary.get_CISA_Proprietary()
        m.consent = proprietary.get_AISConsent().get_consent()
        m.tlp_color = proprietary.get_TLPMarking().get_color()

        return m

    @staticmethod
    def from_dict(marking_dict):
        if not marking_dict:
            return None

        m = AISMarkingStructure()
        MarkingStructure.from_dict(marking_dict, m)
        m.cisa_proprietary = marking_dict.get('cisa_proprietary')
        m.consent = marking_dict.get('consent')
        m.tlp_color = marking_dict.get('tlp_color')

        return m

stix.data_marking.add_extension(AISMarkingStructure)

