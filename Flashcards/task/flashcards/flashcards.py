import argparse
import logging
import os
import sys

logger = logging.getLogger()


class Flashcard:
    ACTIONS = (
        'add', 'remove', 'import', 'export', 'ask', 'exit',
        # stage 6:
        'log', 'hardest card', 'reset stats'
    )
    log_file = 'log.txt'
    cards_file = 'cards.txt'
    after = None

    def __init__(self, **args):
        self.saved = False
        self.terms = dict()
        self.logs = []
        self.args = args

        current_dir = os.getcwd()
        if current_dir.endswith('flashcards'):
            debug_file = f'{current_dir}/debug.log'
        else:
            debug_file = f'{current_dir}/flashcards/debug.log'

        with open(debug_file, 'w') as debug:
            debug.flush()

        logger_handler = logging.FileHandler(filename=debug_file)
        logger_format = '%(asctime)s [%(levelname)s]: %(message)s'
        logger_handler.setFormatter(logging.Formatter(logger_format))
        logger.addHandler(logger_handler)
        logger.setLevel(logging.DEBUG)

        from_ = args['import_from']
        to_ = args['export_to']
        if from_ is not None:
            logger.debug(f'We should import flashes from file: "{from_}"')
            self.import_flashes(from_)
        if to_ is not None:
            logger.debug(f'We should export at the end to file: "{to_}"')
            self.after = lambda: self.export_flashes(args['export_to'])

    def say(self, message, output=None):
        if output is None:
            output = 'info'

        if output == 'info':
            print(message)
            self.logs.append(f'{message}\n')
        else:
            print(message, file=output)

    def save_terms(self):
        with open(f'./{self.cards_file}', 'w') as cards:
            cards_list = [f'{t} {d["definition"]} {d["errors"]}\n' for t, d in
                          self.terms.items()]
            cards.writelines(cards_list)
            cards.flush()

    def add(self):
        term = input(f'The card:\n')
        while term in self.terms.keys():
            self.say(f'The term "{term}" already exists. Try again:')
            term = input()

        self.say(f'The definition of the card:')
        definition = input()

        found = {d['definition']: t for t, d in self.terms.items()}

        while definition in found:
            self.say(
                f'The definition "{definition}" already exists. Try again:')
            definition = input()

        self.terms[term] = {'definition': definition, 'errors': 0}
        self.save_terms()

        self.say(f'The pair ("{term}":"{definition}") has been added.')

    def remove(self):
        term = input("Which card?\n")
        try:
            del self.terms[term]
            self.save_terms()

            self.say('The card has been removed.')
        except KeyError:
            self.say(f'Can\'t remove "{term}": there is no such card.')

    def import_flashes(self, file_name=None):
        with_args = file_name is not None
        if file_name is None:
            file_name = input('File Name:\n')

        try:
            with open(f'./{file_name}') as flashes:
                lines = flashes.readlines()
                imported = [line.strip() for line in lines]

                for f in imported:
                    t, d, e = f.split(':')
                    self.terms[t] = {'definition': d, 'errors': e}
                self.say(f'{len(imported)} cards have been loaded.')

                flashes.close()

        except FileNotFoundError:
            if not with_args:
                self.say('File not found.')

    def export_flashes(self, file_name=None):
        if file_name is None:
            file_name = input('File Name:\n')
        if len(self.terms.items()):
            with open(f'./{file_name}', 'w') as flash_file:
                flash_file.writelines(
                    [f'{t}:{d["definition"]}:{d["errors"]}\n' for t, d in
                     self.terms.items()]
                )
                flash_file.flush()
            self.say(f'{len(self.terms)} cards have been saved.')
        else:
            print('There is nothing to export', file=sys.stderr)

    def ask(self):
        self.say('How many times to ask?')
        count = int(input())

        terms = list(self.terms.keys())
        k = 0
        for i in range(count):
            try:
                term = terms[k]
            except IndexError:
                self.say(f'Whoops! There is no card in cards with index: {k}',
                         sys.stderr)
                break

            definition = self.terms[term]['definition']
            self.say(f'Print the definition of "{term}":')
            answer = input()
            if answer == definition:
                self.say('Correct!')
            else:
                if answer in [d['definition'] for d in self.terms.values()]:
                    correct_term = [t
                                    for t, d in self.terms.items()
                                    if d['definition'] == answer
                                    ][0]

                    message = f'Wrong. The right answer is "{definition}", ' \
                              f'but your definition is correct for "' \
                              f'{correct_term}".'

                    self.say(message)
                else:
                    self.say(f'Wrong. The right answer is "{definition}"')
                self.terms[term]['errors'] = int(
                    self.terms[term]['errors']) + 1
                self.save_terms()
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
        with open(f'./{self.log_file}', 'w') as registry:
            registry.writelines(self.logs)
            registry.flush()
            self.say("The log has been saved.")

    def hardest_card(self):
        """
        print a string that contains the term of the card with the highest
        number of wrong answers, for example, The hardest card is "term".
        You have N errors answering it. If there are several cards with the
        highest number of wrong answers, print all of the terms: The hardest
        cards are "term_1", "term_2". If there are no cards with errors in
        the user's answers, print the message There are no cards with errors.
        """
        hardest_dict = {t: d['errors']
                        for t, d in self.terms.items()
                        if int(d['errors']) > 0}
        logger.debug('hardest_dict: {}'.format(len(hardest_dict)))
        if len(hardest_dict.keys()) == 0:
            self.say('There are no cards with errors')
        else:
            hardest_counts = list(hardest_dict.values())
            hardest_score = max(hardest_counts)
            hardest = [(t, e) for t, e in hardest_dict.items()]
            if hardest_counts.count(hardest_score) == 1:
                term, errors = hardest[0]
                self.say(
                    f'The hardest card is "{term}". You have {errors} errors '
                    f'answering it')
            elif hardest_counts.count(hardest_score) > 1:
                hardest_terms = ', '.join([f'"{t}"' for t, e in hardest])
                self.say(f'The hardest cards are {hardest_terms}')
            else:
                self.say('There are no cards with errors')

    def reset_stats(self):
        """
        set the count of mistakes to 0 for all the cards and output the
        message Card statistics have been reset.
        """
        self.terms = {
            t: {'definition': d['definition'], 'errors': 0}
            for t, d in self.terms.items()
        }
        self.save_terms()
        self.say('Card statistics have been reset.')

    def run(self):
        actions = ', '.join([a for a in self.ACTIONS])
        self.say(f"Input the action ({actions}):")
        action = input()
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

        if self.after is not None and not self.saved:
            logger.debug('We should export when exit to given file file:')
            self.after()
            self.saved = True

        return self


parser = argparse.ArgumentParser()
parser.add_argument('-i', '--import_from')
parser.add_argument('-e', '--export_to')

if __name__ == '__main__':
    arguments = parser.parse_args().__dict__
    game = Flashcard(**arguments).run()
    game.say("Bye bye!")
