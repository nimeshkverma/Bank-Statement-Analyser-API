CIBIL_ATTRIBUTES = {
    'cibil_score_data': {
        'attribute_list': [
            'cibil_score',
        ],
        'attribute_data': {
            'cibil_score': {
                'regex': r'cibil\s*transunion\s*score\s*version\s*2.0\s*(\d{1,3}|-1)',
                'name': 'CIBIL Score',
                'explanation': 'The CIBIL Score of the User',
                'attribute_type': 'number'
            },
        },
        'info': 'CIBIL 2.0 Score of the User, Given by Transunion',
    },
    'loan_accounts_summary_data': {
        'attribute_list': [
            'total_loan_accounts',
            'total_loan_accounts_overdue',
            'total_loan_accounts_zero_balance',
            'total_amount_sanctioned',
            'total_amount_current',
            'total_amount_overdue',
            'last_reporting_date',
            'credit_history_since_date',
        ],
        'attribute_data': {
            'total_loan_accounts': {
                'regex': r'accounts\s*total:\s*(\d*)\s*overdue:\s*\d*\s*zero-balance:\s*\d*',
                'name': 'Total Loan Accounts',
                'explanation': 'Number of Loan Accounts the User have had up till the generation of the report.',
                'attribute_type': 'number'
            },
            'total_loan_accounts_overdue': {
                'regex': r'accounts\s*total:\s*\d*\s*overdue:\s*(\d*)\s*zero-balance:\s*\d*',
                'name': 'Total Loan Accounts Over',
                'explanation': 'Number of Loan Accounts the User have and loan repayment is running late',
                'attribute_type': 'number'
            },
            'total_loan_accounts_zero_balance': {
                'regex': r'accounts\s*total:\s*\d*\s*overdue:\s*\d*\s*zero-balance:\s*(\d*)',
                'name': 'Total Loan Accounts Zero Balance',
                'explanation': 'Number of Loan Accounts the User have and which has successfulled repaid and closed',
                'attribute_type': 'number'
            },
            'total_amount_sanctioned': {
                'regex': r'high\s*cr/sanc\.\s*amt:\s*([0-9,\,]+)\s*current:\s*[0-9,\,]+\s*overdue:\s*[0-9,\,]+',
                'name': 'Total Amount Sanctioned',
                'explanation': 'Total Loans Amount disbursed to the User.',
                'attribute_type': 'amount'
            },
            'total_amount_current': {
                'regex': r'high\s*cr/sanc\.\s*amt:\s*[0-9,\,]+\s*current:\s*([0-9,\,]+)\s*overdue:\s*[0-9,\,]+',
                'name': 'Total Amount Current',
                'explanation': ' Total Loans Amount which is yet to be paid by the User',
                'attribute_type': 'amount'
            },
            'total_amount_overdue': {
                'regex': r'high\s*cr/sanc\.\s*amt:\s*[0-9,\,]+\s*current:\s*[0-9,\,]+\s*overdue:\s*([0-9,\,]+)',
                'name': 'Total Amount Over Due',
                'explanation': 'Total Loans Amount which is not paid by the User and is overdue',
                'attribute_type': 'amount'
            },
            'last_reporting_date': {
                'regex': r'recent:\s*(\d{2}-\d{2}-\d{4})\s*oldest:\s*\d{2}-\d{2}-\d{4}',
                'name': 'Last Reporting Date',
                'explanation': 'Date at which the last CIBIL enquiry was made for the User',
                'attribute_type': 'date'
            },
            'credit_history_since_date': {
                'regex': r'recent:\s*\d{2}-\d{2}-\d{4}\s*oldest:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Credit History Since Date',
                'explanation': 'Date at which the first CIBIL enquiry was made for the User',
                'attribute_type': 'date'
            },
        },
        'info': 'Summary of all the Loan accounts of the User',
    },
    'loan_enquiry_data': {
        'attribute_list': [
            'total_loan_enquiries',
            'total_loan_enquiries_30_days',
            'total_loan_enquiries_12_months',
            'total_loan_enquiries_24_months',
            'last_date_of_enquiry',
        ],
        'attribute_data': {
            'total_loan_enquiries': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*(\d*)\s*\d*\s*\d*\s*\d*\s*\d{2}-\d{2}-\d{4}',
                'name': 'Total Loan Enquiries',
                'explanation': 'Number of times loan enquiry has been made by lender for the given user in Total',
                'attribute_type': 'number'
            },
            'total_loan_enquiries_30_days': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*(\d*)\s*\d*\s*\d*\s*\d{2}-\d{2}-\d{4}',
                'name': 'Total Loan Enquiries in Past 30 Days',
                'explanation': 'Number of times loan enquiry has been made by lender for the given user in past 30 Days',
                'attribute_type': 'number'
            },
            'total_loan_enquiries_12_months': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*\d*\s*(\d*)\s*\d*\s*\d{2}-\d{2}-\d{4}',
                'name': 'Total Loan Enquiries in Past 12 Months',
                'explanation': 'Number of times loan enquiry has been made by lender for the given user in Past 12 Months',
                'attribute_type': 'number'
            },
            'total_loan_enquiries_24_months': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*\d*\s*\d*\s*(\d*)\s*\d{2}-\d{2}-\d{4}',
                'name': 'Total Loan Enquiries in Past 24 Months',
                'explanation': 'Number of times loan enquiry has been made by lender for the given user in Past 24 Months',
                'attribute_type': 'number'
            },
            'last_date_of_enquiry': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*\d*\s*\d*\s*\d*\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Last Date of Loan Enquiry',
                'explanation': 'Last date of loan enquiry which has been made by lender for the given user',
                'attribute_type': 'date'
            },
        },
        'info': 'Loan Enquiry made by the Lenders for the User',

    },
}

