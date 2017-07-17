from rest_framework import serializers
from tasks import send_bank_statement_analysis_mail


class StatementAnalyserSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    document_type_id = serializers.IntegerField()

    def bank_data(self):
        send_bank_statement_analysis_mail.delay(self.validated_data)
        return {
            "email": "sent"
        }
