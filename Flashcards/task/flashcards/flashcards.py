import inspect
import logging
import sys

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

error_logger = logging.getLogger()
error_logger.setLevel(40)
error_handler = logging.StreamHandler(sys.stderr)
error_logger.addHandler(error_handler)


class Flashcard:
    ACTIONS = (
        'add', 'remove', 'import', 'export', 'ask', 'exit',
        # stage 6:
        'log', 'hardest card', 'reset stats'
    )
    log_file = 'log.log'
    cards_file = 'cards.txt'

    def __init__(self):
        self.terms = dict()

        cards = open(self.cards_file, 'w')
        cards.flush()
        cards.close()

    def add(self):
        term = input(f'The card:\n')
        while term in self.terms.keys():
            term = input(f'The term "{term}" already exists. Try again:\n')

        definition = input(f'The definition of the card:\n')
        while definition in self.terms.values():
            definition = input(
                f'The definition "{definition}" already exists. Try '
                f'again:\n')

        self.terms[term] = definition
        with open(self.cards_file, 'w') as cards:
            cards_list = [f'{t} {d}\n' for t, d in self.terms.items()]
            print('Trying to add card to cards: ', self.terms, cards_list)
            cards.writelines(cards_list)
            cards.flush()

        print(f'The pair ("{term}":"{definition}") has been added.')

    def remove(self):
        term = input("Which card?\n")
        try:
            del self.terms[term]
            with open(self.cards_file, 'w') as cards:
                cards_list = [f'{t} {d}\n' for t, d in self.terms.items()]
                cards.writelines(cards_list)
                cards.flush()
            print('The card has been removed.')
        except KeyError:
            print(f'Can\'t remove "{term}": there is no such card.')

    def import_flashes(self):
        file_name = input('File Name:\n')
        try:
            with open(file_name) as flashes:
                lines = flashes.readlines()
                imported = [line.strip() for line in lines]
                for f in imported:
                    t, d = f.split(':')
                    self.terms[t] = d
                print(f'{len(imported)} cards have been loaded.')

                flashes.close()

        except FileNotFoundError:
            print('File not found.')

    def export_flashes(self):
        file_name = input('File Name:\n')
        with open(file_name, 'w') as flash_file:
            flash_file.writelines(
                [f'{t}:{d}\n' for t, d in self.terms.items()]
            )
            flash_file.close()
        print(f'{len(self.terms)} cards have been saved.')

    def ask(self):
        count = int(input('How many times to ask?\n'))

        terms = list(self.terms.keys())
        k = 0
        for i in range(count):
            try:
                term = terms[k]
            except IndexError:
                print(
                    f'Ups! There is no card in cards with index: {k}',
                    file=sys.stderr
                )
                break

            definition = self.terms[term]
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
            if i + 1 > count:
                break
            else:
                k = k + 1
                if k > len(self.terms) - 1:
                    k = 0

    def log(self):
        """
        ask the user where to save the log with the message File name:,
        save all the lines that have been input in/output to the console to
        the file, and print the message The log has been saved. Don't clear
        the log after saving it to the file.
        """
        self.log_file = input('File name:\n')
        with open(self.log_file, 'w') as registry:
            registry.flush()

        logger_handler = logging.FileHandler(filename=self.log_file)
        logger_format = '%(asctime)s | %(levelname)s: %(message)s'
        logger_handler.setFormatter(logging.Formatter(logger_format))
        logger.addHandler(logger_handler)

    def hardest_card(self):
        """
        print a string that contains the term of the card with the highest
        number of wrong answers, for example, The hardest card is "term".
        You have N errors answering it. If there are several cards with the
        highest number of wrong answers, print all of the terms: The hardest
        cards are "term_1", "term_2". If there are no cards with errors in
        the user's answers, print the message There are no cards with errors.
        """
        print(f'Function "{inspect.stack()[0][3]}" is not implemented jet!',
              file=sys.stderr)

        return

    def reset_stats(self):
        """
        set the count of mistakes to 0 for all the cards and output the
        message Card statistics have been reset.
        """
        print(f'Function "{inspect.stack()[0][3]}" is not implemented jet!',
              file=sys.stderr)

        return

    def run(self):
        actions = ', '.join([a for a in self.ACTIONS])
        action = input(f"\nInput the action ({actions}):\n")
        if action == 'add':
            self.add()
        elif action == 'remove':
            self.remove()
        elif action == 'import':
            self.import_flashes()
        elif action == 'export':
            self.export_flashes()
        elif action == 'ask':
            self.ask()
        elif action == 'log':
            self.log()
        elif action == 'reset stats':
            self.reset_stats()
        elif action == 'hardest card':
            self.hardest_card()
        elif action != 'exit':
            raise Exception('Unknown action!')

        if action != 'exit':
            self.run()


Flashcard().run()

print("Bye bye!")
