# Copyright (c) 2014, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix
import stix.bindings.stix_common as stix_common_binding
#TODO: handle normalization
#from cybox.utils import normalize_to_xml, denormalize_from_xml


class VocabString(stix.Entity):
    _binding = stix_common_binding
    _binding_class = stix_common_binding.ControlledVocabularyStringType
    _namespace = 'http://stix.mitre.org/common-1'

    # All subclasses should override this
    _XSI_TYPE = None

    def __init__(self, value=None):
        super(VocabString, self).__init__()
        self.value = value
        self.xsi_type = self._XSI_TYPE

        self.vocab_name = None
        self.vocab_reference = None

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        # Check to make sure the values are identical.
        if isinstance(other, VocabString):
            other = other.value

        return other == self.value

    def is_plain(self):
        """Whether the VocabString can be represented as a single value.

        If `xsi:type` and `value` are the only non-None properties, the
        VocabString can be represented by a single value rather than a
        dictionary. This makes the JSON representation simpler without losing
        any data fidelity.
        """
        return (
            # ignore value and xsi_type
            self.vocab_name is None and
            self.vocab_reference is None
        )

    def to_obj(self, return_obj=None):
        if not return_obj:
            return_obj = self._binding_class()

        #TODO: handle normalization
        #vocab_obj.set_valueOf_(normalize_to_xml(self.value))
        return_obj.set_valueOf_(self.value)
        return_obj.set_xsi_type(self.xsi_type)

        if self.vocab_name is not None:
            return_obj.set_vocab_name(self.vocab_name)
        if self.vocab_reference is not None:
            return_obj.set_vocab_reference(self.vocab_reference)

        return return_obj

    def to_dict(self):
        if self.is_plain():
            return self.value

        d = {}
        if self.value is not None:
            d['value'] = self.value
        if self.xsi_type is not None:
            d['xsi:type'] = self.xsi_type
        if self.vocab_name is not None:
            d['vocab_name'] = self.vocab_name
        if self.vocab_reference is not None:
            d['vocab_reference'] = self.vocab_reference

        return d

    @classmethod
    def from_obj(cls, vocab_obj, return_obj=None):
        if not vocab_obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        # xsi_type should be set automatically by the class's constructor.

        #TODO: handle denormalization
        #vocab_str.value = denormalize_from_xml(vocab_obj.get_valueOf_())
        return_obj.value = vocab_obj.get_valueOf_()
        return_obj.vocab_name = vocab_obj.get_vocab_name()
        return_obj.vocab_reference = vocab_obj.get_vocab_reference()

        return return_obj

    @classmethod
    def from_dict(cls, vocab_dict, return_obj=None):
        if not vocab_dict:
            return None
        if not return_obj:
            return_obj = cls()
            
        # xsi_type should be set automatically by the class's constructor.

        # In case this is a "plain" string, just set it.
        if not isinstance(vocab_dict, dict):
            return_obj.value = vocab_dict
        else:
            return_obj.xsi_type = vocab_dict.get('xsi:type')
            return_obj.value = vocab_dict.get('value')
            return_obj.vocab_name = vocab_dict.get('vocab_name')
            return_obj.vocab_reference = vocab_dict.get('vocab_reference')

        return return_obj


class HighMediumLow(VocabString):
    _namespace = 'http://stix.mitre.org/default_vocabularies-1'
    _XSI_TYPE = 'stixVocabs:HighMediumLowVocab-1.0'

