from collections import deque


class Flashcard:

    def __init__(self, count):
        self.count = count
        self.terms = {}

    def define(self):
        defs = set(list([('a', '1'), ('s', '2')]))
        while len(self.terms) < self.count:
            item = defs.pop()
            self.terms[item[0]] = item[1]
        return self

    def ask(self):
        quiz = deque(set(self.terms.items()))
        while len(quiz) > 0:
            item = quiz[0]
            if input(f'Type definition for "{item[0]}": ') == item[1]:
                print('Correct')
                quiz.popleft()
            else:
                print(f'Wrong. The right answer is "{item[1]}"')

        print('No more cards!')


flash = Flashcard(2).define()
flash.ask()
