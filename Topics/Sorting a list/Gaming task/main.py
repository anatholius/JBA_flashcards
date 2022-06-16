# the following line reads the list from the input, do not modify it, please
toys = input().split()

print(sorted(toys, key=len))
