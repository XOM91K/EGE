import itertools
ct = 0
for i in itertools.product('01234567', repeat=8):
    i = ''.join(i)
    if i.count('3') <= 1 and i[0] != '0':
        i = i.replace('3', '1')
        i = i.replace('5', '1')
        i = i.replace('7', '1')
        if '11' not in i:
            ct += 1
            print(i)
print(ct)