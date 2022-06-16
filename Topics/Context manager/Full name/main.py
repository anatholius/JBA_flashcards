with open('full_name.txt', 'w') as f3, open('name.txt') as f1, open('surname.txt') as f2:
    f3.write(f'{f1.read()} {f2.read()}')
