import math

# 에라토스테네스의 체 #
MAXIMUM = 10000
erastos = [1] * (2 * MAXIMUM + 1)
erastos[0] = 0
erastos[1] = 0

for i in range(2, int(math.sqrt(len(erastos)))):
    if erastos[i]:
        for j in range(i * 2, len(erastos), i):
            erastos[j] = 0

numList = []
t = int(input())
for i in range(t):
    numList.append(int(input()))

for num in numList:
    n1 = int(num / 2)
    n2 = n1

    while erastos[n1] == 0 or erastos[n2] == 0:
        n1 -= 1
        n2 += 1

    print(n1,n2)