import math

x = abs(int(input()))
b = int(input())
print(round(
    math.log(x)
    if b <= 0 or b == 1 else
    math.log(x, b),
    2))
