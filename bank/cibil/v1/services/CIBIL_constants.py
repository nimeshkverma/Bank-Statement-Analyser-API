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
        'regex': r'recent:\s*\d{2}-\d{2}-\d{4}\s*oldest:(\s*\d{2}-\d{2}-\d{4})',
        'name': 'Credit History Since Date',
        'explanation': 'Date at which the first CIBIL enquiry was made for the User',
        'attribute_type': 'date'
    },
}
