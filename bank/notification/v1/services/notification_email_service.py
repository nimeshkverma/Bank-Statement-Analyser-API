from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from notification_email_constants import NOTIFICATION_EMAIL_TYPE_DATA, DEFAULT_SENDER


class NotificationEmail(object):

    def __init__(self, email_type, email_data):
        self.email_type = email_type
        self.email_data = email_data
        self.template_data = self.__template_data()
        self.html_part = self.__html_part()
        self.subject = self.__subject()
        self.sender = self.__sender()
        self.recievers = self.__recievers()

    def __template_data(self):
        return self.email_data.get('template_data', {})

    def __html_part(self):
        template_path = NOTIFICATION_EMAIL_TYPE_DATA.get(
            self.email_type, {}).get('template_path')
        template = get_template(template_path) if template_path else ''
        html_part = template.render(self.template_data)
        return html_part

    def __subject(self):
        return self.email_data.get('subject', '')

    def __sender(self):
        return DEFAULT_SENDER

    def __recievers(self):
        return self.email_data.get('recievers', [])

    def send(self):
        msg = EmailMultiAlternatives(
            self.subject, None, self.sender, self.recievers)
        msg.attach_alternative(self.html_part, 'text/html')
        msg.send(True)
