import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    def print(self):
        print(self.letters)
    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)
    def  is_en_letter(self, letter):
        if letter in self.letters:
            return True
        else:
            return False
    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print('Example text in English')

if __name__ == '__main__':
    # Это создание объекта в классе EngAlphabet, входные параметры здесь не указываются,
    # так как они указаны в самом коде.
    eng = EngAlphabet()
    eng.print()
    print(eng.letters_num())
    print(eng.is_en_letter('F'))
    print(eng.is_en_letter('Щ'))
    eng.example()

    # Это создание объекта в классе Alphabet, поэтому здесь есть входные параметры.
    eng1 = Alphabet('En', string.ascii_uppercase)
    eng1.print()
    print(eng1.letters_num())