CIBIL_ATTRIBUTES_CATEGORY_LIST = [
    'cibil_score_data',
    'loan_accounts_summary_data',
    'loan_enquiry_data'
]

CIBIL_ATTRIBUTE_LIST = [
    'cibil_score',
    'total_loan_accounts',
    'total_loan_accounts_overdue',
    'total_loan_accounts_zero_balance',
    'total_amount_sanctioned',
    'total_amount_current',
    'total_amount_overdue',
    'last_reporting_date',
    'credit_history_since_date',
    'total_loan_enquiries',
    'total_loan_enquiries_30_days',
    'total_loan_enquiries_12_months',
    'total_loan_enquiries_24_months',
    'last_date_of_enquiry',
]

CIBIL_ATTRIBUTE_DATA = {
    'cibil_score': {
        'regex': r'cibil\s*transunion\s*score\s*version\s*2.0\s*(\d{1,3}|-1)',
        'name': 'CIBIL Score',
        'explanation': 'The CIBIL Score of the User',
        'attribute_type': 'number'
    },
    'total_loan_accounts': {
        'regex': r'accounts\s*total:\s*(\d*)\s*overdue:\s*\d*\s*zero-balance:\s*\d*',
        'name': 'Total Loan Accounts',
        'explanation': 'Number of Loan Accounts the User have had up till the generation of the report.',
        'attribute_type': 'number'
    },
    'total_loan_accounts_overdue': {
        'regex': r'accounts\s*total:\s*\d*\s*overdue:\s*(\d*)\s*zero-balance:\s*\d*',
        'name': 'Total Loan Accounts Over',
        'explanation': 'Number of Loan Accounts the User have and loan repayment is running late',
        'attribute_type': 'number'
    },
    'total_loan_accounts_zero_balance': {
        'regex': r'accounts\s*total:\s*\d*\s*overdue:\s*\d*\s*zero-balance:\s*(\d*)',
        'name': 'Total Loan Accounts Zero Balance',
        'explanation': 'Number of Loan Accounts the User have and which has successfulled repaid and closed',
        'attribute_type': 'number'
    },
    'total_amount_sanctioned': {
        'regex': r'high\s*cr/sanc\.\s*amt:\s*([0-9,\,]+)\s*current:\s*[0-9,\,]+\s*overdue:\s*[0-9,\,]+',
        'name': 'Total Amount Sanctioned',
        'explanation': 'Total Loans Amount disbursed to the User.',
        'attribute_type': 'amount'
    },
    'total_amount_current': {
        'regex': r'high\s*cr/sanc\.\s*amt:\s*[0-9,\,]+\s*current:\s*([0-9,\,]+)\s*overdue:\s*[0-9,\,]+',
        'name': 'Total Amount Current',
        'explanation': ' Total Loans Amount which is yet to be paid by the User',
        'attribute_type': 'amount'
    },
    'total_amount_overdue': {
        'regex': r'high\s*cr/sanc\.\s*amt:\s*[0-9,\,]+\s*current:\s*[0-9,\,]+\s*overdue:\s*([0-9,\,]+)',
        'name': 'Total Amount Over Due',
        'explanation': 'Total Loans Amount which is not paid by the User and is overdue',
        'attribute_type': 'amount'
    },
    'last_reporting_date': {
        'regex': r'recent:\s*(\d{2}-\d{2}-\d{4})\s*oldest:\s*\d{2}-\d{2}-\d{4}',
        'name': 'Last Reporting Date',
        'explanation': 'Date at which the last CIBIL enquiry was made for the User',
        'attribute_type': 'date'
    },
    'credit_history_since_date': {
        'regex': r'recent:\s*\d{2}-\d{2}-\d{4}\s*oldest:\s*(\d{2}-\d{2}-\d{4})',
        'name': 'Credit History Since Date',
        'explanation': 'Date at which the first CIBIL enquiry was made for the User',
        'attribute_type': 'date'
    },
    'total_loan_enquiries': {
        'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*(\d*)\s*\d*\s*\d*\s*\d*\s*\d{2}-\d{2}-\d{4}',
        'name': 'Total Loan Enquiries',
        'explanation': 'Number of times loan enquiry has been made by lender for the given user in Total',
        'attribute_type': 'number'
    },
    'total_loan_enquiries_30_days': {
        'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*(\d*)\s*\d*\s*\d*\s*\d{2}-\d{2}-\d{4}',
        'name': 'Total Loan Enquiries in Past 30 Days',
        'explanation': 'Number of times loan enquiry has been made by lender for the given user in past 30 Days',
        'attribute_type': 'number'
    },
    'total_loan_enquiries_12_months': {
        'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*\d*\s*(\d*)\s*\d*\s*\d{2}-\d{2}-\d{4}',
        'name': 'Total Loan Enquiries in Past 12 Months',
        'explanation': 'Number of times loan enquiry has been made by lender for the given user in Past 12 Months',
        'attribute_type': 'number'
    },
    'total_loan_enquiries_24_months': {
        'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*\d*\s*\d*\s*(\d*)\s*\d{2}-\d{2}-\d{4}',
        'name': 'Total Loan Enquiries in Past 24 Months',
        'explanation': 'Number of times loan enquiry has been made by lender for the given user in Past 24 Months',
        'attribute_type': 'number'
    },
    'last_date_of_enquiry': {
        'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*\d*\s*\d*\s*\d*\s*(\d{2}-\d{2}-\d{4})',
        'name': 'Last Date of Loan Enquiry',
        'explanation': 'Last date of loan enquiry which has been made by lender for the given user',
        'attribute_type': 'date'
    },

}
