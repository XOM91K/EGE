import itertools
ct = 0
for x in itertools.product('012345678', repeat = 6):
    x =''.join(x)
    if x[0] != '0' and (( x.count('0') + x.count('2') + x.count('4') + x.count('6') + x.count('8')) <= 2) and int(x) % 2 ==0:
        ct += 1
        print(x)
print(ct)