DEFAULT_SENDER = 'help@go-upwards.com'

NOTIFICATION_EMAIL_TYPE_DATA = {
    'follow_up': {
        'template_path': 'notification/v1/follow_up_email.html',
    },
    'eligibility_documents_uploaded': {
        'template_path': 'notification/v1/eligibility_documents_uploaded_email.html',
    },
    'bank_statement_incomplete': {
        'template_path': 'notification/v1/bank_statement_incomplete_email.html',
    },
    'eligibility_evaluation_submit': {
        'template_path': 'notification/v1/eligibility_evaluation_submit_email.html',
    },
    'eligibility_evaluation_approved': {
        'template_path': 'notification/v1/eligibility_evaluation_approved_email.html',
    },
    'eligibility_evaluation_reject': {
        'template_path': 'notification/v1/eligibility_evaluation_reject_email.html',
    },
    'post_eligibility_follow_up': {
        'template_path': 'notification/v1/post_eligibility_follow_up_email.html',
    },
    'kyc_documents_uploaded': {
        'template_path': 'notification/v1/kyc_documents_uploaded_email.html',
    },
    'kyc_submit': {
        'template_path': 'notification/v1/kyc_submit_email.html',
    },
    'kyc_approved': {
        'template_path': 'notification/v1/kyc_approved_email.html',
    },
    'kyc_reject': {
        'template_path': 'notification/v1/kyc_reject_email.html',
    },
}
