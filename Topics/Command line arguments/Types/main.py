args = sys.argv
print(sum([int(n) for i, n in enumerate(args) if i > 0]))
