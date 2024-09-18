import itertools
ct = 0
for x in itertools.product('01234567', repeat = 5):
    x = ''.join(x)
    if x[0] != '0' and x.count('3') <= 1:
        x = x.replace('1', '5')
        x = x.replace('3', '5')
        x = x.replace('5', '5')
        x = x.replace('7', '5')
        if '55' not in x:
            print(x)
            ct += 1
print(ct)