PROMINENT_BANK_LIST = ['idfc_a', 'idbi_a', 'idbi_b', 'kotak_c', 'kotak_b',
                       'kotak_a', 'icici_a', 'hdfc_a', 'axis_a', 'axis_b', 'sbi_a', 'icici_b', ]

LESS_PROMINENT_BANK_LIST = ['citi_a', 'citi_b', 'canara_a', 'canara_b',
                            'yes_a', 'baroda_a', 'indusind_a', 'indusind_b',
                            'pnb_a', 'union_a', 'indian_a', 'andra_a', 'andra_b',
                            'corporation_a', 'oriental_a', 'overseas_a']

TABLE_ROW_MINIMUM_COVERAGE = 70

LESS_PROMINENT_BANK_MAX_CONSIDERATION = 8

PROMINENT_BANK_MINIMUM_SCORE = 50

PROMINENT_BANK_FEATURES = {
    'axis_a': {
        'keywords': {
            'features': [
                {
                    'string': 'statement of axis account no',
                    'weight': 1
                },
                {
                    'string': 'axis bank',
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
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(statement of axis account no(\s+)?:(\s+)?\d+(\s+)?for the period(\sof\s|\s+)?\(from(\s+)?:(\s+)?\d{2}-\d{2}-\d{4}(\s+)?to(\s+)?:(\s+)?\d{2}-\d{2}-\d{4}\))',
                    'weight': 1
                }],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 4,
                    'weight': 1
                },
                {
                    'maximum_columns': 7,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
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
            ],
            'weight': 2
        }
    },
    'axis_b': {
        'keywords': {
            'features': [
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
                    'string': 'registered office: "trishul" - 3rd floor, opp. samartheshwar temple, near law garden, ellisbridge, ahmedabad',
                    'weight': 1
                }
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(ifsc code(\s+)?:(\s+)?utib\d{7})',
                    'weight': 1
                },
                {
                    'string': r'(between(\s+)?\d{2}-\d{2}-\d{4}(\s+)?to(\s+)?\d{2}-\d{2}-\d{4})',
                    'weight': 1
                }
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 3,
                    'weight': 1
                },
                {
                    'maximum_columns': 4,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
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
                    'string': 'outstanding amount',
                    'weight': 1
                },
                {
                    'string': 'txn date',
                    'weight': 1
                },
                {
                    'string': 'transaction',
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
            ],
            'weight': 2
        }
    },
    'hdfc_a': {
        'keywords': {
            'features': [
                {
                    'string': 'hdfc bank limited',
                    'weight': 1
                },
                {
                    'string': 'hdfc bank service tax registration number',
                    'weight': 1
                },
                {
                    'string': 'hdfc bank house',
                    'weight': 1
                }
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'from(\s+)?:(\s+)?\d{2}/\d{2}/\d{2,4}(\s+)?to(\s+)?:(\s+)?\d{2}/\d{2}/\d{2,4}',
                    'weight': 1
                },
                {
                    'string': r'(hdfc\d{7})',
                    'weight': 1
                }
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 5,
                    'weight': 1
                },
                {
                    'maximum_columns': 7,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'date',
                    'weight': 1
                },
                {
                    'string': 'narration',
                    'weight': 1
                },
                {
                    'string': 'chq.',
                    'weight': 1
                },
                {
                    'string': 'ref.no.',
                    'weight': 1
                },
                {
                    'string': 'ref no.',
                    'weight': 1
                },
                {
                    'string': 'value d',
                    'weight': 1
                },
                {
                    'string': 'withdrawal am',
                    'weight': 1
                },
                {
                    'string': 'deposit am',
                    'weight': 1
                },
                {
                    'string': 'closing balance',
                    'weight': 1
                },
                {
                    'string': 'closing balnace',
                    'weight': 1
                }
            ],
            'weight': 2
        }
    },
    'icici_a': {
        'keywords': {
            'features': [
                {
                    'string': 'advanced search',
                    'weight': 1
                },
                {
                    'string': 'transaction date from',
                    'weight': 1
                },
                {
                    'string': 'cheque number from',
                    'weight': 1
                }
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 7,
                    'weight': 1
                },
                {
                    'maximum_columns': 9,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
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
            ],
            'weight': 2
        }
    },
    'icici_b': {
        'keywords': {
            'features': [
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
            'weight': 4
        },
        'regex_words': {
            'features': [],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 2,
                    'weight': 1
                },
                {
                    'maximum_columns': 9,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'account type',
                    'weight': 1
                },
                {
                    'string': 'a/c balance(i)',
                    'weight': 1
                },
                {
                    'string': 'nomination',
                    'weight': 1
                },
                {
                    'string': 'mode',
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
            ],
            'weight': 2
        }
    },
    'idbi_a': {
        'keywords': {
            'features': [
                {
                    'string': 'website:www.idbi.com',
                    'weight': 1
                },
                {
                    'string': 'idbi bank ltd',
                    'weight': 1
                }
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(transactions date from(\s+)?\d{2}/\d{2}/\d{2}(\s+)?to(\s+)?\d{2}/\d{2}/\d{2})',
                    'weight': 1
                }],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 4,
                    'weight': 1
                },
                {
                    'maximum_columns': 10,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
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
            ],
            'weight': 2
        }
    },
    'idbi_b': {
        'keywords': {
            'features': [],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(statement criteria(\s+)?:(\s+)?from(\s+)?\d{2}/\d{2}/\d{2}(\s+)?to(\s+)?\d{2}/\d{2}/\d{2})',
                    'weight': 1
                }],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 4,
                    'weight': 1
                },
                {
                    'maximum_columns': 10,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'sl',
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
                    'string': 'cheque no.',
                    'weight': 1
                },
                {
                    'string': 'cr/dr',
                    'weight': 1
                },
                {
                    'string': 'currency',
                    'weight': 1
                },
                {
                    'string': 'transaction amount',
                    'weight': 1
                },
                {
                    'string': 'balance amount',
                    'weight': 1
                }
            ],
            'weight': 2
        }
    },
    'idfc_a': {
        'keywords': {
            'features': [
                {
                    'string': 'banker@idfcbank.com',
                    'weight': 1
                }],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(registered office(\s+)?:(\s+)?idfc bank limited)',
                    'weight': 1
                },
                {
                    'string': r'(statement period(\s+)?:(\s+)?\d{2}-[a-za-z]{3}-\d{4}(\s+)?to(\s+)?\d{2}-[a-za-z]{3}-\d{4})',
                    'weight': 1
                }
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 3,
                    'weight': 1
                },
                {
                    'maximum_columns': 10,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
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
                }
            ],
            'weight': 2
        }
    },
    'kotak_a': {
        'keywords': {
            'features': [
                {
                    'string': 'cust.reln.no',
                    'weight': 1
                }],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(\d{2}-\d{2}-\d{4}(\s+)?to(\s+)?\d{2}-\d{2}-\d{4})',
                    'weight': 1
                }],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 3,
                    'weight': 1
                },
                {
                    'maximum_columns': 10,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'date',
                    'weight': 1
                },
                {
                    'string': 'narration',
                    'weight': 1
                },
                {
                    'string': 'chq/ref no',
                    'weight': 1
                },
                {
                    'string': 'withdrawal (dr)',
                    'weight': 1
                },
                {
                    'string': 'deposit (cr)',
                    'weight': 1
                },
                {
                    'string': 'balance',
                    'weight': 1
                }
            ],
            'weight': 2
        }
    },
    'kotak_b': {
        'keywords': {
            'features': [
                {
                    'string': 'kotak mahindra bank ltd',
                    'weight': 1
                },
                {
                    'string': 'overdraft sanction limit',
                    'weight': 1
                }
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(kkbk\d{7})',
                    'weight': 1
                },
                {
                    'string': r'(\d{2}-[a-zA-Z]{3}-\d{2} to \d{2}-[a-zA-Z]{3}-\d{2})',
                    'weight': 1
                }
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 4,
                    'weight': 1
                },
                {
                    'maximum_columns': 6,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
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
            ],
            'weight': 2
        }
    },
    'kotak_c': {
        'keywords': {
            'features': [
                {
                    'string': 'cust. reln. no.',
                    'weight': 1
                },
                {
                    'string': 'toll free or email at service.bank@kotak.com',
                    'weight': 1
                },
                {
                    'string': 'write to us at customer contact centre',
                    'weight': 1
                },
                {
                    'string': 'kotak mahindra bank ltd',
                    'weight': 1
                }
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(from \d{2}/\d{2}/\d{4}(\s+)?to(\s+)?\d{2}/\d{2}/\d{4})',
                    'weight': 1
                }],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 7,
                    'weight': 1
                },
                {
                    'maximum_columns': 8,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'account statement',
                    'weight': 1
                },
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
            ],
            'weight': 2
        }
    },
    'sbi_a': {
        'keywords': {
            'features': [
                {
                    'string': 'interest rate(% p.a.)',
                    'weight': 1
                },
                {
                    'string': 'account description',
                    'weight': 1
                },
                {
                    'string': 'mod balance',
                    'weight': 1
                }
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(ifs code(\s+)?:\(cid:9\)sbin\d{7})',
                    'weight': 1
                },
                {
                    'string': r'(micr code(\s+)?:\(cid:9\)\d{3}002\d{3})',
                    'weight': 1
                }
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 2,
                    'weight': 1
                },
                {
                    'maximum_columns': 6,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
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
                }
            ],
            'weight': 2
        }
    }
}

