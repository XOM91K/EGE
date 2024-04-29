import itertools
ct=  0
for x in itertools.product('0123456', repeat=5):
    x = ''.join(x)
    if x[0] != '0' and x.count('6') == 1:
        ch = x.count('2') * 2 + x.count('4') * 4 + x.count('6') * 6
        nch = x.count('1') * 1 + x.count('3') * 3 + x.count('5') * 5
        if ch < nch:
            ct += 1
print(ct)