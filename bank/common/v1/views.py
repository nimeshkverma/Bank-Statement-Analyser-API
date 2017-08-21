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
        print response
        return Response({}, status.HTTP_200_OK)
