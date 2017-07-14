from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def send_mail(email_details, template, attachments):
    template = get_template(template)
    html_part = template.render(email_details['data'])
    msg = EmailMultiAlternatives(email_details['subject'],
                                 email_details['body'],
                                 email_details['sender_email_id'],
                                 email_details['reciever_email_ids'])
    msg.attach_alternative(html_part, 'text/html')
    for attachment in attachments:
        msg.attach_file(attachment)
    msg.send(True)
