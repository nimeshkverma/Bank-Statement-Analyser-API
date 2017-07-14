from __future__ import absolute_import
from celery import shared_task
from statements.v1.services import bank_statements_service


@shared_task(name="send_bank_statement_analysis_mail")
def send_bank_statement_analysis_mail(customer_data):
    bank_statements_service.BankStatementsAnalyser(customer_data['customer_id'], customer_data[
        'document_type_id']).send_bank_analysis_email()
