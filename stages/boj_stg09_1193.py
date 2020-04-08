n = int(input())

i = 1
while True:
    if (n > i*(i-1)/2) and (n <= i*(i+1)/2):
        break
    i += 1
k = (int) (n - i*(i-1)/2)

if i % 2 == 0:
    print('{}/{}'.format(k, i-k+1))
else:
    print('{}/{}'.format(i-k+1, k))