import requests
from copy import deepcopy
from django.conf import settings
from notification_sms_constants import NOTIFICATION_SMS_TYPE_DATA, DEFAULT_SENDER


class NotificationSMS(object):

    def __init__(self, sms_type, sms_data):
        self.sms_type = sms_type
        self.sms_data = sms_data
        self.sms_variables = self.__sms_variables()
        self.sender = self.__sender()
        self.reciever = self.__reciever()

    def __sender(self):
        return DEFAULT_SENDER

    def __reciever(self):
        return self.sms_data.get('reciever', '')

    def __sms_variables(self):
        return self.sms_data.get('template_data', '')

    def __template_name(self):
        template = NOTIFICATION_SMS_TYPE_DATA.get(
            self.sms_type, {}).get('template', '')
        return template

    def __sms_post_request(self, payload):
        url = settings.SMS_GATEWAY_TRANSACTIONAL_URL.format(
            sms_gateway_api_key=settings.SMS_GATEWAY_API_KEY)
        try:
            response = requests.request("POST", url, data=payload)
            print response.text
        except Exception as e:
            print e, 'fail'
            pass

    def send(self):
        payload = deepcopy(self.sms_variables)
        payload.update({
            'From': self.__sender(),
            'To': self.__reciever(),
            'TemplateName': self.__template_name(),
        })
        self.__sms_post_request(payload)
