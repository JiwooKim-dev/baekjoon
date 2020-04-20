import math

str = input().split()
x = int(str[0])
y = int(str[1])
w = int(str[2])
h = int(str[3])

print(min(x, y, w-x, h-y))