characters = ['c=', 'c-', 'dz=', 'd-',
              'lj', 'nj', 's=', 'z=']

str = input()

for cmp in characters:
    if cmp in str:
        str = str.replace(cmp, '.')

print(len(str))

'''
이건 왜 틀린 건지 고민해보기

characters = ['c=', 'c-', 'dz=', 'd-',
              'lj', 'nj', 's=', 'z=']

str = input()

count = len(str)
cont = True
while(cont):
    cont = False
    for cmp in characters:
        if cmp in str:
            idx = str.index(cmp)
            str = str[:idx] + ' ' + str[idx+len(cmp):]
            count = count - len(cmp) + 1
            cont = True

print(count)
'''