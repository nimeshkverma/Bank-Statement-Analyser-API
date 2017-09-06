import re
import datetime
from copy import deepcopy

MIN_COLUMNS = 7
MAX_COLUMNS = 9

HEADER = set(['S No.', 'Value Date', 'Transaction Date', 'Cheque Number',
              'Transaction Remarks', 'Withdrawal Amount', 'Deposit Amount', 'Balance (INR )'])

MAX_START_DAY_OF_MONTH = 5
MIN_END_DAY_OF_MONTH = 25


class ICICIBankStatementsA(object):
    """Class to analyse the data obtained from ICICI Bank"""

    def __init__(self, raw_table_data, pdf_text):
        self.raw_table_data = raw_table_data
        self.pdf_text = pdf_text
        self.statements = []
        self.transactions = {}
        self.__set_statements_and_transaction()
        self.stats = {}
        self.__set_pdf_text_stats()
        self.all_day_transactions = self.__get_all_day_transactions()
        self.__set_stats()

    def __get_amount(self, input_string):
        comma_remove_input_string = input_string.replace(',', '')
        try:
            return int(float(comma_remove_input_string))
        except Exception as e:
            return 0

    def __get_date(self, date_input):
        try:
            return datetime.datetime.strptime(date_input, '%d/%m/%Y')
        except Exception as e:
            return datetime.datetime.strptime(date_input, '%d-%m-%Y')

    def __get_statement_set_transaction(self, data_list):
        statement_dict = {}
        try:
            if len(data_list) in [8, 9]:
                statement_dict = {
                    'sr_no': data_list[0],
                    'value_date': self.__get_date(data_list[1]),
                    'transaction_date': self.__get_date(data_list[2]),
                    'cheque_no': data_list[3],
                }
                if len(data_list) == 8:
                    statement_dict.update({
                        'transaction_remark': str(data_list[4]),
                        'withdrawal_amount': self.__get_amount(data_list[5]),
                        'deposit_amount': self.__get_amount(data_list[6]),
                        'balance': self.__get_amount(data_list[7])
                    })
                elif len(data_list) == 9:
                    statement_dict.update({
                        'transaction_remark': str(data_list[4]) + str(data_list[5]),
                        'withdrawal_amount': self.__get_amount(data_list[6]),
                        'deposit_amount': self.__get_amount(data_list[7]),
                        'balance': self.__get_amount(data_list[8])
                    })
                else:
                    statement_dict = {}
                if statement_dict:
                    self.transactions[statement_dict[
                        'transaction_date']] = statement_dict['balance']
            elif len(data_list) in [7]:
                statement_dict = {
                    'value_date': self.__get_date(data_list[0]),
                    'transaction_date': self.__get_date(data_list[1]),
                    'cheque_no': data_list[2],
                    'transaction_remark': str(data_list[3]),
                    'withdrawal_amount': self.__get_amount(data_list[4]),
                    'deposit_amount': self.__get_amount(data_list[5]),
                    'balance': self.__get_amount(data_list[6])
                }
                self.transactions[statement_dict[
                    'transaction_date']] = statement_dict['balance']
            else:
                pass

        except Exception as e:
            print "Following error occured while processing {data_list} : {error}".format(data_list=str(data_list), error=str(e))
        return statement_dict

    def __set_statements_and_transaction(self):
        for data_list in self.raw_table_data.get('body', []):
            if MIN_COLUMNS <= len(data_list) <= MAX_COLUMNS and not HEADER.intersection(set(data_list)):
                statement_dict = self.__get_statement_set_transaction(
                    data_list)
                self.statements.append(
                    statement_dict) if statement_dict else None

    def __set_pdf_text_stats(self):
        self.stats['start_date'] = min(self.transactions.keys())
        self.stats['end_date'] = max(self.transactions.keys())
        all_string_date_list = re.findall(
            r'(from\s?\d{2}/\d{2}/\d{2,4}\s?to\s?\d{2}/\d{2}/\d{2,4})', self.pdf_text)
        if not all_string_date_list:
            all_string_date_list = re.findall(
                r'(\d{2}/\d{2}/\d{2,4})', self.pdf_text)
        all_date_list = []
        for string_date in all_string_date_list:
            try:
                for date_match in re.findall(r'(\d{2}/\d{2}/\d{2,4})', string_date):
                    all_date_list.append(
                        datetime.datetime.strptime(date_match, '%d/%m/%Y'))
            except Exception as e:
                pass
        self.stats['pdf_text_start_date'] = min(
            all_date_list) if all_date_list else self.stats['start_date']
        self.stats['pdf_text_end_date'] = max(
            all_date_list) if all_date_list else self.stats['end_date']
        self.stats['days'] = (self.stats['pdf_text_end_date'] -
                              self.stats['pdf_text_start_date'] + datetime.timedelta(1)).days

    def __get_first_day_balance(self):
        if self.stats['start_date'] == self.stats['pdf_text_start_date']:
            return self.transactions[self.stats['start_date']]
        return int(self.statements[0].get('balance', '0')) - int(self.statements[0].get('deposit_amount', '0')) + int(self.statements[0].get('withdrawal_amount', '0'))

    def __get_all_day_transactions(self):
        all_day_transactions = {}
        all_day_transactions[self.stats[
            'pdf_text_start_date']] = self.__get_first_day_balance()
        for day_no in xrange(1, self.stats['days']):
            day_date = self.stats['pdf_text_start_date'] + \
                datetime.timedelta(days=day_no)
            if day_date in self.transactions.keys():
                all_day_transactions[day_date] = self.transactions[day_date]
            else:
                all_day_transactions[day_date] = all_day_transactions[
                    day_date - datetime.timedelta(days=1)]
        return all_day_transactions

    def __min_date(self):
        if self.stats['pdf_text_start_date'].day <= MAX_START_DAY_OF_MONTH:
            return self.stats['pdf_text_start_date']
        day = 1
        month = self.stats['pdf_text_start_date'].month + \
            1 if self.stats['pdf_text_start_date'].month != 12 else 1
        year = self.stats['pdf_text_start_date'].year if self.stats[
            'pdf_text_start_date'].month != 12 else self.stats['pdf_text_start_date'].year + 1
        return datetime.datetime(year, month, day)

    def __max_date(self):
        if self.stats['pdf_text_end_date'].day >= MIN_END_DAY_OF_MONTH:
            return self.stats['pdf_text_end_date']
        return datetime.datetime(self.stats['pdf_text_end_date'].year, self.stats['pdf_text_end_date'].month, 1) - datetime.timedelta(days=1)

    def get_days_above_given_balance_unpartial_months(self, given_balance):
        min_date = self.__min_date()
        max_date = self.__max_date()
        above_given_balance_daywise = {}
        for day, balance in self.all_day_transactions.iteritems():
            if balance >= given_balance and min_date <= day <= max_date:
                above_given_balance_daywise[day] = balance
        return {
            'given_balance': given_balance,
            'no_of_days': len(above_given_balance_daywise),
            'above_balance_daywise': above_given_balance_daywise,
        }

    def get_days_above_given_balance(self, given_balance):
        above_given_balance_daywise = {}
        for day, balance in self.all_day_transactions.iteritems():
            if balance >= given_balance:
                above_given_balance_daywise[day] = balance
        return {
            'given_balance': given_balance,
            'no_of_days': len(above_given_balance_daywise),
            'above_balance_daywise': above_given_balance_daywise,
        }

    def __set_stats(self):
        self.stats['average_balance'] = round(sum(
            self.all_day_transactions.values()) / len(self.all_day_transactions.values()), 2)

    def __json_statements(self):
        statements = []
        for statement in self.statements:
            data = deepcopy(statement)
            for key in ['value_date', 'transaction_date']:
                data[key] = data[key].strftime("%d/%m/%y")
            for key in ['withdrawal_amount', 'deposit_amount', 'balance']:
                data[key] = str(data[key])
            statements.append(data)
        return statements

    def __json_transactions(self):
        transactions = {}
        for day, balance in self.all_day_transactions.iteritems():
            transactions[day.strftime("%d/%m/%y")] = str(balance)
        return transactions

    def __json_stats(self):
        stats = {}
        for key, value in self.stats.iteritems():
            if type(value) == datetime.datetime:
                stats[key] = value.strftime("%d/%m/%y")
            elif type(value) in [float, int]:
                stats[key] = str(value)
            else:
                stats[key] = value
        return stats

    def __json_days_above_given_balance(self, threshhold):
        days_above_given_balance = self.get_days_above_given_balance(
            threshhold)
        above_balance_daywise = days_above_given_balance.pop(
            'above_balance_daywise', {})
        days_above_given_balance['above_balance_daywise'] = {}
        for day, balance in above_balance_daywise.iteritems():
            days_above_given_balance['above_balance_daywise'][
                day.strftime("%d/%m/%y")] = str(balance)
        return days_above_given_balance

    def __json_monthly_stats(self, threshhold):
        monthly_stats = {}
        for day, balance in self.all_day_transactions.iteritems():
            month_year_key = day.strftime("%m-%Y")
            if monthly_stats.get(month_year_key):
                monthly_stats[month_year_key]['all_day_count'] += 1
                monthly_stats[month_year_key]['balance_above_day_count'] = monthly_stats[month_year_key][
                    'balance_above_day_count'] + 1 if balance >= threshhold else monthly_stats[month_year_key]['balance_above_day_count']
            else:
                monthly_stats[month_year_key] = {
                    'all_day_count': 1,
                    'balance_above_day_count': 1 if balance >= threshhold else 0,
                }
        return monthly_stats

    def data_json(self, threshhold):
        data = {
            'raw_statements': self.__json_statements(),
            'all_transactions': self.__json_transactions(),
            'stats': self.__json_stats(),
            'above_emi_balance_data': self.__json_days_above_given_balance(threshhold),
            'monthly_stats': self.__json_monthly_stats(threshhold),
            'bank_name': 'ICICI Type A',
        }
        return data
