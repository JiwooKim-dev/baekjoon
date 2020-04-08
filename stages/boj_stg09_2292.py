n = int(input())

if n == 1:
    print(1)
    exit(0)

x = 2
i = 0
j = 1
while True:
    if (n >= 6*i + 2) and (n <= 6*j + 1):
        print(x)
        break
    else:
        i = j
        j = j + x
        x += 1
