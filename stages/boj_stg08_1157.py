str = input().upper()
counts = [0 for i in range(90-65+1)]
for i in range(len(str)):
    idx = ord(str[i]) - 65
    counts[idx] += 1
m = max(counts)

res = -1
for i in range(len(counts)):
    if counts[i] == m:
        if res != -1:
            print('?')
            exit(0)
        else:
            res = i

print(chr(res + 65))