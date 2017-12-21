from __future__ import absolute_import

from celery import shared_task
from notification.v1.services import notification_email_service, notification_sms_service, notification_fcm_service, loan_agreement_service


@shared_task(name="send_email_notification")
def send_email_notification(email_type, email_data_list):
    for email_data in email_data_list:
        notification_email_service.NotificationEmail(
            email_type, email_data).send()


@shared_task(name="send_sms_notification")
def send_sms_notification(sms_type, sms_data_list):
    for sms_data in sms_data_list:
        notification_sms_service.NotificationSMS(
            sms_type, sms_data).send()


@shared_task(name="send_fcm_notification")
def send_fcm_notification(fcm_type, fcm_data_list):
    for fcm_data in fcm_data_list:
        notification_fcm_service.NotificationFCM(
            fcm_type, fcm_data).send()


@shared_task(name="send_loan_agreement")
def send_loan_agreement(loan_agreement_data):
    loan_agreement_service.LoanAgreement(
        loan_agreement_data).send_loan_agreement()
