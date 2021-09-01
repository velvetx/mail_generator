import colorama
import os


class Reader:
    def __init__(self):
        self.data_for_substitution = None
        self.amount_of_letters = None
        self.patterns = []
        self.selected_file = None

    def get_input_file(self):
        try:
            self.selected_file = input('\nSelect a file with patterns (learn about it in readme.txt), '
                                       'default="patterns.txt": ')
            if not os.path.exists(self.selected_file):
                raise FileNotFoundError
            if self.selected_file[-1] == '/':
                self.selected_file = self.selected_file[:-1]
            if os.path.splitext(self.selected_file)[1] != '.txt':
                raise FileNotFoundError
        except FileNotFoundError:
            answer = input('Want to use default patterns? (Yes/No) ')
            if answer.lower().strip() == 'no':
                print(f'{colorama.Fore.GREEN}Use the correct path!')
                self.get_input_file()
            else:
                self.selected_file = 'data/patterns.txt'

    def get_file_with_patterns(self):
        with open(f'{self.selected_file}', 'r') as reader:
            for pattern in reader:
                self.patterns.append(pattern.strip())

    def execution(self, data_for_substitution, amount_of_letters):
        self.data_for_substitution = data_for_substitution
        self.amount_of_letters = amount_of_letters
        self.get_input_file()
        self.get_file_with_patterns()
        return self.patterns
