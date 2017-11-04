from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext

from common.v1.services import document_service
from . import forms
from . import tasks
import logging
LOGGER = logging.getLogger(__name__)


class CIBILReportTool(View):
    form_class = forms.CIBILReportDetailsForm
    form_template = 'cibil/v1/cibil_report_analysis.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render_to_response(
            self.form_template,
            {
                'form': form,
                'msg': {}
            },
            context_instance=RequestContext(request)
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            pdf_path = document_service.Document(
                request.FILES['cibil_report_pdf'].name,
                request.FILES['cibil_report_pdf'],
                '/cibil/v1/services').file_path
            # tasks.send_bank_statement_analysis_tool_mail.delay(form.cleaned_data[
            tasks.send_cibil_report_analysis_tool_mail(
                pdf_path, request.FILES['cibil_report_pdf'].name)
            print pdf_path, request.FILES['cibil_report_pdf'].name
            return render_to_response(
                self.form_template,
                {
                    'form': form,
                    'msg': {
                        'CIBIL Report Analysis Email Sent': 'Success'
                    }
                },
                context_instance=RequestContext(request)
            )
        return render_to_response(
            self.form_template,
            {
                'form': form,
                'msg': {
                    'CIBIL Report Analysis Email Sent': 'Failure'
                }
            },
            context_instance=RequestContext(request)
        )
