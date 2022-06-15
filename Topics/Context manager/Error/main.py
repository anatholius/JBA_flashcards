with open('years.txt', 'w', encoding='utf-8') as f:
    for i in range(int('2010'), int('2020')):
        f.write(f'{i} ')
        # print(i, file=f, end=' ')  # nice :) but longer :/
    f.write('2020')
