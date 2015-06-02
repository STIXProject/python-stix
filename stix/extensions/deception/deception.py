from stix.common import vocabs

@vocabs.register_vocab
class Deception_1_0(vocabs.VocabString):
    _namespace = 'http://stix.mitre.org/deception-1'
    _XSI_TYPE = 'stixVocabs:DeceptionVocab-1.0'
    _VOCAB_VERSION = '1.0'

    TERM_PURPOSE = 'Purpose'
    TERM_COLLECT = "Collect Intelligence"
    TERM_DESIGN = "Design Cover Story"
    TERM_PLAN ="Plan"
    TERM_PREPARE="Prepare"
    TERM_EXECUTE ="Execute"
    TERM_MONITOR ="Monitor"
    TERM_REINFORCE = 'Reinforce'    