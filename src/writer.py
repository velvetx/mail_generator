import colorama
import os
from random import choice


colorama.init(autoreset=True)


class Writer:
    def __init__(self):
        self.email = None
        self.data_to_write = None
        self.user_path = None

    def get_input_path(self):
        try:
            self.user_path = input('\nAlmost done! Specify the path where you would like to save the '
                                   'result [/home/user/Desktop]: ')
            if not os.path.exists(self.user_path):
                raise FileNotFoundError
            if not os.path.isdir(self.user_path):
                raise FileNotFoundError
            if self.user_path[-1] == '/':
                self.user_path = self.user_path[:-1]
        except FileNotFoundError:
            answer = input('Want to use default path? (Yes/No) ')
            if answer.lower().strip() == 'no':
                print(f'{colorama.Fore.GREEN}Use the correct path!')
                self.get_input_path()
            else:
                self.user_path = 'logs'

    def filing(self, result=True):
        if result:
            with open(f'{self.user_path}/result.txt', 'w') as writer:
                for i in self.data_to_write:
                    writer.write(f'{choice(self.email)}\n{"="*30}\n{i}\n\n\n')
            file_location = self.user_path + '/result.txt'
            print(f'\n{colorama.Back.BLUE}{colorama.Fore.GREEN}Done! Your file is located at: '
                  f'{os.path.abspath(file_location)}')
        else:
            with open(f"{os.path.abspath('logs/parsed_data.txt')}", 'w') as writer:
                for name in self.data_to_write:
                    writer.write(f"{name}\n")
            print(f'\nFile with data is located at: {os.path.abspath("logs/parsed_data.txt")}')

    def execution(self, email, data_to_write):
        self.data_to_write = data_to_write
        self.user_path = None
        if email:
            self.email = email.split(' ')
            self.get_input_path()
            self.filing()
        else:
            self.filing(False)
