n = int(input())
res = list()
for i in range(n):
    line = input()
    repeat = int(line[0])
    str = line[2:]
    output = ""
    for j in range(len(str)):
        output += str[j] * repeat
    res.append(output)

for i in range(n):
    print(res[i])