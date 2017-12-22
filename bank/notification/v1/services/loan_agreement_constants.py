IMAGE_SIZES = (200, 200)

LOAN_AGREEMENT_PAGE_DATA = {
    1: {
        'template_path': 'notification/v1/loan_agreement/page1.html',
        'pdf_name': 'page1_pdf',
        'attributes': ['borrower_full_name',
                       'pan',
                       'aadhaar',
                       'company',
                       'address',
                       'city',
                       'pincode',
                       'is_co_borrower_populated',
                       'city',
                       'borrower_full_name', ],
    },
    2: {
        'template_path': 'notification/v1/loan_agreement/page2.html',
        'pdf_name': 'page2_pdf',
        'attributes': [],
    },
    3: {
        'template_path': 'notification/v1/loan_agreement/page3.html',
        'pdf_name': 'page3_pdf',
        'attributes': [],
    },
    4: {
        'template_path': 'notification/v1/loan_agreement/page4.html',
        'pdf_name': 'page4_pdf',
        'attributes': [],
    },
    5: {
        'template_path': 'notification/v1/loan_agreement/page5.html',
        'pdf_name': 'page5_pdf',
        'attributes': [],
    },
    6: {
        'template_path': 'notification/v1/loan_agreement/page6.html',
        'pdf_name': 'page6_pdf',
        'attributes': [],
    },
    7: {
        'template_path': 'notification/v1/loan_agreement/page7.html',
        'pdf_name': 'page7_pdf',
        'attributes': [],
    },
    8: {
        'template_path': 'notification/v1/loan_agreement/page8.html',
        'pdf_name': 'page8_pdf',
        'attributes': ['borrower_full_name',
                       'loan_amount',
                       'interest_rate_per_tenure',
                       'loan_tenure',
                       'loan_emi_start_date',
                       'loan_emi_emi_date',
                       'loan_emi',
                       'processing_fees',
                       'processing_fees_gst',
                       'pre_emi_days', ],
    },
    9: {
        'template_path': 'notification/v1/loan_agreement/page9.html',
        'pdf_name': 'page9_pdf',
        'attributes': [],
    },
    10: {
        'template_path': 'notification/v1/loan_agreement/page10.html',
        'pdf_name': 'page10_pdf',
        'attributes': ['borrower_full_name',
                       'loan_amount',
                       'loan_amount_words',
                       'borrower_full_name',
                       'pan',
                       'address',
                       'city',
                       'pincode', ],
    },
    11: {
        'template_path': 'notification/v1/loan_agreement/page11.html',
        'pdf_name': 'page11_pdf',
        'attributes': ['loan_amount',
                       'loan_amount_words',
                       'borrower_full_name',
                       'pan',
                       'address',
                       'city',
                       'pincode', ],
    },
    12: {
        'template_path': 'notification/v1/loan_agreement/page12.html',
        'pdf_name': 'page12_pdf',
        'attributes': [],
    },
}

DOCUMENT_TEMPLATE = {
    1: 'notification/v1/loan_agreement/document_1_page.html',
    2: 'notification/v1/loan_agreement/document_2_page.html',
    3: 'notification/v1/loan_agreement/document_3_page.html',
}

DOCUMENT_NAME_ID = {
    1: "AADHHAR",
    11: "AADHHAR",
    2: "Profile-Picture",
    3: "PAN-Card",
    5: "Address-Proof",
}


IMAGE_EXTENSIONS = ['jpg',
                    'png',
                    'gif',
                    'webp',
                    'cr2',
                    'tif',
                    'bmp',
                    'jxr',
                    'psd',
                    'ico', ]
PDF_EXTENSIONS = ['pdf']


DOCUMENT_MISSING_PIC = 'https://s3-us-west-2.amazonaws.com/upwardsimages/document_missing.png'
LOAN_AGREEMENT_EMAIL = {
    'subject': 'Your Loan Is Approved :) - Detailed Mail With Next Steps For Loan Disbursal',
    'sender': 'help@go-upwards.com',
    'template_path': 'notification/v1/loan_agreement/loan_agreement_email.html',
}
