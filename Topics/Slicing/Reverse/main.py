# the following line reads the list from the input; do not modify it, please
numbers = [int(num) for num in input().split()]

# print(numbers[16:3:-1])  # the line with an error
print(numbers[4:int('17')][::-1])
#               w_t_f the magic number?!!!!!
