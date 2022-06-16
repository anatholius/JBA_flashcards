# the following line reads the list from the input, do not modify it, please
passwords = input().split()

print(*['{} {}'.format(p, len(p)) for p in sorted(passwords, key=len)], sep='\n')
