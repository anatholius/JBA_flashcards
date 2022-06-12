with open('sums.txt') as sums:
    print('\n'.join([str(
        sum(int(n) for n in line.strip().split()),
    ) for line in sums]))
    sums.close()
