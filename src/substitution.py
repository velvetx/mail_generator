from random import choice


class Substitution:
    def __init__(self):
        self.data = None
        self.patterns = None
        self.amount_of_letters = None
        self.result = []

    def get_data_format(self):
        for _ in range(self.amount_of_letters):
            sentence = choice(self.patterns)
            try:
                self.result.append(sentence % choice(self.data))
            except TypeError:
                self.result.append(sentence)

    def execution(self, patterns, data, amount_of_letters):
        self.data = data
        self.patterns = patterns
        self.amount_of_letters = amount_of_letters
        self.get_data_format()
        return self.result
