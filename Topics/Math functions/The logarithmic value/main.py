import math

x = int(input())
b = int(input())
print(round(math.log(x) if b <= 1 else math.log(x, b), 2))
