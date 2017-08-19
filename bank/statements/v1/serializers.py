from rest_framework import serializers
from tasks import send_bank_statement_analysis_mail, dump_bank_data_to_dynamo


class StatementAnalyserSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    document_type_id = serializers.IntegerField()

    def bank_data(self):
        send_bank_statement_analysis_mail(self.validated_data)
        return {
            "email": "sent"
        }


class StatementAnalyseDumperSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    document_type_id = serializers.IntegerField()

    def dump_bank_data(self):
        dump_bank_data_to_dynamo.delay(self.validated_data)
        return {
            "data_dump": "sent"
        }
