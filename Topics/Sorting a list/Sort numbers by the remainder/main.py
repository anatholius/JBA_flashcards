nums = [int(num) for num in list(input())]

print(sorted(nums, key=lambda n: n % 3))
