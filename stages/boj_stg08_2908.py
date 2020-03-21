str = input()
a = int(str[2]) * 100 + int(str[1]) * 10 + int(str[0])
b = int(str[6]) * 100 + int(str[5]) * 10 + int(str[4])

if a > b:
    print(a)
else:
    print(b)

