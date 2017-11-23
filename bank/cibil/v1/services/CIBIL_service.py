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
                             LOAN_ACCOUNT_ENQUIRY_AMOUNT_CLEANER,
                             ACCOUNT_SUMMARY_STARTER, ADDRESS_DATA_SPLITTER)


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
        pdf_text_unicode = unicode(self.pdf_text, 'utf-8')
        pdf_text_fixed = unicodedata.normalize(
            'NFKD', pdf_text_unicode).encode('ascii', 'ignore')
        return' '.join(pdf_text_fixed.lower().split())

    def __get_tabula_params(self, password_type='original'):
        if password_type == 'original':
            return self.tabula_params
        elif password_type == 'empty':
            tabula_params = deepcopy(self.tabula_params)
            tabula_params['password'] = ''
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
        self.pre_summary_text = self.__get_pre_summary_text()
        self.data = {
            'cibil_score_data': {},
            'cibil_kyc_data': {},
            'cibil_contact_data': {},
            'loan_accounts_summary_data': {},
            'loan_enquiry_summary_data': {},
            'loan_accounts_data': [],
            'loan_accounts_dpd_data': [],
            'loan_accounts_enquiry_data': [],
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

    def __set_cibil_score_kyc_data(self):
        for attribute_category in ['cibil_score_data', 'cibil_kyc_data']:
            for attribute_name, attribute_info in CIBIL_ATTRIBUTES.get(attribute_category, {}).get('attribute_data', {}).iteritems():
                self.data[attribute_category][
                    attribute_name] = self.__get_attribute_data(attribute_info, self.pre_summary_text)

    def __set_telephone_email_data(self):
        telephone_data = []
        email_data = []
        telephone_email_data_text_list = re.findall(CIBIL_ATTRIBUTES.get('cibil_contact_data', {}).get(
            'attribute_data', {}).get('telephone_email_data', {}).get('regex', ''), self.pre_summary_text)
        if telephone_email_data_text_list:
            telephone_type_list = re.findall(CIBIL_ATTRIBUTES.get('cibil_contact_data', {}).get(
                'attribute_data', {}).get('telephone_type', {}).get('regex', ''), telephone_email_data_text_list[0])
            telephone_number_list = re.findall(CIBIL_ATTRIBUTES.get('cibil_contact_data', {}).get(
                'attribute_data', {}).get('telephone_number', {}).get('regex', ''), telephone_email_data_text_list[0])
            email_data = re.findall(CIBIL_ATTRIBUTES.get('cibil_contact_data', {}).get(
                'attribute_data', {}).get('email', {}).get('regex', ''), telephone_email_data_text_list[0])
            for index in xrange(0, min(len(telephone_type_list), len(telephone_number_list))):
                telephone_data.append({
                    'telephone_type': telephone_type_list[index],
                    'telephone_number': telephone_number_list[index],
                })
        self.data['cibil_contact_data']['telephone_data'] = telephone_data
        self.data['cibil_contact_data']['email_data'] = [
            {'email': email} for email in email_data]

    def __set_address_data(self):
        address_data_list = []
        address_data_text_corpus_list = re.findall(CIBIL_ATTRIBUTES.get('cibil_contact_data', {}).get(
            'attribute_data', {}).get('address_data', {}).get('regex', ''), self.pre_summary_text)
        if address_data_text_corpus_list:
            address_data_text_list = re.split(
                ADDRESS_DATA_SPLITTER, address_data_text_corpus_list[0])
            for address_data_text in address_data_text_list:
                address_data = {}
                address = deepcopy(address_data_text)
                for attribute_name in ['address_category', 'address_code', 'address_report_date']:
                    attribute_info = CIBIL_ATTRIBUTES.get(
                        'cibil_contact_data', {}).get('attribute_data', {}).get(attribute_name, {})
                    address_data[attribute_name] = self.__get_attribute_data(
                        attribute_info, address_data_text)
                    address = re.sub(attribute_info.get(
                        'regex', ''), '', address)
                address_data['address'] = address
                address_data_list.append(address_data)
        self.data['cibil_contact_data']['address_data'] = address_data_list

    def __set_cibil_contact_data(self):
        self.__set_telephone_email_data()
        self.__set_address_data()

    def __set_loan_account_summary_enquiry_data(self):
        for attribute_category in ['loan_accounts_summary_data', 'loan_enquiry_summary_data']:
            for attribute_name, attribute_info in CIBIL_ATTRIBUTES.get(attribute_category, {}).get('attribute_data', {}).iteritems():
                self.data[attribute_category][
                    attribute_name] = self.__get_attribute_data(attribute_info)

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

    def __get_pre_summary_text(self):
        summary_text = ''
        summary_text_list = self.cibil_report_raw.processed_pdf_text.split(
            ACCOUNT_SUMMARY_STARTER)
        if summary_text_list:
            summary_text = re.sub('\(cid:\d{1,4}\)', '', summary_text_list[0])
        return summary_text

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
        self.__set_cibil_score_kyc_data()
        self.__set_loan_account_summary_enquiry_data()
        self.__set_cibil_contact_data()
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
            for attribute_category in ['cibil_score_data', 'cibil_kyc_data', 'loan_accounts_summary_data', 'loan_enquiry_summary_data']:
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

            writer.writerow(['DPD Data Account wise'])
            account_no = 1
            for account_data in self.cibil_data.get('loan_accounts_dpd_data', []):
                writer.writerow(
                    ['', 'Account No, {account_no}'.format(account_no=account_no)])
                writer.writerow(
                    ['', '', 'DPD Whole Text', 'DPD/Code', 'Month', 'Year'])
                for dpd_text, dpd_data in account_data.iteritems():
                    writer.writerow(
                        ['', '', dpd_text, dpd_data.get('dpd', 'Not Found'), dpd_data.get('dpd_month',  'Not Found'), dpd_data.get('dpd_year',  'Not Found')])
                account_no += 1

            writer.writerow(['Loan Enquiry Account Wise'])
            account_no = 1
            writer.writerow(['Loan Enquiry Account Wise'])
            writer.writerow(['', 'Account No', 'Date of Enquiry',
                             'Enquiry Amount', 'Purpose of Enquiry'])
            for enquiry_data in self.cibil_data.get('loan_accounts_enquiry_data', []):
                writer.writerow(['', '{account_no}'.format(account_no=account_no), enquiry_data[
                                'enquiry_date'],  enquiry_data['enquiry_amount'], enquiry_data['enquiry_purpose']])
                account_no += 1

            writer.writerow(['Contact Data'])
            writer.writerow(['', 'Address Info'])
            writer.writerow(['', '', 'Sr No', 'Address Code',
                             'Address Category', 'Address Reported Date', 'Address'])
            sr_no = 1
            for address_data in self.cibil_data.get('cibil_contact_data', {}).get('address_data', []):
                writer.writerow(['', '', sr_no, address_data.get('address_code', 'Not Found'), address_data.get(
                    'address_category', 'Not Found'), address_data.get('address_report_date', 'Not Found'), address_data.get('address', 'Not Found')])
                sr_no += 1

            writer.writerow(['', 'Email Info'])
            writer.writerow(['', '', 'Sr No', 'Email'])
            sr_no = 1
            for email_data in self.cibil_data.get('cibil_contact_data', {}).get('email_data', []):
                writer.writerow(
                    ['', '', sr_no, email_data.get('email', 'Not Found')])
                sr_no += 1

            writer.writerow(['', 'Telephone Info'])
            writer.writerow(
                ['', '', 'Sr No', 'Telephone Type', 'Telephone No'])
            sr_no = 1
            for telephone_data in self.cibil_data.get('cibil_contact_data', {}).get('telephone_data', []):
                writer.writerow(['', '', sr_no, telephone_data.get(
                    'telephone_type', 'Not Found'), telephone_data.get('telephone_number', 'Not Found')])
                sr_no += 1

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


class CIBILAnalysisTool(object):

    def __init__(self, cibil_data, report_unique_identifier):
        self.cibil_data = cibil_data
        self.report_unique_identifier = report_unique_identifier
        self.cibil_analysed_data = {
            'loan_accounts_summary_data': {},
            'loan_enquiry_summary_data': {},
            'loan_accounts_enquiry_data': {},
            'loan_accounts_data': {},
        }
        self.__set_cibil_analysed_data()
        self.template = 'cibil/v1/cibil_report_analysed_data.html'
        self.pwd = self.__pwd()

    def __get_amount(self, number):
        if type(number) == str:
            comma_remove_number = number.replace(',', '')
            try:
                return int(float(comma_remove_number))
            except Exception as e:
                return 0
        else:
            return number

    def __set_loan_accounts_summary_data(self):
        source_data = self.cibil_data['loan_accounts_summary_data']

        def __existing_emi_estimate(source_data):
            return self.__get_amount(source_data.get('total_amount_current', 0)) * 0.03

        def __credit_history_years(source_data):
            credit_history_years = 0
            try:
                credit_history_years = datetime.datetime.now().year - datetime.datetime.strptime(
                    source_data.get('credit_history_since_date', ''), '%d-%m-%Y').year
            except Exception as e:
                pass
            return credit_history_years

        def __overdue_vs_current_liability(source_data):
            total_amount_current = self.__get_amount(source_data.get(
                'total_amount_current', 1)) if source_data.get('total_amount_current', 1) else 1
            return self.__get_amount(source_data.get('total_amount_overdue', 0)) * 1.0 / total_amount_current

        def __debt_reduction(source_data):
            total_amount_sanctioned = self.__get_amount(source_data.get(
                'total_amount_sanctioned', 1)) if source_data.get('total_amount_sanctioned', 1) else 1
            return 1 - (self.__get_amount(source_data.get('total_amount_current', 0)) * 1.0 / total_amount_sanctioned)

        self.cibil_analysed_data['loan_accounts_summary_data'] = {
            'existing_emi_estimate': __existing_emi_estimate(source_data),
            'credit_history_years': __credit_history_years(source_data),
            'overdue_vs_current_liability': __overdue_vs_current_liability(source_data),
            'debt_reduction': __debt_reduction(source_data),
        }

    def __set_loan_enquiry_summary_data(self):
        source_data = self.cibil_data['loan_enquiry_summary_data']

        def __average_enquiries(source_data):
            return self.__get_amount(source_data.get('total_loan_enquiries_12_months')) * 1.0 / 12
        self.cibil_analysed_data['loan_enquiry_summary_data'] = {
            'average_enquiries': __average_enquiries(source_data)
        }

    def __set_loan_accounts_enquiry_data(self):
        source_data = self.cibil_data['loan_accounts_enquiry_data']

        def __datewise_all_data_dict(source_data):
            datewise_all_data_dict = {}
            for data_dict in source_data:
                try:
                    enquiry_date = datetime.datetime.strptime(
                        data_dict.get('enquiry_date', ''), '%d-%m-%Y')
                    if datewise_all_data_dict.get(enquiry_date):
                        datewise_all_data_dict[enquiry_date].apend(data_dict)
                    else:
                        datewise_all_data_dict[enquiry_date] = [data_dict]
                except Exception as e:
                    pass
            return datewise_all_data_dict

        def __datewise_all_data_list(datewise_all_data_dict):
            datewise_all_data_dict_key = datewise_all_data_dict.keys()
            datewise_all_data_dict_key.sort()
            datewise_all_data_list = []
            for key in datewise_all_data_dict_key:
                datewise_all_data_list = datewise_all_data_list + \
                    datewise_all_data_dict[key]
            return datewise_all_data_list
        datewise_all_data_dict = __datewise_all_data_dict(source_data)
        datewise_all_data_list = __datewise_all_data_list(
            datewise_all_data_dict)

        def __nth_enquiry_date(n, datewise_all_data_list):
            nth_enquiry_date = ''
            if len(datewise_all_data_list) >= n:
                nth_enquiry_date = datewise_all_data_list[
                    n - 1]['enquiry_date']
            return nth_enquiry_date

        def __nth_enquiry_average_amount(n, datewise_all_data_list, enquiry_type_list=None):
            nth_enquiry_amount_sum = 0
            counter = 0
            for index in xrange(0, len(datewise_all_data_list)):
                if not enquiry_type_list:
                    counter += 1
                    nth_enquiry_amount_sum += self.__get_amount(
                        datewise_all_data_list[index]['enquiry_amount'])
                else:
                    if datewise_all_data_list[index]['enquiry_purpose'] in enquiry_type_list:
                        counter += 1
                        nth_enquiry_amount_sum += self.__get_amount(
                            datewise_all_data_list[index]['enquiry_amount'])
                if counter == n:
                    break
            return nth_enquiry_amount_sum * 1.0 / n

        self.cibil_analysed_data['loan_accounts_enquiry_data'] = {
            'enquiry_date_1th': __nth_enquiry_date(1, datewise_all_data_list),
            'enquiry_date_3th': __nth_enquiry_date(3, datewise_all_data_list),
            'enquiry_date_5th': __nth_enquiry_date(5, datewise_all_data_list),
            'enquiry_date_10th': __nth_enquiry_date(10, datewise_all_data_list),
            'average_enquiry_amount_all_5': __nth_enquiry_average_amount(5, datewise_all_data_list),
            'average_enquiry_amount_all_10': __nth_enquiry_average_amount(10, datewise_all_data_list),
            'average_enquiry_amount_all_5_personal': __nth_enquiry_average_amount(5, datewise_all_data_list, ['personal loan']),
            'average_enquiry_amount_all_10_personal': __nth_enquiry_average_amount(10, datewise_all_data_list, ['personal loan']),
            'average_enquiry_amount_all_5_personal_and_creditcard': __nth_enquiry_average_amount(5, datewise_all_data_list, ['personal loan', 'credit card']),
            'average_enquiry_amount_all_10_personal_and_creditcard': __nth_enquiry_average_amount(10, datewise_all_data_list, ['personal loan', 'credit card']),
        }

    def __set_loan_accounts_data(self):
        source_data = self.cibil_data['loan_accounts_data']

        def __write_offs(source_data, days=None, loan_type=None):
            write_offs = 0
            for data_dict in source_data:
                for date_key in ['account_close_date', 'account_last_reported_date']:
                    try:
                        date = datetime.datetime.strptime(
                            data_dict.get(date_key, ''), '%d-%m-%Y')
                        within_period = False
                        if days == None or (datetime.datetime.now() - date).days <= days:
                            within_period = True
                        if loan_type == None and within_period and data_dict.get('write_off', '') in ['settled', 'written']:
                            write_offs += 1
                        elif data_dict.get('account_type', '') in loan_type and within_period and data_dict.get('write_off', '') in ['settled', 'written']:
                            write_off += 1
                        else:
                            pass
                        break
                    except Exception as e:
                        pass
            return write_offs

        self.cibil_analysed_data['loan_accounts_data'] = {
            'write_offs_all_time': __write_offs(source_data,),
            'write_offs_6_months': __write_offs(source_data, 183),
            'write_offs_12_months': __write_offs(source_data, 365),
            'write_offs_24_months': __write_offs(source_data, 730),
            'write_offs_36_months': __write_offs(source_data, 1095),
            'write_offs_all_time_personal': __write_offs(source_data, loan_type=['personal loan']),
            'write_offs_6_months_personal': __write_offs(source_data, 183, ['personal loan']),
            'write_offs_12_months_personal': __write_offs(source_data, 365, ['personal loan']),
            'write_offs_24_months_personal': __write_offs(source_data, 730, ['personal loan']),
            'write_offs_36_months_personal': __write_offs(source_data, 1095, ['personal loan']),
        }

    def __set_cibil_analysed_data(self):
        self.__set_loan_accounts_summary_data()
        self.__set_loan_enquiry_summary_data()
        self.__set_loan_accounts_enquiry_data()
        self.__set_loan_accounts_data()

    def __pwd(self):
        pwd = ''
        try:
            subprocess_pwd = subprocess.check_output('pwd')
            pwd = subprocess_pwd.split('\n')[0] + '/cibil/v1/services'
        except Exception as e:
            pass
        return pwd

    def __create_cibil_statement_csv(self):
        csv_name = "{pwd}/{uuid}.csv".format(pwd=self.pwd,
                                             uuid=uuid.uuid4().hex)
        with open(csv_name, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Section', 'Attribute', 'Value'])
            for attribute_category in ['loan_accounts_summary_data', 'loan_enquiry_summary_data',
                                       'loan_accounts_enquiry_data', 'loan_accounts_data']:
                writer.writerow([attribute_category])
                for key, value in self.cibil_analysed_data.get(attribute_category, {}).iteritems():
                    writer.writerow(['', key, value])

        return csv_name

    def __remove_file(self, file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)

    def send_cibil_analysed_data_email(self):
        csvfile = self.__create_cibil_statement_csv()
        email_data = {
            'data': {
                'report_unique_identifier': self.report_unique_identifier,
            }
        }
        email_details = {
            'data': email_data,
            'subject': "CIBIL Report Analysed Data for :{report_unique_identifier} ".format(report_unique_identifier=self.report_unique_identifier),
            'body': "Empty",
            'sender_email_id': settings.SERVER_EMAIL,
            'reciever_email_ids': settings.RECIEVER_EMAILS,
        }
        send_mail(email_details, self.template, [csvfile])
        self.__remove_file(csvfile)


# class CIBILTablePopulation(object):

#     def __init__(self, customer_id, cibil_data):
#         self.customer_id = customer_id
#         self.cibil_data = cibil_data
#         self.__cibil_loan_accounts_summary_query()
#         self.__cibil_loan_accounts_enquiry_query()
#         self.__cibil_loan_accounts_enquiry_summary_query()
#         self.__cibil_contact_address_query()
#         self.__cibil_contact_query()
#         self.__cibil_data_query()

#     def __clean_data_dict(self, data_dict):
#         for key, value in data_dict.iteritems():
#             data_dict[key] = '-9999' if value in [
#                 None, '', ' ', 'Not Found'] else value
#         return data_dict

#     def __change_date_format(self, data_dict, key_list):
#         for key in key_list:
#             try:
#                 data_dict[key] = "'" + datetime.datetime.strptime(
#                     data_dict[key], '%d-%m-%Y').strftime('%Y-%m-%d') + "'"
#             except Exception as e:
#                 data_dict[key] = 'null'
#         return data_dict

#     def __clean_amount(self, data_dict, key_list):
#         for key in key_list:
#             for to_be_replaced in [' ', ',']:
#                 data_dict[key] = data_dict[key].replace(to_be_replaced, '')
#         return data_dict

#     def __cibil_loan_accounts_summary_query(self):
#         data = {
#             'customer_id': self.customer_id
#         }
#         data.update(self.__clean_data_dict(
#             self.cibil_data['loan_accounts_summary_data']))
#         data = self.__change_date_format(
#             data, ['credit_history_since_date', 'last_reporting_date'])
#         sql_query = """ INSERT INTO cibil_loan_accounts_summary
#                         (customer_id, total_loan_accounts, total_amount_sanctioned,
#                         total_amount_overdue,total_loan_accounts_overdue,total_loan_accounts_zero_balance,
#                         total_amount_current, credit_history_since_date,last_reporting_date,
#                          created_at, updated_at, is_active)
#                         VALUES ({customer_id}, {total_loan_accounts}, {total_amount_sanctioned},
#                         {total_amount_overdue},{total_loan_accounts_overdue}, {total_loan_accounts_zero_balance},
#                         {total_amount_current}, {credit_history_since_date}, {last_reporting_date},
#                         ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'),
#                         ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'), TRUE);""".format(**data)
#         print sql_query
#         return sql_query

#     def __cibil_loan_accounts_enquiry_query(self):
#         sql_query = """
#             INSERT INTO cibil_loan_accounts_enquiry
#             (customer_id, amount, date, purpose,
#             created_at, updated_at, is_active)
#             VALUES
#         """
#         for data_dict in self.cibil_data['loan_accounts_enquiry_data']:
#             data = self.__clean_data_dict(data_dict)
#             data = self.__change_date_format(data, ['enquiry_date'])
#             data = self.__clean_amount(data, ['enquiry_amount'])
#             data.update({'customer_id': self.customer_id})
#             sql_query += """({customer_id}, {enquiry_amount}, {enquiry_date},'{enquiry_purpose}',
#                         ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'),
#                         ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'), TRUE),""".format(**data)
#         sql_query = sql_query[:-1]
#         sql_query += " ; "
#         print sql_query
#         return sql_query

#     def __cibil_loan_accounts_enquiry_summary_query(self):
#         data = {
#             'customer_id': self.customer_id
#         }
#         data.update(self.__clean_data_dict(
#             self.cibil_data['loan_enquiry_summary_data']))
#         data = self.__change_date_format(
#             data, ['last_date_of_enquiry'])
#         sql_query = """
#             INSERT INTO cibil_loan_accounts_enquiry_summary
#             (customer_id, total_enquiries, total_enquiries_1,
#             total_enquiries_12,total_enquiries_24, last_date_of_enquiry,
#             created_at, updated_at, is_active)
#             VALUES ({customer_id}, {total_loan_enquiries}, {total_loan_enquiries_30_days},
#             {total_loan_enquiries_12_months},{total_loan_enquiries_24_months}, {last_date_of_enquiry},
#             ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'),
#             ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'), TRUE);""".format(**data)
#         print sql_query
#         return sql_query

#     def __cibil_contact_address_query(self):
#         sql_query = """
#             INSERT INTO cibil_contact_address
#             (customer_id, code, category, address, report_date,
#             created_at, updated_at, is_active)
#             VALUES
#         """
#         for data_dict in self.cibil_data['cibil_contact_data']['address_data']:
#             data = self.__clean_data_dict(data_dict)
#             data = self.__change_date_format(data, ['address_report_date'])
#             data.update({'customer_id': self.customer_id})
#             sql_query += """({customer_id}, '{address_code}', '{address_category}', '{address}',{address_report_date},
#                         ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'),
#                         ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'), TRUE),""".format(**data)
#         sql_query = sql_query[:-1]
#         sql_query += " ; "
#         print sql_query
#         return sql_query

#     def __cibil_contact_query(self):
#         sql_query = """
#             INSERT INTO cibil_contact
#             (customer_id, contact, contact_type, contact_value,
#             created_at, updated_at, is_active)
#             VALUES
#         """
#         for data_dict in self.cibil_data['cibil_contact_data']['telephone_data']:
#             data = self.__clean_data_dict(data_dict)
#             data.update({
#                 'customer_id': self.customer_id,
#                 'contact': 'Telephone'
#             })
#             sql_query += """({customer_id}, '{contact}', '{telephone_type}', '{telephone_number}',
#                         ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'),
#                         ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'), TRUE),""".format(**data)
#         for data_dict in self.cibil_data['cibil_contact_data']['email_data']:
#             data = self.__clean_data_dict(data_dict)
#             data.update({
#                 'customer_id': self.customer_id,
#                 'contact': 'Email'
#             })
#             sql_query += """({customer_id}, '{contact}', null, '{email}',
#                         ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'),
#                         ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'), TRUE),""".format(**data)
#         sql_query = sql_query[:-1]
#         sql_query += " ; "
#         print sql_query
#         return sql_query

#     def __cibil_data_query(self):
#         data = {
#             'customer_id': self.customer_id,
#             'name': self.cibil_data['cibil_kyc_data'].get('name'),
#             'gender': self.cibil_data['cibil_kyc_data'].get('gender'),
#             'birth_date': self.cibil_data['cibil_kyc_data'].get('birth_date'),
#         }
#         data.update(self.cibil_data['cibil_score_data'])
#         data = self.__clean_data_dict(data)
#         data = self.__change_date_format(data, ['birth_date'])
#         sql_query = """
#             INSERT INTO cibil_data
#             (customer_id, name, gender,
#             birth_date, score, comments,
#             created_at, updated_at, is_active)
#             VALUES ({customer_id}, '{name}', '{gender}',
#             {birth_date},{cibil_score}, '{cibil_comments}',
#             ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'),
#             ( select now()::timestamp with time zone at time zone 'Asia/Kolkata'), TRUE);""".format(**data)
#         print sql_query
#         # return sql_query
