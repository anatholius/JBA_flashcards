with open('./data/dataset/input.txt') as sample:
    print([line.strip() for line in sample.readlines()].count('summer'))
    sample.close()
