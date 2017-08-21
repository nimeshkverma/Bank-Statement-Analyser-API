import re
import datetime
from copy import deepcopy

DATA_MIN_COLUMNS = 5
DATA_MAX_COLUMNS = 6

HEADER = set(['Txn Date', 'Value', 'Description', 'Ref No./Cheque',
              'Debit', 'Credit', 'Balance', 'Date', 'No.', 'Txn', 'Value Date', ])

MAX_START_DAY_OF_MONTH = 5
MIN_END_DAY_OF_MONTH = 25

MONTH_LIST = ['Jan', 'Feb', 'Mar', 'Apr', 'May',
              'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', ]

DAY_LIST = [str(day) for day in xrange(1, 32)]

YEAR_LIST = [str(year) for year in xrange(
    2001, 1 + datetime.datetime.now().year)]


class SBIBankStatements(object):
    """Class to analyse the data obtained from SBI Bank"""

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

    def __is_date(self, input_string):
        is_date = False
        try:
            datetime.datetime.strptime(input_string, '%d-%m-%Y')
            is_date = True
        except Exception as e:
            pass
        return is_date

    def __is_int(self, string_value, maximum, minimum):
        is_int = False
        try:
            int_value = int(string_value)
            is_int = minimum <= int_value <= maximum
        except Exception as e:
            pass
        return is_int

    def __get_amount(self, input_string):
        comma_remove_input_string = input_string.replace(',', '')
        try:
            return int(float(comma_remove_input_string))
        except Exception as e:
            return 0

    def __deconcatinate_numbers(self, input_string):
        number_list = input_string.split(' ')
        if len(number_list) == 2:
            for index in xrange(0, len(number_list)):
                number_list[index] = self.__get_amount(number_list[index])
            return number_list
        return [0.0, 0.0]

    def __get_statement_set_transaction(self, index, partition_data='simple'):
        statement_dict = {}
        if partition_data == 'simple' and len(self.raw_table_data['body'][index]) in [4, 5, 6]:
            try:
                statement_dict = {
                    'transaction_date': datetime.datetime.strptime(self.raw_table_data['body'][index][0], '%d %b %Y'),
                    'description': self.raw_table_data['body'][index][-4],
                    'cheque_no': self.raw_table_data['body'][index][-3],
                    'withdraw_deposit': self.__get_amount(self.raw_table_data['body'][index][-2]),
                    'balance': self.__get_amount(self.raw_table_data['body'][index][-1]),
                }
            except Exception as e:
                print "Following error occured while processing {data_list} : {error}".format(data_list=str(self.raw_table_data['body'][index]), error=str(e))
        elif partition_data == 'splitted' and len(self.raw_table_data['body'][index]) in [4, 5, 6] and index + 1 < len(self.raw_table_data['body']) and self.raw_table_data['body'][index + 1][0] in YEAR_LIST:
            try:
                statement_dict = {
                    'transaction_date': datetime.datetime.strptime(self.raw_table_data['body'][index][0] + ' ' + self.raw_table_data['body'][index + 1][0], '%d %b %Y'),
                    'description': self.raw_table_data['body'][index][-4],
                    'cheque_no': self.raw_table_data['body'][index][-3],
                    'withdraw_deposit': self.__get_amount(self.raw_table_data['body'][index][-2]),
                    'balance': self.__get_amount(self.raw_table_data['body'][index][-1]),
                }
            except Exception as e:
                print "Following error occured while processing {data_list} : {error}".format(data_list=str(self.raw_table_data['body'][index]), error=str(e))
        elif partition_data == 'complex' and len(self.raw_table_data['body'][index]) >= 2 and re.findall(r'\d{1,2} [a-zA-Z]{3} \d{4}', self.raw_table_data['body'][index][0]):
            try:
                date_list = re.findall(
                    r'\d{1,2} [a-zA-Z]{3} \d{4}', self.raw_table_data['body'][index][0])
                statement_dict = {
                    'transaction_date': datetime.datetime.strptime(date_list[0], '%d %b %Y'),
                    'balance': self.__get_amount(self.raw_table_data['body'][index][-1]),
                }
            except Exception as e:
                print "Following error occured while processing {data_list} : {error}".format(data_list=str(self.raw_table_data['body'][index]), error=str(e))
        elif partition_data == 'complex' and len(self.raw_table_data['body'][index]) >= 2 and re.findall(r'\d{1,2} [a-zA-Z]{3}', self.raw_table_data['body'][index][0]) and index + 1 < len(self.raw_table_data['body']):
            try:
                date_part1_list = re.findall(
                    r'\d{1,2} [a-zA-Z]{3}', self.raw_table_data['body'][index][0])
                date_part2_list = re.findall(
                    r'\d{4}', self.raw_table_data['body'][index + 1][0])
                date_string = date_part1_list[
                    0] + ' ' + date_part2_list[0] if date_part2_list else None
                if date_string:
                    statement_dict = {
                        'transaction_date': datetime.datetime.strptime(date_string, '%d %b %Y'),
                        'balance': self.__get_amount(self.raw_table_data['body'][index][-1]),
                    }
            except Exception as e:
                print "Following error occured while processing {data_list} : {error}".format(data_list=str(self.raw_table_data['body'][index]), error=str(e))
        else:
            pass
        if statement_dict:
            self.transactions[statement_dict[
                'transaction_date']] = statement_dict['balance']
        return statement_dict

    def __set_statements_and_transaction(self):
        statement_count = len(self.raw_table_data.get('body', []))
        statement_dict = None
        index = 0
        while index < statement_count:
            if not HEADER.intersection(set(self.raw_table_data['body'][index])) and self.raw_table_data['body'][index]:
                first_column_parts = self.raw_table_data[
                    'body'][index][0].split(' ')
                if len(first_column_parts) == 3 and first_column_parts[0] in DAY_LIST and first_column_parts[1] in MONTH_LIST and first_column_parts[2] in YEAR_LIST:
                    statement_dict = self.__get_statement_set_transaction(
                        index, 'simple')
                elif len(first_column_parts) == 2 and first_column_parts[0] in DAY_LIST and first_column_parts[1] in MONTH_LIST:
                    statement_dict = self.__get_statement_set_transaction(
                        index, 'splitted')
                    index += 1
                elif len(first_column_parts) > 3:
                    statement_dict = self.__get_statement_set_transaction(
                        index, 'complex')
                else:
                    pass
            index += 1
            self.statements.append(statement_dict) if statement_dict else None

    def __get_pdf_dates(self):
        pdf_dates = []
        from_to_string_date_list = re.findall(
            r'Account Statement from \d{1,2} [a-zA-Z]{3} \d{4} to \d{1,2} [a-zA-Z]{3} \d{4}', self.pdf_text)
        for from_to_string_date in from_to_string_date_list:
            pdf_dates.append(from_to_string_date.split(' to ')[-1])
            pdf_dates.append(from_to_string_date.split(' to ')[
                             0].split('Account Statement from ')[-1])
        return pdf_dates

    def __set_pdf_text_stats(self):
        self.stats['start_date'] = min(self.transactions.keys())
        self.stats['end_date'] = max(self.transactions.keys())
        all_string_date_list = self.__get_pdf_dates()
        all_date_list = []
        for string_date in all_string_date_list:
            try:
                all_date_list.append(
                    datetime.datetime.strptime(string_date, '%d %b %Y'))
            except Exception as e:
                pass
        self.stats['pdf_text_start_date'] = min(
            all_date_list) if all_date_list else self.stats['start_date']
        self.stats['pdf_text_end_date'] = max(
            all_date_list) if all_date_list else self.stats['end_date']
        self.stats['days'] = (self.stats['pdf_text_end_date'] -
                              self.stats['pdf_text_start_date'] + datetime.timedelta(1)).days

    def __get_first_day_balance(self):
        balance = 0.0
        balance_string = re.findall(
            r'Balance as on \d{1,2} [a-zA-Z]{3} \d{4}[^\n]+', self.pdf_text)
        if balance_string and '(cid:9)' in balance_string[0]:
            balance = self.__get_amount(balance_string[0].split('(cid:9)')[-1])
        elif balance_string:
            balance = self.__get_amount(balance_string[0].split(':')[-1])
        else:
            pass
        if self.stats['start_date'] == self.stats['pdf_text_start_date']:
            opening_balance = None
            opening_balance_statement = {}
            for statement in self.statements:
                if statement['transaction_date'] != self.stats['start_date']:
                    break
                opening_balance_statement = statement
            if opening_balance_statement:
                opening_balance = opening_balance_statement['balance']
            if opening_balance != None:
                balance = opening_balance
        return balance

    def __get_all_day_transactions(self):
        all_day_transactions = {}
        all_day_transactions[self.stats[
            'pdf_text_start_date']] = self.__get_first_day_balance()
        number_of_days = (self.stats[
                          'end_date'] - self.stats['pdf_text_start_date'] + datetime.timedelta(1)).days
        for day_no in xrange(1, number_of_days):
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

    def __min_date(self):
        if self.stats['end_date'].day <= MAX_START_DAY_OF_MONTH:
            return self.stats['end_date']
        day = 1
        month = self.stats['end_date'].month + \
            1 if self.stats['end_date'].month != 12 else 1
        year = self.stats['end_date'].year if self.stats[
            'end_date'].month != 12 else self.stats['end_date'].year + 1
        return datetime.datetime(year, month, day)

    def __max_date(self):
        if self.stats['pdf_text_end_date'].day >= MIN_END_DAY_OF_MONTH:
            return self.stats['pdf_text_end_date']
        return datetime.datetime(self.stats['pdf_text_end_date'].year,
                                 self.stats['pdf_text_end_date'].month, 1) - datetime.timedelta(days=1)

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
            self.all_day_transactions.values()) /
            len(self.all_day_transactions.values()), 2)

    def __json_statements(self):
        statements = []
        for statement in self.statements:
            data = deepcopy(statement)
            for key in ['transaction_date']:
                data[key] = data[key].strftime("%d/%m/%y")
            for key in ['withdraw_deposit',  'balance']:
                if data.get(key):
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
            'bank_name': 'SBI',
        }
        return data
