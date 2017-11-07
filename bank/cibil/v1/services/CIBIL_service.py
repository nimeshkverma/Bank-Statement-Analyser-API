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
from CIBIL_constants import CIBIL_ATTRIBUTE_DATA, CIBIL_ATTRIBUTE_LIST, CIBIL_ATTRIBUTES, CIBIL_ATTRIBUTES_CATEGORY_LIST


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
        self.attribute_list = CIBIL_ATTRIBUTE_LIST
        self.data = {
            "cibil_score_data": {},
            "loan_accounts_summary_data": {},
            "loan_enquiry_data": {},
            "loan_accounts_data": [],
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

    def __get_attribute_data(self, attribute_info):
        value = self.__get_attribute_value_from_regex(attribute_info)
        attribute_data = {
            'name': attribute_info.get('name', 'Not Found'),
            'value': value if value else 'Not Found',
            'explanation': attribute_info.get('explanation', 'Not Found'),
        }
        return attribute_data

    def __set_score_loan_account_summary_enquiry_data(self):
        for attribute_category in ['cibil_score_data', 'loan_accounts_summary_data', 'loan_enquiry_data']:
            for attribute_name, attribute_info in CIBIL_ATTRIBUTES.get(attribute_category, {}).get('attribute_data', {}).iteritems():
                self.data[attribute_category][
                    attribute_name] = self.__get_attribute_data(attribute_info)

    def __set_loan_accounts_data(self):
        pass

    def __set_data(self):
        self.__set_score_loan_account_summary_enquiry_data()
        self.__set_loan_accounts_data()

    # def __get_attribute_value_from_cibil_regex(self, attribute):
    #     attribute_value = None
    #     regex_string = CIBIL_ATTRIBUTE_DATA.get(
    #         attribute, {}).get('regex')
    #     attribute_type = CIBIL_ATTRIBUTE_DATA.get(
    #         attribute, {}).get('attribute_type')
    #     attribute_value_patterns = re.findall(
    #         regex_string, self.cibil_report_raw.processed_pdf_text)
    #     try:
    #         if attribute_value_patterns:
    #             if attribute_type == 'amount':
    #                 attribute_value = self.__get_amount(
    #                     attribute_value_patterns[0])
    #             elif attribute_type == 'date':
    #                 attribute_value = self.__get_date(
    #                     attribute_value_patterns[0])
    #             else:
    #                 attribute_value = attribute_value_patterns[0]
    #     except Exception as e:
    #         pass
    #     return attribute_value

    # def __get_data(self):
    #     data = []
    #     default_header_dict = {
    #         'name': 'Not Found',
    #         'value': 'Not Found',
    #         'explanation': 'Not Found'
    #     }
    #     for attribute in self.attribute_list:
    #         attribute_data = dict()
    #         for header_name in ['name', 'explanation']:
    #             attribute_data[header_name] = CIBIL_ATTRIBUTE_DATA.get(
    #                 attribute, {}).get(header_name, 'Not Found')
    #         value = self.__get_attribute_value_from_cibil_regex(attribute)
    #         attribute_data['value'] = value if value else 'Not Found'
    #         data.append(attribute_data)
    #     return data


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
            for attribute_category in CIBIL_ATTRIBUTES_CATEGORY_LIST:
                writer.writerow([''])
                writer.writerow([CIBIL_ATTRIBUTES.get(
                    attribute_category, {}).get('info')])
                writer.writerow(
                    [' ', 'Attribute Name', 'Value', 'Explanation'])
                for attribute_name in CIBIL_ATTRIBUTES.get(attribute_category, {}).get('attribute_list', []):
                    row_data = self.cibil_data.get(
                        attribute_category, {}).get(attribute_name, {})
                    writer.writerow([' ', row_data.get('name', 'Not Found'), row_data.get(
                        'value', 'Not Found'), row_data.get('name', ' '), ])
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
