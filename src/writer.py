import colorama
from random import choice
from os import path


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
        except Exception as error:
            print(error)
            self.get_input_path()

    def filing(self, result=True):
        if result:
            if self.user_path:
                with open(f'{self.user_path}/result.txt', 'w') as writer:
                    for i in self.data_to_write:
                        writer.write(f'{choice(self.email)}\n{"="*30}\n{i}\n\n\n')
                print(f'\n{colorama.Back.BLUE}{colorama.Fore.GREEN}Done! Your file is located at: '
                      f'{self.user_path}/result.txt')
            else:
                with open(f'logs/result.txt', 'w') as writer:
                    for i in self.data_to_write:
                        writer.write(f'{choice(self.email)}\n{"="*30}\n{i}\n\n\n')
                print(f'\n{colorama.Back.BLUE}{colorama.Fore.GREEN}Done! Your file is located at: '
                      f'{path.abspath("logs/result.txt")}')
        else:
            with open(f"{path.abspath('logs/parsed_data.txt')}", 'w') as writer:
                for name in self.data_to_write:
                    writer.write(f"{name}\n")
            print(f'\nFile with data is located at: {path.abspath("logs/parsed_data.txt")}')

    def execution(self, email, data_to_write):
        self.data_to_write = data_to_write
        self.user_path = None
        if email:
            self.email = email.split(' ')
            self.get_input_path()
            self.filing()
        else:
            self.filing(False)

