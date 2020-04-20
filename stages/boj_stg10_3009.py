x = []
y = []

for i in range(3):
    str = input().split()
    x.append(int(str[0]))
    y.append(int(str[1]))

if x.count(x[0]) == 1:
    pos_x = x[0]
elif x.count(x[1]) == 1:
    pos_x = x[1]
else:
    pos_x = x[2]

if y.count(y[0]) == 1:
    pos_y = y[0]
elif y.count(y[1]) == 1:
    pos_y = y[1]
else:
    pos_y = y[2]

print(pos_x, pos_y)