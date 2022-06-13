class Flashcard:

    def __init__(self, count: int):
        self.count = count
        self.terms = dict()

    def define(self):
        term = None
        definition = None
        while len(self.terms) < self.count:
            no = len(self.terms) + 1
            if not term:
                term = input(f'The term for card #{no}:\n')
            if term in self.terms.keys():
                term = input(f'The term "{term}" already exists. Try again:\n')
                continue
            if not definition:
                definition = input(f'The definition for card #{no}:\n')
            if definition in self.terms.values():
                definition = input(
                    f'The definition "{definition}" already exists. Try '
                    f'again:\n')
                continue
            if term and definition:
                self.terms[term] = definition
            term = None
            definition = None

        return self

    def ask(self):
        for term, definition in self.terms.items():
            print(f'Print the definition of "{term}":')
            answer = input()
            if answer == definition:
                print('Correct!')
            else:
                if answer in self.terms.values():
                    correct_answer = list(self.terms.keys())[
                        list(self.terms.values()).index(answer)
                    ]
                    # correct_term = self.terms[correct_answer]

                    print(
                        f'Wrong. The right answer is "{definition}", '
                        f'but your definition is correct for "'
                        f'{correct_answer}".')
                else:
                    print(f'Wrong. The right answer is "{definition}"')


flash = Flashcard(int(input('Input the number of cards:\n'))).define()
flash.ask()
