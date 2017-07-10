from rest_framework import serializers
from services.bank_statements_service import BankStatementsAnalyser


class StatementAnalyserSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    document_type_id = serializers.IntegerField()

    def bank_data(self):
        return BankStatementsAnalyser(self.validated_data['customer_id'], self.validated_data['document_type_id']).bank_data
