import math


def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


m = int(input())
n = int(input())

isMin = True
sumVal = 0
for i in range(m, n+1):
    if is_prime(i):
        if isMin:
            minVal = i
            isMin = False
        sumVal += i

if sumVal == 0:
    print(-1)
else:
    print(sumVal)
    print(minVal)
