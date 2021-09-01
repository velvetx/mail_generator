import colorama
import os


colorama.init(autoreset=True)


class InputParser:
    def __init__(self):
        self.amount_of_data = None
        self.amount_of_letters = None
        self.recipients_email_address = None

    def get_amount_of_data(self):
        self.amount_of_data = input(f'{colorama.Back.MAGENTA}{colorama.Fore.BLACK}'
                                    f'Enter the amount of data to parse (1-99999): {colorama.Back.RESET}'
                                    f'{colorama.Fore.RESET}')
        if len(self.amount_of_data) == 0:
            print(f"{colorama.Fore.RED}Enter a valid value!")
            self.get_amount_of_data()
        self.amount_of_data = int(self.amount_of_data)

    def get_amount_of_letters(self):
        self.amount_of_letters = input(f'{colorama.Back.MAGENTA}{colorama.Fore.BLACK}'
                                       f'Enter the amount of letters: {colorama.Back.RESET}'
                                       f'{colorama.Fore.RESET}')
        if len(self.amount_of_letters) == 0:
            print(f"{colorama.Fore.RED}Enter a valid value!")
            self.get_amount_of_letters()
        self.amount_of_letters = int(self.amount_of_letters)

    def get_recipients_email_address(self):
        self.recipients_email_address = input(f'{colorama.Back.MAGENTA}{colorama.Fore.BLACK}'
                                              f'Enter the recipients email addresses separated by a space: '
                                              f'{colorama.Back.RESET}{colorama.Fore.RESET}')
        if len(self.recipients_email_address) == 0 or self.recipients_email_address.count('@') \
                < len(self.recipients_email_address.split(' ')):
            print(f"{colorama.Fore.RED}Enter a valid email!")
            self.get_recipients_email_address()

    def execution(self):
        try:
            self.get_amount_of_data(), self.get_amount_of_letters(), self.get_recipients_email_address()
        except Exception as error:
            print(f'{colorama.Fore.RED}{error}')
            os.system('clear')
            self.execution()
        return self.amount_of_data, self.amount_of_letters, self.recipients_email_address
