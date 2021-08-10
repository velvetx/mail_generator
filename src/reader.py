import colorama


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
        except Exception as error:
            print(error)
            self.get_input_file()

    def get_file_with_patterns(self):
        if self.selected_file:
            try:
                with open(f'{self.selected_file}', 'r') as reader:
                    for pattern in reader:
                        self.patterns.append(pattern.strip())
            except FileNotFoundError:
                print(f'{colorama.Fore.RED}Bad path!')
                self.get_input_file()
            except NotADirectoryError:
                print(f'{colorama.Fore.RED}Bad path!"')
                self.get_input_file()
        else:
            with open('patterns.txt', 'r') as reader:
                for pattern in reader:
                    self.patterns.append(pattern.strip())

    def execution(self, data_for_substitution, amount_of_letters):
        self.data_for_substitution = data_for_substitution
        self.amount_of_letters = amount_of_letters
        self.get_input_file()
        self.get_file_with_patterns()
        return self.patterns
