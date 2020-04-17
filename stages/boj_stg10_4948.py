import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def count_prime_nums(n):
    count = 0
    for i in range(n + 1, n * 2 + 1):
        if is_prime(i):
            count += 1
    return count


numList = []
while True:
    n = int(input())
    if n == 0:
        break
    numList.append(n)

for num in numList:
    print(count_prime_nums(num))
