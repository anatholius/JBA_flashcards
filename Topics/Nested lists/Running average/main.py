entry = input()
x = [int(n) for n in entry]
print([
    (x[i] + x[i + 1]) / 2
    for i in range(len(x) - 1)
])
