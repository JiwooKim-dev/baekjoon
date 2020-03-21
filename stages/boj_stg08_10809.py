str = input()
list = [-1 for i in range(122-97+1)]

for i in range(len(str)):
    idx = ord(str[i])-97
    if (list[idx] == -1):
        list[idx] = i

for i in range(len(list)):
    print(list[i], end=' ')
