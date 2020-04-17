import math


def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


line = input().split(' ')
m = int(line[0])
n = int(line[1])

for i in range(m, n+1):
    if is_prime(i):
        print(i)
