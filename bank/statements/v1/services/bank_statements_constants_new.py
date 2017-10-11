BANK_IDENTIFIER_CONSTANTS_NEW = {
    'citi_a': {
        'keywords': [
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
        'regex_words': [
            {
                'string': r'(statement period:(\s+)?[a-zA-Z]{3,9} \d{2},\d{4} to [a-zA-Z]{3,9} \d{2},\d{4})',
                'weight': 1
            },
            {
                'string': r'(opening balance:(\s+)?\d+.\d{2})',
                'weight': 1
            },
        ],
        'table_headers': [
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
        ]
    },
    'citi_b': {
        'keywords': [
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
        'regex_words': [
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
        'table_headers': [
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

        ]
    },
    'canara_a': {
        'keywords': [
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
        'regex_words': [
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
        'table_headers': [
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
        ]
    },
    'canara_b': {
        'keywords': [
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
        'regex_words': [
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
        'table_headers': [
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

        ]
    },
    'yes_a': {
        'keywords': [
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
        'regex_words': [
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
        'table_headers': [
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

        ]
    },
    'baroda': {
        'keywords': [
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
        'regex_words': [
            {
                'string': r'(From(\s+)\d{2}/\d{2}/\d{4}(\s+)?to(\s+)?\d{2}/\d{2}/\d{4})',
                'weight': 1
            },
        ],
        'table_headers': [
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

        ]
    },
    'indusind_a': {
        'keywords': [
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
        'regex_words': [
            {
                'string': r'(account([a-zA-Z.\s]+)?(\s+)?:(\s+)?\d{12})',
                'weight': 1
            },
            {
                'string': r'(From(\s+):(\s+)[a-zA-Z]{3} \d{1,2}, \d{4}(\s+)?To(\s+)?:(\s+)[a-zA-Z]{3} \d{1,2}, \d{4})'
                'weight': 1
            },
        ],
        'table_headers': [
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

        ]
    },
    # 'indusind_b': {
    #     'keywords': [
    #         {
    #             'string': 'savings account indus comfort',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'account branch',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'address',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'account type',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'account no.',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'this is a computer generated statement and does not require signature.',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'imps outward',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'imps inward',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'funds on earmarking / hold',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'banking reward points for the a/c',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'www.citi.co.in/',
    #             'weight': 1
    #         },
    #     ],
    #     'regex_words': [
    #         {
    #             'string': r'(account no.(\s+)?:(\s+)?\d{12})',
    #             'weight': 1
    #         },
    #         {
    #             'string': r'(From(\s+):(\s+)[a-zA-Z]{3} \d{1,2}, \d{4}(\s+)?To(\s+)?:(\s+)[a-zA-Z]{3} \d{1,2}, \d{4})'
    #             'weight': 1
    #         },
    #         {
    #             'string': r'(statement period:(\s+)?[a-zA-Z]{3,9}(\s+)?\d{1,2},(\s+)?\d{4}(\s+)?to(\s+)?[a-zA-Z]{3,9}(\s+)?\d{1,2},(\s+)?\d{4})',
    #             'weight': 1
    #         },
    #         {
    #             'string': r'(opening balance:(\s+)?\d+.\d{2})',
    #             'weight': 1
    #         },
    #     ],
    #     'table_headers': [
    #         {
    #             'string': 'transaction details',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'withdrawals (inr)',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'deposits (inr)',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'balance(inr)',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'date',
    #             'weight': 1
    #         },

    #     ]
    # },
    # 'indusind_c': {
    #     'keywords': [
    #         {
    #             'string': 'savings account indus comfort',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'account branch',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'address',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'account type',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'account no.',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'this is a computer generated statement and does not require signature.',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'imps outward',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'imps inward',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'funds on earmarking / hold',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'banking reward points for the a/c',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'www.citi.co.in/',
    #             'weight': 1
    #         },
    #     ],
    #     'regex_words': [
    #         {
    #             'string': r'(account no.(\s+)?:(\s+)?\d{12})',
    #             'weight': 1
    #         },
    #         {
    #             'string': r'(From(\s+):(\s+)[a-zA-Z]{3} \d{1,2}, \d{4}(\s+)?To(\s+)?:(\s+)[a-zA-Z]{3} \d{1,2}, \d{4})'
    #             'weight': 1
    #         },
    #         {
    #             'string': r'(statement period:(\s+)?[a-zA-Z]{3,9}(\s+)?\d{1,2},(\s+)?\d{4}(\s+)?to(\s+)?[a-zA-Z]{3,9}(\s+)?\d{1,2},(\s+)?\d{4})',
    #             'weight': 1
    #         },
    #         {
    #             'string': r'(opening balance:(\s+)?\d+.\d{2})',
    #             'weight': 1
    #         },
    #     ],
    #     'table_headers': [
    #         {
    #             'string': 'transaction details',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'withdrawals (inr)',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'deposits (inr)',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'balance(inr)',
    #             'weight': 1
    #         },
    #         {
    #             'string': 'date',
    #             'weight': 1
    #         },

    #     ]
    # },
}
