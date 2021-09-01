import sys
import colorama
from src import logo
from src import input_parser
from src import data_parser
from src import writer
from src import reader
from src import substitution
from src import requester

colorama.init(autoreset=True)


class Program:
    def __init__(self):
        self.amount_of_data = None
        self.amount_of_letters = None
        self.recipients_email_address = None
        self.list_with_data = None
        self.patterns = None
        self.result = None
        try:
            self.execution()
        except KeyboardInterrupt:
            print(f'\n\n{colorama.Fore.LIGHTYELLOW_EX}CTRL+C\n{colorama.Fore.RED}Exiting...')
            sys.exit(0)
        except EOFError:
            print(f'\n\n{colorama.Fore.RED}Exiting...')
            sys.exit(0)

    @staticmethod
    def greeting():
        logo.Logo.printing_logo()
        print(f'{colorama.Fore.GREEN}Processing...')

    def get_user_input(self):
        self.amount_of_data, self.amount_of_letters, self.recipients_email_address = \
            input_parser.InputParser().execution()

    def get_request(self):
        return requester.Requester().execution(self.amount_of_data)

    def get_parsed_data(self):
        self.list_with_data = data_parser.DataParser().get_html_parser(self.get_request())

    def get_file_with_data(self):
        writer.Writer().execution(None, self.list_with_data)

    def get_list_with_patterns(self):
        self.patterns = reader.Reader().execution(self.list_with_data, self.amount_of_letters)

    def get_result_list(self):
        print(f'\n{colorama.Fore.GREEN}Found {len(self.list_with_data)} records!\n'
              f'Generating result file with {self.amount_of_letters} records.')
        self.result = substitution.Substitution().execution(self.patterns, self.list_with_data, self.amount_of_letters)

    def get_result(self):
        writer.Writer().execution(self.recipients_email_address, self.result)

    def execution(self):
        self.greeting()
        self.get_user_input()
        self.get_parsed_data()
        self.get_file_with_data()
        self.get_list_with_patterns()
        self.get_result_list()
        self.get_result()
        sys.exit(0)


if __name__ == '__main__':
    Program()