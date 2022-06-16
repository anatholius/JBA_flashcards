for i in range(1, int('11')):
    with open(f'file{i}.txt', 'w') as file:
        file.write(str(i))
