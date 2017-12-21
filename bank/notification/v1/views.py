from django.shortcuts import get_object_or_404
from django_ses.signals import bounce_received, complaint_received, delivery_received
from django.dispatch import receiver

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
