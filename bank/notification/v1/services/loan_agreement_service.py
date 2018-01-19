import os
import uuid
import random
import subprocess
import pdfkit
import filetype
import requests
from pdfrw import PdfReader, PdfWriter
from html2text import html2text
from django.template.loader import get_template
from rest_framework.reverse import reverse
from django.conf import settings
from common.v1.services.database_service import Database
from common.v1.services.image_service import ImageResizer
from django.core.mail import EmailMultiAlternatives
from loan_agreement_constants import (LOAN_AGREEMENT_PAGE_DATA, DOCUMENT_NAME_ID,
                                      PDF_EXTENSIONS, IMAGE_EXTENSIONS,
                                      DOCUMENT_MISSING_PIC, DOCUMENT_TEMPLATE,
                                      IMAGE_SIZES, LOAN_AGREEMENT_EMAIL)


class LoanAgreement(object):

    def __init__(self, loan_agreement_data):
        self.db = Database('backend_db')
        self.pwd = self.__pwd()
        self.nach_form = self.pwd + 'nach_form.pdf'
        self.loan_agreement_data = loan_agreement_data
        self.customer_id = self.__customer_id()
        self.documents_data = []
        self.loan_agreement_path = self.__document_path('LA-No', '.pdf')
        self.pdf_pages = []
        self.document_pages = []
        self.downloaded_files = []

    def __download_document(self, url, file_path):
        downloaded = False
        if url and file_path:
            r = requests.get(url, timeout=20)
            if r.status_code == 200:
                with open(file_path, 'wb') as f:
                    f.write(r.content)
                    downloaded = True
        return downloaded

    def __customer_id(self):
        return self.loan_agreement_data.get('customer_id')

    def __set_document_data(self):
        sql_query = """
            SELECT document_1, document_type_id
            FROM customer_documents
            WHERE document_type_id IN (1,2,3,5,11)
            AND customer_id={customer_id} order by document_type_id;
        """.format(customer_id=self.customer_id)
        rows = self.db.execute_query(sql_query)
        for row in rows:
            document_data = {
                'url': settings.S3_URL + str(row['document_1']),
                'name': DOCUMENT_NAME_ID.get(row['document_type_id'], ''),
                'file_path': self.__document_path(DOCUMENT_NAME_ID.get(row['document_type_id'], '')),
                'downloaded': False,
            }
            self.documents_data.append(document_data)

    def __download_all_documents(self):
        for document_data in self.documents_data:
            document_data['downloaded'] = self.__download_document(
                document_data['url'], document_data['file_path'])
            self.downloaded_files.append(document_data['file_path'])

    def __document_path(self, doc_name, extension=None):
        if not extension:
            extension = ''
        return '{pwd}{doc_name}-{rand}{extension}'.format(pwd=self.pwd,
                                                          doc_name=doc_name,
                                                          rand=random.randrange(
                                                              10**8),
                                                          extension=extension)

    def __remove_file(self, file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)

    def __clean_up(self):
        self.db.close_connection()
        for file_path in self.pdf_pages + self.downloaded_files:
            self.__remove_file(file_path)
        self.__remove_file(self.loan_agreement_path)

    def __pwd(self):
        pwd = ''
        try:
            subprocess_pwd = subprocess.check_output('pwd')
            pwd = subprocess_pwd.split(
                '\n')[0] + '/notification/v1/services/loan_agreement_files/'
        except Exception as e:
            pass
        return pwd

    def __creat_pdf(self, html_part, pdf_path):
        pdfkit.from_string(html_part, pdf_path)

    def __page_template_data(self, attribute_list):
        template_data = {}
        for attribute in attribute_list:
            attribute_data = self.loan_agreement_data.get(
                attribute, '____________')
            try:
                attribute_data = attribute_data.upper()
            except Exception as e:
                pass
            template_data[attribute] = attribute_data
        return template_data

    def __create_14_loan_pages(self):
        for page_no, pdf_page_data in LOAN_AGREEMENT_PAGE_DATA.iteritems():
            template = get_template(pdf_page_data['template_path'])
            html_part = template.render(
                self.__page_template_data(pdf_page_data['attributes']))
            pdf_page_path = self.__document_path(
                pdf_page_data['pdf_name'], '.pdf')
            self.__creat_pdf(html_part, pdf_page_path)
            self.pdf_pages.append(pdf_page_path)

    def __create_document_loan_page(self, template, template_data, pdf_page_path):
        template = get_template(template)
        html_part = template.render(template_data)
        self.__creat_pdf(html_part, pdf_page_path)
        return pdf_page_path

    def __create_document_loan_pages(self):
        image_data = []
        pdf_pages = []
        missing_data = []
        self.__set_document_data()
        self.__download_all_documents()
        for document_data in self.documents_data:
            if document_data['downloaded'] and filetype.guess(document_data['file_path']) and filetype.guess(document_data['file_path']).extension in PDF_EXTENSIONS:
                pdf_pages.append(document_data['file_path'])
            elif document_data['downloaded'] and filetype.guess(document_data['file_path']) and filetype.guess(document_data['file_path']).extension in IMAGE_EXTENSIONS:
                image_data.append(document_data)
            else:
                document_data['url'] = DOCUMENT_MISSING_PIC
                image_data.append(document_data)

        image_data_chunks = [image_data[i:i + 3]
                             for i in xrange(0, len(image_data), 3)]
        for image_data_chunk in image_data_chunks:
            template_data = {}
            template = DOCUMENT_TEMPLATE.get(len(image_data_chunk), 3)
            pdf_page_path = self.__document_path('image_document', '.pdf')
            element_no = 1
            for image_data in image_data_chunk:
                url_key = "image_{element_no}_url".format(
                    element_no=element_no)
                name_key = "image_{element_no}_name".format(
                    element_no=element_no)
                ImageResizer(image_data['file_path'], IMAGE_SIZES).resize()
                template_data[url_key] = image_data['file_path']
                template_data[name_key] = image_data['name']
                element_no += 1
            self.__create_document_loan_page(
                template, template_data, pdf_page_path)
            self.pdf_pages.append(pdf_page_path)
        self.pdf_pages = self.pdf_pages + pdf_pages

    def __stitch_pdfs(self):
        writer = PdfWriter()
        for pdf_page_path in self.pdf_pages:
            writer.addpages(PdfReader(pdf_page_path).pages)
        writer.addpages(PdfReader(self.nach_form).pages)
        writer.write(self.loan_agreement_path)

    def get_loan_agreement(self):
        self.__create_14_loan_pages()
        self.__create_document_loan_pages()
        self.__stitch_pdfs()
        return self.loan_agreement_path

    def send_loan_agreement(self, reciever_emails=[]):
        loan_agreement_path = self.get_loan_agreement()
        if not reciever_emails:
            reciever_emails = self.loan_agreement_data.get(
                'reciever_emails', [])
        template = get_template(LOAN_AGREEMENT_EMAIL['template_path'])
        html_part = template.render(template)
        msg = EmailMultiAlternatives(subject=LOAN_AGREEMENT_EMAIL['subject'],
                                     body=html_part,
                                     from_email=LOAN_AGREEMENT_EMAIL['sender'],
                                     to=reciever_emails,
                                     bcc=['help@go-upwards.com'])
        msg.attach_file(loan_agreement_path)
        msg.content_subtype = 'html'
        msg.send(fail_silently=False)
        self.__clean_up()
