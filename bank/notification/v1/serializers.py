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
            tasks.send_email_notification(
                self.validated_data['email_notification_type'], email_data_list)
        if self.validated_data.get('sms_notification_type'):
            sms_data_list = self.validated_data.get(
                'sms_notification_data', {}).get('data_list', [])
            tasks.send_sms_notification(
                self.validated_data['sms_notification_type'], sms_data_list)
        if self.validated_data.get('fcm_notification_type'):
            fcm_data_list = self.validated_data.get(
                'fcm_notification_data', {}).get('data_list', [])
            tasks.send_fcm_notification(
                self.validated_data['fcm_notification_type'], fcm_data_list)
