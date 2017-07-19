from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from common.v1.decorators import catch_exception, meta_data_response, iam

from . import serializers

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