LESS_PROMINENT_BANK_FEATURES = {
    'citi_a': {
        'keywords': {
            'features': [
                {
                    'string': 'citibank account',
                    'weight': 1
                },
                {
                    'string': 'summary of transactions on savings account number',
                    'weight': 1
                },
                {
                    'string': 'statement period',
                    'weight': 1
                },
                {
                    'string': 'final tally',
                    'weight': 1
                },
                {
                    'string': 'closing balance:',
                    'weight': 1
                },
                {
                    'string': 'purchase subject:',
                    'weight': 1
                },
                {
                    'string': 'imps outward',
                    'weight': 1
                },
                {
                    'string': 'imps inward',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(statement period:(\s+)?[a-zA-Z]{3,9} \d{2},\d{4} to [a-zA-Z]{3,9} \d{2},\d{4})',
                    'weight': 1
                },
                {
                    'string': r'(opening balance:(\s+)?\d+.\d{2})',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 4,
                    'weight': 1
                },
                {
                    'maximum_columns': 4,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'date',
                    'weight': 1
                },
                {
                    'string': 'transaction details',
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
            ],
            'weight': 2
        }
    },
    'citi_b': {
        'keywords': {
            'features': [
                {
                    'string': 'citibank account',
                    'weight': 1
                },
                {
                    'string': 'savings account details for account number',
                    'weight': 1
                },
                {
                    'string': 'statement period',
                    'weight': 1
                },
                {
                    'string': 'your citibank account statement as on',
                    'weight': 1
                },
                {
                    'string': 'branch address:',
                    'weight': 1
                },
                {
                    'string': 'branch phone no',
                    'weight': 1
                },
                {
                    'string': 'imps outward',
                    'weight': 1
                },
                {
                    'string': 'imps inward',
                    'weight': 1
                },
                {
                    'string': 'funds on earmarking / hold',
                    'weight': 1
                },
                {
                    'string': 'banking reward points for the a/c',
                    'weight': 1
                },
                {
                    'string': 'www.citi.co.in/',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(ifsc(\s+)?:(\s+)?citi\d{7})',
                    'weight': 1
                },
                {
                    'string': r'(micr code(\s+)?:(\s+)?\d{3}037\d{3})',
                    'weight': 1
                },
                {
                    'string': r'(statement period:(\s+)?[a-zA-Z]{3,9}(\s+)?\d{1,2},(\s+)?\d{4}(\s+)?to(\s+)?[a-zA-Z]{3,9}(\s+)?\d{1,2},(\s+)?\d{4})',
                    'weight': 1
                },
                {
                    'string': r'(opening balance:(\s+)?\d+.\d{2})',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 2,
                    'weight': 1
                },
                {
                    'maximum_columns': 4,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'transaction details',
                    'weight': 1
                },
                {
                    'string': 'withdrawals (inr)',
                    'weight': 1
                },
                {
                    'string': 'deposits (inr)',
                    'weight': 1
                },
                {
                    'string': 'balance(inr)',
                    'weight': 1
                },
                {
                    'string': 'date',
                    'weight': 1
                },
            ],
            'weight': 2
        }
    },
    'canara_a': {
        'keywords': {
            'features': [
                {
                    'string': 'searched by',
                    'weight': 1
                },
                {
                    'string': 'customer name',
                    'weight': 1
                },
                {
                    'string': 'account currency',
                    'weight': 1
                },
                {
                    'string': 'balance b/f',
                    'weight': 1
                },
                {
                    'string': 'branch',
                    'weight': 1
                },
                {
                    'string': 'customer id',
                    'weight': 1
                },
                {
                    'string': 'closing balance',
                    'weight': 1
                },
                {
                    'string': 'imps inward',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(\d{2}-\d{2}-\d{4}(\s+)?to(\s+)?\d{2}-\d{2}-\d{4})',
                    'weight': 1
                },
                {
                    'string': r'(account statement as of(\s+)?\d{2}-\d{2}-\d{4}(\s+)?\d{2}:\d{2}:\d{2}(\s+)?gmt)',
                    'weight': 1
                },
                {
                    'string': r'(opening balance:(\s+)?\d+.\d{2})',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 5,
                    'weight': 1
                },
                {
                    'maximum_columns': 10,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'txn date',
                    'weight': 1
                },
                {
                    'string': 'value date',
                    'weight': 1
                },
                {
                    'string': 'cheque no.',
                    'weight': 1
                },
                {
                    'string': 'description',
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
            ],
            'weight': 2
        }
    },
    'canara_b': {
        'keywords': {
            'features': [
                {
                    'string': 'customer id',
                    'weight': 1
                },
                {
                    'string': 'account name',
                    'weight': 1
                },
                {
                    'string': 'address',
                    'weight': 1
                },
                {
                    'string': 'account description',
                    'weight': 1
                },
                {
                    'string': 'ifsc code',
                    'weight': 1
                },
                {
                    'string': 'branch',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(cnrb\d{7})',
                    'weight': 1
                },
                {
                    'string': r'(Account Statement from(\s+)?\d{2} [a-zA-Z]{3} \d{4}(\s+)?to(\s+)?\d{2} [a-zA-Z]{3} \d{4})',
                    'weight': 1
                },
                {
                    'string': r'(please(\s+)?do(\s+)?not(\s+)?share(\s+)?your(\s+)?atm,(\s+)?debit/credit(\s+)?card(\s+)?number,(\s+)?pin(\s+)?and(\s+)?otp(\s+)?with(\s+)?anyone(\s+)?over(\s+)?mail,(\s+)?sms,(\s+)?phone(\s+)?call(\s+)?or(\s+)?any(\s+)?other(\s+)?media.(\s+)?bank(\s+)?never(\s+)?asks(\s+)?for(\s+)?such(\s+)?information.)',
                    'weight': 1
                },
                {
                    'string': r'(this(\s+)is(\s+)a(\s+)computer(\s+)generated(\s+)statement(\s+)and(\s+)does(\s+)not(\s+)require(\s+)a(\s+)signature.)',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 3,
                    'weight': 1
                },
                {
                    'maximum_columns': 10,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'txn date',
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
                    'string': 'value',
                    'weight': 1
                },
            ],
            'weight': 2
        }
    },
    'yes_a': {
        'keywords': {
            'features': [
                {
                    'string': 'statement of accounts',
                    'weight': 1
                },
                {
                    'string': 'your branch details :',
                    'weight': 1
                },
                {
                    'string': 'this is a system generated statement and does not require signature.',
                    'weight': 1
                },
                {
                    'string': 'nomination:',
                    'weight': 1
                },
                {
                    'string': 'account status:',
                    'weight': 1
                },
                {
                    'string': 'yes for you!',
                    'weight': 1
                },
                {
                    'string': 'transaction codes in your account statement',
                    'weight': 1
                },
                {
                    'string': 'closing balance figure includes funds not clear, hold amounts if any.',
                    'weight': 1
                },
                {
                    'string': 'applicable service tax is levied on all items of service charges levied by the bank for services rendered',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features':  [
                {
                    'string': r'(ifsc(\s+)?:(\s+)?yesb\d{7})',
                    'weight': 1
                },
                {
                    'string': r'(micr(\s+)?:(\s+)?\d{3}532\d{3})',
                    'weight': 1
                },
                {
                    'string': r'(period(\s+)?:(\s+)?[a-za-z]{3,9} \d{2}, \d{4}(\s+)?to(\s+)?[a-za-z]{3,9} \d{2}, \d{4})',
                    'weight': 1
                },
                {
                    'string': r'(transaction details for your account no.\d+)',
                    'weight': 1
                },
                {
                    'string': r'(opening balance:(\s+)?\d+.\d{2})',
                    'weight': 1
                },
                {
                    'string': r'(od limit:(\s+)?\d+.\d{2})',
                    'weight': 1
                },
                {
                    'string': r'(total debits:(\s+)?\d+)',
                    'weight': 1
                },
                {
                    'string': r'(total credits:(\s+)?\d+)',
                    'weight': 1
                },
                {
                    'string': r'(closing balance:(\s+)?\d+.\d{2})',
                    'weight': 1
                },
                {
                    'string': r'(unclear amt:(\s+)?\d+.\d{2})',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 2,
                    'weight': 1
                },
                {
                    'maximum_columns': 6,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'transaction',
                    'weight': 1
                },
                {
                    'string': 'description',
                    'weight': 1
                },
                {
                    'string': 'value date',
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
            ],
            'weight': 2
        }
    },
    'baroda_a': {
        'keywords': {
            'features': [
                {
                    'string': 'bank of baroda',
                    'weight': 1
                },
                {
                    'string': 'account statement',
                    'weight': 1
                },
                {
                    'string': 'account number',
                    'weight': 1
                },
                {
                    'string': 'currency code',
                    'weight': 1
                },
                {
                    'string': 'branch name',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(From(\s+)\d{2}/\d{2}/\d{2,4}(\s+)?to(\s+)?\d{2}/\d{2}/\d{2,4})',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 7,
                    'weight': 1
                },
                {
                    'maximum_columns': 8,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features':  [
                {
                    'string': 's.no',
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
                    'string': 'cheque',
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
                    'string': 'value date',
                    'weight': 1
                },
            ],
            'weight': 2
        }
    },
    'indusind_a': {
        'keywords': {
            'features': [
                {
                    'string': 'savings account indus comfort',
                    'weight': 1
                },
                {
                    'string': 'account branch',
                    'weight': 1
                },
                {
                    'string': 'address',
                    'weight': 1
                },
                {
                    'string': 'account type',
                    'weight': 1
                },
                {
                    'string': 'this is a computer generated statement and does not require signature.',
                    'weight': 1
                },
                {
                    'string': 'transfer credit',
                    'weight': 1
                },
                {
                    'string': 'transfer debit',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(account([a-zA-Z.\s]+)?(\s+)?:(\s+)?\d{12})',
                    'weight': 1
                },
                {
                    'string': r'(From(\s+):(\s+)[a-zA-Z]{3} \d{1,2}, \d{4}(\s+)?To(\s+)?:(\s+)[a-zA-Z]{3} \d{1,2}, \d{4})',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 4,
                    'weight': 1
                },
                {
                    'maximum_columns': 9,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'date',
                    'weight': 1
                },
                {
                    'string': 'type',
                    'weight': 1
                },
                {
                    'string': 'description',
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
            ],
            'weight': 2
        }
    },
    'indusind_b': {
        'keywords': {
            'features': [
                {
                    'string': 'reachus@indusind.com',
                    'weight': 1
                },
                {
                    'string': 'www.indusind.com',
                    'weight': 1
                },
                {
                    'string': 'indusind bank ltd',
                    'weight': 1
                },
                {
                    'string': 'l65191pn1994plc076333',
                    'weight': 1
                },
                {
                    'string': 'aaaci1314gst001',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'(saving(s)?(\s+)?account(\s+)?-(\s+)?indus(\s+)?comfort)',
                    'weight': 1
                },
                {
                    'string': r'(\d{2}-[a-zA-Z]{3}-\d{4}(\s+)?To(\s+)?\d{2}-[a-zA-Z]{3}-\d{4})',
                    'weight': 1
                }
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 2,
                    'weight': 1
                },
                {
                    'maximum_columns': 4,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'date',
                    'weight': 1
                },
                {
                    'string': 'particulars',
                    'weight': 1
                },
                {
                    'string': 'chq./ref. no',
                    'weight': 1
                },
                {
                    'string': 'closing balance',
                    'weight': 1
                },
                {
                    'string': 'withdrawal',
                    'weight': 1
                },
                {
                    'string': 'deposit',
                    'weight': 1
                },
                {
                    'string': 'balance',
                    'weight': 1
                }
            ],
            'weight': 2
        }
    },
    'pnb_a': {
        'keywords': {
            'features': [
                    {
                        'string': 'account statement for account number',
                        'weight': 1
                    },
                {
                        'string': 'branch details',
                        'weight': 1
                        },
                {
                        'string': 'customer details',
                        'weight': 1
                        },
                {
                        'string': 'please ensure that all the cheque leaves in your custody are duly branded',
                        'weight': 1
                        },
                {
                        'string': 'customers are requested in their own interest not to issue cheques without',
                        'weight': 1
                        },
                {
                        'string': 'please maintain minimum average balance',
                        'weight': 1
                        },
                {
                        'string': 'to avoid levy of charges',
                        'weight': 1
                        },
                {
                        'string': 'pls note penal interest may be charged in loan accounts due to financial reasons',
                        'weight': 1
                        },
                {
                        'string': 'quarterly average balances',
                        'weight': 1
                        },
                {
                        'string': 'ledger folio charges',
                        'weight': 1
                        },
                {
                        'string': 'point of sale',
                        'weight': 1
                        },
            ],
            'weight': 4
        },
        'regex_words': {
            'features': [
                {
                    'string': r'([0-9,]+\d{0,3}\.\d{2} [C|D]r.)',
                    'weight': 1
                },
                {
                    'string': r'(\d{2}[/|-][a-zA-Z0-9]{2,3}[/|-]\d{4}(\s+)?to(\s+)?\d{2}[/|-][a-zA-Z0-9]{2,3}[/|-]\d{4})',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 3,
                    'weight': 1
                },
                {
                    'maximum_columns': 5,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'date',
                    'weight': 1
                },
                {
                    'string': 'narration',
                    'weight': 1
                },
                {
                    'string': 'cheque',
                    'weight': 1
                },
                {
                    'string': 'withdrawal',
                    'weight': 1
                },
                {
                    'string': 'deposit',
                    'weight': 1
                },
                {
                    'string': 'balance',
                    'weight': 1
                },
                {
                    'string': 'transaction',
                    'weight': 1
                },
                {
                    'string': 'number',
                    'weight': 1
                }
            ],
            'weight': 2
        }
    },
    'union_a': {
        'keywords': {
            'features': [
                {
                    'string': 'account statement through internet banking',
                    'weight': 1
                },
                {
                    'string': 'account name',
                    'weight': 1
                },
                {
                    'string': 'addressline1',
                    'weight': 1
                },
                {
                    'string': 'addressline2',
                    'weight': 1
                },
                {
                    'string': 'bank id',
                    'weight': 1
                },
                {
                    'string': 'branch id',
                    'weight': 1
                },
                {
                    'string': 'branch name',
                    'weight': 1
                },
                {
                    'string': 'full statement',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features':  [
                {
                    'string': r'(Date ranging from(\s+)?\d{2}/\d{2}/\d{4}(\s+)?to(\s+)?\d{2}/\d{2}/\d{4})',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 7,
                    'weight': 1
                },
                {
                    'maximum_columns': 8,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'tran id',
                    'weight': 1
                },
                {
                    'string': 'txn date',
                    'weight': 1
                },
                {
                    'string': 'cheque no',
                    'weight': 1
                },
                {
                    'string': 'description',
                    'weight': 1
                },
                {
                    'string': 'currency',
                    'weight': 1
                },
                {
                    'string': 'cr/dr',
                    'weight': 1
                },
                {
                    'string': 'amount',
                    'weight': 1
                },
                {
                    'string': 'balance',
                    'weight': 1
                },
                {
                    'string': 'personal details',
                    'weight': 1
                },
                {
                    'string': 'account details',
                    'weight': 1
                },
            ],
            'weight': 2
        }
    },
    'indian_a': {
        'keywords': {
            'features': [
                {
                    'string': 'indian bank',
                    'weight': 1
                },
                {
                    'string': 'branch code',
                    'weight': 1
                },
                {
                    'string': 'account number :',
                    'weight': 1
                },
                {
                    'string': 'product type :',
                    'weight': 1
                },
                {
                    'string': 'email :',
                    'weight': 1
                },
                {
                    'string': 'statement date :',
                    'weight': 1
                },
                {
                    'string': 'cleared balance :',
                    'weight': 1
                },
                {
                    'string': 'uncleared amount :',
                    'weight': 1
                },
                {
                    'string': 'drawing power :',
                    'weight': 1
                },
                {
                    'string': 'interest rate :',
                    'weight': 1
                },
                {
                    'string': 'statement downloaded by',
                    'weight': 1
                },
                {
                    'string': 'end of statement - from internet banking',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features':  [
                {
                    'string': r'(statement of account from(\s+)?\d{2}/\d{2}/\d{4}(\s+)?to(\s+)?\d{2}/\d{2}/\d{4})',
                    'weight': 1
                },
                {
                    'string': r'(for account number(\s+)?\d+)',
                    'weight': 1
                },


            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 4,
                    'weight': 1
                },
                {
                    'maximum_columns': 6,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'value',
                    'weight': 1
                },
                {
                    'string': 'post date',
                    'weight': 1
                },
                {
                    'string': 'remitter',
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
                    'string': 'branch',
                    'weight': 1
                },
                {
                    'string': 'dr',
                    'weight': 1
                },
                {
                    'string': 'cr',
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
                    'string': 'balance b/f',
                    'weight': 1
                },
            ],
            'weight': 2
        }
    },
    'andra_a': {
        'keywords': {
            'features': [
                {
                    'string': 'name',
                    'weight': 1
                },
                {
                    'string': 'address',
                    'weight': 1
                },
                {
                    'string': 'branch',
                    'weight': 1
                },
                {
                    'string': 'branch address',
                    'weight': 1
                },
                {
                    'string': 'ifsc code',
                    'weight': 1
                },
                {
                    'string': 'opening balance',
                    'weight': 1
                },
                {
                    'string': 'note: this is a system generated report need not to be signed.',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features':  [
                {
                    'string': r'(andb\d{7})',
                    'weight': 1
                },
                {
                    'string': r'(Account Statement of(\s+)?\d*(\s+)?from(\s+)?\d{2}-\d{2}-\d{4}(\s+)?to(\s+)?\d{2}-\d{2}-\d{4})',
                    'weight': 1
                }
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 3,
                    'weight': 1
                },
                {
                    'maximum_columns': 4,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'date',
                    'weight': 1
                },
                {
                    'string': 'description',
                    'weight': 1
                },
                {
                    'string': 'withdrawal',
                    'weight': 1
                },
                {
                    'string': 'deposit',
                    'weight': 1
                },
                {
                    'string': 'balance',
                    'weight': 1
                },
            ],
            'weight': 2
        }
    },
    'andra_b': {
        'keywords': {
            'features': [
                {
                    'string': 'account name',
                    'weight': 1
                },
                {
                    'string': 'address1',
                    'weight': 1
                },
                {
                    'string': 'pin code',
                    'weight': 1
                },
                {
                    'string': 'branch code',
                    'weight': 1
                },
                {
                    'string': 'branch city ',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features':  [
                {
                    'string': r'(Statement of account(\s+)?\d*(\s+)?for the period of(\s+)?\d{2}/\d{2}/\d{2}(\s+)?to(\s+)?\d{2}/\d{2}/\d{2})',
                    'weight': 1
                },
                {
                    'string': r'(branch ifsc(\s+)?:(\s+)?andb\d{7})',
                    'weight': 1
                },
                {
                    'string': r'(branch micr(\s+)?:(\s+)?\d{3}011\d{3})',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 4,
                    'weight': 1
                },
                {
                    'maximum_columns': 5,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'tran',
                    'weight': 1
                },
                {
                    'string': 'date',
                    'weight': 1
                },
                {
                    'string': 'cheque no',
                    'weight': 1
                },
                {
                    'string': 'transaction',
                    'weight': 1
                },
                {
                    'string': 'description',
                    'weight': 1
                },
                {
                    'string': 'withdrawals(rs.)',
                    'weight': 1
                },
                {
                    'string': 'deposits (rs.)',
                    'weight': 1
                },
                {
                    'string': 'balance (rs.)',
                    'weight': 1
                }
            ],
            'weight': 2
        }
    },
    'corporation_a': {
        'keywords': {
            'features': [
                {
                    'string': 'statement of accounts',
                    'weight': 1
                },
                {
                    'string': 'address',
                    'weight': 1
                },
                {
                    'string': 'pin code',
                    'weight': 1
                },
                {
                    'string': 'branch address',
                    'weight': 1
                },
                {
                    'string': 'currency',
                    'weight': 1
                },
                {
                    'string': 'branch :',
                    'weight': 1
                },
                {
                    'string': 'account total',
                    'weight': 1
                },
                {
                    'string': 'branch total',
                    'weight': 1
                },
                {
                    'string': 'grand total',
                    'weight': 1
                },
                {
                    'string': 'some of the transactions pending for updation are not shown in this statement. to know the exact balance, you can do the balance enquiry.',
                    'weight': 1
                },
                {
                    'string': 'this report is generated from the data available at web centre.',
                    'weight': 1
                },
                {
                    'string': 'please contact the web centre / branch if there is any discrepancy in the report.',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features':  [
                {
                    'string': r'(From Date(\s+)?:(\s+)?\d{2}/\d{2}/\d{4}(\s+)?To Date(\s+)?:(\s+)?\d{2}/\d{2}/\d{4})',
                    'weight': 1
                },
                {
                    'string': r'(ifsc code(\s+)?:(\s+)?corp\d{7})',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 5,
                    'weight': 1
                },
                {
                    'maximum_columns': 6,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'txn. date',
                    'weight': 1
                },
                {
                    'string': 'particulars',
                    'weight': 1
                },
                {
                    'string': 'chq no.',
                    'weight': 1
                },
                {
                    'string': 'txn.type',
                    'weight': 1
                },
                {
                    'string': 'withdrawal',
                    'weight': 1
                },
                {
                    'string': 'deposit',
                    'weight': 1
                },
                {
                    'string': 'balance',
                    'weight': 1
                },
            ],
            'weight': 2
        }
    },
    'oriental_a': {
        'keywords': {
            'features': [
                {
                    'string': 'account statement for account number',
                    'weight': 1
                },
                {
                    'string': 'branch details',
                    'weight': 1
                },
                {
                    'string': 'branch details',
                    'weight': 1
                },
                {
                    'string': 'bank address',
                    'weight': 1
                },
                {
                    'string': 'acc. statement date',
                    'weight': 1
                },
                {
                    'string': 'customer details',
                    'weight': 1
                },
                {
                    'string': 'customer name ',
                    'weight': 1
                },
                {
                    'string': 'oriental bank of commerce',
                    'weight': 1
                },
                {
                    'string': 'nominee',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features':  [
                {
                    'string': r'(Statement Period(\s+)?:(\s+)?From Date(\s+)?:(\s+)?\d{2}/\d{2}/\d{4}(\s+)?To Date(\s+)?:(\s+)?\d{2}/\d{2}/\d{4})',
                    'weight': 1
                },
                {
                    'string': r'(ifsc code(\s+)?:(\s+)?orbc\d{7})',
                    'weight': 1
                },
            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 5,
                    'weight': 1
                },
                {
                    'maximum_columns': 7,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'sl.',
                    'weight': 1
                },
                {
                    'string': 'transaction',
                    'weight': 1
                },
                {
                    'string': 'value date',
                    'weight': 1
                },
                {
                    'string': 'instrument',
                    'weight': 1
                },
                {
                    'string': 'account',
                    'weight': 1
                },
                {
                    'string': 'date',
                    'weight': 1
                },
                {
                    'string': 'narration',
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
                    'string': 'remarks',
                    'weight': 1
                },
            ],
            'weight': 2
        }
    },
    'overseas_a': {
        'keywords': {
            'features': [
                {
                    'string': 'denotes cancelled transaction',
                    'weight': 1
                },
                {
                    'string': 'email id',
                    'weight': 1
                },
                {
                    'string': 'customer id',
                    'weight': 1
                },
                {
                    'string': 'open dt',
                    'weight': 1
                },
                {
                    'string': 'status',
                    'weight': 1
                },
                {
                    'string': 'address',
                    'weight': 1
                },
            ],
            'weight': 4
        },
        'regex_words': {
            'features':  [
                {
                    'string': r'(Statement for the period from(\s+)?\d{2}/\d{2}/\d{4}(\s+)?to(\s+)?\d{2}/\d{2}/\d{4})',
                    'weight': 1
                },
                {
                    'string': r'(ifsc(\s+)?code(\s+)?[:|-](\s+)?ioba\d{7})',
                    'weight': 1
                },
                {
                    'string': r'(micr(\s+)?code(\s+)?[:|-](\s+)?\d{3}020\d{3})',
                    'weight': 1
                },

            ],
            'weight': 3
        },
        'table_dimensions': {
            'features': [
                {
                    'minimum_columns': 5,
                    'weight': 1
                },
                {
                    'maximum_columns': 5,
                    'weight': 1
                }
            ],
            'weight': 1
        },
        'table_headers': {
            'features': [
                {
                    'string': 'date',
                    'weight': 1
                },
                {
                    'string': 'chq',
                    'weight': 1
                },
                {
                    'string': 'naration',
                    'weight': 1
                },
                {
                    'string': 'cod',
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
                    'string': 'no',
                    'weight': 1
                },
            ],
            'weight': 2
        }
    },
}
