import json
from django.conf import settings
from pyfcm import FCMNotification
from notification_fcm_constants import NOTIFICATION_FCM_TYPE_DATA


class NotificationFCM(object):

    def __init__(self, fcm_type, fcm_data):
        self.fcm_type = fcm_type
        self.fcm_data = fcm_data
        self.push_service = FCMNotification(api_key=settings.FCM_API_KEY)
        self.data_message = self.__data_message()
        self.message_body = self.__message_body()
        self.reciever = self.__reciever()

    def __reciever(self):
        return self.fcm_data.get('reciever', '')

    def __data_message(self):
        data_message = NOTIFICATION_FCM_TYPE_DATA.get(
            self.fcm_type, {}).get('data_message', '')
        data_message_vars = self.fcm_data.get('data_message_vars')
        if data_message_vars and data_message:
            data_message = data_message.format(**data_message_vars)
        return data_message

    def __message_body(self):
        message_body = NOTIFICATION_FCM_TYPE_DATA.get(
            self.fcm_type, {}).get('message_body', '')
        message_body_vars = self.fcm_data.get('message_body_vars')
        if message_body_vars and message_body:
            message_body = message_body.format(**message_body_vars)
        return message_body

    def send(self):
        result = self.push_service.notify_multiple_devices(
            registration_ids=[self.reciever], data_message=self.data_message, message_body=self.message_body)
        print result
