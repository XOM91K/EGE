import itertools
ct = 0 #переменная ct для количества
for x in itertools.product('012345678', repeat=7):
    x = ''.join(x)
    if x.count('6') == 1 and x[0] != '0':
        if x.count('1') + x.count('3') + x.count('5') + x.count('7') == 2:
            ct += 1
print(ct)