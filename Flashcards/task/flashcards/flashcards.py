term = input()
definition = input()
answer = input(term)
print('Your answer is {}'.format(
    'right!' if definition == answer else 'wrong...'
))
