ACCOUNT_SUMMARY_SPLITTER = r'\d{2}-\d{2} [a-z,0-9,:,\,-]{4,} [a-z,0-9,:,\,-]{4,}'
ACCOUNT_SUMMARY_RECTIFIER_SPLITTER = 'amounts status'

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
                'attribute_type': 'integer'
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
                'attribute_type': 'integer'
            },
            'total_loan_accounts_overdue': {
                'regex': r'accounts\s*total:\s*\d*\s*overdue:\s*(\d*)\s*zero-balance:\s*\d*',
                'name': 'Total Loan Accounts Over',
                'explanation': 'Number of Loan Accounts the User have and loan repayment is running late',
                'attribute_type': 'integer'
            },
            'total_loan_accounts_zero_balance': {
                'regex': r'accounts\s*total:\s*\d*\s*overdue:\s*\d*\s*zero-balance:\s*(\d*)',
                'name': 'Total Loan Accounts Zero Balance',
                'explanation': 'Number of Loan Accounts the User have and which has successfulled repaid and closed',
                'attribute_type': 'integer'
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
                'attribute_type': 'integer'
            },
            'total_loan_enquiries_30_days': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*(\d*)\s*\d*\s*\d*\s*\d{2}-\d{2}-\d{4}',
                'name': 'Total Loan Enquiries in Past 30 Days',
                'explanation': 'Number of times loan enquiry has been made by lender for the given user in past 30 Days',
                'attribute_type': 'integer'
            },
            'total_loan_enquiries_12_months': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*\d*\s*(\d*)\s*\d*\s*\d{2}-\d{2}-\d{4}',
                'name': 'Total Loan Enquiries in Past 12 Months',
                'explanation': 'Number of times loan enquiry has been made by lender for the given user in Past 12 Months',
                'attribute_type': 'integer'
            },
            'total_loan_enquiries_24_months': {
                'regex': r'total\s*past\s*30\s*days\s*past\s*12\s*months\s*past\s*24\s*months\s*recent\s*\d*\s*\d*\s*\d*\s*(\d*)\s*\d{2}-\d{2}-\d{4}',
                'name': 'Total Loan Enquiries in Past 24 Months',
                'explanation': 'Number of times loan enquiry has been made by lender for the given user in Past 24 Months',
                'attribute_type': 'integer'
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
    'loan_accounts_data': {
        'attribute_list': [
            'account_type',
            'account_ownership',
            'account_open_date',
            'account_close_date',
            'account_last_reported_date',
            'account_emi_start_date',
            'account_emi_end_date',
            'credit_card_highest_amount',
            'current_balance',
            'credit_card_credit_limit',
            'credit_card_cash_limit',
            'sanctioned_amount',
            'overdue_amount',
            'emi_frequency',
            'emi',
            'interest_rate',
            'actual_payment',
            'last_payment',
            'write_off',
            'write_off_total',
            'write_off_principal',
            'collateral_type',
            'repayment_tenure',
        ],
        'attribute_data': {
            'account_type': {
                'regex': r'type:\s*(other|[a-zA-z,-,\s]+ card|overdraft|[a-zA-z,-,\s]+ loan)',
                'name': 'Loan Account Type',
                'explanation': 'Loan account type in the Loan accounts information for the Users',
                'attribute_type': 'string'
            },
            'account_ownership': {
                'regex': r'ownership:\s*(individual|authorized\s*user|guarantor|joint)',
                'name': 'Loan Account Ownership',
                'explanation': 'Loan account ownership in the Loan accounts information for the Users',
                'attribute_type': 'string'
            },
            'account_open_date': {
                'regex': r'opened:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Loan Account Open Date',
                'explanation': 'Date the account was opened. For credit cards and fleet cards, this is the date the card becomes active',
                'attribute_type': 'date'
            },
            'account_close_date': {
                'regex': r'closed:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Loan Account Close Date',
                'explanation': 'Date the account was Closed',
                'attribute_type': 'date'
            },
            'account_last_reported_date': {
                'regex': r'reported\s*and\s*certified:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Loan Account Last Reported Date',
                'explanation': 'The most recent date the reporting member reported information about the account to CIBIL',
                'attribute_type': 'date'
            },
            'account_emi_start_date': {
                'regex': r'pmt\s*hist\s*start:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Loan Account EMI Start Date',
                'explanation': 'EMI start Date for this Loan Account',
                'attribute_type': 'date'
            },
            'account_emi_end_date': {
                'regex': r'pmt\s*hist\s*end:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Loan Account EMI End Date',
                'explanation': 'EMI End Date for this Loan Account',
                'attribute_type': 'date'
            },
            'credit_card_highest_amount': {
                'regex': r'high\s*credit:\s*([0-9,\,]+)',
                'name': 'Highest Amount Drawn from Credit Card',
                'explanation': 'Highest Amount Drawn from Credit Card. This applies in case of Credit Card account',
                'attribute_type': 'amount'
            },
            'current_balance': {
                'regex': r'current\s*balance:\s*([0-9,\,]+)',
                'name': 'Current Balance of the Loan Account',
                'explanation': 'The sum of the entire amount of credit/loan outstanding, including the current and overdue portion, if any, together with interest last applied for all the accounts. A negative sign indicates a credit balance',
                'attribute_type': 'amount'
            },
            'credit_card_credit_limit': {
                'regex': r'credit\s*limit:\s*([0-9,\,]+)',
                'name': 'Credit Limit for Credit Card. This applies in case of Credit Card account',
                'explanation': 'Credit Limit for Credit Card',
                'attribute_type': 'amount'
            },
            'credit_card_cash_limit': {
                'regex': r'cash\s*limit:\s*([0-9,\,]+)',
                'name': 'Cash Limit for Credit Card. This applies in case of Credit Card account',
                'explanation': 'Cash Limit for Credit Card',
                'attribute_type': 'amount'
            },
            'sanctioned_amount': {
                'regex': r'sanctioned:\s*([0-9,\,]+)',
                'name': 'Total amount Sanctioned',
                'explanation': 'Total amount Sanctioned for this Loan account',
                'attribute_type': 'amount'
            },
            'overdue_amount': {
                'regex': r'overdue:\s*([0-9,\,]+)',
                'name': 'Total amount the account is past due',
                'explanation': 'Total amount the account is past due for this Loan account',
                'attribute_type': 'amount'
            },
            'emi_frequency': {
                'regex': r'pmt\s*freq:\s*([weekly|fortnightly|monthly|quarterly]+)',
                'name': 'EMI Frequency',
                'explanation': 'EMI Frequency for the given Loan Account',
                'attribute_type': 'string'
            },
            'emi': {
                'regex': r'emi:\s*([0-9,\,]+)',
                'name': 'EMI Amount',
                'explanation': 'EMI Amount for the given Loan Account',
                'attribute_type': 'amount'
            },
            'interest_rate': {
                'regex': r'interest\s*rate:\s*(\d{2}\.\d{2})',
                'name': 'Interest Rate',
                'explanation': 'Interest Rate for the given Loan Account',
                'attribute_type': 'decimal'
            },
            'actual_payment': {
                'regex': r'actual\s*payment:\s*([0-9,\,]+)',
                'name': 'Actual Payment',
                'explanation': 'Actual Payment done for the given Loan Account',
                'attribute_type': 'amount'
            },
            'last_payment': {
                'regex': r'last payment:\s*(\d{2}-\d{2}-\d{4})',
                'name': 'Last Payment',
                'explanation': 'Last Payment date for the given Loan Account',
                'attribute_type': 'date'
            },
            'write_off': {
                'regex': r'written\s*off\s*/\s*settled\s*status:\s*(written-off|[0-9,\,]+)',
                'name': 'Write off or Settled',
                'explanation': 'Is the Loan Account Written off or Settled',
                'attribute_type': 'string'
            },
            'write_off_total': {
                'regex': r'written\s*off\s*\(total\)\s*:\s*([0-9,\,]+)',
                'name': 'Write off Total',
                'explanation': 'Total Write off Amount for the Loan Account',
                'attribute_type': 'amount'
            },
            'write_off_principal': {
                'regex': r'written\s*off\s*\(principal\)\s*:\s*([0-9,\,]+)',
                'name': 'Write off Principal',
                'explanation': 'Principal Write off Amount for the Loan Account',
                'attribute_type': 'amount'
            },
            'collateral_type': {
                'regex': r'collateral\s*type:\s*(no collateral|[a-zA-z,-,\s]+)',
                'name': 'Collateral Type',
                'explanation': 'Type of collateral used in the loan',
                'attribute_type': 'string'
            },
            'repayment_tenure': {
                'regex': r'repayment tenure:\s*(\d+)',
                'name': 'Repayment Tenure',
                'explanation': 'No of Repayment Cycles',
                'attribute_type': 'integer'
            },
        },
        'info': 'Loan Accounts Information of the User, Given by CIBIL 2.0 Transunion',
    },
}
