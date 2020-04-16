import math


def is_prime(num):
    if num == 1:
        return False

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False

    return True


n = int(input())
nums = input().split(' ')

count = 0
for i in range(n):
    if is_prime(int(nums[i])):
        count += 1

print(count)
