with open('test.txt') as sample:
    print('\n'.join([line[0] for line in sample.readlines()]))
    sample.close()
