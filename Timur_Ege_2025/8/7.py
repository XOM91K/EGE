import itertools
ct = 0
for x in itertools.product('012345', repeat=3):
    x = ''.join(x)
    if x.count('5') == 1 and x[0] != '0':
        if (x[0] == '5' and x[1] not in '024') or (x[1] == '5' and x[0] not in '024' and x[2] not in '024') or (x[2] == '5' and x[1] not in '024'):
                ct += 1
                print(x)
print(ct)

        # if '54' not in x


# s = '12110100103012'
# if '3' in s:
#     print('Есть')
# else:
#     print('Нет')
