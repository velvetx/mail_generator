import pyfiglet


class Logo:
    @staticmethod
    def printing_logo():
        return pyfiglet.print_figlet('mail generator', font='slant')