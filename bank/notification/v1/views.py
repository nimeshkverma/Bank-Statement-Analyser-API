from django.shortcuts import get_object_or_404
from django_ses.signals import bounce_received, complaint_received, delivery_received
from django.dispatch import receiver
from django.views.generic import View
from django.shortcuts import render_to_response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from common.v1.decorators import meta_data_response, catch_exception

import logging
LOGGER = logging.getLogger(__name__)


@receiver(bounce_received)
def bounce_handler(sender, *args, **kwargs):
    print("This is bounce email object")
    print(kwargs.get('mail_obj'))


@receiver(complaint_received)
def complaint_handler(sender, *args, **kwargs):
    print("This is complaint email object")
    print(kwargs.get('mail_obj'))


@receiver(complaint_received)
def delivery_handler(sender, *args, **kwargs):
    print("This is delivery email object")
    print(kwargs.get('mail_obj'))


class NotificationCreate(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    def post(self, request):
        serializer = serializers.NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.send_notification()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoanAgreementCreate(APIView):

    @catch_exception(LOGGER)
    @meta_data_response()
    def post(self, request):
        serializer = serializers.LoanAgreementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.send_loan_agreement()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoanAgreementDetails(View):
    page_template = 'notification/v1/loan_agreement/page{page_no}.html'
    document_template = 'notification/v1/loan_agreement/document_{page_no}_page.html'

    def get(self, request, *args, **kwargs):
        page_no = int(request.GET.get('page', '1'))
        print page_no, type(page_no)
        if page_no in range(1, 14):
            template = self.page_template.format(page_no=page_no)
        if page_no == 14:
            page_no = 1
            template = self.document_template.format(page_no=page_no)
        if page_no == 15:
            page_no = 2
            template = self.document_template.format(page_no=page_no)
        if page_no == 16:
            page_no = 3
            template = self.document_template.format(page_no=page_no)
        return render_to_response(template)
