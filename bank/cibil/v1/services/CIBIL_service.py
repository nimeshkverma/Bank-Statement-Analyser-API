import os
import re
import subprocess
import uuid
import unicodedata
import requests
import json
import time
import datetime
import csv
from copy import deepcopy
from cStringIO import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

from tabula import read_pdf
from django.conf import settings

from common.v1.services.email_service import send_mail
from CIBIL_constants import (CIBIL_ATTRIBUTES, ACCOUNT_SUMMARY_SPLITTER,
                             ACCOUNT_SUMMARY_RECTIFIER, FIRST_ACCOUNT_SUMMARY_RECTIFIER,
                             ACCOUNT_DBP_REGEX, LOAN_ACCOUNT_ENQUIRY_CLEANERS,
                             LOAN_ACCOUNT_ENQUIRY_STARTER, LOAN_ACCOUNT_ENQUIRY_FINISHER,
                             LOAN_ACCOUNT_ENQUIRY_AMOUNT_CLEANER)


class CIBILReportRawData(object):
    """Class to obtain the Raw data from the CIBIL Report"""

    def __init__(self, pdf_path, password=''):
        self.pdf_path = pdf_path
        self.password = password
        self.tabula_params = {
            'pages': 'all',
            'guess': True,
            'pandas_options': {
                'error_bad_lines': False
            },
            'password': self.password,
            'output_format': 'json',
        }
        self.pdf_json = self.__get_pdf_json()
        self.raw_table_data = self.__get_raw_table_data()
        self.pdf_text = self.__get_pdf_text()
        self.processed_pdf_text = self.__processed_pdf_text()

    def __processed_pdf_text(self):
        pdf_text_unicode = unicode(self.pdf_text, "utf-8")
        pdf_text_fixed = unicodedata.normalize(
            'NFKD', pdf_text_unicode).encode('ascii', 'ignore')
        return' '.join(pdf_text_fixed.lower().split())

    def __get_tabula_params(self, password_type='original'):
        if password_type == 'original':
            return self.tabula_params
        elif password_type == 'empty':
            tabula_params = deepcopy(self.tabula_params)
            tabula_params['password'] = ""
            return tabula_params
        elif password_type == 'capilatized':
            tabula_params = deepcopy(self.tabula_params)
            tabula_params['password'] = self.password.upper()
            return tabula_params
        else:
            return self.tabula_params

    def __get_pdf_json(self):
        try:
            return read_pdf(self.pdf_path, **self.__get_tabula_params('original'))
        except Exception as e:
            try:
                return read_pdf(self.pdf_path, **self.__get_tabula_params('empty'))
            except Exception as e:
                return read_pdf(self.pdf_path, **self.__get_tabula_params('capilatized'))

    def __get_decrypted_pdf_path(self):
        if '.pdf' in self.pdf_path:
            path_list = self.pdf_path.split('.pdf')
            return path_list[0] + '_decrypted.pdf'
        else:
            self.pdf_path + '_decrypted.pdf'

    def __pdf_decryption(self, password_type='original'):
        pdf_decryption = False
        pdf_text = ''
        pdf_path_decrypt = self.__get_decrypted_pdf_path()
        if password_type == 'capilatized':
            password = self.password.upper()
        elif password_type == 'empty':
            password = ''
        else:
            password = self.password
        try:
            decrypt_command = 'qpdf --password={password} --decrypt {pdf_path} {pdf_path_decrypt}'.format(
                password=password, pdf_path=self.pdf_path, pdf_path_decrypt=pdf_path_decrypt)
            decrypt_command_output = subprocess.call(
                decrypt_command, shell=True)
            if decrypt_command_output == 0:
                pdf_decryption = True
        except Exception as e:
            pass
        return pdf_decryption

    def __get_pdf_text(self):
        for password_type in ['original', 'empty', 'capilatized']:
            pdf_decryption = self.__pdf_decryption(password_type)
            if pdf_decryption:
                break
        pdf_path_decrypt = self.__get_decrypted_pdf_path()
        file_clean_command = 'rm {pdf_path_decrypt}'.format(
            pdf_path_decrypt=pdf_path_decrypt)
        pdf_text = self.__pdf_to_text(pdf_path_decrypt)
        subprocess.call(file_clean_command, shell=True)
        return pdf_text

    def __get_raw_table_data(self):
        rows_data_list = []
        for data_dict in self.pdf_json:
            for rows_data in data_dict.get('data', []):
                row_data_list = []
                for row_data in rows_data:
                    if row_data.get('text'):
                        row_data_list.append(row_data['text'])
                if row_data_list:
                    rows_data_list.append(row_data_list)
        return rows_data_list

    def __pdf_to_text(self, pdf_path_decrypt):
        pagenums = set()
        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)

        infile = file(pdf_path_decrypt, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close
        return text


class CIBILReport(object):

    def __init__(self, cibil_report_path):
        self.cibil_report_path = cibil_report_path
        self.cibil_report_raw = CIBILReportRawData(self.cibil_report_path)
        self.account_text_list = self.__get_account_text_list()
        self.enquiry_text = self.__get_cleaned_enquiry_text()
        self.data = {
            "cibil_score_data": {},
            "loan_accounts_summary_data": {},
            "loan_enquiry_summary_data": {},
            "loan_accounts_data": [],
            "loan_accounts_dpd_data": [],
            "loan_accounts_enquiry_data": [],
        }
        self.__set_data()

    def __get_amount(self, amount_input):
        all_amount_list = []
        all_string_amount_list = re.findall(r'[0-9,\,]+', amount_input)
        for string_amount in all_string_amount_list:
            try:
                comma_remove_input_string = string_amount.replace(',', '')
                all_amount_list.append(int(float(comma_remove_input_string)))
            except Exception as e:
                pass
        return all_amount_list[0] if all_amount_list else None

    def __get_date(self, date_input):
        return date_input

    def __get_attribute_value_from_regex(self, attribute_info, text_corpus=None):
        text_corpus = self.cibil_report_raw.processed_pdf_text if not text_corpus else text_corpus
        attribute_value = None
        regex_string = attribute_info.get('regex')
        attribute_type = attribute_info.get('attribute_type')
        attribute_value_patterns = re.findall(regex_string, text_corpus)
        try:
            if attribute_value_patterns:
                if attribute_type == 'amount':
                    attribute_value = self.__get_amount(
                        attribute_value_patterns[0])
                elif attribute_type == 'date':
                    attribute_value = self.__get_date(
                        attribute_value_patterns[0])
                else:
                    attribute_value = attribute_value_patterns[0]
        except Exception as e:
            pass
        return attribute_value

    def __get_attribute_data(self, attribute_info, text_corpus=None):
        text_corpus = self.cibil_report_raw.processed_pdf_text if not text_corpus else text_corpus
        value = self.__get_attribute_value_from_regex(
            attribute_info, text_corpus)
        return value if value not in [None, '', ' '] else 'Not Found'

    def __set_score_loan_account_summary_enquiry_data(self):
        for attribute_category in ['cibil_score_data', 'loan_accounts_summary_data', 'loan_enquiry_summary_data']:
            for attribute_name, attribute_info in CIBIL_ATTRIBUTES.get(attribute_category, {}).get('attribute_data', {}).iteritems():
                self.data[attribute_category][
                    attribute_name] = self.__get_attribute_data(attribute_info)

    def __get_account_text_list(self):
        account_text_list = re.split(
            ACCOUNT_SUMMARY_SPLITTER, self.cibil_report_raw.processed_pdf_text)
        account_text_list[0] = account_text_list[
            0].split(FIRST_ACCOUNT_SUMMARY_RECTIFIER)[-1]
        for index in xrange(1, len(account_text_list) - 1):
            account_rectifier_list = re.findall(
                ACCOUNT_SUMMARY_RECTIFIER, account_text_list[index])
            if account_rectifier_list:
                account_text_list[
                    index - 1] = account_text_list[index - 1] + account_rectifier_list[0]
                account_text_list[index] = account_text_list[
                    index].split(account_rectifier_list[0])[-1]
        account_text_list[-2] = account_text_list[-2] + \
            account_text_list[-1].split(LOAN_ACCOUNT_ENQUIRY_STARTER)[0]
        return account_text_list[:-1]

    def __set_loan_accounts_data(self):
        account_text_list = self.account_text_list[:-1]
        for account_text in account_text_list:
            account_data = {}
            for attribute_name, attribute_info in CIBIL_ATTRIBUTES.get('loan_accounts_data', {}).get('attribute_data', {}).iteritems():
                account_data[attribute_name] = self.__get_attribute_data(
                    attribute_info, account_text)
            self.data['loan_accounts_data'].append(account_data)

    def __set_loan_accounts_dpd_data(self):
        account_text_list = self.account_text_list
        for account_text in account_text_list:
            account_text_dbp_data = {}
            dpd_text_list = re.findall(ACCOUNT_DBP_REGEX, account_text)
            for dpd_text in dpd_text_list:
                account_text_dbp_data[dpd_text] = {}
                for attribute_name, attribute_info in CIBIL_ATTRIBUTES.get('loan_accounts_dpd_data', {}).get('attribute_data', {}).iteritems():
                    account_text_dbp_data[dpd_text][
                        attribute_name] = self.__get_attribute_data(attribute_info, dpd_text)
            self.data['loan_accounts_dpd_data'].append(account_text_dbp_data)

    def __get_cleaned_enquiry_text(self):
        enquiry_text = self.cibil_report_raw.processed_pdf_text.split(
            LOAN_ACCOUNT_ENQUIRY_STARTER)[-1].split(LOAN_ACCOUNT_ENQUIRY_FINISHER)[0]
        for cleaner in LOAN_ACCOUNT_ENQUIRY_CLEANERS.values():
            enquiry_text = re.sub(cleaner, '', enquiry_text)
        return enquiry_text

    def __enquiry_attribute_values(self, attribute_name):
        enquiry_attribute_values = []
        attribute_regex = CIBIL_ATTRIBUTES.get('loan_accounts_enquiry_data', {}).get(
            'attribute_data', {}).get(attribute_name, {}).get('regex')
        if attribute_name == 'enquiry_amount':
            enquiry_attribute_values = re.findall(attribute_regex, re.sub(
                LOAN_ACCOUNT_ENQUIRY_AMOUNT_CLEANER, '', self.enquiry_text))
        else:
            enquiry_attribute_values = re.findall(
                attribute_regex, self.enquiry_text)
        return enquiry_attribute_values

    def __set_loan_accounts_enquiry_data(self):
        enquiry_data = dict()
        for attribute_name in CIBIL_ATTRIBUTES.get('loan_accounts_enquiry_data', {}).get('attribute_list', []):
            enquiry_data[attribute_name] = self.__enquiry_attribute_values(
                attribute_name)
        minimum_size = min([len(attribute_data)
                            for attribute_data in enquiry_data.values()])
        for index in xrange(0, minimum_size):
            data = {}
            for attribute_name in CIBIL_ATTRIBUTES.get('loan_accounts_enquiry_data', {}).get('attribute_list', []):
                data[attribute_name] = enquiry_data[attribute_name][index]
            self.data['loan_accounts_enquiry_data'].append(data)

    def __set_data(self):
        self.__set_score_loan_account_summary_enquiry_data()
        self.__set_loan_accounts_data()
        self.__set_loan_accounts_dpd_data()
        self.__set_loan_accounts_enquiry_data()


class CIBILReportTool(object):

    def __init__(self, cibil_report_path, report_unique_identifier):
        self.cibil_report_path = cibil_report_path
        self.report_unique_identifier = report_unique_identifier
        self.template = 'cibil/v1/cibil_report_analysis_email.html'
        self.pwd = self.__pwd()
        self.cibil_report = self.__get_cibil_report()
        self.cibil_data = self.__get_cibil_data()
        self.__clean_up()

    def __clean_up(self):
        subprocess.call('rm {cibil_report_path}'.format(
            cibil_report_path=self.cibil_report_path), shell=True)

    def __get_cibil_report(self):
        cibil_report = None
        try:
            cibil_report = CIBILReport(
                self.cibil_report_path)
        except Exception as e:
            print e
            pass
        return cibil_report

    def __pwd(self):
        pwd = ''
        try:
            subprocess_pwd = subprocess.check_output('pwd')
            pwd = subprocess_pwd.split('\n')[0] + '/cibil/v1/services'
        except Exception as e:
            pass
        return pwd

    def __get_cibil_data(self):
        return self.cibil_report.data

    def __create_cibil_statement_csv(self):
        csv_name = "{pwd}/{uuid}.csv".format(pwd=self.pwd,
                                             uuid=uuid.uuid4().hex)
        with open(csv_name, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for attribute_category in ['cibil_score_data', 'loan_accounts_summary_data', 'loan_enquiry_summary_data']:
                writer.writerow([''])
                writer.writerow([CIBIL_ATTRIBUTES.get(
                    attribute_category, {}).get('info')])
                writer.writerow(
                    [' ', 'Attribute Name', 'Value', 'Explanation'])
                for attribute_name in CIBIL_ATTRIBUTES.get(attribute_category, {}).get('attribute_list', []):
                    row_data = deepcopy(CIBIL_ATTRIBUTES.get(attribute_category, {}).get(
                        'attribute_data', {}).get(attribute_name, {}))
                    row_data['value'] = self.cibil_data.get(
                        attribute_category, {}).get(attribute_name)
                    writer.writerow([' ', row_data.get('name', 'Not Found'), str(row_data.get(
                        'value', 'Not Found')).upper(), row_data.get('explanation', ' '), ])
            writer.writerow([''])
            writer.writerow([CIBIL_ATTRIBUTES.get(
                'loan_accounts_data', {}).get('info')])
            account_no = 1
            for account_data in self.cibil_data.get('loan_accounts_data', []):
                writer.writerow(
                    ['', 'Account No, {account_no}'.format(account_no=account_no)])
                for attribute_name in CIBIL_ATTRIBUTES.get('loan_accounts_data', {}).get('attribute_list', []):
                    row_data = deepcopy(CIBIL_ATTRIBUTES.get('loan_accounts_data', {}).get(
                        'attribute_data', {}).get(attribute_name, {}))
                    row_data['value'] = account_data.get(attribute_name)
                    writer.writerow([' ', row_data.get('name', 'Not Found'), str(row_data.get(
                        'value', 'Not Found')).upper(), row_data.get('explanation', ' '), ])
                account_no += 1

            account_no = 1
            for account_data in self.cibil_data.get('loan_accounts_dpd_data', []):
                writer.writerow(
                    ['DPD Data Account wise'])
                writer.writerow(
                    ['', 'Account No, {account_no}'.format(account_no=account_no)])
                writer.writerow(
                    ['', '', 'DPD Whole Text', 'DPD/Code', 'Month', 'Year'])
                for dpd_text, dpd_data in account_data.iteritems():
                    writer.writerow(
                        ['', '', dpd_text, dpd_data.get('dpd', 'Not Found'), dpd_data.get('dpd_month',  'Not Found'), dpd_data.get('dpd_year',  'Not Found')])
                account_no += 1

            account_no = 1
            for enquiry_data in self.cibil_data.get('loan_accounts_enquiry_data', []):
                writer.writerow(
                    ['Loan Enquiry Account Wise'])
                writer.writerow(
                    ['', 'Account No', 'Date of Enquiry', 'Enquiry Amount', 'Purpose of Enquiry'])
                writer.writerow(['', '{account_no}'.format(account_no=account_no), enquiry_data[
                                'enquiry_date'],  enquiry_data['enquiry_amount'], enquiry_data['enquiry_purpose']])
                account_no += 1
        return csv_name

    def __remove_file(self, file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)

    def send_cibil_analysis_email(self):
        csvfile = self.__create_cibil_statement_csv()
        email_data = {
            'data': {
                'report_unique_identifier': self.report_unique_identifier,
            }
        }
        email_details = {
            'data': email_data,
            'subject': "CIBIL Report Analysis for :{report_unique_identifier} ".format(report_unique_identifier=self.report_unique_identifier),
            'body': "Empty",
            'sender_email_id': settings.SERVER_EMAIL,
            'reciever_email_ids': settings.RECIEVER_EMAILS,
        }
        send_mail(email_details, self.template, [csvfile])
        self.__remove_file(csvfile)
