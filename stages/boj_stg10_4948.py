import math

# ### 시간초과 ###
# def is_prime(n):
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

# 에라토스테네스의 체 #
MAXIMUM = 123456
erastos = [1] * (2 * MAXIMUM + 1)
erastos[0] = 0
erastos[1] = 0

for i in range(2, int(math.sqrt(len(erastos)))):
    if erastos[i]:
        for j in range(i * 2, len(erastos), i):
            erastos[j] = 0

numList = []
while True:
    n = int(input())
    if n == 0:
        break
    numList.append(n)

for num in numList:
    print(sum(erastos[num + 1 : num * 2 + 1]))
