"""Copyright extraction for English using NLTK and NLTK pre-trained maximum entropy classifier.

This module implements basic Copyright extraction functionality in English relying on the pre-trained
NLTK functionality, including POS tagger and NE (fuzzy) chunkers.

Todo: -
"""

# Imports
import string
from typing import Generator, List, Tuple

from lexnlp.extract.common.copyrights.copyright_en_style_parser import CopyrightEnStyleParser
from lexnlp.extract.common.annotations.copyright_annotation import CopyrightAnnotation
from lexnlp.extract.common.annotations.phrase_position_finder import PhrasePositionFinder
from lexnlp.extract.en.utils import NPExtractor

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2019, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/master/LICENSE"
__version__ = "0.2.7"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


grammar = r"""
    NBAR:
        {<NNP.*|JJ|CD|NN|\(|\)|,>*<NNP.*|CD>}  # Nouns, Adj-s, brackets, terminated with Nouns/Numbers
    IN:
        {<CC|IN>}   # &, and, of
    NP:
        {(<NBAR><IN>)*<NBAR>}
"""


class CopyrightNPExtractor(NPExtractor):

    allowed_sym = ['&', 'and', 'of', '©']
    allowed_pos = ['IN', 'CC', 'NN']

    @staticmethod
    def strip_np(np):
        return np.strip(string.punctuation.replace('(', '') + string.whitespace)


np_extractor = CopyrightNPExtractor(grammar=grammar)


class CopyrightEnParser(CopyrightEnStyleParser):
    @classmethod
    def extract_phrases_with_coords(cls, sentence: str) -> List[Tuple[str, int]]:
        phrases = list(np_extractor.get_np(sentence))
        tagged_phrases = PhrasePositionFinder.find_phrase_int_source_text(
            sentence, phrases)
        return tagged_phrases


def get_copyright(text: str,
                  return_sources=False) -> Generator:
    for ant in get_copyright_annotations(text, return_sources):
        ret = (ant.sign,
               ant.date,
               ant.name)
        if return_sources:
            ret += (ant.text,)
        yield ret


def get_copyright_annotations(text: str, return_sources=False) -> \
        Generator[CopyrightAnnotation, None, None]:
    for ant in CopyrightEnParser.get_copyright_annotations(text,
                                                           return_sources):
        ant.locale = 'en'
        yield ant
