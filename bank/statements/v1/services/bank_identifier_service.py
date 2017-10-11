import re
import unicodedata
import math

from ICICI_bank_statements_a_service import ICICIBankStatementsA
from ICICI_bank_statements_b_service import ICICIBankStatementsB
from HDFC_bank_statements_service import HDFCBankStatements
from AXIS_bank_statements_a_service import AXISBankStatementsA
from AXIS_bank_statements_b_service import AXISBankStatementsB
from SBI_bank_statements_service import SBIBankStatements
from Kotak_bank_statements_a_service import KotakBankStatementsA
from Kotak_bank_statements_b_service import KotakBankStatementsB
from Kotak_bank_statements_c_service import KotakBankStatementsC
from IDBI_bank_statements_service import IDBIBankStatements
from IDFC_bank_statements_service import IDFCBankStatements
# from CITI_bank_statements_a_service import CITIBankStatementsA
# from CITI_bank_statements_b_service import CITIBankStatementsB
# from Canara_bank_statements_a_service import CanaraBankStatementsA
# from Canara_bank_statements_b_service import CanaraBankStatementsB

from bank_identifier_constants import (PROMINENT_BANK_LIST, PROMINENT_BANK_FEATURES,
                                       TABLE_ROW_MINIMUM_COVERAGE, PROMINENT_BANK_LIST,
                                       PROMINENT_BANK_MINIMUM_SCORE)


class ProminentBankIdentifier(object):
    """Class to Identify the prominent banks from the Bank Statements"""

    def __init__(self, raw_table_data, pdf_text):
        self.raw_table_data = raw_table_data
        self.pdf_text = pdf_text
        self.processed_pdf_text = self.__processed_pdf_text()
        self.raw_table_data_set = self.__raw_table_data_set()
        self.row_lenth_distribution = self.__row_lenth_distribution()
        self.bank_dict = {
            'icici_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': ICICIBankStatementsA,
            },
            'icici_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': ICICIBankStatementsB,
            },
            'axis_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': AXISBankStatementsA,
            },
            'axis_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': AXISBankStatementsB,
            },
            'idbi_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': IDBIBankStatements,
            },
            'idbi_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': IDBIBankStatements,
            },
            'idfc_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': IDFCBankStatements,
            },
            'sbi_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': SBIBankStatements,
            },
            'hdfc_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': HDFCBankStatements,
            },
            'kotak_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': KotakBankStatementsA,
            },
            'kotak_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': KotakBankStatementsB,
            },
            'kotak_c': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
                'class': KotakBankStatementsC,
            },
        }
        self.score_map = dict()
        self.__get_likelihood()
        self.bank_list = self.__bank_list()

    def __processed_pdf_text(self):
        pdf_text_unicode = unicode(self.pdf_text, "utf-8")
        pdf_text_fixed = unicodedata.normalize(
            'NFKD', pdf_text_unicode).encode('ascii', 'ignore')
        return' '.join(pdf_text_fixed.lower().split())

    def __raw_table_data_set(self):
        raw_table_data_set = set()
        for statement in self.raw_table_data.get('body', [])[:21] + [self.raw_table_data.get('headers', [])]:
            for string in statement:
                raw_table_data_set.add(string.lower())
        return raw_table_data_set

    def __row_lenth_distribution(self):
        row_lenth_distribution = {}
        for statement in self.raw_table_data.get('body', []):
            if row_lenth_distribution.get(len(statement)):
                row_lenth_distribution[len(statement)] += 1
            else:
                row_lenth_distribution[len(statement)] = 1
        return row_lenth_distribution

    def __regex_bool(self, regex_word, input_string):
        output_list = [output for output in re.findall(
            regex_word, input_string) if output != ' ']
        return True if output_list else False

    def __table_dimensions_bool(self, minimum_rows, maximum_rows):
        in_range = 0
        total_rows = 0
        for row_lenth, number_of_rows in self.row_lenth_distribution.iteritems():
            if row_lenth >= 3:
                total_rows += number_of_rows
            if minimum_rows <= row_lenth <= maximum_rows:
                in_range += number_of_rows
        in_range_percentage = math.ceil(
            in_range * 100.0 / total_rows) if in_range and total_rows else 0
        return True if in_range_percentage >= TABLE_ROW_MINIMUM_COVERAGE else False

    def __get_score(self, metric, bank):
        if metric == 'table_dimensions':
            minimum_rows_data, maximum_rows_data = PROMINENT_BANK_FEATURES.get(
                bank, {}).get(metric, {}).get('features', [{}, {}])
            if self.__table_dimensions_bool(minimum_rows_data['minimum_columns'], maximum_rows_data['maximum_columns']):
                return 100.0
            else:
                return 0
        normalized_score = None
        total_score = 0
        total_weight = 0
        for keyword_data in PROMINENT_BANK_FEATURES.get(bank, {}).get(metric, {}).get('features', []):
            total_weight += keyword_data['weight']
            if metric == 'keywords':
                if keyword_data['string'] in self.processed_pdf_text:
                    total_score += keyword_data['weight']
            elif metric == 'regex_words':
                if self.__regex_bool(keyword_data['string'], self.processed_pdf_text):
                    total_score += keyword_data['weight']
            elif metric == 'table_headers':
                if keyword_data['string'] in '*'.join(self.raw_table_data_set):
                    total_score += keyword_data['weight']
            else:
                pass
        if PROMINENT_BANK_FEATURES.get(bank, {}).get(metric, {}).get('features'):
            if total_weight:
                normalized_score = total_score * 100.0 / total_weight
            else:
                normalized_score = total_score
        return normalized_score

    def __get_likelihood(self):
        for bank in PROMINENT_BANK_LIST:
            total_score = 0
            total_weight = 0
            for metric in ['keywords', 'regex_words', 'table_headers', 'table_dimensions']:
                self.bank_dict[bank][metric] = self.__get_score(metric, bank)
                if self.bank_dict[bank][metric] is not None:
                    total_weight += PROMINENT_BANK_FEATURES.get(
                        bank, {}).get(metric, {}).get('weight', 0)
                    total_score += self.bank_dict[bank][metric] * 1.0 * PROMINENT_BANK_FEATURES.get(
                        bank, {}).get(metric, {}).get('weight', 0)
            self.score_map[bank] = math.ceil(
                total_score * 1.0 / total_weight) if total_weight else 0

    def __bank_list(self):
        bank_list = []
        for bank in PROMINENT_BANK_LIST:
            if self.score_map[bank] >= PROMINENT_BANK_MINIMUM_SCORE:
                bank_list.append(bank)
        return bank_list
