import os

from lexnlp.extract.common.language_dictionary_reader import LanguageDictionaryReader

__author__ = "ContraxSuite, LLC; LexPredict, LLC"
__copyright__ = "Copyright 2015-2019, ContraxSuite, LLC"
__license__ = "https://github.com/LexPredict/lexpredict-lexnlp/blob/master/LICENSE"
__version__ = "0.2.7"
__maintainer__ = "LexPredict, LLC"
__email__ = "support@contraxsuite.com"


class EnLanguageTokens:
    abbreviations = {'nr.', 'abs.', 'no.', 'act.', 'inc.', 'p.', 'Inc.'}
    articles = ['a', 'the', 'an']
    conjunctions = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']
    pronouns = {'I', 'he', 'she', 'we', 'you', 'they'}

    @staticmethod
    def init():
        abr_file_path = os.path.join(os.path.dirname(__file__),
                                     'data/abbreviations.txt')
        if os.path.isfile(abr_file_path):
            file_set = LanguageDictionaryReader.read_str_set(abr_file_path)
            EnLanguageTokens.abbreviations = \
                EnLanguageTokens.abbreviations.union(file_set)

        prn_file_path = os.path.join(os.path.dirname(__file__),
                                     'data/pronouns.txt')
        if os.path.isfile(prn_file_path):
            file_set = LanguageDictionaryReader.read_str_set(prn_file_path)
            EnLanguageTokens.pronouns = \
                EnLanguageTokens.pronouns.union(file_set)


EnLanguageTokens.init()
