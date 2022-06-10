from collections import deque


class Flashcard:

    def __init__(self, count: int):
        self.count = count
        self.terms = {}

    def define(self):
        while len(self.terms) < self.count:
            no = len(self.terms) + 1
            term = input(f'The term for card #{no}:\n')
            definition = input(f'The definition for card #{no}:\n')
            self.terms[term] = definition
        return self

    def ask(self):
        for term, definition in self.terms.items():
            print(f'Print the definition of "{term}":')
            answer = input()
            if answer == definition:
                print('Correct!')
            else:
                print(f'Wrong. The right answer is "{definition}"')


flash = Flashcard(int(input('Input the number of cards:\n'))).define()
flash.ask()
