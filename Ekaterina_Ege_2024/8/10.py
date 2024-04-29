import itertools
ct = 0
for x in itertools.product('01234567', repeat=6):
    x = ''.join(x)
    if x == x[::-1]:
        sm_ch = x.count('2') * 2 + x.count('4') * 4 + x.count('6') * 6
        sm_nch = x.count('1') + x.count('3') * 3 + x.count('5') * 5 + x.count('7') * 7
        if sm_ch <= sm_nch and x[0] != '0':
            ct += 1
            print(x)
print(ct)