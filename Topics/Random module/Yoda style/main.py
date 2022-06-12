import random

# your sentence is assigned to the variable
sentence = input().split()

# write your python code below
random.seed(int('43'))
random.shuffle(sentence)

# shows the message
print(' '.join(sentence))
