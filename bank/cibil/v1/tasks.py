from __future__ import absolute_import

from celery import shared_task
from cibil.v1.services import CIBIL_service


@shared_task(name="send_cibil_report_analysis_tool_mail")
def send_cibil_report_analysis_tool_mail(cibil_reports_pdf, report_unique_identifier, customer_id):
    cibil_report_tool = CIBIL_service.CIBILReportTool(
        cibil_reports_pdf, report_unique_identifier)
    cibil_report_tool.send_cibil_analysis_email()
    CIBIL_service.CIBILAnalysisTool(
        cibil_report_tool.cibil_data, report_unique_identifier).send_cibil_analysed_data_email()
