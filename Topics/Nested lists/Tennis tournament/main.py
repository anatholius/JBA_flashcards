comprehension = [i[:-4] for i in [
    input(' ') for _ in range(0, int(input(' ')))
] if 'win' in i]
print(comprehension, len(comprehension), sep='\n')
