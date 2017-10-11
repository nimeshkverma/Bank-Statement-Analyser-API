PROMINENT_BANK_LIST = ['idfc_a', 'idbi_a', 'idbi_b', 'kotak_c', 'kotak_b',
                       'kotak_a', 'icici_a', 'hdfc_a', 'axis_a', 'axis_b', 'sbi_a', 'icici_b', ]

TABLE_ROW_MINIMUM_COVERAGE = 70

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
                    'minimum_columns': 3,
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


# PROMINENT_BANK_CONSTANTS = {
#     'idfc_a': {
#         'keywords': [
#             {
#                 'string': 'banker@idfcbank.com',
#                 'weight': 1
#             }
#         ],
#         'regex_words': [
#             {
#                 'string': r'(registered office(\s+)?:(\s+)?idfc bank limited)',
#                 'weight': 1
#             },
#             {
#                 'string':  r'(STATEMENT PERIOD(\s+)?:(\s+)?\d{2}-[a-zA-Z]{3}-\d{4}(\s+)?to(\s+)?\d{2}-[a-zA-Z]{3}-\d{4})',
#                 'weight': 1
#             }
#         ],
#         'table_headers': [
#             {
#                 'string': 'opening balance',
#                 'weight': 1
#             },
#             {
#                 'string': 'total debit',
#                 'weight': 1
#             },
#             {
#                 'string': 'total credit',
#                 'weight': 1
#             },
#             {
#                 'string': 'closing balance',
#                 'weight': 1
#             },
#             {
#                 'string': 'date',
#                 'weight': 1
#             },
#             {
#                 'string': 'particulars',
#                 'weight': 1
#             },
#             {
#                 'string': 'cheque no.',
#                 'weight': 1
#             },
#             {
#                 'string': 'debit',
#                 'weight': 1
#             },
#             {
#                 'string': 'credit',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance',
#                 'weight': 1
#             }]
#     },
#     'idbi_a': {
#         'keywords': [
#             {
#                 'string': 'website:www.idbi.com',
#                 'weight': 1
#             },
#             {
#                 'string': 'idbi bank ltd',
#                 'weight': 1
#             },
#         ],
#         'regex_words': [
#             {
#                 'string': r'(transactions date from(\s+)?\d{2}/\d{2}/\d{2}(\s+)?to(\s+)?\d{2}/\d{2}/\d{2})',
#                 'weight': 1
#             }
#         ],
#         'table_headers': [
#             {
#                 'string': 'srl',
#                 'weight': 1
#             },
#             {
#                 'string': 'txn date',
#                 'weight': 1
#             },
#             {
#                 'string': 'value date',
#                 'weight': 1
#             },
#             {
#                 'string': 'description',
#                 'weight': 1
#             },
#             {
#                 'string': 'cheque',
#                 'weight': 1
#             },
#             {
#                 'string': 'cr/dr',
#                 'weight': 1
#             },
#             {
#                 'string': 'ccy',
#                 'weight': 1
#             },
#             {
#                 'string': 'trxn amount',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance',
#                 'weight': 1
#             }
#         ]
#     },
#     'idbi_b': {
#         'keywords': [],
#         'regex_words': [
#             {
#                 'string': r'(statement criteria(\s+)?:(\s+)?from(\s+)?\d{2}/\d{2}/\d{2}(\s+)?to(\s+)?\d{2}/\d{2}/\d{2})',
#                 'weight': 1
#             }
#         ],
#         'table_headers': [
#             {
#                 'string': 'sl no.',
#                 'weight': 1
#             },
#             {
#                 'string': 'txn date',
#                 'weight': 1
#             },
#             {
#                 'string': 'value date',
#                 'weight': 1
#             },
#             {
#                 'string': 'description',
#                 'weight': 1
#             },
#             {
#                 'string': 'cheque no.',
#                 'weight': 1
#             },
#             {
#                 'string': 'cr/dr',
#                 'weight': 1
#             },
#             {
#                 'string': 'currency',
#                 'weight': 1
#             },
#             {
#                 'string': 'transaction amount',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance amount',
#                 'weight': 1
#             }
#         ]
#     },
#     'kotak_c': {
#         'keywords': [
#             {
#                 'string': 'cust. reln. no.',
#                 'weight': 1
#             },
#             {
#                 'string': 'toll free or email at service.bank@kotak.com',
#                 'weight': 1
#             },
#             {
#                 'string': 'write to us at customer contact centre',
#                 'weight': 1
#             },
#             {
#                 'string': 'kotak mahindra bank ltd',
#                 'weight': 1
#             }
#         ],
#         'regex_words': [
#             {
#                 'string':  r'(from \d{2}/\d{2}/\d{4}(\s+)?to(\s+)?\d{2}/\d{2}/\d{4})',
#                 'weight': 1
#             },
#         ],
#         'table_headers': [
#             {
#                 'string': 'account statement',
#                 'weight': 1
#             },
#             {
#                 'string': 'sl. no.',
#                 'weight': 1
#             },
#             {
#                 'string': 'date',
#                 'weight': 1
#             },
#             {
#                 'string': 'description',
#                 'weight': 1
#             },
#             {
#                 'string': 'chq / ref number',
#                 'weight': 1
#             },
#             {
#                 'string': 'amount',
#                 'weight': 1
#             },
#             {
#                 'string': 'dr / cr',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance',
#                 'weight': 1
#             },
#             {
#                 'string': 'dr / cr',
#                 'weight': 1
#             }
#         ]
#     },
#     'kotak_b': {
#         'keywords': [
#             {
#                 'string': 'kotak mahindra bank ltd',
#                 'weight': 1
#             },
#             {
#                 'string': 'overdraft sanction limit',
#                 'weight': 1
#             }
#         ],
#         'regex_words': [
#             {
#                 'string': r'(\d{2}-[a-zA-Z]{3}-\d{2} to \d{2}-[a-zA-Z]{3}-\d{2})',
#                 'weight': 1
#             },
#             {
#                 'string':   r'(kkbk\d{7})',
#                 'weight': 1
#             },
#         ],
#         'table_headers': [
#             {
#                 'string': 'date',
#                 'weight': 1
#             },
#             {
#                 'string': 'narration',
#                 'weight': 1
#             },
#             {
#                 'string': 'chq/ref no.',
#                 'weight': 1
#             },
#             {
#                 'string': 'withdrawal (dr)/deposit (cr)',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance',
#                 'weight': 1
#             }
#         ]
#     },
#     'kotak_a': {
#         'keywords': [
#             {
#                 'string': 'cust.reln.no',
#                 'weight': 1
#             },
#         ],
#         'regex_words': [
#             {
#                 'string': r'(\d{2}-\d{2}-\d{4}(\s+)?to(\s+)?\d{2}-\d{2}-\d{4})',
#                 'weight': 1
#             },
#         ],
#         'table_headers': [
#             {
#                 'string': 'date',
#                 'weight': 1
#             },
#             {
#                 'string': 'narration',
#                 'weight': 1
#             },
#             {
#                 'string': 'chq/ref no',
#                 'weight': 1
#             },
#             {
#                 'string': 'withdrawal (dr)',
#                 'weight': 1
#             },
#             {
#                 'string': ' deposit (cr)',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance',
#                 'weight': 1
#             },
#         ]
#     },
#     'icici_a': {
#         'keywords': [
#             {
#                 'string': 'advanced search',
#                 'weight': 1
#             },
#             {
#                 'string': 'transaction date from',
#                 'weight': 1
#             },
#             {
#                 'string': 'cheque number from',
#                 'weight': 1
#             },
#         ],
#         'regex_words': [],
#         'table_headers': [
#             {
#                 'string': 's no.',
#                 'weight': 1
#             },
#             {
#                 'string': 'value date',
#                 'weight': 1
#             },
#             {
#                 'string': 'transaction date',
#                 'weight': 1
#             },
#             {
#                 'string': 'cheque number',
#                 'weight': 1
#             },
#             {
#                 'string': 'transaction remarks',
#                 'weight': 1
#             },
#             {
#                 'string': 'withdrawal amount',
#                 'weight': 1
#             },
#             {
#                 'string': 'deposit amount',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance (inr )',
#                 'weight': 1
#             }
#         ]
#     },
#     'hdfc_a': {
#         'keywords': [
#             {
#                 'string': 'hdfc bank limited',
#                 'weight': 1
#             },
#             {
#                 'string': 'hdfc bank service tax registration number',
#                 'weight': 1
#             },
#             {
#                 'string': 'hdfc bank house',
#                 'weight': 1
#             },
#         ],
#         'regex_words': [
#             {
#                 'string': r'(hdfc\d{7})',
#                 'weight': 1
#             },
#             {
#                 'string': r'from(\s+)?:(\s+)?\d{2}/\d{2}/\d{2,4}(\s+)?to(\s+)?:(\s+)?\d{2}/\d{2}/\d{2,4}',
#             }
#         ],
#         'table_headers': [
#             {
#                 'string': 'date',
#                 'weight': 1
#             },
#             {
#                 'string': 'narration',
#                 'weight': 1
#             },
#             {
#                 'string': 'chq./ref.no.',
#                 'weight': 1
#             },
#             {
#                 'string': 'value dt',
#                 'weight': 1
#             },
#             {
#                 'string': 'withdrawal amt.',
#                 'weight': 1
#             },
#             {
#                 'string': 'deposit amt.',
#                 'weight': 1
#             },
#             {
#                 'string': 'closing balance',
#                 'weight': 1
#             }
#         ]
#     },
#     'axis_a': {
#         'keywords': [
#             {
#                 'string': 'statement of axis account no',
#                 'weight': 1
#             },
#             {
#                 'string': 'axis bank',
#                 'weight': 1
#             },
#             {
#                 'string': 'www.axisbank.com',
#                 'weight': 1
#             },
#             {
#                 'string': 'customer.service@axisbank.com',
#                 'weight': 1
#             },
#             {
#                 'string': 'registered office - axis bank ltd,trishul,opp. samartheswar temple, near law garden, ellisbridge',
#                 'weight': 1
#             }
#         ],
#         'regex_words': [
#             {
#                 'string': r'(statement of axis account no(\s+)?:(\s+)?\d+(\s+)?for the period(\sof\s|\s+)?\(from(\s+)?:(\s+)?\d{2}-\d{2}-\d{4}(\s+)?to(\s+)?:(\s+)?\d{2}-\d{2}-\d{4}\))',
#                 'weight': 1
#             }
#         ],
#         'table_headers': [
#             {
#                 'string': 'tran date',
#                 'weight': 1
#             },
#             {
#                 'string': 'chq no',
#                 'weight': 1
#             },
#             {
#                 'string': 'particulars',
#                 'weight': 1
#             },
#             {
#                 'string': 'debit',
#                 'weight': 1
#             },
#             {
#                 'string': 'credit',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance',
#                 'weight': 1
#             },
#             {
#                 'string': 'init.',
#                 'weight': 1
#             }

