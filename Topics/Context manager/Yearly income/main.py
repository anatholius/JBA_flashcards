with open('salary.txt') as s:
    with open('salary_year.txt', 'w') as y:
        y.writelines(['{}\n'.format(int(a.strip()) * int('12')) for a in s.readlines()])
