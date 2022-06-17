with open('animals.txt') as sample:
    animals = sample.readlines()

    with open('animals_new.txt', 'w') as spaces:
        spaces.writelines(' '.join([a.strip() for a in animals]))
        spaces.close()

    sample.close()
