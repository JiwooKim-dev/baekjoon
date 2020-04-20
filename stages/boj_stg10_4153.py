sides = []
res = []
while True:
    str = input().split()
    if str == ['0', '0', '0']:
        break
    for i in range(3):
        sides.append(int(str[i]))
    sides.sort()
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        res.append('right')
    else:
        res.append('wrong')
    sides = []

for ans in res:
    print(ans)
