from __future__ import absolute_import
import time
import requests
import json
from django.conf import settings
from celery import shared_task
from statements.v1.services import bank_statements_service


@shared_task(name="send_bank_statement_analysis_mail")
def send_bank_statement_analysis_mail(customer_data):
    bank_statements_service.BankStatementsAnalyser(customer_data['customer_id'], customer_data[
        'document_type_id']).send_bank_analysis_email()


@shared_task(name="dump_bank_data_to_dynamo")
def dump_bank_data_to_dynamo(customer_data):
    data = {
        "created_at": int(time.time()),
        "customer_id": customer_data['customer_id'],
        "data": bank_statements_service.BankStatementsAnalyser(customer_data['customer_id'], customer_data[
            'document_type_id']).bank_data
    }
    url = settings.DYNAMO_DATA_DUMP['url']
    headers = {
        settings.DYNAMO_DATA_DUMP['auth_key']: settings.DYNAMO_DATA_DUMP['auth_value'],
        "Content-Type": "application/json",
    }
    request_status = None
    try:
        request_data = requests.post(
            url, data=json.dumps(data), headers=headers)
        request_status = request_data.status_code
        print request_status, request_data.text
    except Exception as e:
        print e
    return data


@shared_task(name="send_bank_statement_analysis_tool_mail")
def send_bank_statement_analysis_tool_mail(threshold, bank_statements_pdf, bank_statements_pdf_password):
    bank_statements_service.BankStatementsAnalyserTool(
        bank_statements_pdf, bank_statements_pdf_password, threshold).send_bank_analysis_email()
