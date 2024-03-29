import nltk

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2019, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/master/LICENSE"
__version__ = "0.2.7"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class SpanTokenizer:
    @staticmethod
    def get_token_spans(txt: str):
        """
        returns: [('word', 'token', (word_start, word_end)), ...]
        """
        words = nltk.word_tokenize(txt)
        tokens = nltk.pos_tag(words)
        offset = 0
        last_symbol = len(txt) - 1

        for word, token in tokens:
            next_offset = txt.find(word, offset)
            offset = next_offset if next_offset >= 0 else offset + 1
            offset = min(offset, last_symbol)

            right_margin = offset + len(word)

            yield word, token, offset, right_margin - 1
            offset = right_margin
