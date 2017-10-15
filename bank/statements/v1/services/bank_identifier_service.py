import re
import unicodedata
import math
import copy

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
from Andra_bank_statements_a_service import AndraBankStatementsA
from Andra_bank_statements_b_service import AndraBankStatementsB
from Bank_of_Baroda_bank_statements_a_service import BankOfBarodaBankStatementsA
from CITI_bank_statements_a_service import CITIBankStatementsA
from CITI_bank_statements_b_service import CITIBankStatementsB
from Canara_bank_statements_a_service import CanaraBankStatementsA
from Canara_bank_statements_b_service import CanaraBankStatementsB
from Corporation_bank_statements_a_service import CorporationBankStatementsA
from IndianOverseas_bank_statements_service import IndianOverseasStatementsA
from Indian_bank_statements_a_service import IndianBankStatementsA
from IndusInd_bank_statements_a_service import IndusIndBankStatementsA
from IndusInd_bank_statements_b_service import IndusIndBankStatementsB
from OrientalBankOfCommerce_bank_statements_b_service import OrientalBankOfCommerceBankStatementsA
from PunjabNational_bank_statements_a_service import PunjabNationalBankStatementsA
from Union_bank_statements_a_service import UnionBankStatementsA
from Yes_bank_statements_a_service import YesBankStatementsA

from bank_identifier_constants import (PROMINENT_BANK_LIST, PROMINENT_BANK_FEATURES,
                                       TABLE_ROW_MINIMUM_COVERAGE, PROMINENT_BANK_LIST,
                                       PROMINENT_BANK_MINIMUM_SCORE, LESS_PROMINENT_BANK_FEATURES,
                                       LESS_PROMINENT_BANK_LIST, LESS_PROMINENT_BANK_MAX_CONSIDERATION)


class BankIdentifier(object):
    """Class to Identify the prominent banks from the Bank Statements"""

    def __init__(self, raw_table_data, pdf_text):
        self.raw_table_data = raw_table_data
        self.pdf_text = pdf_text
        self.processed_pdf_text = self.__processed_pdf_text()
        self.raw_table_data_set = self.__raw_table_data_set()
        self.row_lenth_distribution = self.__row_lenth_distribution()
        self.bank_features = self.__bank_features()
        self.bank_dict = {
            'icici_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'icici_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'hdfc_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'axis_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'axis_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'sbi_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'kotak_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'kotak_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'kotak_c': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'idbi_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'idbi_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'idfc_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'citi_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'citi_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'canara_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'canara_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'yes_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'baroda_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'indusind_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'indusind_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'pnb_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'union_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'indian_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'andra_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'andra_b': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'corporation_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'oriental_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
            'overseas_a': {
                'keywords': None,
                'regex_words': None,
                'table_headers': None,
                'table_dimensions': None,
            },
        }
        self.score = dict()
        self.__get_likelihood()
        self.score_map = self.__invert_dictionary(self.score)
        self.prominent_bank_list = self.__prominent_bank_list()
        self.less_prominent_bank_list = self.__less_prominent_bank_list()

    def __bank_features(self):
        all_bank = copy.deepcopy(PROMINENT_BANK_FEATURES)
        all_bank.update(LESS_PROMINENT_BANK_FEATURES)
        return all_bank

    def __invert_dictionary(self, input_dict):
        output_dict = {}
        for key in input_dict:
            value = input_dict.get(key)
            output_dict.setdefault(value, []).append(key)
        return output_dict

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
            minimum_rows_data, maximum_rows_data = self.bank_features.get(
                bank, {}).get(metric, {}).get('features', [{}, {}])
            if self.__table_dimensions_bool(minimum_rows_data['minimum_columns'], maximum_rows_data['maximum_columns']):
                return 100.0
            else:
                return 0
        normalized_score = None
        total_score = 0
        total_weight = 0
        for keyword_data in self.bank_features.get(bank, {}).get(metric, {}).get('features', []):
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
        if self.bank_features.get(bank, {}).get(metric, {}).get('features'):
            if total_weight:
                normalized_score = total_score * 100.0 / total_weight
            else:
                normalized_score = total_score
        return normalized_score

    def __get_likelihood(self):
        for bank in PROMINENT_BANK_LIST + LESS_PROMINENT_BANK_LIST:
            total_score = 0
            total_weight = 0
            for metric in ['keywords', 'regex_words', 'table_headers', 'table_dimensions']:
                self.bank_dict[bank][metric] = self.__get_score(metric, bank)
                if self.bank_dict[bank][metric] is not None:
                    total_weight += self.bank_features.get(
                        bank, {}).get(metric, {}).get('weight', 0)
                    total_score += self.bank_dict[bank][metric] * 1.0 * self.bank_features.get(
                        bank, {}).get(metric, {}).get('weight', 0)
            self.score[bank] = math.ceil(
                total_score * 1.0 / total_weight) if total_weight else 0

    def __prominent_bank_list(self):
        bank_list = []
        for bank in PROMINENT_BANK_LIST:
            print bank, self.score[bank], 11
            if self.score[bank] >= PROMINENT_BANK_MINIMUM_SCORE:
                bank_list.append(bank)
        return bank_list

    def __less_prominent_bank_list(self):
        bank_list = []
        print self.score_map
        score_list = self.score_map.keys()
        print score_list
        score_list.sort()
        score_list.reverse()
        print score_list
        for score in score_list:
            print score, 9090
            for bank in self.score_map[score]:
                print bank, 88
                if bank in LESS_PROMINENT_BANK_LIST:
                    bank_list.append(bank)
                    print bank, score, 22
        return bank_list[:LESS_PROMINENT_BANK_MAX_CONSIDERATION]
