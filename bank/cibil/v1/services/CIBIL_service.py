import os
import subprocess
import re
import csv
import uuid
import requests
import json
import time
import datetime
from copy import deepcopy
from cStringIO import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

from tabula import read_pdf
from django.conf import settings

from common.v1.services.email_service import send_mail


class CIBILReport(object):

    def __init__(self, cibil_report_path):
        self.cibil_report_path = cibil_report_path
        self.data = self.__get_data()

    def __get_data(self):
        return [
            {'name': 'Score', 'value': 'TEST', 'explanation': 'CIBIL Score of User'},
            {'name': 'Loans', 'value': 'TEST', 'explanation': 'Loans of User'},
        ]


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
            writer.writerow(['Attribute Name', 'Value', 'Explanation'])
            for row_data in self.cibil_data:
                writer.writerow([row_data['name'], row_data['value'], row_data[
                                'explanation'] if row_data['explanation'] else ''])
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
            'subject': "CIBIL Statements Analysis for :{report_unique_identifier} ".format(report_unique_identifier=self.report_unique_identifier),
            'body': "Empty",
            'sender_email_id': settings.SERVER_EMAIL,
            'reciever_email_ids': settings.RECIEVER_EMAILS,
        }
        send_mail(email_details, self.template, [csvfile])
        self.__remove_file(csvfile)