#         ]
#     },
#     'axis_b': {
#         'keywords': [
#             {
#                 'string': 'axis bank',
#                 'weight': 1
#             },
#             {
#                 'string': 'www.axisbank.com',
#                 'weight': 1
#             },
#             {
#                 'string': 'relationship summary as on date',
#                 'weight': 1
#             },
#             {
#                 'string': 'profile completeness',
#                 'weight': 1
#             },
#             {
#                 'string': 'registered office: "trishul" - 3rd floor, opp. samartheshwar temple, near law garden, ellisbridge, ahmedabad',
#                 'weight': 1
#             }
#         ],
#         'regex_words': [
#             {
#                 'string': r'(ifsc code(\s+)?:(\s+)?utib\d{7})',
#                 'weight': 1
#             },
#             {
#                 'string': r'(between(\s+)?\d{2}-\d{2}-\d{4}(\s+)?to(\s+)?\d{2}-\d{2}-\d{4})',
#                 'weight': 1
#             }
#         ],
#         'table_headers': [
#             {
#                 'string': 'bank account',
#                 'weight': 1
#             },
#             {
#                 'string': 'crn',
#                 'weight': 1
#             },
#             {
#                 'string': 'amount',
#                 'weight': 1
#             },
#             {
#                 'string': 'other account',
#                 'weight': 1
#             },
#             {
#                 'string': 'outstanding amount',
#                 'weight': 1
#             },
#             {
#                 'string': 'txn date',
#                 'weight': 1
#             },
#             {
#                 'string': 'transaction',
#                 'weight': 1
#             },
#             {
#                 'string': 'withdrawals',
#                 'weight': 1
#             },
#             {
#                 'string': 'deposits',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance',
#                 'weight': 1
#             },
#             {
#                 'string': 'information',
#                 'weight': 1
#             }
#         ]
#     },
#     'sbi_a': {
#         'keywords': [
#             {
#                 'string': 'interest rate(% p.a.)',
#                 'weight': 1
#             },
#             {
#                 'string': 'account description',
#                 'weight': 1
#             },
#             {
#                 'string': 'mod balance',
#                 'weight': 1
#             },
#         ],
#         'regex_words': [
#             {
#                 'string': r'(ifs code(\s+)?:\(cid:9\)sbin\d{7})',

