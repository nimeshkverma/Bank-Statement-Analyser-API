import requests
from django.conf import settings
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class OtpCreate(APIView):

    def get(self, request):
        mobile_number = request.query_params.get('mobile_number')
        otp_code = request.query_params.get('otp_code')
        sms_gateway_template = settings.SMS_GATEWAY_TEMPLATE
        sms_gateway_api_key = settings.SMS_GATEWAY_API_KEY
        url = settings.SMS_GATEWAY_URL.format(sms_gateway_api_key=settings.SMS_GATEWAY_API_KEY,
                                              mobile_number=mobile_number,
                                              otp_code=otp_code,
                                              sms_gateway_template=settings.SMS_GATEWAY_TEMPLATE)
        response = requests.request("GET", url)
        return Response({}, status.HTTP_200_OK)


class TransactionalSMS(APIView):

    def post(self, request):
        payload = {'From': request.data.get('From'),
                   'To': request.data.get('To'),
                   'TemplateName': request.data.get('TemplateName'),
                   'VAR1': request.data.get('VAR1'),
                   'VAR2': request.data.get('VAR2'),
                   'VAR3': request.data.get('VAR3'),
                   }
        url = settings.SMS_GATEWAY_TRANSACTIONAL_URL.format(
            sms_gateway_api_key=settings.SMS_GATEWAY_API_KEY)
        response = requests.request("POST", url, data=payload)
        return Response({}, status.HTTP_200_OK)
