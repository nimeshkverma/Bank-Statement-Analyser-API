from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from django.views.generic import View
from django.shortcuts import render_to_response
from django.template import RequestContext

from common.v1.decorators import catch_exception, meta_data_response, iam

from services import document_service
from . import serializers
from . import forms
from . import tasks
import logging
LOGGER = logging.getLogger(__name__)


class StatementAnalyserDetails(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @iam('admin')
    def post(self, request, *args, **kwargs):
        serializer = serializers.StatementAnalyserSerializer(data=request.data)
        if serializer.is_valid() and kwargs.get('user_name_auth'):
            return Response(serializer.bank_data(), status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class StatementAnalyseDumperDetails(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    @iam('admin')
    def post(self, request, *args, **kwargs):
        serializer = serializers.StatementAnalyseDumperSerializer(
            data=request.data)
        if serializer.is_valid() and kwargs.get('user_name_auth'):
            return Response(serializer.dump_bank_data(), status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class StatementAnalyserToolDetails(View):
    form_class = forms.StatementAnalyserToolForm
    form_template = 'statements/v1/bank_statement_analysis.html'

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
                request.FILES['bank_statements_pdf'].name, request.FILES['bank_statements_pdf']).file_path
            print pdf_path
            tasks.send_bank_statement_analysis_tool_mail(form.cleaned_data[
                                                         'threshold'], pdf_path, form.cleaned_data['bank_statements_pdf_password'])
            return render_to_response(
                self.form_template,
                {
                    'form': form,
                    'msg': {
                        'Analysis Email Sent': 'Success'
                    }
                },
                context_instance=RequestContext(request)
            )
        return render_to_response(
            self.form_template,
            {
                'form': form,
                'msg': {
                    'Analysis Email Sent': 'Failure'
                }
            },
            context_instance=RequestContext(request)
        )