#                 'weight': 1
#             },
#             {
#                 'string': r'(micr code(\s+)?:\(cid:9\)\d{3}002\d{3})',
#                 'weight': 1
#             }
#         ],
#         'table_headers': [
#             {
#                 'string': 'txn date',
#                 'weight': 1
#             },
#             {
#                 'string': 'value',
#                 'weight': 1
#             },
#             {
#                 'string': 'description',
#                 'weight': 1
#             },
#             {
#                 'string': 'ref no./cheque',
#                 'weight': 1
#             },
#             {
#                 'string': 'debit',
#                 'weight': 1
#             },
#             {
#                 'string': 'credit',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance',
#                 'weight': 1
#             },
#             {
#                 'string': 'date',
#                 'weight': 1
#             },
#         ]
#     },
#     'icici_b': {
#         'keywords': [
#             {
#                 'string': 'www.icicibank.com',
#                 'weight': 1
#             },
#             {
#                 'string': 'your base branch',
#                 'weight': 1
#             },
#             {
#                 'string': 'dial your bank',
#                 'weight': 1
#             },
#             {
#                 'string': 'summary of accounts held under cust id',
#                 'weight': 1
#             },
#             {
#                 'string': 'statement of transactions in savings account number',
#                 'weight': 1
#             },
#             {
#                 'string': 'account related other information',
#                 'weight': 1
#             },
#             {
#                 'string': 'for icici bank limited',
#                 'weight': 1
#             },
#             {
#                 'string': 'authorised signatory',
#                 'weight': 1
#             }
#         ],
#         'regex_words': [],
#         'table_headers': [
#             {
#                 'string': 'account type',
#                 'weight': 1
#             },
#             {
#                 'string': 'a/c balance(i)',
#                 'weight': 1
#             },
#             {
#                 'string': 'nomination',
#                 'weight': 1
#             },
#             {
#                 'string': 'mode',
#                 'weight': 1
#             },
#             {
#                 'string': 'particulars',
#                 'weight': 1
#             },
#             {
#                 'string': 'deposits',
#                 'weight': 1
#             },
#             {
#                 'string': 'withdrawals',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance',
#                 'weight': 1
#             },
#             {
#                 'string': 'withdrawal amount',
#                 'weight': 1
#             },
#             {
#                 'string': 'deposit amount',
#                 'weight': 1
#             },
#             {
#                 'string': 'balance (inr )',
#                 'weight': 1
#             }
#         ]
#     },
# }
