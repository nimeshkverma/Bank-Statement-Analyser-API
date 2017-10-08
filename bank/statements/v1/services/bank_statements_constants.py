BANK_IDENTIFIER_CONSTANTS = {
    'axis_a': {
        'keywords': [
            {
                'string': 'customer no',
                'weight': 1
            },
            {
                'string': 'statement of axis account no',
                'weight': 1
            },
            {
                'string': 'axis bank',
                'weight': 1
            },
            {
                'string': 'www.axisbank.com',
                'weight': 1
            },
            {
                'string': 'customer.service@axisbank.com',
                'weight': 1
            },
            {
                'string': 'registered office - axis bank ltd,trishul,opp. samartheswar temple, near law garden, ellisbridge',
                'weight': 1
            }
        ],
        'regex_words': [],
        'table_headers': [
            {
                'string': 'tran date',
                'weight': 1
            },
            {
                'string': 'chq no',
                'weight': 1
            },
            {
                'string': 'particulars',
                'weight': 1
            },
            {
                'string': 'debit',
                'weight': 1
            },
            {
                'string': 'credit',
                'weight': 1
            },
            {
                'string': 'balance',
                'weight': 1
            },
            {
                'string': 'init.',
                'weight': 1
            }

        ]
    },
    'axis_b': {
        'keywords': [
            {
                'string': 'axis bank',
                'weight': 1
            },
            {
                'string': 'www.axisbank.com',
                'weight': 1
            },
            {
                'string': 'relationship summary as on date',
                'weight': 1
            },
            {
                'string': 'profile completeness',
                'weight': 1
            },
            {
                'string': 'detailed statement for a/c no',
                'weight': 1
            },
            {
                'string': 'registered office: "trishul" - 3rd floor, opp. samartheshwar temple, near law garden, ellisbridge, ahmedabad',
                'weight': 1
            }
        ],
        'regex_words': [
            {
                'string': r'utib\d{7}',
                'weight': 1
            }
        ],
        'table_headers': [
            {
                'string': 'bank account',
                'weight': 1
            },
            {
                'string': 'crn',
                'weight': 1
            },
            {
                'string': 'amount',
                'weight': 1
            },
            {
                'string': 'other account',
                'weight': 1
            },
            {
                'string': 'crn',
                'weight': 1
            },
            {
                'string': 'outstanding amount',
                'weight': 1
            },
            {
                'string': 'txn date transaction',
                'weight': 1
            },
            {
                'string': 'withdrawals',
                'weight': 1
            },
            {
                'string': 'deposits',
                'weight': 1
            },
            {
                'string': 'balance',
                'weight': 1
            },
            {
                'string': 'information',
                'weight': 1
            }
        ]
    },
    'hdfc_a': {
        'keywords': [
            {
                'string': 'account branch',
                'weight': 1
            },
            {
                'string': 'a/c open date',
                'weight': 1
            },
            {
                'string': 'account status',
                'weight': 1
            },
            {
                'string': 'hdfc bank limited',
                'weight': 1
            },
            {
                'string': 'hdfc bank service tax registration number',
                'weight': 1
            },
            {
                'string': 'registered office address',
                'weight': 1
            },
            {
                'string': 'hdfc bank house',
                'weight': 1
            },
        ],
        'regex_words': [
            {
                'string': r'hdfc\d{7}',
                'weight': 1
            },
            {
                'string': r'(registered office address\\s?:\\s?hdfc bank house\\s?,\\s?senapati bapat marg\\s?,\\s?lower parel\\s?,\\s?mumbai\\s?400013)',
                'weight': 1
            }
        ],
        'table_headers': [
            {
                'string': 'date',
                'weight': 1
            },
            {
                'string': 'narration',
                'weight': 1
            },
            {
                'string': 'chq./ref.no.',
                'weight': 1
            },
            {
                'string': 'value dt',
                'weight': 1
            },
            {
                'string': 'withdrawal amt.',
                'weight': 1
            },
            {
                'string': 'deposit amt.',
                'weight': 1
            },
            {
                'string': 'closing balance',
                'weight': 1
            }
        ]
    },
    'icici_a': {
        'keywords': [
            {
                'string': 'detailed statement',
                'weight': 1
            },
            {
                'string': 'search',
                'weight': 1
            },
            {
                'string': 'advanced search',
                'weight': 1
            },
            {
                'string': 'transaction date from',
                'weight': 1
            },
            {
                'string': 'amount from',
                'weight': 1
            },
            {
                'string': 'cheque number from',
                'weight': 1
            },
            {
                'string': 'transactions list',
                'weight': 1
            },
            {
                'string': 'transaction type',
                'weight': 1
            }
        ],
        'regex_words': [],
        'table_headers': [
            {
                'string': 's no.',
                'weight': 1
            },
            {
                'string': 'value date',
                'weight': 1
            },
            {
                'string': 'transaction date',
                'weight': 1
            },
            {
                'string': 'cheque number',
                'weight': 1
            },
            {
                'string': 'transaction remarks',
                'weight': 1
            },
            {
                'string': 'withdrawal amount',
                'weight': 1
            },
            {
                'string': 'deposit amount',
                'weight': 1
            },
            {
                'string': 'balance (inr )',
                'weight': 1
            }
        ]
    },
    'icici_b': {
        'keywords': [
            {
                'string': 'www.icicibank.com',
                'weight': 1
            },
            {
                'string': 'your base branch',
                'weight': 1
            },
            {
                'string': 'dial your bank',
                'weight': 1
            },
            {
                'string': 'summary of accounts held under cust id',
                'weight': 1
            },
            {
                'string': 'statement of transactions in savings account number',
                'weight': 1
            },
            {
                'string': 'account related other information',
                'weight': 1
            },
            {
                'string': 'for icici bank limited',
                'weight': 1
            },
            {
                'string': 'authorised signatory',
                'weight': 1
            }
        ],
        'regex_words': [],
        'table_headers': [
            {
                'string': 'date mode',
                'weight': 1
            },
            {
                'string': 'date mode**',
                'weight': 1
            },
            {
                'string': 'particulars',
                'weight': 1
            },
            {
                'string': 'deposits',
                'weight': 1
            },
            {
                'string': 'withdrawals',
                'weight': 1
            },
            {
                'string': 'balance',
                'weight': 1
            },
            {
                'string': 'withdrawal amount',
                'weight': 1
            },
            {
                'string': 'deposit amount',
                'weight': 1
            },
            {
                'string': 'balance (inr )',
                'weight': 1
            }
        ]
    },
    'idbi_a': {
        'keywords': [
            {
                'string': 'your savings a/c status',
                'weight': 1
            },
            {
                'string': 'website:www.idbi.com',
                'weight': 1
            },
            {
                'string': 'idbi bank ltd',
                'weight': 1
            },
            {
                'string': 'contact number for customers residing outside india',
                'weight': 1
            }
        ],
        'regex_words': [],
        'table_headers': [
            {
                'string': 'srl',
                'weight': 1
            },
            {
                'string': 'txn date',
                'weight': 1
            },
            {
                'string': 'value date',
                'weight': 1
            },
            {
                'string': 'description',
                'weight': 1
            },
            {
                'string': 'cheque',
                'weight': 1
            },
            {
                'string': 'cr/dr',
                'weight': 1
            },
            {
                'string': 'ccy',
                'weight': 1
            },
            {
                'string': 'trxn amount',
                'weight': 1
            },
            {
                'string': 'balance',
                'weight': 1
            }
        ]
    },
    'idbi_b': {
        'keywords': [
            {
                'string': 'statement criteria',
                'weight': 1
            }],
        'regex_words': [],
        'table_headers': [
            {
                'string': 'srl',
                'weight': 1
            },
            {
                'string': 'txn date',
                'weight': 1
            },
            {
                'string': 'value date',
                'weight': 1
            },
            {
                'string': 'description',
                'weight': 1
            },
            {
                'string': 'cheque',
                'weight': 1
            },
            {
                'string': 'cr/dr',
                'weight': 1
            },
            {
                'string': 'ccy',
                'weight': 1
            },
            {
                'string': 'trxn amount',
                'weight': 1
            },
            {
                'string': 'balance',
                'weight': 1
            }
        ]
    },
    'idfc_a': {
        'keywords': [
            {
                'string': 'statement of account',
                'weight': 1
            },
            {
                'string': 'statement period',
                'weight': 1
            },
            {
                'string': 'date of opening',
                'weight': 1
            },
            {
                'string': 'banker@idfcbank.com',
                'weight': 1
            }
        ],
        'regex_words': [
            {
                'string': r'registered office\\s?:\\s?idfc bank limited',
                'weight': 1
            }
        ],
        'table_headers': [
            {
                'string': 'opening balance',
                'weight': 1
            },
            {
                'string': 'total debit',
                'weight': 1
            },
            {
                'string': 'total credit',
                'weight': 1
            },
            {
                'string': 'closing balance',
                'weight': 1
            },
            {
                'string': 'date',
                'weight': 1
            },
            {
                'string': 'particulars',
                'weight': 1
            },
            {
                'string': 'cheque no.',
                'weight': 1
            },
            {
                'string': 'debit',
                'weight': 1
            },
            {
                'string': 'credit',
                'weight': 1
            },
            {
                'string': 'balance',
                'weight': 1
            }]
    },
    'kotak_a': {
        'keywords': [
            {
                'string': 'deposit count',
                'weight': 1
            },
            {
                'string': 'withdrawal count',
                'weight': 1
            },
            {
                'string': 'cust.reln.no',
                'weight': 1
            },
            {
                'string': 'total withdrawal amount',
                'weight': 1
            },
            {
                'string': 'total deposit amount',
                'weight': 1
            }
        ],
        'regex_words': [],
        'table_headers': [
            {
                'string': 'date',
                'weight': 1
            },
            {
                'string': 'narration chq/ref no',
                'weight': 1
            },
            {
                'string': 'withdrawal (dr)/deposit (cr)',
                'weight': 1
            },
            {
                'string': 'withdrawal (dr)/',
                'weight': 1
            },
            {
                'string': 'balance',
                'weight': 1
            },
            {
                'string': 'narration',
                'weight': 1
            },
            {
                'string': 'chq/ref no',
                'weight': 1
            }
        ]
    },
    'kotak_b': {
        'keywords': [
            {
                'string': 'total withdrawal amount',
                'weight': 1
            },
            {
                'string': 'total deposit amount',
                'weight': 1
            },
            {
                'string': 'kotak mahindra bank ltd',
                'weight': 1
            },
            {
                'string': 'my portfolio',
                'weight': 1
            },
            {
                'string': 'deposit accounts-inr',
                'weight': 1
            },
            {
                'string': 'asset class',
                'weight': 1
            },
            {
                'string': 'overdraft sanction limit',
                'weight': 1
            }
        ],
        'regex_words': [],
        'table_headers': [
            {
                'string': 'date',
                'weight': 1
            },
            {
                'string': 'narration',
                'weight': 1
            },
            {
                'string': 'chq/ref no.',
                'weight': 1
            },
            {
                'string': 'withdrawal (dr)/deposit (cr)',
                'weight': 1
            },
            {
                'string': 'balance',
                'weight': 1
            }
        ]
    },
    'kotak_c': {
        'keywords': [
            {
                'string': 'cust. reln. no.',
                'weight': 1
            },
            {
                'string': 'toll free or email at service.bank@kotak.com',
                'weight': 1
            },
            {
                'string': 'call 1800 102 6022 24 hrs',
                'weight': 1
            },
            {
                'string': 'write to us at customer contact centre',
                'weight': 1
            },
            {
                'string': 'post box number 16344, mumbai 400 013',
                'weight': 1
            },
            {
                'string': 'kotak mahindra bank ltd',
                'weight': 1
            }
        ],
        'regex_words': [],
        'table_headers': [
            {
                'string': 'sl. no.',
                'weight': 1
            },
            {
                'string': 'date',
                'weight': 1
            },
            {
                'string': 'description',
                'weight': 1
            },
            {
                'string': 'chq / ref number',
                'weight': 1
            },
            {
                'string': 'amount',
                'weight': 1
            },
            {
                'string': 'dr / cr',
                'weight': 1
            },
            {
                'string': 'balance',
                'weight': 1
            },
            {
                'string': 'dr / cr',
                'weight': 1
            }
        ]
    },
    'sbi_a': {
        'keywords': [
            {
                'string': 'interest rate(% p.a.)',
                'weight': 1
            },
            {
                'string': 'drawing power',
                'weight': 1
            },
            {
                'string': 'account description',
                'weight': 1
            },
            {
                'string': 'mod balance',
                'weight': 1
            },
            {
                'string': 'this is a computer generated statement and does not require a signature',
                'weight': 1
            }
        ],
        'regex_words': [
            {
                'string': r'sbin\d{7}',
                'weight': 1
            }
        ],
        'table_headers': [
            {
                'string': 'txn date',
                'weight': 1
            },
            {
                'string': 'value',
                'weight': 1
            },
            {
                'string': 'description',
                'weight': 1
            },
            {
                'string': 'ref no./cheque',
                'weight': 1
            },
            {
                'string': 'debit',
                'weight': 1
            },
            {
                'string': 'credit',
                'weight': 1
            },
            {
                'string': 'balance',
                'weight': 1
            },
            {
                'string': 'date',
                'weight': 1
            },
            {
                'string': 'no.',
                'weight': 1
            },
            {
                'string': 'txn',
                'weight': 1
            },
            {
                'string': 'value date',
                'weight': 1
            }
        ]
    },
}
