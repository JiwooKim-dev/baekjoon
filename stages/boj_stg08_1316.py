n = int(input())

count = 0
for i in range(n):
    alphabets = list()
    word = input()
    isChecked = True
    for letter in word:
        alphabets.append(letter)
    for alphabet in alphabets:
        tmp = alphabet * word.count(alphabet)
        if tmp not in word:
            isChecked = False
    if isChecked:
        count += 1

print(count)