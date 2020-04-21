import math

t = int(input())

res = []
for i in range(t):
    str = input().split()
    x1 = int(str[0])
    y1 = int(str[1])
    r1 = int(str[2])
    x2 = int(str[3])
    y2 = int(str[4])
    r2 = int(str[5])
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            res.append(-1)
        else:
            res.append(0)
    else:
        dist = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
        if r1 > dist + r2 or r2 > dist + r1 or r1 + r2 < dist:
            res.append(0)
        elif r1 == dist + r2 or r2 == dist + r1 or r1 + r2 == dist:
            res.append(1)
        elif r1 + r2 > dist:
            res.append(2)

for ans in res:
    print(ans)
