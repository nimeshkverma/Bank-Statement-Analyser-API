import json
from rest_framework import serializers
from . import tasks


class NotificationSerializer(serializers.Serializer):
    email_notification_type = serializers.CharField(
        required=False, allow_null=True)
    email_notification_data = serializers.JSONField(
        required=False, allow_null=True)
    sms_notification_type = serializers.CharField(
        required=False, allow_null=True)
    sms_notification_data = serializers.JSONField(
        required=False, allow_null=True)
    fcm_notification_type = serializers.CharField(
        required=False, allow_null=True)
    fcm_notification_data = serializers.JSONField(
        required=False, allow_null=True)

    def send_notification(self):
        if self.validated_data.get('email_notification_type'):
            email_data_list = self.validated_data.get(
                'email_notification_data', {}).get('data_list', [])
            tasks.send_email_notification.delay(
                self.validated_data['email_notification_type'], email_data_list)
        if self.validated_data.get('sms_notification_type'):
            sms_data_list = self.validated_data.get(
                'sms_notification_data', {}).get('data_list', [])
            tasks.send_sms_notification.delay(
                self.validated_data['sms_notification_type'], sms_data_list)
        if self.validated_data.get('fcm_notification_type'):
            fcm_data_list = self.validated_data.get(
                'fcm_notification_data', {}).get('data_list', [])
            tasks.send_fcm_notification.delay(
                self.validated_data['fcm_notification_type'], fcm_data_list)


class LoanAgreementSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField(required=True)
    borrower_full_name = serializers.CharField()
    pan = serializers.RegexField(regex=r'[a-zA-Z]{5}\d{4}[a-zA-Z]{1}')
    aadhaar = serializers.RegexField(regex=r'^\d{12}$')
    company = serializers.CharField()
    address = serializers.CharField()
    city = serializers.CharField()
    pincode = serializers.RegexField(regex=r'^[1-9][0-9]{5}$')
    is_co_borrower_populated = serializers.CharField()
    loan_amount = serializers.IntegerField(required=True)
    interest_rate_per_tenure = serializers.FloatField()
    loan_tenure = serializers.IntegerField(required=True)
    loan_emi = serializers.IntegerField(required=True)
    loan_emi_start_date = serializers.CharField()
    loan_emi_end_date = serializers.CharField()
    processing_fees = serializers.IntegerField(required=True)
    processing_fees_gst = serializers.IntegerField(required=True)
    pre_emi_days = serializers.IntegerField(required=True)
    pre_emi_amount = serializers.IntegerField(required=True)
    reciever_emails = serializers.ListField(
        child=serializers.EmailField(allow_null=True))

    def send_loan_agreement(self):
        if self.validated_data:
            tasks.send_loan_agreement.delay(self.validated_data)
